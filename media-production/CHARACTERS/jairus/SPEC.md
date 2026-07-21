# JAIRUS — CHARACTER SPEC

**Status:** sheet rendered, AWAITING CAMERON'S APPROVAL
**Approved by Cameron:** (pending)
**Appears in:** #57 Jairus' Daughter

## What scripture tells us
- Mark 5:22 — "one of the rulers of the synagogue, Jairus by name; and when
  he saw him, he fell at his feet" — a man of standing who kneels anyway.
- Mark 5:23 — "My little daughter lieth at the point of death" — the father
  of a girl "of the age of twelve years" (Mark 5:42), so a middle-aged man.
- Luke 8:41 — "he was a ruler of the synagogue" — respectable, devout,
  known to the whole town.
- Scripture is silent on his features; the default is a historically
  accurate first-century Judean of rank — a dignified, devout synagogue
  ruler, dressed above the working folk but below the Jerusalem elite.

## Written description
(Adopts the shipped look from build #57 — already shipped, must not drift.)
A dignified synagogue ruler in his mid-forties, warm Middle Eastern olive
skin, a full well-kept dark beard, strong careworn features — a respected
man whose composure the story breaks open: anguish, hope, then disbelieving
joy. Carries himself upright and devout even on his knees.

## Standard garments
The fuller formal robe of a synagogue ruler (locked in #57): DEEP
INDIGO-BLUE and BROWN with a woven prayer-fringe at the hem — plainly finer
than the townsfolk's dun and faded wool, clearly not cream — with a
respectable dark head covering and leather sandals.

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
Jairus, a ruler of the synagogue, a dignified first-century Judean man in
his mid-forties, warm olive skin, a full well-kept dark beard, strong
careworn devout features, earnest dark eyes, a respectable dark head
covering. He wears a fuller formal robe of deep indigo-blue and brown with
a woven prayer-fringe — clearly not cream. Warm even light on his face,
plain soft warm-brown background. One single continuous scene painted edge
to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
beard and head covering: a reverent three-quarter bust portrait of Jairus
the synagogue ruler, mid-forties, warm olive skin, full well-kept dark
beard, dark head covering, formal deep indigo-blue and brown robe with a
woven prayer-fringe, turned three-quarters toward warm light, earnest and
hopeful. Plain muted earth-tone background. One single continuous scene
painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
beard and head covering: a full-length standing figure, head to feet fully
in frame: Jairus, a dignified ruler of the synagogue in his mid-forties,
full dark beard, respectable dark head covering, standing upright and
devout in his fuller ankle-length formal robe of deep indigo-blue and brown
with a woven prayer-fringe at the hem, a plain sash, leather sandals —
finer cloth than a working man's, clearly not cream. Plain muted earth-tone
background, gentle ground shadow. Every figure has two arms, two hands, two
legs and one head. One single continuous scene painted edge to edge, no
panels.
