# BARTIMAEUS — CHARACTER SPEC

**Status:** 🔒 LOCKED — approved by Cameron
**Approved by Cameron:** 2026-07-21
**Appears in:** #12 Blind Bartimaeus

## What scripture tells us (Mark 10:46-52)
- 10:46 — "blind Bartimaeus, the son of Timaeus, sat by the highway side
  begging" — a blind beggar at the Jericho roadside.
- 10:47-48 — cries out and will not be silenced — dignity and grit, not
  pity; "he cried the more a great deal."
- 10:50 — "And he, casting away his garment, rose, and came to Jesus" — the
  ragged cloak he throws off is part of the story; the sheet keeps it.
- 10:52 — "immediately he received his sight, and followed Jesus in the
  way" — the sheet covers BOTH states, same face (same pattern as
  naaman/SPEC.md: before blind, after seeing, one identical man).

## Written description
(Adopts the BARTIMAEUS LOCK from build #12 verbatim — already shipped, must
not drift.) A lean weathered grown man in his mid-forties, sun-browned skin,
tangled shoulder-length dark hair, a short rough dark beard, a dignified
ordinary face. BEFORE state: pale milky-gray clouded eyes that do not see,
open and aimed slightly past everything — never grotesque, never pitiable.
AFTER state (healed): the same man with deep warm brown clear seeing eyes.
His face is identical in both.

## Standard garments
A patched OATMEAL-colored rough wool tunic with a simple cord belt (locked
in #12 — plainly a beggar's patched dull wool, nothing like the Lord's clean
cream), and over it the single ragged SAND-BROWN wool cloak with frayed
edges — threadbare, weathered, the garment he casts away in Mark 10:50.
Bare feet or the crudest sandals.

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
Bartimaeus, a lean weathered beggar in his mid-forties, sun-browned skin,
tangled shoulder-length dark hair, a short rough dark beard, a dignified
ordinary face, pale milky-gray clouded unseeing eyes open and aimed slightly
past the viewer — dignified, never grotesque. He wears a patched
oatmeal-colored rough wool tunic with a ragged frayed sand-brown cloak over
his shoulders. Warm even light on his face, plain soft warm-brown
background. One single continuous scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a reverent three-quarter bust portrait of Bartimaeus the
blind beggar of Jericho, mid-forties, sun-browned weathered skin, tangled
shoulder-length dark hair, short rough dark beard, pale milky-gray clouded
eyes, patched oatmeal wool tunic and ragged frayed sand-brown cloak, his
head tilted slightly, listening, turned three-quarters toward warm light.
Plain muted earth-tone background. One single continuous scene painted edge
to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a full-length standing figure, head to feet fully in frame:
Bartimaeus, a lean weathered beggar in his mid-forties, tangled
shoulder-length dark hair, short rough dark beard, pale milky-gray clouded
unseeing eyes, standing upright with quiet dignity in his patched
knee-to-ankle oatmeal-colored rough wool tunic with a simple cord belt, the
single ragged sand-brown wool cloak with frayed edges draped over his
shoulders, bare weathered feet. Plain muted earth-tone background, gentle
ground shadow. Every figure has two arms, two hands, two legs and one head.
One single continuous scene painted edge to edge, no panels.

**Note for #12:** the sheet shows the BEFORE (blind, cloak on) state; the
healed AFTER state is the same sheet — condition on the same three refs,
swap "pale milky-gray clouded eyes" for "deep warm brown clear seeing eyes"
(per the shipped #12 lock), and drop the cloak once he has cast it away in
Mark 10:50.
