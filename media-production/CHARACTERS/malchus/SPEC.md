# MALCHUS — CHARACTER SPEC

**Status:** sheet rendered, AWAITING CAMERON'S APPROVAL
**Approved by Cameron:** (pending)
**Appears in:** #66 Malchus' Ear

## What scripture tells us
- John 18:10 — "Then Simon Peter having a sword drew it, and smote the high
  priest's servant, and cut off his right ear. The servant's name was
  Malchus." — the high priest's servant, present at the arrest in the
  garden.
- Luke 22:51 — "And he touched his ear, and healed him." — the last miracle
  before the cross, done for a man in the arresting party.
- Scripture is silent on his features; the default is a historically
  accurate first-century Judean — a household servant of the high priest,
  well-kept but not wealthy, young enough to be sent out on a night arrest.

## Written description
(Adopts the [SERVANT LOCK] from build #66 verbatim — already shipped, must
not drift.) A Middle Eastern man of about thirty-five, a short dark beard,
no head-covering, warm olive skin, an ordinary alert face shown startled
then astonished — the servant who came to seize a prisoner and went home
healed. Per the shipped #66 lock: his ear is WHOLE AND UNHURT in every
image, never any blood or wound visible — the same man throughout.

## Standard garments
A good DEEP WALNUT-BROWN tunic (the "good dark tunic" of the #66 lock,
color hereby fixed) with a servant's plain leather belt, a high priest's
household servant's neat but unadorned wool, sturdy leather sandals — never
cream, no fringe, no rank.

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
Malchus, servant of the high priest, a Middle Eastern man of about
thirty-five, warm olive skin, a short dark beard, no head-covering, neat
dark hair, an ordinary alert honest face, both ears whole and unhurt, no
blood or wound anywhere. He wears a good deep walnut-brown tunic with a
servant's plain leather belt — never cream. Warm even light on his face,
plain soft warm-brown background. One single continuous scene painted edge
to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a reverent three-quarter bust portrait of Malchus the high
priest's servant, about thirty-five, warm olive skin, short dark beard, no
head-covering, good deep walnut-brown tunic with a servant's belt, both
ears whole and unhurt, no blood or wound anywhere, turned three-quarters
toward warm light, startled wonder on his face. Plain muted earth-tone
background. One single continuous scene painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a full-length standing figure, head to feet fully in frame:
Malchus, servant of the high priest, a Middle Eastern man of about
thirty-five, short dark beard, no head-covering, standing alert in a good
knee-length deep walnut-brown tunic with a servant's plain leather belt,
sturdy leather sandals, both ears whole and unhurt, no blood or wound
anywhere on him — never cream, nothing fine, a household servant's neat
plain wool. Plain muted earth-tone background, gentle ground shadow. Every
figure has two arms, two hands, two legs and one head. One single
continuous scene painted edge to edge, no panels.
