# BARABBAS — CHARACTER SPEC

**Status:** sheet rendered, AWAITING CAMERON'S APPROVAL
**Approved by Cameron:** (pending)
**Appears in:** #93 Barabbas Goes Free

## What scripture tells us
- Matt 27:16 — "they had then a notable prisoner, called Barabbas" — a
  known, notorious man.
- Mark 15:7 — "which lay bound with them that had made insurrection with
  him, who had committed murder in the insurrection" — an insurrectionist,
  a violent man, held bound.
- John 18:40 — "Now Barabbas was a robber."
- Luke 23:25 — "him that for sedition and murder was cast into prison" —
  released in the Lord's place.
- Scripture is silent on his features beyond this; the default is a
  historically accurate first-century Judean — hardened by prison and
  violence, but a man, not a monster: the story turns on him receiving
  undeserved freedom.

## Written description
(Adopts the [BARABBAS LOCK] from build #93 verbatim — already shipped, must
not drift.) A powerfully built Middle Eastern man of about forty, a hard
weathered face, a FULL hairline of shaggy unkempt black hair, a rough short
black beard, a scarred brow, rough hardened hands — a prisoner of violence,
stunned by mercy. He appears EXACTLY ONCE in any frame; no other figure in
the frame resembles him.

## Standard garments
A ragged DARK CHARCOAL-BROWN tunic (locked in #93 — never cream), torn and
prison-stained, a frayed cord at the waist, bare feet or crude sandals. In
pre-release scenes he wears heavy iron shackles on his wrists until they
are struck off; the sheet's full-body shows him unshackled, wrists bare and
chafed.

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
Barabbas, a powerfully built Middle Eastern prisoner of about forty, a hard
weathered face, a full hairline of shaggy unkempt black hair, a rough short
black beard, a scarred brow, wary dark eyes — hardened but human, never
monstrous. He wears a ragged dark charcoal-brown tunic, torn at the collar
— never cream. Warm even light on his face, plain soft warm-brown
background. One single continuous scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a reverent three-quarter bust portrait of Barabbas the
prisoner, powerfully built, about forty, hard weathered face, shaggy
unkempt black hair, rough short black beard, scarred brow, ragged dark
charcoal-brown tunic, turned three-quarters toward warm light, guarded and
disbelieving. Plain muted earth-tone background. One single continuous
scene painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a full-length standing figure, head to feet fully in frame:
Barabbas, a powerfully built Middle Eastern man of about forty, broad and
heavy-shouldered, shaggy unkempt black hair, rough short black beard,
scarred brow, standing planted with rough hardened hands loose at his
sides, wrists bare and chafed where shackles have been, wearing a ragged
knee-length dark charcoal-brown tunic with a frayed cord at the waist,
bare weathered feet — never cream, nothing fine on him. Plain muted
earth-tone background, gentle ground shadow. Every figure has two arms, two
hands, two legs and one head. One single continuous scene painted edge to
edge, no panels.
