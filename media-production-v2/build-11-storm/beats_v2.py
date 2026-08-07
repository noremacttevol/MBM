#!/usr/bin/env python3
"""V2 beat map — row 11, build-11-storm (Mark 4:35-41).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE (STORY-COVERAGE-LAW): 34 pictures against V1's 10 unique stills, over
199.8 s — 5.9 s per picture, the band rows 5-10 shipped at.

⚠️ THIS ROW HAS ITS OWN REJECTION HISTORY, AND BOTH DEFECTS ARE STAGING, NOT ART.
They are written into the beats below because prose did not hold them last time:

  1. TIME-OF-DAY LAW (Cameron, 2026-07-10 — storm V2 rejected). Mark 4:35 is
     "when the EVEN was come", and the narration's own ending puts STARS over
     the calm. The rejected build coloured the storm like a sunset. So:
       · b01-b04 (the shore, before they sail) are LAST LIGHT — the sun already
         gone, the west going out. That much evening is correct and is what the
         narration asks for ("until the light was going").
       · FROM b05 TO THE LAST FRAME IT IS NIGHT. The crossing, storm, and
         post-command calm have separate locks so violent waves and lightning
         can never leak into the "great calm." There are no boat lamps or glass
         lanterns. There is NO sunset band, NO sunrise, NO warm horizon, and NO
         golden light on the water anywhere from b05 onward.

  2. ACTION-LOGIC LAW (Cameron — storm V1 rejected). The first build had
     fishermen who appeared to pour water INTO their own boat, and a rope that
     led out of the hull to nothing. So every bailing frame states that the
     water is being flung OUT over the gunwale and AWAY from the hull, and every
     rope in this build runs to the mast or the rigging INSIDE the boat. QC each
     frame by asking "what does this person appear to be DOING?"

  3. Figures stay visibly INSIDE the boat — deck under their feet, gunwale
     running behind them. Nobody stands on water in this story; that is row 7.

  4. BOAT + CREW UNIFORMITY (Cameron, 2026-08-06 — the v4 rejection that made this
     a NEEDS-REBUILD). His words: "10 pictures of 4 people in one kind of boat and
     10 pictures of 5 people in a different kind of boat ... some pictures dont have
     jesus in the boat at all and some have him in the front and some have him in
     the back ... the one that says they wake him with rough hands has someone else
     jesus being woken." The root cause was that the boat was PROSE-locked only, so
     every generation invented a fresh hull and headcount. The cure is IMAGE, the
     same cure faces got:
       · BOAT PLATE. s07's boat is promoted to PLACE-REF/boat.jpeg and wired
         (PLACE_REFS) into all 23 hull beats. The plate carries the hull identity —
         planking, sheer line, bow, single amidships mast, furled/lashed sail,
         gunwale, oar stations, coiled bow rope, stone anchor — so every regenerated
         boat frame is the SAME boat. Scene text supplies only ACTION and LIGHT.
       · CREW-LOCK = EIGHT, always (Jesus + Peter, Andrew, James, John, Matthew +
         two unnamed early followers). A tighter shot is a CROP of that same eight —
         bodies exiting the frame edges — NEVER a smaller crew in an emptier boat.
       · JESUS POSITION-LOCK (his "front/back" complaint). Jesus is aboard the whole
         crossing and his position is fixed, never wandering: asleep on the stern
         cushion b14-b16, rising and standing IN THE STERN b19-b21, then back among
         them amidships in the swamped boat b25/b27/b28/b34. He is never bow-ward,
         never mid-boat during the storm, and never omitted from a wide whole-boat
         frame. b16 is his named "rough hands" frame — the woken man IS the locked
         Jesus, the only cream robe in the picture, no second bearded cream figure.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 4:35-41 KJV):
  v35    "when the even was come" — the crossing starts at nightfall.
  v36    "they took him EVEN AS HE WAS" — no rest, no supper, straight from the
         last word into the boat. He is exhausted before the storm begins, which
         is what makes v38 make sense. "And there were also with him OTHER
         LITTLE SHIPS" — b06 puts them in frame; almost every telling drops them.
  v37    "the waves BEAT INTO the ship, so that it was now FULL."
  v38    "he was in the HINDER PART of the ship, ASLEEP ON A PILLOW" — the stern,
         on the steersman's cushion. Not lying in the bow, not on bare boards.
  v38    "Master, carest thou not that we perish?" — the narration's whole hinge:
         they never doubted his power, they doubted his heart.
  v39    "he AROSE, and REBUKED THE WIND, and SAID UNTO THE SEA, Peace, be still."
         He speaks to the storm, not to the men — b27 turns him away from them.
  v39    "and there was a GREAT CALM" — instantly flat, which is why b30/b31 show
         water like glass rather than a swell dying down.
  v40    "Why are ye so fearful? how is it that ye have no faith?" — the
         narration says he asked it GENTLY, and b34 is built on that word.
  v41    "they feared EXCEEDINGLY" — more awe after the calm than during the
         storm. The fear does not leave the boat; it changes direction.

  The four named fishermen (n1b) are Peter, Andrew, James and John, so this build
  uses the shared CAST_LOCKS for all four — same men as every other video.

CONTENT-CARE: row 11 is not in the §3 flag table = GREEN. The terror is real but
stays on faces and effort; nobody is injured, nothing is gruesome.
"""

from pathlib import Path

CHARACTERS = Path(__file__).resolve().parents[2] / "media-production" / "CHARACTERS"


def _sheet(slug):
    """All three canonical views required by CHARACTER LAW rule 3."""
    return [str(CHARACTERS / slug / f"{view}.jpeg") for view in (
        "face-front", "three-quarter", "full-body"
    )]


EARLY_COMPANY = ("peter", "andrew", "james", "john-beloved", "matthew")
OUTPUT_ASSET_DIR = "assets-realistic"
# Reviewer cut name. v3 was DENIED by Cameron (board sync 2026-08-01): bad first
# picture, a man who read as climbing the mast (b10), bailing that read as pouring
# water INTO the boat (b11), and "Peace, be still" spoken too fast. v4 is the fix.
OUTPUT_VIDEO_NAME = "mark-4_calming-the-storm-realistic-v4.mp4"
EARLY_COMPANY_REFS = [str(
    Path(__file__).resolve().parents[1]
    / "CAST-V2-REF" / "early-company-reference-board.jpg"
)]

LOCKS = {
    # SETTING LOCKS NAME NO CHARACTER (STRAY-JESUS defect).
    "SHORE-EVENING": (
        "SHORE-EVENING LOCK: the grassy western shore of the Sea of Galilee at the "
        "very end of the day — trodden grass running down to a shingle beach, fishing "
        "boats drawn up on the stones, nets spread on frames to dry, low bare hills "
        "behind. The sun is already down behind the hills and the western sky is a "
        "narrow band of dull fading orange going out fast into deep blue, with the "
        "first stars showing overhead. The light is dim, cool and almost gone."
    ),
    "SEA-STORM-NIGHT": (
        "SEA-STORM-NIGHT LOCK: the Sea of Galilee at NIGHT in a violent squall, hours "
        "from any dawn. The sky is NIGHT — torn fast-moving black storm cloud with "
        "hard gaps where cold white stars show through, a high broken moon putting "
        "silver edges on the cloud and hard white crests on the water, and sheet "
        "lightning flickering blue-white over the black hills that ring the lake. The "
        "water is deep blue-black, running in steep breaking waves with white foam "
        "torn off the tops, and cold spray fills the air. Every colour in the frame is "
        "cold — silver, black, blue-black, storm-grey and foam white. Lighting comes "
        "only from the moon and distant lightning. There is no lamp, lantern, glass, "
        "fire, orange light, sunset band, sunrise, or warm horizon."
    ),
    "SEA-CROSSING-NIGHT": (
        "SEA-CROSSING-NIGHT LOCK: the Sea of Galilee at NIGHT before the squall. The "
        "water is dark blue-black and only moderately choppy, the far hills are a low "
        "black line, and cold moonlight and stars reflect in broken silver strips. "
        "The sail is fully furled and the men row with the oars outside the hull. "
        "There is no storm yet: no lightning, breaking wave, heavy rain or panic. "
        "There is also no lamp, lantern, glass, fire, orange light, sunset or sunrise."
    ),
    "SEA-CALM-NIGHT": (
        "SEA-CALM-NIGHT LOCK: the same Sea of Galilee at NIGHT after Jesus has spoken. "
        "The storm is completely over. The water is perfectly mirror-flat right to "
        "the hull, the sail and every loose cloth hang slack, ropes hang straight, "
        "and stars and moonlight reflect unbroken in the water. Soaked clothing, "
        "puddles and dripping rope are the only remnants of the squall. There are "
        "absolutely no waves, spray, wind, rain, lightning, storm action, lamp, "
        "lantern, glass, fire, orange light, sunset or sunrise."
    ),
    "BOAT": (
        "BOAT LOCK: one open first-century Galilean fishing boat about eight paces "
        "long — heavy overlapping wooden planks dark with water, a low gunwale running "
        "right around the hull, a short mast stepped amidships with its small square "
        "sail hauled down and lashed, long oars through leather-strapped tholes along "
        "both sides, coiled rope, folded nets, wooden bailing scoops and a stone "
        "anchor stowed on the deck timbers, a raised steering platform in the stern "
        "with a leather-covered steersman's cushion on it. Every rope in the boat runs "
        "to the mast or to the rigging inside the hull, with both ends physically "
        "accounted for; no rope drops into the lake or ties to a purposeless post. "
        "Every oar passes through one believable side thole and extends out that SAME "
        "side of the hull; an oar never stretches across the boat or exits the opposite "
        "side. The mast is the only tall upright post. The deck planking is always "
        "visible under the men's feet. No lamp, lantern or glass lighting is aboard. "
        "Whenever the whole travelling company is visible, the main boat contains the "
        "same EIGHT adult men total: Jesus; Peter; Andrew; James the son of Zebedee; "
        "John the beloved; Matthew; and the same two unnamed early followers. This is "
        "an early-ministry boat company, not a posed picture of all Twelve. A tighter "
        "shot may frame only a clearly cropped subset."
    ),
    "DISCIPLES": (
        "EARLY-BOAT-COMPANY LOCK: the same seven companions travel with Jesus in every "
        "whole-boat shot: Peter, Andrew, James the son of Zebedee, John the beloved, "
        "Matthew, and the same two unnamed early followers. Together with Jesus that "
        "makes EIGHT men in the full company, no more and no fewer. Peter, Andrew, "
        "James, John and Matthew must match their attached canonical CHARACTER sheets; "
        "their different ages, faces, builds, hair, beard states and tunic colours are "
        "not interchangeable. John remains the youngest and clean-shaven. Matthew is a "
        "non-sailor and does not expertly work the mast or oars. Peter may steer; "
        "Andrew, James and John may handle familiar fishing-boat work. The two unnamed "
        "followers remain two distinct recurring men and never become twins. Nobody "
        "poses, circles Jesus, or looks toward him unless that exact narrated moment "
        "requires it. Worship is conveyed through the truthful story, not a tableau."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------- n0 — the last story ----
    {
        "id": "v2-r011-b01", "out": "s01-teaching-till-the-light-went.jpeg", "seg": "n0 p1-p2",
        "window": "0.00-11.02", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "SHORE-EVENING"],
        "narration": ("Evening, on the Sea of Galilee. Jesus had been teaching crowds "
                      "on the shore all day — story after story, until the light was "
                      "going and his voice was nearly gone with it."),
        "must_show": "the end of a long day's teaching on the shore — a big crowd seated on the grass, the light almost gone, Jesus still speaking.",
        "must_not_show": "no halo, glare or rim-light. NOTE: dim fading evening light is CORRECT in this frame and the three after it — the narration says the light was going.",
        "scene": (
            "The grassy shore at the very end of the day. A large crowd sits and "
            "stands on the trodden grass in the failing light, hundreds of them, faces "
            "turned in toward Jesus, who stands lower down near the water still "
            "speaking, one hand lifted, plainly at the end of a long day. The western "
            "sky behind the hills is a narrow band of dull fading orange going out into "
            "deep blue and the first stars are showing above. Boats are drawn up on the "
            "shingle. The camera is back far enough to hold the crowd and Jesus head to "
            "sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b02", "out": "s02-worn-through.jpeg", "seg": "n0 p3-p4",
        "window": "11.02-17.01", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE-EVENING"],
        "narration": ("He was worn through. And when the last story was told, he said "
                      "to his friends:"),
        "must_show": "close on Jesus at the end of a long day — the SAME man as the reference face, plainly weary: shoulders low, eyelids heavy, turning slowly to speak to the men beside him. The tiredness is in his posture and heavy eyes, NOT in his features.",
        "must_not_show": "his face must stay exactly the reference man — do NOT gaunt, hollow, thin, age, blotch, dirty or sicken him, no sunken cheeks, no bruised eye-sockets, no wild frizzed hair, no grey pallor; keep his warm olive-tan skin, smooth dark wavy shoulder-length hair, full dark beard and warm brown eyes. No halo, glare or rim-light.",
        "scene": (
            "Close on Jesus in the last of the light — unmistakably the same man as the "
            "reference face, only tired. He carries the weariness in his body: shoulders "
            "settled low, his gaze soft and heavy-lidded, breathing slow after a whole "
            "day of talking. His skin is the same warm olive-tan, his dark hair the same "
            "smooth shoulder-length waves, his beard full and dark, his eyes the same warm "
            "brown — healthy and himself, just spent. He has half turned his head to speak "
            "to someone beside him, the turn unhurried and easy. The dim shore and the "
            "dying western band are soft behind him."
        ),
    },
    {
        "id": "v2-r011-b03", "out": "s03-unto-the-other-side.jpeg", "seg": "j0",
        "window": "17.01-20.95", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "SHORE-EVENING"],
        "narration": "Let us pass over unto the other side. (Mark 4:35)",
        "must_show": "Jesus gesturing out across the darkening water toward the far shore, the men beside him looking where he points.",
        "must_not_show": "no halo, glare or rim-light; the water is still calm here — nothing has gone wrong yet.",
        "scene": (
            "At the water's edge Jesus lifts one hand and points out across the "
            "darkening lake toward the far shore, saying it to the men around him. "
            "Peter and two others stand with him looking out the way he is pointing, "
            "one already glancing back at the beached boat. The water is quiet and "
            "dark with the last dull light lying flat on it, the far hills a low black "
            "line. The camera is back far enough to see them head to sandals. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n1 — even as he was ----
    {
        "id": "v2-r011-b04", "out": "s04-even-as-he-was.jpeg", "seg": "n1 p1",
        "window": "20.95-29.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SHORE-EVENING"],
        "narration": ("So they took him, Mark says, even as he was — no rest, no "
                      "supper, straight from the last word into the boat."),
        "must_show": "him being helped straight from the shore into the boat with nothing in his hands — no food, no bundle, no pause; the men shoving off the shingle.",
        "must_not_show": "no halo, glare or rim-light; nobody is eating or resting; he is not carrying anything.",
        "scene": (
            "At the shingle the men are launching the boat in the last of the light. "
            "Two have their shoulders against the bow shoving it off the stones, "
            "another is already aboard reaching a hand down, and Jesus is stepping over "
            "the gunwale with empty hands and nothing with him at all, moving slowly "
            "with tiredness. Behind them the emptying shore still has the trodden grass "
            "and the last of the crowd walking away up the slope. Deep blue dusk, the "
            "dull western band nearly out. The camera is back far enough to hold the "
            "boat and the men head to sandals. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r011-b05", "out": "s05-other-little-boats.jpeg", "seg": "n1 p2",
        "window": "29.81-33.37", "wide": True, "jesus": False, "ref": False,
        "locks": ["BOAT", "SEA-CROSSING-NIGHT"],
        "narration": "Other little boats followed them out.",
        "must_show": "SCRIPTURE DETAIL almost every telling drops (v36): two or three other small boats out on the dark water behind theirs, following.",
        "must_not_show": "NIGHT BEGINS HERE — no sunset band, no warm horizon, no golden water from this frame on. Do not put Jesus in this frame.",
        "scene": (
            "Out on the open lake at night. The fishing boat pulls away from the "
            "shore under a black sky, and behind it two or three other small boats "
            "follow, strung out across the dark water, each outlined by moonlight with "
            "the pale flicker of oars. The water is still only choppy. Cold "
            "moonlight comes through breaks in the moving cloud and lays silver on the "
            "swell; there is no warm colour anywhere. The camera is back far enough to "
            "hold all the boats. Every figure has two arms, two hands and one head."
        ),
    },
    # ----------------------------------------------- n1b — the fishermen ----
    {
        "id": "v2-r011-b06", "out": "s06-men-at-the-oars.jpeg", "seg": "n1b p1",
        "window": "33.37-39.24", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-CROSSING-NIGHT"],
        "narration": ("And here is something worth knowing about the men at the oars: "
                      "at least four of them were professional fishermen."),
        "must_show": "ACTION-LOGIC: men rowing properly — oar blades biting the water OUTSIDE the hull, both hands on each loom, feet braced on the deck, easy practised rhythm.",
        "must_not_show": "no oar held in the air doing nothing; nobody outside the hull; no strain yet — this is competent easy work. Do not put Jesus in this frame.",
        "scene": (
            "Inside the boat at night, four men at the oars in an easy practised "
            "rhythm — each with both hands closed on the loom, shoulders rolling back "
            "into the stroke, feet braced against the deck timbers, the blades dipping "
            "and biting the black water outside the hull and lifting again together. "
            "Peter is nearest, pulling steadily. Nobody is straining. Cold moonlight "
            "reflecting off the water reveals their faces against the night. The "
            "camera is back far enough to see the men and the oars. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b07", "out": "s07-peter-andrew-james-john.jpeg", "seg": "n1b p2",
        "window": "39.24-44.95", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "ANDREW", "JOHN", "JAMES-Z", "BOAT", "SEA-CROSSING-NIGHT"],
        "narration": ("Peter and his brother Andrew, and James and John, the sons of "
                      "Zebedee."),
        "must_show": "the four named men together and individually readable — Peter and Andrew on one side, James and John on the other, all four at the oars.",
        "must_not_show": "do not put Jesus in this frame; all four faces must be visible and distinct, since the narration names them.",
        "scene": (
            "The four fishermen at the oars, framed so each face is clearly readable "
            "in reflected moonlight — Peter and Andrew pulling together on one side of the "
            "boat, James and John opposite them on the other, all four leaning into "
            "the stroke in time. Their tunics are already dark with spray. The mast "
            "and the lashed sail stand between them and the black sky. The camera is "
            "back far enough to see all four head to feet inside the hull. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b08", "out": "s08-this-lake-was-their-workplace.jpeg", "seg": "n1b p3-p5",
        "window": "44.95-53.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "ANDREW", "BOAT", "SEA-CROSSING-NIGHT"],
        "narration": ("This lake was their workplace. They had crossed it at night "
                      "their whole lives. Nothing about dark water scared them."),
        "must_show": "unbothered competence — one man talking over his shoulder mid-stroke, another half smiling, completely at home on black water at night.",
        "must_not_show": "no fear or tension anywhere in this frame — it exists purely so the next one lands. Do not put Jesus in it.",
        "scene": (
            "Close on Peter and Andrew at the oars in the moonlight. Peter has turned "
            "his head to say something back over his shoulder mid-stroke, entirely "
            "unbothered, and Andrew is answering with the beginning of a grin, both "
            "still pulling without looking at what their hands are doing. Their faces "
            "are relaxed and capable, men doing on a black night the thing they have "
            "done ten thousand times. Spray on their beards. The dark water runs past "
            "outside the hull behind them. Each hand has five fingers."
        ),
    },
    # ---------------------------------------------------- n2 — the squall ----
    {
        "id": "v2-r011-b09", "out": "s09-the-lake-turned.jpeg", "seg": "n2 p1-p2",
        "window": "53.77-65.49", "wide": True, "jesus": False, "ref": False,
        "locks": ["BOAT", "SEA-STORM-NIGHT"],
        "narration": ("Then the lake turned on them. The Sea of Galilee lies seven "
                      "hundred feet below sea level, in a bowl of hills — when cold "
                      "wind spills down those slopes, calm water can turn violent in "
                      "minutes."),
        "must_show": "the geography doing it: a wide night view of the lake in its bowl of black hills, with the squall visibly pouring down the slopes and tearing the water white where it lands.",
        "must_not_show": "no sunset or dawn light on the hills; the boat is small in this frame — the lake and the hills are the subject. Do not put Jesus in it.",
        "scene": (
            "A wide high night view of the whole lake lying in its ring of black "
            "hills. Down one dark slope a wall of squall is visibly pouring — cloud "
            "shredding off the ridge, a curtain of driven rain and spray sweeping out "
            "across the water — and where it lands the black surface is being torn "
            "into white running chaos. Ahead of it the water is still nearly smooth. "
            "The little fishing boat is small and low out in the middle with its oars "
            "still out. Broken moon behind the racing cloud, lightning flickering "
            "blue-white over the far ridge, cold stars in a gap. No warm light "
            "anywhere."
        ),
    },
    {
        "id": "v2-r011-b10", "out": "s10-savage-even-for-that-lake.jpeg", "seg": "n2 p3",
        "window": "65.49-69.77", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-STORM-NIGHT"],
        "narration": "This storm was savage even by that lake's standard.",
        "must_show": "the boat in the worst of it — heeled hard over, a wave standing above the gunwale, the mast raked, men crouched low and grabbing for whatever is fixed. Jesus lies asleep, small and undisturbed, on the raised stern cushion at the back of the boat — present but clearly not the focus of this frame.",
        "must_not_show": "⚠️ NOBODY CLIMBS. Cameron rejected this frame because a man read as climbing the mast. No man touches the mast, hangs from a rope overhead, or has a foot off the deck — every man is LOW, knees bent, feet flat on the deck planking, hands gripping the gunwale, a thwart, or a rope at chest height or lower. Nobody outside the hull; no rope leading off the boat to nothing — every line runs to the mast or the rigging inside. Jesus is present but ASLEEP in the stern (his locked position) — do NOT wake him, enlarge him, halo him, or move him toward the bow or midships; he is a small undisturbed shape at the back, the only cream robe.",
        "scene": (
            "The boat is heeled hard over in the middle of the squall, its mast raked "
            "steeply against the torn black sky, as a steep wave stands up higher than "
            "the gunwale on the windward side. The men are all DOWN LOW in the hull, "
            "crouched with their knees bent and both feet flat on the deck planking — "
            "one grips the near gunwale with both hands, another is braced with a hand "
            "on a thwart and a foot jammed against a rib of the hull, a third crouches "
            "with one fist closed on a rope at his chest. No man touches the mast, no "
            "man reaches above his own head, and no man's feet leave the deck. Every "
            "man is inside the hull with the deck under him. At the very back, on the "
            "raised stern platform, Jesus lies asleep on the leather steersman's "
            "cushion, small and undisturbed by the chaos, his cream robe the only cream "
            "in the boat — he is not the focus, just plainly present and asleep. "
            "Driving spray, white "
            "foam, lightning on the far hills. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    # ------------------------------------------------- n2b — the boat fills ----
    {
        "id": "v2-r011-b11", "out": "s11-bailing.jpeg", "seg": "n2b p1",
        "window": "69.77-73.20", "wide": True, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "BOAT", "SEA-STORM-NIGHT"],
        "narration": "Waves broke over the side faster than the men could bail.",
        "must_show": "⚠️ ACTION-LOGIC, THE DEFECT THAT GOT V1 AND V3 REJECTED: two men bailing, and the direction of every drop of moving water must read correctly at one glance. The bailing water is being flung OUT OVER THE GUNWALE AND AWAY FROM THE BOAT — the scoop is past the rail on its outward throw and the whole sheet of thrown water is OUTSIDE the hull, falling down toward the open sea, visibly clear of and beyond the wooden rail. Deep water already covers the deck around their shins to justify the bailing.",
        "must_not_show": "⚠️ Cameron rejected two cuts over this exact frame. NO wave may be breaking into the boat in this picture, NO water may arc over the men or over the deck, and NO thrown water may hang between the men or above the hull — any of those reads as men pouring water INTO their own boat and is a hard fail. The only airborne water is the one sheet leaving the near man's scoop, already outside the rail, falling toward the sea. Nobody pours anything toward the deck. Do not put Jesus in this frame.",
        "scene": (
            "Two men are bailing hard, seen from inside the boat looking outward over "
            "the near gunwale so the sea is beyond the rail. The nearest man is caught "
            "at the very end of his OUTWARD throw — his wooden scoop has crossed above "
            "the top of the gunwale with its mouth turned outward and downward, away "
            "from the boat, and the single sheet of water leaving it is entirely "
            "OUTSIDE the hull, beyond the rail, falling away down toward the sea. No "
            "part of the thrown water is over the deck or over any man. His other hand "
            "grips the rail as he swings. Behind him the second man is bent low, his "
            "scoop dipped INTO the black water sloshing around their shins on the deck "
            "timbers, filling it for his own throw. The sea beyond the rail runs in "
            "steep white-torn waves but no wave is breaking into the boat in this "
            "instant. Night, spray, cold broken moonlight. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b12", "out": "s12-the-boat-was-filling.jpeg", "seg": "n2b p2",
        "window": "73.20-74.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOAT", "SEA-STORM-NIGHT"],
        "narration": "The boat was filling.",
        "must_show": "the water level INSIDE the hull — black water surging around the men's shins over the deck planking, nets and rope floating in it.",
        "must_not_show": "no bailing action in this frame — this is the losing side of the fight; do not put Jesus in it.",
        "scene": (
            "Low and close inside the hull. Black water is surging back and forth "
            "across the deck timbers well up the men's shins, sloshing against the "
            "ribs of the boat with each roll, and a coil of rope and a folded net are "
            "lifting and turning in it. A wooden bailing scoop floats past on its side. "
            "The planking is barely visible under the water. Cold moonlight and "
            "distant lightning reveal the moving surface inside the boat against the "
            "black night beyond the rail."
        ),
    },
    {
        "id": "v2-r011-b13", "out": "s13-their-last-storm.jpeg", "seg": "n2b p3",
        "window": "74.62-82.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "ANDREW", "JOHN", "DISCIPLES", "BOAT", "SEA-STORM-NIGHT"],
        "narration": ("And the fishermen who had survived a hundred storms looked at "
                      "this one — and believed it was going to be their last."),
        "must_show": "THE INVERSE OF b08: the same competent men now openly terrified — Peter's face white and fixed, John gripping the rail and shouting, the certainty gone out of all of them. Behind them, small and undisturbed on the stern cushion, Jesus lies asleep (his locked position) — the quiet contrast that the whole story turns on.",
        "must_not_show": "no comic terror; this is the specific fear of professionals who have run out of answers. Jesus is present but ASLEEP in the stern (his locked position) — do NOT wake him, enlarge him, halo him, or move him toward the bow or midships; he is a small undisturbed shape at the back, the only cream robe.",
        "scene": (
            "Inside the pitching boat, the men who were easy a minute ago have gone to "
            "pieces. Peter has stopped rowing altogether with his oar dragging, his "
            "face bloodless and fixed on the sea over the bow. Young John is gripping "
            "the rail with both hands and shouting something into the wind with his "
            "eyes shut. Andrew is hauling at a rope that runs up to the rigging inside "
            "the boat with his teeth bared. Another man has simply sat down in the "
            "water on the deck with his arms over his head. Every one of them is "
            "inside the hull. At the very back, on the raised stern platform, Jesus "
            "lies asleep on the leather steersman's cushion, small and undisturbed, his "
            "cream robe the only cream in the boat — present and plainly asleep while "
            "they come apart, not the focus of the frame. Spray, black water, lightning "
            "on the hills. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------------ n3 — asleep ----
    {
        "id": "v2-r011-b14", "out": "s14-asleep-in-the-stern.jpeg", "seg": "n3 p1-p2",
        "window": "82.19-91.78", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BOAT", "SEA-STORM-NIGHT"],
        "narration": ("And Jesus was asleep. In the stern, on the steersman's cushion, "
                      "soaked with spray, rising and falling with the pitching deck — "
                      "asleep."),
        "must_show": "SCRIPTURE-EXACT (v38): he is in the HINDER PART of the boat, on the leather steersman's CUSHION on the raised stern platform, genuinely asleep while the boat pitches.",
        "must_not_show": "no halo, glare or rim-light; he is not in the bow and not on bare boards; he is soaked like everything else — no dry patch of calm around him.",
        "scene": (
            "In the raised stern of the pitching boat, Jesus lies asleep on the "
            "leather-covered steersman's cushion, one arm folded under his head and "
            "the other across his chest, his knees drawn up against the slope of the "
            "deck. He is soaked through — water runs off his hair and his robe is dark "
            "and heavy with it — and he rises and falls bodily with the boat as it "
            "pitches. Behind him a wave stands white over the stern rail and the black "
            "sky is torn with cloud. Nothing around him is calm or dry. The camera is "
            "back far enough to hold him and the pitching stern. He has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r011-b15", "out": "s15-not-afraid-of-it.jpeg", "seg": "n3 p3-p4",
        "window": "91.78-97.63", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SEA-STORM-NIGHT"],
        "narration": ("Not because he didn't know what was happening. Because he "
                      "wasn't afraid of it.",),
        "must_show": "close on his sleeping face — deeply, restfully asleep, entirely peaceful, with storm water running across it.",
        "must_not_show": "no halo, glare or rim-light; not a troubled or restless sleep, and not an unnaturally serene glowing one — an exhausted man sleeping soundly.",
        "scene": (
            "Very close on Jesus's sleeping face in the stern. He is deeply and "
            "restfully asleep — eyes closed and still, brows smooth, mouth slightly "
            "open, his breathing even — while cold spray runs in sheets across his "
            "cheek and temple and drips off his beard, and the whole frame tilts with "
            "the pitch of the boat. The leather cushion is under his cheek. Cold "
            "broken moonlight and a flicker of distant lightning are the only light on "
            "him. Nothing about his face is troubled."
        ),
    },
    # ---------------------------------------------- n4 — carest thou not ----
    {
        "id": "v2-r011-b16", "out": "s16-they-woke-him.jpeg", "seg": "n4",
        "window": "97.63-105.58", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-STORM-NIGHT"],
        "narration": ("So they woke him. Rough hands on his shoulder, screaming over "
                      "the wind the question people have been asking in storms ever "
                      "since:"),
        "must_show": "⚠️ CAMERON'S NAMED FRAME ('someone else jesus being woken with rough hands'). The reclining man being shaken awake IS the one locked Jesus — the attached JESUS reference face exactly, on the stern cushion where he slept in b14/b15, and he is the ONLY man in the frame wearing cream. Hands grabbing and shaking HIS shoulder, men leaning over HIM shouting into HIS face over the wind — rough, desperate, not reverent.",
        "must_not_show": "⚠️ HARD FAIL: no SECOND bearded man in a cream/off-white robe anywhere in this frame — only Jesus wears cream, and the man being woken must not read as a stranger. The sleeper is not a look-alike; his face must match the attached Jesus reference. No halo, glare or rim-light; nobody is kneeling politely — this is a panicked shaking-awake.",
        "scene": (
            "Two men have lunged into the stern and got hold of Jesus where he lies. "
            "Peter has a big hand clamped on his shoulder shaking him hard, leaning "
            "right down over him with his mouth wide open shouting into his face, and "
            "another man behind him has both hands on the stern rail yelling as well, "
            "his hair plastered flat. Jesus is just coming awake underneath them, his "
            "eyes opening. There is nothing reverent about it. Black water breaking "
            "behind, spray across the whole frame, cold moonlight. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b17", "out": "s17-carest-thou-not.jpeg", "seg": "s38",
        "window": "105.58-109.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SEA-STORM-NIGHT"],
        "narration": "Master, carest thou not that we perish? (Mark 4:38)",
        "must_show": "close on Peter's face shouting the question — terror and accusation together, soaked, mouth wide.",
        "must_not_show": "do not put Jesus in this frame; this is not polite petition, it is an accusation shouted in a gale.",
        "scene": (
            "Very close on Peter's face in the dark, streaming with water, shouting. "
            "His mouth is wide, the tendons stand out in his neck, his soaked hair is "
            "flat to his skull and his eyes are wild — and underneath the terror there "
            "is plain accusation in the look, the face of a man demanding to know why "
            "somebody is not helping. A white crest breaks behind his shoulder. Cold "
            "broken moonlight and a flash of lightning."
        ),
    },
    {
        "id": "v2-r011-b18", "out": "s18-they-doubted-his-heart.jpeg", "seg": "n4b",
        "window": "109.54-118.93", "wide": True, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "BOAT", "SEA-STORM-NIGHT"],
        "narration": ("Don't you care that we are going down? Listen to what they were "
                      "really saying. They never doubted his power. They doubted his "
                      "heart."),
        "must_show": "the ring of soaked faces turned back toward the stern — every one of them asking the same thing, terrified and hurt at once.",
        "must_not_show": "do not put Jesus in this frame; the look must be wounded as well as frightened — that is the narration's whole point.",
        "scene": (
            "Inside the swamped boat, the men have all turned back toward the stern at "
            "once. Four or five soaked faces are caught by cold moonlight and distant "
            "lightning, all fixed on the same spot out of frame — mouths open, eyes wide, "
            "and in every face something more than fear: the hurt of people who "
            "believe they have been left. One has both hands out, palms up, "
            "questioning. Water sloshes over the deck around their legs. Night, spray, "
            "torn black sky. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n5 — he stood up ----
    {
        "id": "v2-r011-b19", "out": "s19-he-stood-in-the-stern.jpeg", "seg": "n5 p1-p2",
        "window": "118.93-125.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "BOAT", "SEA-STORM-NIGHT"],
        "narration": ("He got up. He stood in the stern of a sinking boat, in the "
                      "middle of the worst storm those fishermen had ever seen."),
        "must_show": "him standing UP and steady on the raised stern of a boat that is pitching and full of water, while everyone else is crouching, gripping or down.",
        "must_not_show": "no halo, glare or rim-light; he is not braced against anything and not holding on — the contrast with the crouching men is the picture.",
        "scene": (
            "Jesus has risen and stands upright on the raised stern platform of the "
            "pitching boat, his soaked robe streaming and dragged sideways by the wind, "
            "his feet planted on the wet deck and both hands free at his sides — "
            "holding on to nothing. Below and in front of him every other man is down "
            "or gripping something: one crouched over an oar, one clutching the mast, "
            "one on his knees in the water on the deck. A wave stands white behind the "
            "stern. Torn black sky, lightning on the hills, cold moonlight. The camera "
            "is back far enough to see him head to sandals above them. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b20", "out": "s20-he-spoke-to-the-storm.jpeg", "seg": "n5 p3-p4",
        "window": "125.81-130.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BOAT", "SEA-STORM-NIGHT"],
        "narration": "And he did not speak to the men. He spoke to the storm.",
        "must_show": "SCRIPTURE-EXACT (v39): he has turned AWAY from the disciples to face out into the wind and the sea — his back or shoulder to them, addressing the storm itself.",
        "must_not_show": "no halo, glare or rim-light; he must NOT be facing the men — the direction he is turned is the whole beat.",
        "scene": (
            "Jesus has turned his whole body away from the men in the boat to face out "
            "over the stern into the oncoming wind and sea, seen from behind and to one "
            "side so his shoulder and the line of his jaw are visible against the "
            "storm. His robe and hair are driven straight back off him by the wind he "
            "is facing. Ahead of him is nothing but the black running water and the "
            "torn sky. The men behind him are dim shapes low in the hull. The camera is "
            "back far enough to hold him and the sea he is facing. He has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r011-b21", "out": "s21-peace-be-still.jpeg", "seg": "j1",
        "window": "130.74-134.50", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SEA-STORM-NIGHT"],
        "narration": "Peace, be still. (Mark 4:39)",
        "must_show": "close on Jesus speaking the words out into the storm — calm, level, quiet authority, one hand come up.",
        "must_not_show": "no halo, glare or rim-light; no light, wave, or force coming from his hand; no shouting or straining — it is said the way you speak to a dog you own.",
        "scene": (
            "Close on Jesus from the side, facing out into the wind, speaking two "
            "words. His face is completely calm and level — no strain, no shouting, no "
            "effort at all — his eyes steady on the water ahead of him, and one hand "
            "has come up and open in front of him, low and unhurried. Water streams "
            "off his hair and beard and the wind drives everything sideways past him. "
            "Nothing is coming out of his hand. Cold moonlight and a flicker of "
            "lightning are the only light."
        ),
    },
    # ------------------------------------------------- n6 — the great calm ----
    {
        "id": "v2-r011-b22", "out": "s22-the-wind-quit.jpeg", "seg": "n6 p1",
        "window": "134.50-135.82", "wide": True, "jesus": False, "ref": False,
        "locks": ["BOAT", "SEA-CALM-NIGHT"],
        "narration": "And the wind quit.",
        "must_show": "the instant of stopping caught mid-air — the last wave collapsing with nothing holding it up, spray still hanging, the sail's lashings gone slack.",
        "must_not_show": "not still stormy and not yet calm — this frame is the exact hinge; do not put Jesus in it.",
        "scene": (
            "The exact instant. A steep black wave just off the bow is collapsing in "
            "on itself with no wind left to hold it up, its white crest slumping and "
            "tearing apart, and a whole sheet of thrown spray still hangs motionless in "
            "the air above water that has already gone slack underneath it. The lashed "
            "sail has dropped loose against the mast and a rope end that was streaming "
            "straight out has fallen limp. Cold moonlight through a widening tear in "
            "the cloud."
        ),
    },
    {
        "id": "v2-r011-b23", "out": "s23-glass-flat-under-stars.jpeg", "seg": "n6 p2",
        "window": "135.82-145.27", "wide": True, "jesus": False, "ref": False,
        "locks": ["BOAT", "SEA-CALM-NIGHT"],
        "narration": ("The sea fell flat — glass flat — with stars where the storm had "
                      "been, and the only sound left was water dripping off the ropes."),
        "must_show": "DEAD FLAT BLACK WATER under a sky full of stars, the boat motionless, and water still dripping off the slack rigging.",
        "must_not_show": "NO sunrise, NO dawn band, NO warm colour on the horizon — the narration says STARS, and this is the frame most likely to drift. Do not put Jesus in it.",
        "scene": (
            "A wide view across water gone absolutely flat and still, black and "
            "polished as glass from the hull right out to the black hills. The storm "
            "cloud has torn open overhead and the whole sky is full of cold hard "
            "stars, every one of them reflected unbroken below, so the boat sits "
            "motionless between two skies. Water still runs and drips from the slack "
            "ropes and the lashed sail, each drop making one small ring in the "
            "mirror. Moonlight lays one long unwavering silver line down the water. "
            "There is no light at all on the horizon."
        ),
    },
    {
        "id": "v2-r011-b24", "out": "s24-it-obeyed.jpeg", "seg": "n6 p3-p6",
        "window": "145.27-155.56", "wide": True, "jesus": False, "ref": False,
        "locks": ["BOAT", "SEA-CALM-NIGHT"],
        "narration": ("Sailors will tell you the waves keep rolling for hours after a "
                      "wind dies. These didn't. The lake did not calm down. It obeyed."),
        "must_show": "the water RIGHT AT THE HULL — no swell at all, not even a residual roll; the waterline against the planks perfectly still, as if painted.",
        "must_not_show": "no leftover swell, no rocking, no wake — the total absence of motion is the entire argument. Do not put Jesus in this frame.",
        "scene": (
            "Close on the waterline where the black sea meets the wooden planking of "
            "the hull. The surface is absolutely motionless against the boat — no "
            "swell, no roll, not even the smallest lap of water on the timber, the "
            "waterline sitting as still and hard-edged as if it had been painted on. "
            "Stars are reflected perfectly in the black glass right up to the planks. "
            "A single drop falls from the rail above and its rings spread out across "
            "an otherwise flawless mirror. Cold starlight lies along the wet wood."
        ),
    },
    # -------------------------------------------- n7 / j2 — he turned to them ----
    {
        "id": "v2-r011-b25", "out": "s25-he-turned-to-his-friends.jpeg", "seg": "n7",
        "window": "155.56-162.78", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-CALM-NIGHT"],
        "narration": ("Then he turned to his friends — soaked, shaking, still gripping "
                      "the ropes — and he asked them, gently:"),
        "must_show": "he turns back from the sea to face the men, who are still braced and gripping ropes and rails for a storm that has already stopped.",
        "must_not_show": "no halo, glare or rim-light; the men must still be in storm postures — that is the joke and the tenderness of the moment.",
        "scene": (
            "Jesus has turned back from the stern rail to face the men in the boat. "
            "They are all still exactly as the storm left them — one clamped around "
            "the mast with both arms, Peter half crouched with a white-knuckled fist "
            "still locked on a rope that runs up to the rigging, another braced with a "
            "foot against the hull, all of them soaked and shaking and staring at him "
            "with the water dead flat and starlit all around the boat. Nobody has let "
            "go yet. The camera is back far enough to hold Jesus and the men head to "
            "sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b26", "out": "s26-why-are-ye-so-fearful.jpeg", "seg": "j2",
        "window": "162.78-168.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SEA-CALM-NIGHT"],
        "narration": ("Why are ye so fearful? how is it that ye have no faith? "
                      "(Mark 4:40)"),
        "must_show": "⚠️ THE NARRATION SAYS HE ASKED IT GENTLY. Close on Jesus asking — warm, puzzled, genuinely questioning, no rebuke anywhere in the face.",
        "must_not_show": "NOT stern, NOT exasperated, NOT disappointed, NOT a telling-off. If this face reads as a scolding the video's point is lost — the narration says outright he never scolded them. No halo, glare or rim-light.",
        "scene": (
            "Close on Jesus's face in the starlight, soaked through, asking them "
            "something. His expression is warm and open and genuinely puzzled — brows "
            "lifted in the middle rather than drawn down, mouth soft, head tilted a "
            "little to one side, eyes moving from face to face and actually wanting an "
            "answer. There is no anger and no disappointment anywhere in it. Water "
            "still runs from his hair. The flat starlit sea is soft behind him."
        ),
    },
    # ---------------------------------------- n8 — where he asked it from ----
    {
        "id": "v2-r011-b27", "out": "s27-standing-in-their-boat.jpeg", "seg": "n8 p1-p2",
        "window": "168.20-174.07", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "BOAT", "SEA-CALM-NIGHT"],
        "narration": ("Hear where he asked that from. Standing in their boat, on the "
                      "sea he had just flattened to save them."),
        "must_show": "him standing IN the swamped boat with them — water still over the deck around everyone's feet, the flat sea he just stilled all around.",
        "must_not_show": "no halo, glare or rim-light; he is inside the hull with them, not above or apart from them.",
        "scene": (
            "Jesus stands in the middle of the boat among the men, the black water "
            "from the storm still lying across the deck timbers around all of their "
            "feet, the bailing scoops still floating in it. The sea outside the hull is "
            "dead flat and full of reflected stars in every direction. He is as soaked "
            "and dishevelled as any of them and standing on the same wet planking. The "
            "camera is back far enough to hold him and the men and the mirror-still "
            "water around the boat. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b28", "out": "s28-he-came-through-it-with-them.jpeg", "seg": "n8 p3-p4",
        "window": "174.07-182.28", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BOAT", "SEA-CALM-NIGHT"],
        "narration": ("He didn't ask it from the shore. He came through the storm with "
                      "them — and then he asked why the fear had gotten so much bigger "
                      "than their trust."),
        "must_show": "a very wide view proving WHERE they are: the boat alone far out in the middle of the black flat lake, with the shore a distant line on every side.",
        "must_not_show": "they must NOT be near land — the distance from the shore is the entire argument of this beat; no dawn colour anywhere.",
        "scene": (
            "A very wide night view from well back and a little above. The single "
            "fishing boat sits alone far out in the middle of an enormous flat black "
            "lake, its wet hull outlined by moonlight, the men inside it only small "
            "shapes. The black hills that ring the water stand a long way off on every "
            "side with no light on them at all. The whole sky of hard cold stars "
            "stands above and is reflected below. There is nothing else anywhere. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b29", "out": "s29-bigger-than-it.jpeg", "seg": "n8 p5-p7",
        "window": "182.28-189.68", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-CALM-NIGHT"],
        "narration": ("He never said the storm wasn't real. He never scolded them for "
                      "waking them. He was simply bigger than it."),
        "must_show": "Jesus's hand come to rest on Peter's shoulder — the storm acknowledged, the man not corrected; steadiness rather than reproach.",
        "must_not_show": "no halo, glare or rim-light; no wagging finger, no folded arms, nothing corrective anywhere in the frame.",
        "scene": (
            "Close on the two of them in the starlight. Jesus has laid one hand on "
            "Peter's shoulder where he still crouches gripping the rope, and Peter has "
            "turned his soaked shaking face up to him. Jesus's expression is calm and "
            "steady and entirely without reproach, and his hand is heavy and reassuring "
            "on the shoulder. Neither of them is speaking. Water drips from both of "
            "them onto the wet deck. The flat starlit sea is soft beyond the rail. Each "
            "hand has five fingers."
        ),
    },
    # -------------------------------------- n9 — the fear changed direction ----
    {
        "id": "v2-r011-b30", "out": "s30-it-changed-direction.jpeg", "seg": "n9 p1",
        "window": "189.68-195.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "SEA-CALM-NIGHT"],
        "narration": ("And then a strange thing happened: the fear didn't leave the "
                      "boat — it changed direction."),
        "must_show": "the faces changing — the terror of the storm becoming something else entirely: awe, and a new and different fear, aimed at the man in the boat.",
        "must_not_show": "the fear must NOT simply be relief or joy — Mark says they feared exceedingly AFTER the calm; do not put Jesus in this frame.",
        "scene": (
            "Close on Peter and John in the starlight, both still soaked and shaking. "
            "The panic has gone out of their faces and been replaced by something "
            "colder and stranger — Peter has gone completely still with his eyes wide "
            "and fixed on a point out of frame and his mouth slightly open, and John "
            "has drawn back a little, one hand come up part way to his own chest. "
            "Neither of them looks relieved. They look at the thing beside them the way "
            "men look at something they do not have a category for. Flat black water "
            "and cold starlight behind them."
        ),
    },
    {
        "id": "v2-r011-b31", "out": "s31-they-asked-each-other.jpeg", "seg": "n9 p2",
        "window": "195.97-204.01", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "ANDREW", "JOHN", "DISCIPLES", "BOAT", "SEA-CALM-NIGHT"],
        "narration": ("Mark says they feared exceedingly — more awe after the calm than "
                      "in the storm — and they asked each other:"),
        "must_show": "the men turned to EACH OTHER rather than to him — heads together, low urgent talk, glancing back over their shoulders at the stern.",
        "must_not_show": "they are NOT addressing Jesus; v41 says they said it one to another. Do not put Jesus in this frame.",
        "scene": (
            "In the still boat under the stars the men have drawn together in the bow "
            "away from the stern, heads close, talking low and urgently to each other "
            "with their hands moving. Two of them are glancing back over their "
            "shoulders toward the stern out of frame as they speak. Nobody is looking "
            "at anybody else's face for long. The water lies dead flat and starlit "
            "beyond the gunwale and moonlight catches their wet faces. The camera is "
            "back far enough to hold the group inside the hull. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r011-b32", "out": "s32-what-manner-of-man.jpeg", "seg": "s41",
        "window": "204.01-209.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANDREW", "SEA-CALM-NIGHT"],
        "narration": ("What manner of man is this, that even the wind and the sea obey "
                      "him? (Mark 4:41)"),
        "must_show": "close on one man saying it to the others — the question genuinely open, spoken low, nobody with an answer.",
        "must_not_show": "no triumph or celebration in the face; do not put Jesus in this frame.",
        "scene": (
            "Close on Andrew's face in the moonlight, turned toward the men beside "
            "him, speaking low. His soaked hair is flat to his head, his eyes are wide "
            "and searching and moving from one face to another, and his mouth is "
            "mid-question. There is no answer in his expression and none in the "
            "half-lit shoulders of the men around him. Cold starlight on the flat "
            "water beyond."
        ),
    },
    # ------------------------------------------------- n9b — the old psalm ----
    {
        "id": "v2-r011-b33", "out": "s33-they-knew-the-psalm.jpeg", "seg": "n9b p1-p2",
        "window": "209.88-216.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SEA-CALM-NIGHT"],
        "narration": ("These men knew their scriptures. They knew the old psalm that "
                      "says it is God who stills the storm to a whisper."),
        "must_show": "the recognition arriving — a face going slowly slack as an old remembered line lines up with what he has just watched happen.",
        "must_not_show": "no scroll, no book, no text in the frame — the remembering is on the face; do not put Jesus in it.",
        "scene": (
            "Very close on Peter's face in the starlight. He has gone completely still "
            "and his eyes have unfocused and drifted off to nothing, his lips just "
            "moving — a man silently retrieving a line he has known since he was a boy "
            "and setting it beside what he has just watched happen. The blood has gone "
            "out of his face. Water still runs slowly down his cheek. The flat starlit "
            "black water is soft behind him."
        ),
    },
    {
        "id": "v2-r011-b34", "out": "s34-a-man-in-dripping-clothes.jpeg", "seg": "n9b p3",
        "window": "216.29-221.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-CALM-NIGHT"],
        "narration": ("And now they were staring at a man in dripping clothes who had "
                      "just done it."),
        "must_show": "the closing frame: every man in the boat staring at Jesus — and Jesus completely ordinary, soaked, dishevelled, wringing water out of his sleeve, entirely unremarkable.",
        "must_not_show": "no halo, glare or rim-light and nothing majestic about him — the ENTIRE point of the frame is the gap between what he just did and how utterly ordinary he looks. If he looks grand, the frame is a fail.",
        "scene": (
            "In the motionless boat under a sky full of stars, every man is staring at "
            "Jesus. He stands in the middle of the hull entirely unremarkable — soaked "
            "to the skin, his hair plastered flat and dripping, his robe hanging heavy "
            "and dark with water, in the middle of the small ordinary act of squeezing "
            "the water out of one sleeve with his other hand, not even looking up. "
            "Around him the same seven soaked companions are naturally distributed "
            "through the boat, pausing in the places where the storm left them rather "
            "than forming a circle or a posed tableau. The "
            "dead flat sea and the reflected stars "
            "surround the boat. The camera is back far enough to hold the whole boat "
            "and every figure head to feet. Every figure has two arms, two hands and "
            "one head."
        ),
    },
]

# Every generated beat attaches the actual canonical sheets for the named people
# it depicts.  Text descriptions alone were the cause of the changing faces and
# beards in the rejected videos.
_REF_BY_LOCK = {
    "PETER": _sheet("peter"),
    "ANDREW": _sheet("andrew"),
    "JAMES-Z": _sheet("james"),
    "JOHN": _sheet("john-beloved"),
}
for _beat in BEATS:
    _locks = _beat.get("locks", [])
    _refs = list(_beat.get("char_refs", []))
    if "DISCIPLES" in _locks:
        _refs.extend(EARLY_COMPANY_REFS)
    else:
        for _lock in _locks:
            _refs.extend(_REF_BY_LOCK.get(_lock, []))
    # Stable de-duplication preserves the gospel roster order.
    _beat["char_refs"] = list(dict.fromkeys(_refs))
    _asset = Path(__file__).resolve().parent / "assets" / _beat["out"]
    if _asset.is_file():
        _beat["rough_ref"] = str(_asset)

# First-pass visual QC corrections.  `v2_prompt.py --redo` attaches the current
# production frame first and makes only the named repair.  These are kept in the
# beat source so the accepted frame is reproducible instead of depending on an
# unrecorded chat instruction.
_REDO_PROMPTS = {
    "v2-r011-b16": (
        "Cameron's named defect: the man being shaken awake read as a stranger, not "
        "Jesus. The reclining man on the stern cushion MUST be the exact attached Jesus "
        "reference face — long wet dark-brown wavy hair, full dark beard, warm "
        "olive-tan skin — and he is the ONLY man in the frame in a cream/off-white "
        "robe; every other man wears a coloured tunic (blue-grey, olive, ochre). Remove "
        "any second bearded cream-robed figure. Keep the rough panicked shaking, Peter's "
        "hand clamped on Jesus's shoulder, and the storm. Use the wired boat plate so "
        "the hull, planking and gunwale match every other boat frame. No lamp or fire."
    ),
    "v2-r011-b17": (
        "Reframe only slightly wider, from close face to chest-up. Keep Peter's "
        "canonical face, soaked blue-grey tunic, terror and accusation, but show a "
        "clear strip of the wet wooden gunwale and deck behind and below him so he is "
        "unmistakably standing inside the boat, never in the lake. No lamp or fire."
    ),
    "v2-r011-b18": (
        "Keep the same storm, camera direction and wounded reaction, but replace the "
        "near-duplicate men with a clearly cropped subset of five distinct companions "
        "from the attached cast board: different faces, ages, hair, beard states, "
        "builds and locked tunic colours. John is the young clean-shaven man. They are "
        "not a posed row and do not become twins. No lamp or fire."
    ),
    "v2-r011-b19": (
        "Keep Jesus standing at the stern and preserve the rough boat action, but the "
        "whole visible boat must contain exactly EIGHT men total: Jesus plus exactly "
        "seven distinct companions. Add the one missing companion in an open working "
        "space without crowding anyone. Only Jesus wears cream. Match Peter, Andrew, "
        "James, clean-shaven John and Matthew to the attached cast board; nobody is a "
        "clone and nobody forms a circle. No modern metal anchor."
    ),
    "v2-r011-b20": (
        "Preserve this successful wide photograph, Jesus's position, the boat and the "
        "storm. Correct only the headcount: exactly EIGHT adult men total, Jesus plus "
        "seven companions. Remove the extra rearmost disciple cleanly and reconstruct "
        "the boat behind him. Do not add or move anyone else. Only Jesus wears cream."
    ),
    "v2-r011-b22": (
        "Replace the failed giant curling wave with a tight environmental detail of "
        "only the wet bow, the lower furled sail, slack rope and nearby water. Show one "
        "LOW remnant crest, no more than knee-high, collapsing into flat water while "
        "spray drops vertically. No towering breaker, no frozen wall of water and no "
        "people in frame. Every rope remains attached inside the boat and none enters "
        "the lake."
    ),
    "v2-r011-b25": (
        "Preserve the exact eight-man composition and calm setting. Peter's visible "
        "hand must be a natural bare wet hand with normal skin, not white, wrapped, "
        "bandaged or injured. Replace the modern metal anchor at the bow with one "
        "plain first-century stone anchor. Do not change any face, garment or pose."
    ),
    "v2-r011-b26": (
        "Keep the gentle close composition but correct Jesus to the exact attached "
        "Jesus reference face, long wet dark-brown hair, full beard and natural "
        "green-amber eyes. The sail behind him is fully furled and lashed to the mast, "
        "never raised. Keep the gunwale visible so he remains clearly inside the boat."
    ),
    "v2-r011-b27": (
        "Restage the same exact EIGHT men as a candid post-storm moment, not a circle "
        "or devotional tableau. Put Jesus off-centre near the stern. Peter sits by the "
        "steering position; Andrew coils a rope inside the hull; James gathers a wet "
        "net; clean-shaven John bails remaining deck water outward; frightened Matthew "
        "sits catching his breath; the two unnamed men separately check the gunwale "
        "and wring a soaked mantle. At most two men glance toward Jesus. Use the "
        "attached canonical faces and blue-grey, olive, ochre, pale-blue and teal "
        "wardrobes. Only Jesus wears cream. Replace any metal anchor with a stone one."
    ),
    "v2-r011-b29": (
        "Preserve both men, their faces, positions and clothing colours. Correct only "
        "the post-storm continuity: Jesus's cream robe and Peter's blue-grey tunic are "
        "visibly soaked, heavy and darker in irregular wet patches; their hair and "
        "beards are plastered wet and dripping. Do not change their faces or pose."
    ),
    "v2-r011-b32": (
        "Preserve Andrew's canonical face, expression, olive tunic and the surrounding "
        "cropped companions. Remove the rope draped over the gunwale and into the lake, "
        "reconstructing clean wet wood and flat reflected water. No rope crosses the "
        "rail or touches the lake."
    ),
    "v2-r011-b33": (
        "Correct Peter to the exact attached canonical Peter: a sturdy mid-thirties "
        "man with thick dark curly hair, full DARK beard without grey, weathered olive "
        "skin and his blue-grey tunic. Preserve the close composition, wet skin and "
        "quiet remembering expression. He must not look elderly or pale."
    ),
    "v2-r011-b34": (
        "Preserve the exact eight-man distribution, Jesus wringing his sleeve and the "
        "men's unposed positions. Jesus alone wears his recognizable undyed CREAM robe; "
        "it is soaked and darkened by water but remains visibly cream, never brown. "
        "Match his attached face. Remove the rope tied at the bow and dropping into the "
        "lake, reconstructing the bow and mirror-flat water. No rope touches the lake."
    ),
}
for _beat in BEATS:
    if _beat["id"] in _REDO_PROMPTS:
        _beat["redo_prompt"] = _REDO_PROMPTS[_beat["id"]]

# The failed b22 first pass is too structurally wrong to preserve as an edit
# reference.  Generate its corrected close environmental detail from the prompt.
for _beat in BEATS:
    if _beat["id"] == "v2-r011-b22":
        _beat["redo_source"] = "none"


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "BOAT": "PLACE-REF/boat.jpeg",  # build-11-storm s07-peter-andrew-james-john (manual)
}
# === end PLACE-PLATES ===
