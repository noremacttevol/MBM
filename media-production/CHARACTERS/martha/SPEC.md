# MARTHA (of Bethany) — CHARACTER SPEC

**Status:** 🔒 LOCKED — approved by Cameron
**Approved by Cameron:** 2026-07-21
**Appears in:** #16 (Mary and Martha), #17 (Lazarus), #144 (the resurrection
and the life)

## What scripture tells us
- Luke 10:38 — "a certain woman named Martha received him into her house" —
  the householder, the host.
- Luke 10:40 — "Martha was cumbered about much serving" — the worker; hands
  always busy, always doing.
- Luke 10:41 — "thou art careful and troubled about many things" — the
  strain of the doer shows on her face.
- John 11:20-27 — she is the one who GOES OUT to meet him on the road, and
  gives the great confession: "I believe that thou art the Christ, the Son
  of God." Practical faith, spoken plainly.
- John 12:2 — "Martha served" — even after the miracle, she serves.
- Scripture never describes her face; the sheet keeps her a historically
  accurate first-century Judean woman, the older working sister.

## Written description
(Adopts the [MARTHA LOCK] face shipped in build #144 — already on screen,
must not drift.) A Middle Eastern Jewish woman of about forty: a strong
capable face, steady searching eyes, warm brown skin, dark hair kept covered
in public, work-worn practical hands — the older sister, the doer, in
constant motion around her house, whose plain-spoken faith is as solid as
her serving.

## Standard garments
A DEEP RUSSET-RED wool dress (locked in #17 — her signature color, plainly
distinct from Mary of Bethany's dusty-blue and Magdalene's madder-red shawl),
a warm dun head-covering worn fully over her hair in the modest first-century
manner, a plain work apron tied on when she serves (#16), simple leather
sandals.

**Shipped-variance notes:** #17 shipped her head-covering as cream — under
the current garment law (cream is the Lord's alone) the sheet locks it to
warm dun going forward. #144 shipped her in a dark umber dress with a deep
charcoal-blue MOURNING shawl — that is this same woman in mourning dress for
the Lazarus grief scenes: condition on the same three refs and swap the
garments to umber and charcoal-blue only in mourning contexts. The face
never changes.

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
Martha of Bethany, a Middle Eastern Jewish woman of about forty, warm brown
skin, a strong capable face with steady searching eyes, dark hair covered by
a warm dun head-covering, wearing a deep russet-red wool dress (never pale,
never cream) — the practical older sister, warm and a little tired from
serving. Warm even light on her face, plain soft warm-brown background. One
single continuous scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME woman as the attached reference image — identical face
and head-covering: a reverent three-quarter bust portrait of Martha of
Bethany, a Middle Eastern Jewish woman of about forty, strong capable face,
steady searching eyes, dark hair covered by a warm dun head-covering, deep
russet-red wool dress, turned three-quarters toward warm light, earnest and
plain-spoken. Plain muted earth-tone background. One single continuous scene
painted edge to edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME woman as the attached reference image — identical face
and head-covering: a full-length standing figure, head to feet fully in
frame: Martha of Bethany, a Middle Eastern Jewish woman of about forty with a
strong capable face, dark hair fully covered by a warm dun head-covering in
the modest first-century manner, wearing an ankle-length deep russet-red wool
dress with a plain work apron tied at the waist, work-worn practical hands, a
clay serving bowl held in one arm, simple leather sandals. Plain muted
earth-tone background, gentle ground shadow. Every figure has two arms, two
hands, two legs and one head. One single continuous scene painted edge to
edge, no panels.
