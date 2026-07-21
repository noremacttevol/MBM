# PETER (Simon Peter) — CHARACTER SPEC

**Status:** 🔒 LOCKED — approved by Cameron
**Approved by Cameron:** 2026-07-21
**Appears in:** #7, #19, #51, #53, #66, #67, #71, #89, #90, #92, #103, #162
and more — the most-drawn face after Jesus.

## What scripture tells us
- Matt 4:18 — a fisherman of Galilee, casting a net; a man of nets and boats.
- John 21:7 — girds his fisher's coat and THROWS HIMSELF into the sea —
  impulsive physical strength.
- Matt 26:69-75 — bold, quick-spoken, then broken and restored; an expressive
  open face that can carry both.
- John 1:42 — renamed Cephas, "a stone" — solid, sturdy presence.
- Married (Matt 8:14, his wife's mother) — a grown householder, mid-thirties.

## Written description
(Adopts the existing [PETER LOCK] from build #7 — already shipped, must not
drift.) A sturdy Galilean fisherman in his mid-thirties: thick dark curly
hair, a full dark beard, weathered olive skin, broad-shouldered with strong
rope-worn hands, an open expressive face — quick to speak, quick to feel.

## Standard garments
A BLUE-GREY wool tunic (locked in #7 — never cream, so he is never confused
with the cream-robed Lord), rope belt, dun-brown fisher's mantle when a cloak
is needed, bare muscular forearms, simple leather sandals.

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
Simon Peter, a sturdy Galilean fisherman in his mid-thirties, weathered olive
skin, thick dark curly hair, a full dark beard, open expressive dark eyes,
strong honest features of a man who hauls nets. He wears a blue-grey wool
tunic (never cream) with a rope belt. Warm even light on his face, plain soft
warm-brown background. One single continuous scene painted edge to edge, no
panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a reverent three-quarter bust portrait of Simon Peter, sturdy
Galilean fisherman in his mid-thirties, weathered olive skin, thick dark curly
hair, full dark beard, blue-grey wool tunic with rope belt, turned
three-quarters toward warm light, alert and earnest. Plain muted earth-tone
background. One single continuous scene painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a full-length standing figure, head to feet fully in frame:
Simon Peter, sturdy broad-shouldered Galilean fisherman in his mid-thirties,
thick dark curly hair, full dark beard, standing planted and ready, wearing a
knee-to-ankle blue-grey wool tunic with a rope belt, bare muscular forearms,
a dun-brown fisher's mantle over one shoulder, simple leather sandals. Plain
muted earth-tone background, gentle ground shadow. Every figure has two arms,
two hands, two legs and one head. One single continuous scene painted edge to
edge, no panels.
