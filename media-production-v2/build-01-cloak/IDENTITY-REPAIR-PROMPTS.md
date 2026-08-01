# Story 1 V3 identity-repair prompt record

Mode: built-in image generation, identity-preserving edits of the existing
Story 1 realistic frames. The first reference was always the target frame;
subsequent references were the canonical Jesus and/or healed-woman portraits
in `character-refs-v3/`.

## Common prompt contract

> Change only the visible recurring face, hair, and beard where applicable.
> Preserve expression, head angle, gaze, vertical crop, camera, setting,
> lighting, shadows, colors, clothing, body, pose, hands, fingers, feet, props,
> people count, spacing, and story action. Keep natural high-resolution
> live-action photography with real skin, hair, woven cloth, and stone. No
> illustration, painting, cartoon, CGI, glamour retouching, glow, halo, aura,
> text, watermark, malformed anatomy, changed crop, or added, removed, or moved
> people or objects.

Scene-specific hard locks retained the physicians and money exchange; the
woman entering and pressing through the crowd; Jesus remaining ahead of her;
the fingertips barely grazing only the lower hem from behind; the questioning
and disciple-response blocking; the woman kneeling when found; Jesus crouching
at her level without an artificial worship circle; and her departure through
the crowd with Jesus remaining behind her.

## Saved final assets

The accepted identity-edited project assets are:

- `assets-realistic-v3/s01-twelve-years.jpeg`
- `assets-realistic-v3/s02-physicians.jpeg`
- `assets-realistic-v3/s03-untouchable.jpeg`
- `assets-realistic-v3/s04-jairus-urging.jpeg`
- `assets-realistic-v3/s05-crowd-pressing.jpeg`
- `assets-realistic-v3/s06-woman-at-edge.jpeg`
- `assets-realistic-v3/s07-she-hears.jpeg`
- `assets-realistic-v3/s10-pressing-through.jpeg`
- `assets-realistic-v3/s11-touches-hem.jpeg`
- `assets-realistic-v3/s12-he-stops.jpeg`
- `assets-realistic-v3/s13-healed-in-her-body.jpeg`
- `assets-realistic-v3/s14-who-touched.jpeg`
- `assets-realistic-v3/s15-disciples-protest.jpeg`
- `assets-realistic-v3/s16-searching.jpeg`
- `assets-realistic-v3/s17-found-her.jpeg`
- `assets-realistic-v3/s18-daughter.jpeg`
- `assets-realistic-v3/s20-goes-in-peace.jpeg`

`s08`, `s09`, and `s19` were intentionally retained byte-for-byte from the
existing realistic draft because their recurring identity and composition
already passed inspection. Every accepted frame was compared beside its source;
all 20 final frames were then inspected together in
`story1-realistic-v3-contact-sheet.jpg`. Hash-backed identity boards in
`identity-boards-v3/` record the pass for both recurring identities.
