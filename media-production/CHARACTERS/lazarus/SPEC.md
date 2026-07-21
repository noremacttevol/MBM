# LAZARUS (of Bethany) — CHARACTER SPEC

**Status:** 🔒 LOCKED — approved by Cameron
**Approved by Cameron:** 2026-07-21
**Appears in:** #17 (Lazarus)
(NOT this man: the beggar Lazarus of the parable in build #37 — Luke 16 — is
a different, unrelated character and is governed by his own in-build lock.)

## What scripture tells us
- John 11:1 — "a certain man was sick, named Lazarus, of Bethany" — brother
  of Martha and Mary.
- John 11:3 — "he whom thou lovest is sick" — a personal friend of the Lord.
- John 11:39 — "he hath been dead four days" — the sheet covers sick, dead
  and raised; the face is the same man in all three.
- John 11:43-44 — "Lazarus, come forth. And he that was dead came forth,
  bound hand and foot with graveclothes."
- John 12:2 — "Lazarus was one of them which sat at the table with him" —
  alive, well, and back at his own table.
- John 12:10-11 — the chief priests wanted him dead "because that by reason
  of him many of the Jews went away, and believed" — a walking witness.
- Scripture never describes his face; the sheet keeps him a historically
  accurate first-century Judean householder of Bethany.

## Written description
(Adopts the look shipped in build #17 — a man of about forty with dark
hair — already on screen, must not drift.) A Middle Eastern Jewish man of
about forty: warm brown skin, dark hair, a short dark beard, a kind open
family face that echoes his sisters', a settled householder's bearing — and
in his eyes, after the tomb, the quiet dazed wonder of a man who has been
given his life back. SICK state (#17 s1): the same face pale and damp with
fever, hair matted. RAISED state: wrapped in white grave-linen strips, then
unwound, his face full of dazed wonder. The face is identical in every state.

## Standard garments
A DUN sandy grey-brown wool tunic with a dark olive mantle (never cream, and
none of his sisters' colors), a plain cord belt, simple leather sandals.
Grave scenes only: the white linen grave-strips of John 11:44 over the same
man.

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
Lazarus of Bethany, a Middle Eastern Jewish man of about forty, warm brown
skin, dark hair, a short dark beard, a kind open face with warm dark eyes
carrying a quiet dazed wonder — a settled householder, healthy and whole. He
wears a dun sandy grey-brown wool tunic (never cream) with a plain cord
belt. Warm even light on his face, plain soft warm-brown background. One
single continuous scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a reverent three-quarter bust portrait of Lazarus with the SAME short dark curly hair as the reference (never long, never sleek) of Bethany,
a Middle Eastern Jewish man of about forty, warm brown skin, dark hair, short
dark beard, dun sandy grey-brown wool tunic with a dark olive mantle at the
shoulder, turned three-quarters toward warm light, gentle and grateful. Plain
muted earth-tone background. One single continuous scene painted edge to
edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
hair and beard: a full-length standing figure, head to feet fully in frame:
Lazarus of Bethany, a Middle Eastern Jewish man of about forty, dark hair and
short dark beard, standing whole and well with an air of quiet wonder,
wearing a knee-to-ankle dun sandy grey-brown wool tunic with a plain cord
belt, a dark olive mantle over one shoulder, simple leather sandals. Plain
muted earth-tone background, gentle ground shadow. Every figure has two arms,
two hands, two legs and one head. One single continuous scene painted edge to
edge, no panels.

**Note for #17-class stories:** the sick-bed state is the same three refs
with fever pallor, damp skin and matted hair added; the tomb state is the
same man wrapped head to foot in white grave-linen strips (face bindings
loosened so the identical face reads). Never a different man in any state.
