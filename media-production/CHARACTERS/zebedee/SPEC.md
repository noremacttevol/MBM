# ZEBEDEE — CHARACTER SPEC

**Status:** sheet rendered, AWAITING CAMERON'S APPROVAL
**Approved by Cameron:** (pending)
**Appears in:** #51 First Catch of Fish, #71 Calling the Fishermen

## What scripture tells us
- Matt 4:21 — "James the son of Zebedee, and John his brother, in a ship
  with Zebedee their father, mending their nets" — a working Galilean
  fisherman, father of two grown sons, so an older man.
- Mark 1:20 — "they left their father Zebedee in the ship with the hired
  servants" — a man of some means (he keeps hired servants), and the father
  who stays in the boat and lets his sons go.
- Scripture is silent on his features; the default is a historically
  accurate first-century Galilean — an old fisherman who has spent a
  lifetime on the lake.

## Written description
(Adopts the ZEBEDEE LOCK from build #71 verbatim — already shipped, must
not drift.) An old Galilean fisherman father of about sixty, a full
GREY-WHITE beard, deeply weathered sun-browned skin, thinning grey hair, a
lifetime of net-hauling in his thick hands and stooped strong shoulders.
His face is weary and tender — watching his sons go, never angry.

## Standard garments
A heavy DARK-BROWN mantle over a GREY wool tunic (locked in #71 — clearly
NOT cream), a rope belt, bare weathered forearms, simple leather sandals;
fishing nets across his knees when seated in the boat.

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
Zebedee, an old Galilean fisherman of about sixty, deeply weathered
sun-browned skin, a full grey-white beard, thinning grey hair, kind weary
eyes with deep sun-creases — a tender, patient father's face. He wears a
grey wool tunic under a heavy dark-brown mantle — clearly not cream. Warm
even light on his face, plain soft warm-brown background. One single
continuous scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a reverent three-quarter bust portrait of Zebedee the old
fisherman father, about sixty, deeply weathered, full grey-white beard,
thinning grey hair, grey wool tunic under a heavy dark-brown mantle, turned
three-quarters toward warm light, weary and tender. Plain muted earth-tone
background. One single continuous scene painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a full-length standing figure, head to feet fully in frame:
Zebedee, an old Galilean fisherman of about sixty, full grey-white beard,
stooped strong shoulders and thick net-worn hands, standing steady in a
knee-to-ankle grey wool tunic with a rope belt under a heavy dark-brown
mantle, bare weathered forearms, a folded fishing net held against his hip,
simple leather sandals — clearly not cream. Plain muted earth-tone
background, gentle ground shadow. Every figure has two arms, two hands, two
legs and one head. One single continuous scene painted edge to edge, no
panels.
