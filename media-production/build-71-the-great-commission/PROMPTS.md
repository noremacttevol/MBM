# STILL PROMPTS — Story Video #71: The Great Commission (matthew-28_the-great-commission)

PHASE-1 STILLS-ONLY (Law E): 8 painted 9:16 stills, Image mode. No motion clips.
Generate all 8 in Flow, save each to `assets/<name>.jpeg`, then `python3 build.py`.

## CREDIT LAW
Flow credits are PREPAID and EXPIRE MONTHLY — spend them on quality, don't hoard.
Use **Nano Banana Pro** for the figure/face-adjacent shots (s2, s3, s6, s7) and
crowds; Nano Banana 2 is fine for the landscapes (s1, s4). Only the paid Gemini
API is banned. Never call generations "0 credits/free".

## FACE-LAW — READ FIRST (this is the risen Christ)
The risen-jesus sheet is NOT yet rendered/approved, so **Jesus's face is NEVER
shown in this build.** Stage him ONLY from BEHIND, OVER-THE-SHOULDER (camera
behind him, the eleven facing past the camera at him), or at true DISTANCE. No
cheek, profile, eye, nose, or mouth — ever. No rim-light/halo/glow outlining his
head. He is a real warm Middle-Eastern man in ONE plain undyed off-white/cream
wool robe, LONG dark hair past the shoulders (JESUS LOOK STANDARD). Run
`python3 media-production/jesus_face_gate.py --dir build-71-the-great-commission`
— must exit 0 before any credit.

## CHARACTERS
- **Do NOT depict the Father or the Holy Ghost** anywhere (jv19 names them — they
  are spoken, never shown). No dove, no second figure, no Trinity symbol.
- The **eleven** disciples (the Twelve minus Judas, who is gone). Feature the ones
  whose sheets are LOCKED and rendered in the front, recognizable: **Peter, John,
  Andrew, James (Zebedee), Matthew, Thomas** — paste `lock_text('peter')`,
  `lock_text('john')` etc. and attach each one's 3 ref jpegs (`refs('peter')`…).
  The remaining men fill the group as reverent first-century Galilean men at
  varying distance/angle — do NOT individualize Philip, Bartholomew, James son of
  Alphaeus, Thaddaeus, or Simon the Zealot (their sheets are not rendered yet).
- Run `python3 media-production/character_ref_gate.py --dir
  build-71-the-great-commission` — must exit 0 before any credit.

## STYLE PREFIX (paste verbatim before every SCENE)
Beautiful hand-painted 2D animation style, reverent and warm, like a classic
illustrated storybook of scripture brought to life. Soft painterly brushstroke
textures, glowing golden light, muted earth tones with warm gold highlights.
First-century Judea. Sacred, hushed tone. Not photorealistic. No text or captions
in the image. Historically modest clothing: rough-woven wool and linen in undyed
earth colors. No modern objects. A single continuous painted scene — NOT a grid,
NOT split panels, NOT a comic strip. Every figure has exactly two arms and two
hands, correctly attached.

## SHOTS

### s1 — the-mountain  (n1: after the resurrection, to the mountain in Galilee)
A group of eleven weary, hopeful men climbing a grassy Galilean mountainside in the
soft gold light of early morning, seen from behind and below as they ascend toward
the bright open summit and a vast pale sky. Small against the great hill. No Jesus
figure in this shot. Wide, quiet, expectant.

### s2 — they-saw-him  (n2: they saw him, worshipped, some doubted)
On the windswept mountaintop, the eleven have stopped and are reacting to a figure
we see only from BEHIND at the right of the frame — a man in a plain undyed cream
wool robe with long dark hair, his back to us, standing calm against the sky. Most
of the disciples have fallen to their knees in worship, faces lifted toward him,
lit with awe; **Peter** (blue-grey tunic, thick dark curls, full beard) kneels
nearest; **John** (youngest, clean-shaven, faded grey-blue) beside him. One man at
the edge stands half-turned, uncertain, hand hesitating — the honest doubt. Every
gaze converges on the robed man's back. His face is never visible.

### s3 — all-power  (jv18: "All power is given unto me in heaven and in earth")
The robed figure of Jesus seen from BEHIND, centered and close in the lower
foreground, standing on the summit with the whole sky and the far country opening
out beyond him, warm light breaking across the heavens — a sense of all heaven and
earth under his raised, open hand. The eleven are smaller beyond him, faces toward
him in the light. Only the back of his head and cream robe are seen. No halo.

### s4 — all-nations  (jv19a: "teach all nations")
A sweeping view from the mountain's edge over a vast first-century world at dawn —
rolling hills, distant villages, a road winding toward the horizon, the far
shimmer of the sea — every corner of the earth waiting. No central figure; the
land itself is the subject, immense and golden, the whole world to be reached.

### s5 — baptizing  (jv19b: "baptizing them in the name of...")
A reverent baptism in a bright river below green banks: one first-century man
lowering another gently back into clear water, both in wet undyed linen, morning
light on the ripples, a few onlookers on the bank in quiet joy. Warm, clean,
sacred — the command being obeyed. No Jesus figure here; no Father or dove shown.

### s6 — observe-all-things  (jv20a: "teaching them to observe all things")
Over-the-shoulder from BEHIND Jesus (cream robe, long dark hair, back to camera,
lower foreground) as he faces the gathered eleven on the summit, his open hand
extended toward them in teaching. The eleven sit and stand close, faces up and
attentive, receiving it — **Peter, John, Andrew, Matthew** recognizable among
them. His face never shown. Every gaze on him.

### s7 — with-you-alway  (jv20b: "lo, I am with you alway")
The eleven on the mountain at the golden hour, and the robed figure of Jesus among
them seen from BEHIND / at DISTANCE, warm light wrapping the whole group — an
unmistakable feeling of nearness and promise, not farewell. The men's faces are
calm, steadied, no longer afraid. Soft glow in the sky, never a halo on his head.

### s8 — going-out  (n6: the command has never stopped moving; it reached you)
The eleven descending the far side of the mountain in the full light of day,
spreading out toward the wide world and the horizon roads below, purposeful and
unafraid, seen from behind as they go. The empty summit behind them. A sense of a
sending that will not stop — carried outward to the ends of the earth.

## AFTER STILLS
1. Save each as `assets/<name>.jpeg`.
2. Both gates exit 0; then `python3 make_narration.py` is already done — run
   `python3 build.py`.
3. `admin/verify-mp4.sh` the output, drop a one-line `FIXNOTE.txt`, ship. Cameron
   approves on the board.
