# CLEOPAS — CHARACTER SPEC

**Status:** sheet rendered, AWAITING CAMERON'S APPROVAL
**Approved by Cameron:** (pending)
**Appears in:** #18 The Road to Emmaus

## What scripture tells us (Luke 24:13-35)
- 24:13 — "two of them went that same day to a village called Emmaus" —
  a disciple outside the eleven, on foot, threescore furlongs from
  Jerusalem.
- 24:17-18 — "one of them, whose name was Cleopas... Art thou only a
  stranger in Jerusalem?" — the named speaker of the pair; grieving,
  "and are sad."
- 24:29 — "Abide with us: for it is toward evening" — hospitable, earnest.
- 24:32 — "Did not our heart burn within us" — the face must carry grief
  turning to burning recognition and joy.
- Scripture is silent on his features; the default is a historically
  accurate first-century Judean — an ordinary grown disciple, no rank, no
  wealth.

## Written description
(Adopts the shipped look from build #18 — already shipped, must not drift.)
A first-century Judean man in his fifties, warm olive-brown skin, a
grey-streaked dark beard, an ordinary honest weathered face — a walker of
dusty roads. His face carries the whole arc: downcast grief on the road,
then burning wonder at the breaking of bread.
(His companion in #18 — the younger disciple, thirties, short dark beard,
muted olive-green robe — is NOT rostered; his in-build lock governs him.)

## Standard garments
A plain BROWN wool robe (locked in #18) with a simple cord belt, a dusty
travel mantle of the same brown wool, worn leather sandals — an ordinary
disciple's undyed working wool, clearly not cream, plainly not the
olive-green of his younger companion.

## Generation prompts (Nano Banana 2 · 9:16 · 1x, flow_driver.py)
STYLE BLOCK (prepended byte-identical to each):
Beautiful hand-painted 2D animation style, reverent and warm, like a classic
illustrated storybook of scripture brought to life. Soft painterly brushstroke
textures, glowing golden light, muted earth tones with warm gold highlights.
First-century Judea. Sacred, hushed tone. Not photorealistic. No text or
captions in the image. Historically modest clothing: rough-woven wool and
linen in undyed earth colors. No modern objects.

### face-front (no ref — this creates the identity)
[STYLE BLOCK] A reverent close bust portrait, facing the viewer directly:
Cleopas, a first-century Judean disciple in his fifties, warm olive-brown
skin, a grey-streaked dark beard, an ordinary honest weathered face with
earnest dark eyes. He wears a plain brown wool robe — undyed working wool,
clearly not cream. Warm even light on his face, plain soft warm-brown
background. One single continuous scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a reverent three-quarter bust portrait of Cleopas the
disciple of Emmaus, a man in his fifties, warm olive-brown skin,
grey-streaked dark beard, plain brown wool robe, turned three-quarters
toward warm light, earnest and open — a face made for grief turning to
wonder. Plain muted earth-tone background. One single continuous scene
painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a full-length standing figure, head to feet fully in frame:
Cleopas, a first-century Judean disciple in his fifties, grey-streaked dark
beard, standing mid-journey in his plain knee-to-ankle brown wool robe with
a simple cord belt, a dusty brown travel mantle over one shoulder, worn
leather sandals dusted from the road. Plain muted earth-tone background,
gentle ground shadow. Every figure has two arms, two hands, two legs and
one head. One single continuous scene painted edge to edge, no panels.
