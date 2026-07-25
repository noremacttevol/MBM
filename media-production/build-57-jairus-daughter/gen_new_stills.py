#!/usr/bin/env python3
"""Generate the 10 NEW stills for build-57 (STORY-BLUEPRINT 21-beat prescription).

Adds the missing beats the narration paints but the old 9-still cut skipped:
pushing through the crowd, the girl fading at home, messengers on the road, Jairus
breaking (the hinge), lifting his eyes, the mourners weeping, the mourners laughing,
put outside, the girl's eyes opening, and the parents' wonder.

Drives flow_driver.py gen (Nano Banana, 9:16). Jesus shots attach the master ref;
scene shots attach the matching existing still so the room/cast/Jairus stay locked.
Usage: python3 gen_new_stills.py [slug ...]   (no args = all 10)
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE.parent / "flow_driver.py"
MP = HERE.parent  # media-production
JESUS = str(MP / "JESUS-MASTER-REF" / "jesus-face.jpeg")
JAIRUS_REF = str(MP / "CHARACTERS" / "jairus" / "three-quarter.jpeg")
A = HERE / "assets"

STYLE = (
    "Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
    "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
    "textures, glowing golden light, muted earth tones with warm gold highlights. "
    "First-century Judea. Sacred, hushed tone. Not photorealistic. No text or captions "
    "in the image. Historically modest clothing: rough-woven wool and linen in undyed "
    "earth colors. No modern objects."
)
ANTI = (
    "ONE single full-frame illustration of a single frozen instant — no comic strip, "
    "no panels, no stacked or side-by-side frames, no dividing lines."
)
JLOCK = (
    "JESUS LOCK v3: the SAME man as the attached JESUS-MASTER-REF images — identical "
    "face, hair and beard in every picture: a Middle Eastern Jewish man of about "
    "thirty-three, warm tan olive-brown skin, shoulder-length dark brown-black wavy "
    "hair, a full dark beard, kind warm BROWN eyes, one plain undyed off-white cream "
    "wool robe (only he wears cream). No halo, no glow. Never caucasian, never pale, "
    "never blue-eyed, never blond."
)
TAIL = (
    "The painting fills the entire frame edge to edge with no border, no frame and no "
    "cream margin. Every figure has two arms, two hands, two legs and one head. One "
    "single continuous scene painted edge to edge."
)
JAIRUS = (
    "Jairus, a dignified first-century synagogue ruler of middle years with a full "
    "well-kept dark beard and warm olive skin, in a fuller formal robe of deep "
    "indigo-blue and brown with a woven prayer-fringe, clearly not cream"
)
MOTHER = "the girl's mother, head covered, in muted dun and grey-blue, clearly not cream"
GIRL = (
    "the little girl of about twelve, dark hair, in a simple muted pale grey and soft "
    "dun dress, clearly not cream"
)


def jesus_scene(body):
    return f"{STYLE} {ANTI} {body} {JLOCK} {TAIL}"


def plain_scene(body):
    return f"{STYLE} {ANTI} {body} {TAIL}"


# slug -> (prompt, [refs])
SHOTS = {
    # BEAT 1 — n1: pushing through the crowd
    "s1a-pushing-through-crowd": (jesus_scene(
        f"A crowded pale-stone street of a first-century Galilean lakeside town in "
        f"bright daylight. {JAIRUS} is forcing his way forward through a dense press of "
        f"ordinary Galilean townsfolk, his bearded face taut with desperate urgency, one "
        f"arm outstretched ahead of him, straining to reach Jesus. Jesus stands a little "
        f"ahead among the crowd, seen from three-quarter, his face clearly visible, calm "
        f"and turning with compassion toward the approaching father. He wears one plain "
        f"undyed off-white cream wool robe, bare-headed. The crowd presses close all "
        f"around in dun, faded brown, ochre, olive, grey-blue and deep indigo wool, "
        f"head-coverings and short hair, none in cream. Bright warm daylight. Only Jesus "
        f"wears cream."), [JESUS, JAIRUS_REF, str(A / "s1-jairus-at-his-feet.jpeg")]),

    # BEAT 4 — n1b: the girl fading at home (cutaway, no divine figure)
    "s1c-girl-fading-home": (plain_scene(
        f"Inside a modest, warm-lit first-century Galilean home, a quiet cutaway away "
        f"from the street. On a low bed-mat lies a gravely ill young girl of about "
        f"twelve, dark hair, in a simple muted pale grey and soft dun dress, clearly not "
        f"cream, her eyes closed, her face pale and weak, slipping toward death — "
        f"peaceful and dignified, never gruesome, no wound, no blood. {MOTHER} kneels "
        f"close beside the mat, bent over her in anguished tenderness, holding the "
        f"child's limp hand, her face streaked with fear and grief. A small window lets "
        f"in soft pale daylight. No divine figure appears in this frame. Nobody in the "
        f"frame wears off-white or cream."), [str(A / "s6-into-the-room.jpeg")]),

    # BEAT 6 — n3: messengers intercepting on the road (no divine figure)
    "s3a-messengers-on-road": (plain_scene(
        f"On the pale-stone road just outside the Galilean town in bright daylight. Two "
        f"messengers from the house have hurried up and intercepted {JAIRUS}, their "
        f"faces heavy and grave with sorrowful news, one lifting a hand as he begins to "
        f"speak — ordinary Galilean men in dun and faded brown, clearly not cream. "
        f"Jairus has stopped short, turning toward them, dread rising in his eyes but "
        f"his grief not yet broken open. Behind them the road and a few travellers in "
        f"earth tones, none in cream. No divine figure appears in this frame. Nobody in "
        f"the frame wears off-white or cream."),
        [JAIRUS_REF, str(A / "s3-the-worst-news.jpeg")]),

    # BEAT 8 — n3b: Jairus breaking (THE HINGE, his face; Jesus not shown / edge only)
    "s3b-jairus-breaking": (plain_scene(
        f"On the pale-stone road in bright daylight, framed close on {JAIRUS}. The worst "
        f"news has just landed: his face is breaking with grief and disbelief, eyes "
        f"squeezed shut, one hand rising to his chest, his whole body sagging under the "
        f"weight of a father who has just learned his only child is dead. His anguish "
        f"fills the frame. At the very edge of the frame, only the cream-robed shoulder "
        f"and back of a bare-headed man with shoulder-length dark hair is barely seen "
        f"from behind — his face is NOT shown. Muted earth-tone road behind. The moment "
        f"is heavy with loss."),
        [JAIRUS_REF, JESUS, str(A / "s3-the-worst-news.jpeg")]),

    # BEAT 10 — n3c: Jairus lifting his eyes, choosing to keep walking
    "s4a-jairus-lifts-eyes": (jesus_scene(
        f"On the road in warm daylight. {JAIRUS}, still grief-stricken and tear-streaked, "
        f"slowly lifts his eyes and looks forward down the road with a fragile, gathering "
        f"resolve — choosing to keep walking and keep trusting. Beside him Jesus walks "
        f"steadily, seen from three-quarter slightly behind the father, his face visible, "
        f"calm and quietly encouraging, one hand near Jairus' back. He wears one plain "
        f"undyed off-white cream wool robe, bare-headed. A hushed crowd follows in earth "
        f"tones, none in cream. Warm daylight. Only Jesus wears cream."),
        [JESUS, JAIRUS_REF, str(A / "s4-only-believe.jpeg")]),

    # BEAT 11 — n4: the mourners weeping and wailing (before Jesus speaks)
    "s5a-mourners-weeping": (jesus_scene(
        f"At the doorway and courtyard of {JAIRUS}' modest house in warm daylight. The "
        f"mourning has already begun: a cluster of first-century townsfolk weep and wail "
        f"loudly for the little girl, faces streaked with grief, some with hands raised "
        f"in lament, in mourning greys, dun and faded brown, clearly not cream. Jesus "
        f"and his small group are just arriving at the gate at one side of the frame, "
        f"seen from three-quarter, his face visible, calm amid the noise, not yet "
        f"speaking. He wears one plain undyed off-white cream wool robe, bare-headed. "
        f"Warm daylight, loud grief filling the courtyard. Only Jesus wears cream."),
        [JESUS, str(A / "s5-not-dead-but-sleeping.jpeg")]),

    # BEAT 13 — n4b: the mourners laughing / scoffing at him
    "s5b-mourners-laughing": (jesus_scene(
        f"At the doorway of the house in warm daylight. Having just heard that the child "
        f"'only sleeps,' several of the mourners now laugh and scoff openly at Jesus, "
        f"their faces twisted from grief into mocking disbelief, some shaking their "
        f"heads, some smirking scornfully — first-century townsfolk in mourning greys, "
        f"dun and faded brown, clearly not cream. Jesus stands steady and unshaken among "
        f"them, seen from three-quarter, his face visible, calm and patient, unmoved by "
        f"their scorn. He wears one plain undyed off-white cream wool robe, bare-headed. "
        f"Warm daylight. Only Jesus wears cream."),
        [JESUS, str(A / "s5-not-dead-but-sleeping.jpeg")]),

    # BEAT 14 — n5a: he put them all outside
    "s5c-put-them-outside": (jesus_scene(
        f"At the doorway of the house in warm daylight. Jesus is firmly and gently "
        f"putting the scoffing crowd out, one arm extended toward the gate, directing "
        f"the mourners away from the door — seen from three-quarter, his face visible, "
        f"calm and authoritative. He wears one plain undyed off-white cream wool robe, "
        f"bare-headed. The townsfolk turn and file out through the gate, grumbling and "
        f"reluctant, in mourning greys, dun and faded brown, clearly not cream. Behind "
        f"Jesus the doorway into the quiet house waits. Warm daylight. Only Jesus wears "
        f"cream."), [JESUS, str(A / "s5-not-dead-but-sleeping.jpeg")]),

    # BEAT 17 — n6a: the girl's eyes opening, first breath
    "s8a-eyes-opening": (jesus_scene(
        f"Inside the quiet, warm-lit room, framed close and tender. On the low bed-mat "
        f"{GIRL} is just coming back to life — her eyes opening for the first time, "
        f"drawing her first breath, warmth returning to her cheeks, wonder dawning on "
        f"her small face. Her face is the heart of the frame. Jesus kneels beside her "
        f"holding her small hand, seen from behind and three-quarter, his face turned "
        f"mostly away, tender and calm. He wears one plain undyed off-white cream wool "
        f"robe, bare-headed. Soft warm indoor light glows over the waking child. Only "
        f"Jesus wears cream."), [JESUS, str(A / "s7-talitha-cumi.jpeg")]),

    # BEAT 19 — n6c: the parents' wonder
    "s8b-parents-wonder": (jesus_scene(
        f"Inside the warm-lit room, alive with joy. {JAIRUS} and {MOTHER} gaze at their "
        f"living daughter with faces overwhelmed by disbelieving wonder and tears of "
        f"joy, reaching for her, beside themselves that the child they had already "
        f"grieved as dead is standing warm and alive before them. Their astonished, "
        f"joy-flooded faces are the heart of the frame. The girl of about twelve stands "
        f"alive and well in her muted pale grey and soft dun dress, clearly not cream. "
        f"Jesus stands a little back at one side, seen from three-quarter, his face "
        f"visible, warm and quietly glad. He wears one plain undyed off-white cream wool "
        f"robe, bare-headed. Warm golden indoor light. Only Jesus wears cream."),
        [JESUS, str(A / "s8-she-arose.jpeg")]),
}


def gen(slug):
    prompt, refs = SHOTS[slug]
    out = A / f"{slug}.jpeg"
    cmd = [sys.executable, str(DRIVER), "gen", "--prompt", prompt, "--out", str(out)]
    for r in refs:
        cmd += ["--ref", r]
    print(f"\n=== GEN {slug} ({len(refs)} refs) ===", flush=True)
    r = subprocess.run(cmd)
    ok = out.exists() and out.stat().st_size > 20000
    print(f"{'OK' if ok else 'FAIL'} {slug} rc={r.returncode}", flush=True)
    return ok


def main():
    slugs = sys.argv[1:] or list(SHOTS)
    bad = [s for s in slugs if not gen(s)]
    print(f"\nDONE. {len(slugs)-len(bad)}/{len(slugs)} ok. failed={bad}", flush=True)


if __name__ == "__main__":
    main()
