# STEPHEN — CHARACTER SPEC

**Status:** sheet rendered, AWAITING CAMERON'S APPROVAL
**Approved by Cameron:** (pending)
**Appears in:** #137 (retro-check), #179 Stephen's Witness (blocking)

## What scripture tells us
- Acts 6:5 — "a man full of faith and of the Holy Ghost," chosen one of the
  seven; a Hellenist (Greek-speaking Jew), so a younger, city-raised man.
- Acts 6:8 — "full of faith and power, did great wonders."
- Acts 6:15 — "all… saw his face as it had been the face of an angel" — an
  open, luminous, guileless face is the defining note.
- Acts 7:55-56 — steadfast gaze into heaven; calm at the end.
- Acts 7:58 — dies young (contrast with Saul, "a young man," a peer).

## Written description
(Adopts the existing [STEPHEN LOCK] from builds #137/#179 verbatim — already
shipped, must not drift.) A young Middle Eastern man of about thirty, an open
guileless face, a FULL hairline of short dark curly hair, a short neat dark
beard, clear steady eyes. His face and body carry NO marks or injuries in any
frame. First-century Judean features: warm olive-brown skin.

## Standard garments
A deep blue-grey tunic with a dark brown mantle (never cream, never pale).
Simple leather sandals, plain rope-and-leather belt.

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
Stephen, a young Middle Eastern man of about thirty, warm olive-brown skin, an
open guileless face with clear steady eyes, a FULL hairline of short dark
curly hair, a short neat dark beard, a calm luminous expression like the face
of an angel — but NO halo, NO glow. He wears a deep blue-grey tunic with a
dark brown mantle over one shoulder (never cream, never pale). No marks or
injuries. Warm even light on his face, plain soft warm-brown background. One
single continuous scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a reverent three-quarter bust portrait of Stephen, young
Middle Eastern man of about thirty, warm olive-brown skin, short dark curly
hair with a full hairline, short neat dark beard, clear steady eyes, deep
blue-grey tunic with dark brown mantle, turned three-quarters toward soft warm
light. No halo, no glow, no injuries. Plain muted earth-tone background. One
single continuous scene painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a full-length standing figure, head to feet fully in frame:
Stephen, young Middle Eastern man of about thirty, short dark curly hair,
short neat dark beard, standing calm and upright, wearing a deep blue-grey
knee-to-ankle wool tunic, a dark brown mantle draped over one shoulder, a
plain leather belt, simple leather sandals. No marks or injuries, no halo.
Plain muted earth-tone background, gentle ground shadow. Every figure has two
arms, two hands, two legs and one head. One single continuous scene painted
edge to edge, no panels.
