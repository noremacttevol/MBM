#!/usr/bin/env python3
"""Expand the lock tokens in PROMPTS.md into full paste-ready Flow prompts,
one flat block per still/clip, written to FLOW-READY.txt. The browser types
these verbatim into Flow (Flow does not understand [TOKEN] placeholders).
"""
import re

STILL_STYLE = (
    "Beautiful hand-painted 2D animation style, reverent and warm, like a "
    "classic illustrated storybook of scripture brought to life. Soft "
    "painterly brushstroke textures, glowing golden light, muted earth tones "
    "with warm gold highlights. First-century Judea. Sacred, hushed tone. Not "
    "photorealistic. No text or captions in the image. Historically modest "
    "clothing: rough-woven wool and linen in undyed earth colors. No modern "
    "objects."
)
CLIP_STYLE = (
    "Beautiful hand-painted 2D animation style, reverent and warm, like a "
    "classic illustrated storybook of scripture brought to life. Soft "
    "painterly brushstroke textures, glowing golden light, muted earth tones "
    "with warm gold highlights. First-century Judea. Slow, tender movement. "
    "Sacred, hushed tone. Not photorealistic. No text or captions in the "
    "image. Historically modest clothing: rough-woven wool and linen in "
    "undyed earth colors. No modern objects."
)

LORD = (
    "a warm Middle Eastern man with dark shoulder-length hair, in an undyed "
    "cream wool robe with a simple mantle, always seen from behind or over his "
    "shoulder with the back of his head to the camera and kept away from view; "
    "his olive-brown skin and hands may show, never pale or European, no glow "
    "or halo around him, exactly two arms, two hands, two legs"
)
CENTURION = (
    "a broad weathered Roman officer in his late forties, sun-browned skin, "
    "close-cropped iron-gray hair, clean-shaven, wearing worn first-century "
    "Roman military dress: a bronze-and-leather segmented cuirass over a deep "
    "oxblood-red wool tunic, a deep-red wool military cloak pinned at one "
    "shoulder, leather strips hanging at his waist and shoulders, laced "
    "leather sandal-boots, and a sheathed short sword at his left hip, exactly "
    "two arms, two hands, two legs"
)
SERVANT = (
    "a young household servant in his early twenties, olive skin turned gray "
    "and clammy with sickness, dark hair damp with sweat, in a plain undyed "
    "knee-length tunic, lying limp and paralyzed on a low straw pallet with a "
    "thin blanket, weak and suffering but dignified with no wounds or "
    "disfigurement, exactly two arms, two hands, two legs"
)
SERVANT_HEALED = (
    "the same young man, his olive skin warm and living again, eyes open and "
    "clear, sitting up or standing steady, exactly two arms, two hands, two "
    "legs"
)
SETTING = (
    "a first-century lakeside town on the north shore of the Sea of Galilee, "
    "houses of dark basalt stone, narrow packed-earth streets, palm and fig "
    "trees, fishing nets, the wide blue lake glinting in the distance, bright "
    "honest daylight and a blue-white sky"
)
SOLDIERS = (
    "two ordinary Roman legionaries in plainer bronze-and-leather armor with "
    "no crest on their helmets"
)

TOK = {
    "[STILL STYLE BLOCK]": STILL_STYLE,
    "[CLIP STYLE BLOCK]": CLIP_STYLE,
    "[LORD LOCK]": LORD,
    "[CENTURION LOCK]": CENTURION,
    "[SERVANT LOCK — HEALED]": SERVANT_HEALED,  # must run BEFORE [SERVANT LOCK]
    "[SERVANT LOCK]": SERVANT,
    "[SETTING]": SETTING,
    "[SOLDIERS: two ordinary Roman legionaries in plainer bronze-and-leather "
    "armor with NO crest on their helmets]": SOLDIERS,
}

# Beat bodies copied verbatim from PROMPTS.md (token form).
BEATS = {
"s1": "[STILL STYLE BLOCK] Bright honest midday light on [SETTING]. Walking into the town at the head of a small band of travelers, seen from behind with the back of his head and cream-robed shoulders to the camera, is [LORD LOCK], stepping gently forward as the group follows behind him. Off to one side, a single Roman soldier in bronze-and-leather armor stands guard beside a tall military standard, marking this as a town under Roman occupation. The lake and low basalt rooftops spread ahead of them. Every figure has exactly two arms and two hands. One single continuous scene painted edge to edge.",
"s2": "[STILL STYLE BLOCK] The dim plain interior of a Roman officer's stone house, soft daylight falling through a high window. [SERVANT LOCK] lies on the low straw pallet, his body limp and paralyzed, jaw tight with pain, skin gray with fever. Set aside on a bench nearby are a bronze cuirass, a deep-red folded cloak, and a crested helmet — the officer's armor, laid down while he tends the boy. A shallow basin of water and a damp cloth rest on the floor beside the pallet. No one else is in the room. Exactly one young man in the frame, with two arms, two hands, two legs. One single continuous scene painted edge to edge.",
"s3": "[STILL STYLE BLOCK] Bright daylight in a narrow basalt-stone street of [SETTING]. [CENTURION LOCK] strides down the middle of the street with his crested helmet ON his head, his red cloak swinging, his jaw set and eyes forward. Along both sides of the street, Jewish villagers in earth-toned wool and linen pull back against the walls and stare at him — a mother drawing her child close, men with hard wary eyes, an old woman clutching a water jar. Every villager's attention is fixed on the Roman officer. Ahead of him at the far end of the street, a small crowd is gathering. Each person has exactly two arms and two hands. One single continuous scene painted edge to edge.",
"s4": "[STILL STYLE BLOCK] Bright daylight at the edge of the gathered crowd. The camera stands behind [LORD LOCK]: the back of his head and cream-robed shoulder sit soft in the lower corner of the frame, away from view. Facing him across a small gap, [CENTURION LOCK] bows his head low, his crested helmet removed and held under one arm, his other fist pressed to his chest over his heart, his weathered face full of plain honest conviction. Around them, watching Jewish villagers register astonishment that a Roman commander would bow. Every gaze in the crowd is turned toward the robed man's back. Each person has exactly two arms and two hands. One single continuous scene painted edge to edge.",
"s5": "[STILL STYLE BLOCK] Bright daylight. Seen from behind with the back of his head and cream-robed shoulders to the camera, [LORD LOCK] lifts one olive-brown hand and arm and opens it outward toward the town beyond in a gentle offer to come. Before him, [CENTURION LOCK] stands close, head lowered, helmet under his arm, looking toward the robed figure. A few followers in undyed wool stand near, watching. Each person has exactly two arms and two hands. One single continuous scene painted edge to edge.",
"s6": "[STILL STYLE BLOCK] Bright daylight. In the foreground, seen from behind, the cream-robed shoulder and olive-brown hand of [LORD LOCK] sit soft and close, the back of him to the camera and away from view. Filling the frame beyond, [CENTURION LOCK] lifts one open hand to gently STAY him — a respectful halt, palm up — his head bowed, his weathered clean-shaven face lit with complete quiet conviction, his crested helmet under his other arm. Behind the officer, blurred watching villagers show surprise. The composition centers on the Roman's face and his staying hand. Each person has exactly two arms and two hands. One single continuous scene painted edge to edge.",
"s7": "[STILL STYLE BLOCK] Bright daylight in a Roman garrison courtyard of basalt stone. [CENTURION LOCK] stands at the center, one arm extended in a firm pointing command. [SOLDIERS: two ordinary Roman legionaries in plainer bronze-and-leather armor with NO crest on their helmets] obey at once — one striding away out of the courtyard at his order, mid-purposeful-step, the other halted rigidly at attention facing him. A household servant crosses in the background carrying a water jar to a task. Every figure is oriented to the centurion's command; the scene reads clearly as men obeying a word without being touched. Each person has exactly two arms, two hands, two legs. One single continuous scene painted edge to edge.",
"s8": "[STILL STYLE BLOCK] Bright daylight. A half-ring of following disciples and villagers in undyed wool fills the frame, their faces turned in a row toward one point — disbelief, offense, and slow wonder moving across them. At the point where every gaze converges, seen from behind with the back of his head and cream-robed shoulders to the camera, stands [LORD LOCK], one olive-brown hand lifted toward the armored Roman officer who stands at attention to the side. The ring of astonished human faces carries the frame; every one of them looks toward the robed figure's back. Each person has exactly two arms and two hands. One single continuous scene painted edge to edge.",
"s9": "[STILL STYLE BLOCK] A wide honest-daylight vista under an open blue sky: the lakeside town small in the middle distance beside the blue Sea of Galilee, and two long dusty roads reaching away to far horizons on the left and the right. Down both roads, from opposite directions, come small scattered groups of travelers of many different nations and dress — people of varied skin tones and robes — all walking calmly toward the town and the lake. The picture is peaceful, spacious, and inclusive, warm daylight everywhere, no sunset or sunrise coloring. Each person has exactly two arms and two hands. One single continuous scene painted edge to edge.",
"s10": "[STILL STYLE BLOCK] Bright daylight. Seen from behind with the back of his head and cream-robed shoulders to the camera, [LORD LOCK] turns back toward [CENTURION LOCK] and lifts one olive-brown hand gently toward him in a warm, final word. The centurion is straightening from his bow, helmet under his arm, relief rising in him, his body angling to turn for home. A few followers watch softly behind. Each person has exactly two arms and two hands. One single continuous scene painted edge to edge.",
"s11": "[STILL STYLE BLOCK] The same dim stone room of the officer's house, soft daylight through the high window. [SERVANT LOCK — HEALED] is caught in the moment of healing: half-risen on the straw pallet, propped on one steady hand, his chest filling with a sudden deep clean breath, warm living color flooding back into his face, his eyes opening wide and clear, wonder breaking across him. The thin blanket slides from his shoulders. He is completely alone in the room — no one else is present, no visitor, no other figure. Exactly one young man in the frame, with two arms, two hands, two legs. One single continuous scene painted edge to edge.",
"s12": "[STILL STYLE BLOCK] Bright daylight spilling through a stone doorway. [CENTURION LOCK] has just arrived home and stops dead in the doorway, his red cloak still swinging, helmet under his arm — and across the plain room stands [SERVANT LOCK — HEALED] on his own two feet, well and steady, mid-ordinary-task with a water jar in his hands. The two men look straight at each other. The hard weathered officer raises his free hand to cover his mouth, his soldier's composure quietly breaking into overwhelmed relief. Two figures in the frame, each with two arms and two hands. One single continuous scene painted edge to edge.",
"CLIP_A": "[CLIP STYLE BLOCK] Inside a dim first-century stone room lit softly by daylight from a high window, a young household servant in his early twenties with olive skin and dark sweat-damp hair, in a plain undyed knee-length tunic, lies limp and paralyzed on a low straw pallet. Over the course of the video, warm living color floods slowly back into his gray face, he draws one long clean breath that fills his chest, his eyes open wide and clear, and he slowly pushes himself up to sit on the pallet, propped on one steady hand, wonder breaking across his face as the thin blanket slides from his shoulders. He is completely alone in the room the entire time — no other person appears. Exactly one young man, with two arms, two hands, two legs, throughout. The change moves in one direction: from limp and gray to breathing, sitting up, and whole.",
"CLIP_B": "[CLIP STYLE BLOCK] A broad weathered Roman officer in his late forties with close-cropped iron-gray hair, clean-shaven, wearing a bronze-and-leather segmented cuirass over a deep oxblood-red wool tunic, a deep-red military cloak, and a crested helmet on his head, a sheathed sword at his hip, exactly two arms, two hands, two legs, strides steadily down the middle of a narrow first-century basalt-stone village street in bright daylight, his cloak swinging with each step. Along both walls, Jewish villagers in earth-toned wool and linen pull back and stare at him — a mother drawing a child close, men with wary eyes — their heads turning to follow him as he passes. He keeps walking forward toward a small crowd gathering at the far end of the street, jaw set, eyes ahead. His stride cycles fully, each leg swinging in turn, feet leaving the ground. Everyone moves and looks in a way consistent with a lone Roman officer walking a hostile street.",
}


def expand(text):
    for tok, val in TOK.items():
        text = text.replace(tok, val)
    return re.sub(r"\s+", " ", text).strip()


order = ["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12",
         "CLIP_A","CLIP_B"]
with open("FLOW-READY.txt", "w") as f:
    for k in order:
        f.write(f"===== {k} =====\n{expand(BEATS[k])}\n\n")
print("wrote FLOW-READY.txt")
for k in order:
    print(f"{k}: {len(expand(BEATS[k]))} chars")
