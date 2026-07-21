# JOB — CHARACTER SPEC

**Status:** sheet rendered, AWAITING CAMERON'S APPROVAL
**Approved by Cameron:** (pending)
**Appears in:** #120 Job and the Voice from the Whirlwind (shipped — "a
dignified older man with a full grey beard and grey hair, warm Middle-Eastern
skin, in a fine deep burgundy-red robe" when blessed; "torn ash-grey robe" in
the ashes; the build's s6 fix insists GREY-bearded, NOT young, NOT
dark-bearded — that is law), #181 When the Morning Stars Sang (Job 38 verse
video, creation imagery only — Job the man is not depicted)

## What scripture tells us (Job)
- 1:1 — "perfect and upright, and one that feared God, and eschewed evil" —
  his goodness precedes his suffering; dignity is baked into the face.
- 1:3 — "this man was the greatest of all the men of the east" — a wealthy
  patriarch of the land of Uz, flocks and household.
- 2:8 — "he took him a potsherd to scrape himself withal; and he sat down
  among the ashes" — the ash-heap state: gaunt, ash-dusted, torn robe,
  a broken potsherd in hand; painted with dignity, never grotesque (#120
  rule: no graphic sores shown).
- 29:8 — "The young men saw me, and hid themselves: and the aged arose, and
  stood up" — a man of great honor and mature years.
- 42:12 — "the LORD blessed the latter end of Job more than his beginning" —
  the restored state: the same man, clean-robed and at peace.

## Written description
A dignified older man of the east, about sixty: a full grey beard and grey
hair (ALWAYS grey — never young, never dark-bearded, per the shipped #120
fix), warm Middle-Eastern skin, a strong patriarch's face deeply lined,
steady honest eyes that can hold grief without going bitter. The sheet
covers THREE shipped states, same face in all: BLESSED — upright and full
among his flocks; ASHES — gaunt, weary, hollow with suffering yet unbroken,
ash-dusted, holding a rough broken potsherd; RESTORED — calm, gently
comforted, at rest.

## Standard garments
BLESSED / RESTORED state: a fine deep burgundy-red wool robe (his locked
color, from #120) with a dark earth-tone mantle, leather belt, leather
sandals — a wealthy man of the east, rich but never gaudy. ASHES state: the
same robe torn and gone ash-grey, dusted with ash, barefoot. Never cream,
never off-white, in any state.

## Generation prompts (Nano Banana 2 · 9:16 · 1x, flow_driver.py)
STYLE BLOCK (prepended byte-identical to each):
Beautiful hand-painted 2D animation style, reverent and warm, like a classic
illustrated storybook of scripture brought to life. Soft painterly brushstroke
textures, glowing golden light, muted earth tones with warm gold highlights.
The ancient land of Uz in the east, patriarchal era. Sacred, hushed tone. Not
photorealistic. No text or captions in the image. Historically modest
clothing. No modern objects.

### face-front (no ref — this creates the identity)
[STYLE BLOCK] A reverent close bust portrait, facing the viewer directly:
Job, a dignified older man of the east, about sixty, a full grey beard and
grey hair, warm Middle-Eastern skin, a strong deeply-lined patriarch's face,
steady honest eyes. He wears a fine deep burgundy-red wool robe with a dark
earth-tone mantle. Upright, kind and grave — a good man blessed with much.
No halo, no glow. Warm even light, plain soft warm-brown background. One
single continuous scene painted edge to edge, no panels.

### three-quarter (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
grey hair and grey beard: a reverent three-quarter bust portrait of Job,
about sixty, full grey beard and grey hair, warm Middle-Eastern skin,
deeply-lined dignified face, fine deep burgundy-red robe and dark mantle,
turned three-quarters toward warm golden light, grave and grateful. Plain
muted earth-tone background. One single continuous scene painted edge to
edge, no panels.

### full-body (attach face-front.jpeg as --ref)
[STYLE BLOCK] The SAME man as the attached reference image — identical face,
grey hair and grey beard: a full-length standing figure, head to feet fully
in frame: Job, a dignified patriarch of about sixty, standing at peace with
both hands open at his sides, wearing a fine deep burgundy-red ankle-length
wool robe with a dark earth-tone mantle, a leather belt, leather sandals.
The bearing of the greatest man of the east, upright and humble at once.
Plain muted earth-tone background, gentle ground shadow. Every figure has
two arms, two hands, two legs and one head. One single continuous scene
painted edge to edge, no panels.

**Note on states:** the sheet is the BLESSED/RESTORED Job (burgundy-red,
clean). For ash-heap scenes, condition on the same three refs and swap the
garment language to "the same robe torn and ash-grey, dusted with ash,
barefoot, gaunt with suffering, holding a rough broken potsherd — dignified,
no graphic sores" exactly as shipped in #120. The face never changes.
