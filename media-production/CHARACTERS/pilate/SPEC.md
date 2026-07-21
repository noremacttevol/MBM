# PILATE (Pontius Pilate) — CHARACTER SPEC

**Status:** sheet rendered, AWAITING CAMERON'S APPROVAL
**Approved by Cameron:** (pending)
**Appears in:** #93 Barabbas Goes Free

## What scripture tells us
- Luke 3:1 — "Pontius Pilate being governor of Judaea" — the Roman governor,
  not a Judean.
- Matt 27:2 — "delivered him to Pontius Pilate the governor" — he holds the
  judgment seat (Matt 27:19).
- John 18:33-38 — questions Jesus in the judgment hall; "What is truth?" —
  a skeptical, worldly administrator.
- Matt 27:24 — "took water, and washed his hands before the multitude" —
  a man caught between the crowd and his own verdict.
- Scripture is silent on his appearance. He is a Roman patrician official,
  so the default is Roman, NOT first-century Judean: clean-shaven, short
  Roman haircut, Roman civic dress — never Judean robes.

## Written description
(Adopts the [PILATE LOCK] from build #93 — already shipped, must not drift.)
A clean-shaven Roman governor of about forty-five, short dark hair in the
Roman style, a strong lined face — the worn authority of a career
administrator, imperious but uneasy. Roman patrician features, lighter
Mediterranean-olive skin than the Judeans around him, never bearded.

## Standard garments
Roman military-administrative dress, NOT Judean wool (locked in #93): a
WHITE ROMAN TOGA with a DEEP RED-PURPLE border worn over a PALE GREY tunic.
(The toga's Roman white is the shipped #93 lock — it is Roman civic dress,
plainly a toga and never a robe, and reads nothing like the Father's
radiant pure white or the Lord's cream Judean wool.) Roman leather sandals;
no armor, no helmet — a governor, not a soldier.

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
Pontius Pilate, the Roman governor of Judaea, a CLEAN-SHAVEN Roman patrician
of about forty-five, short dark hair cut in the Roman style, a strong lined
face with cool appraising eyes, no beard of any kind. He wears a white Roman
toga with a deep red-purple border over a pale grey tunic — Roman civic
dress, not Judean robes. Composed, imperious, faintly uneasy. Warm even
light on his face, plain soft warm-brown background. One single continuous
scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical
clean-shaven face and short Roman haircut: a reverent three-quarter bust
portrait of Pontius Pilate the Roman governor, about forty-five, strong
lined patrician face, no beard, white Roman toga with a deep red-purple
border over a pale grey tunic, turned three-quarters toward warm light,
weighing a verdict. Plain muted earth-tone background. One single continuous
scene painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical
clean-shaven face and short Roman haircut: a full-length standing figure,
head to feet fully in frame: Pontius Pilate, Roman governor of Judaea, about
forty-five, clean-shaven with short dark Roman-cut hair, standing erect with
a governor's bearing, draped in a full white Roman toga with a deep
red-purple border over a pale grey tunic falling to the calf, Roman leather
sandals — Roman military-administrative dress, plainly a toga, nothing
Judean about him. Plain muted earth-tone background, gentle ground shadow.
Every figure has two arms, two hands, two legs and one head. One single
continuous scene painted edge to edge, no panels.
