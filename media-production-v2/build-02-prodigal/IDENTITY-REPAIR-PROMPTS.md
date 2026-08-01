# Story 2 V3 identity-repair prompt record

Mode: built-in image generation, identity-preserving edits of existing Story 2
frames. The first reference was always the target frame; subsequent references
were the canonical recurring-character portraits in `character-refs-v3/`.

## Common prompt contract

> Change only the visible face, hair, and beard to the exact canonical actor.
> Preserve expression, head angle, gaze, vertical crop, camera, setting,
> lighting, shadows, colors, clothing, body, pose, hands, fingers, feet, props,
> people count, and story action. Natural high-resolution live-action biblical
> film still with real skin pores, hair, cloth, stone, and wood. No illustration,
> painting, cartoon, glow, halo, aura, text, watermark, malformed anatomy, or
> added, removed, or moved people or objects.

Each scene prompt then hard-locked its visible action: the pig trough and exact
pig count; the father's long-distance sightline; the ring on the younger son's
hand and servant fitting the sandal; the musicians and feast; exactly two men
outside; both father hands visible on the elder son's shoulders; and the final
open-door invitation with all three canonical family members. `s24` additionally
replaced the visible modern glass chimney lamp with a period clay oil lamp while
leaving the rest of the frame unchanged.

## Saved final assets

The accepted project-bound results are:

- `assets-realistic-v3/s01-they-murmured.jpeg`
- `assets-realistic-v3/s02-he-answered-with-a-story.jpeg`
- `assets-realistic-v3/s06-feeding-pigs.jpeg`
- `assets-realistic-v3/s07-came-to-his-senses.jpeg`
- `assets-realistic-v3/s08-walking-home.jpeg`
- `assets-realistic-v3/s09-the-rehearsed-speech.jpeg`
- `assets-realistic-v3/s10-father-saw-him.jpeg`
- `assets-realistic-v3/s13-the-embrace.jpeg`
- `assets-realistic-v3/s14-robe-ring-shoes.jpeg`
- `assets-realistic-v3/s15-my-son-was-dead.jpeg`
- `assets-realistic-v3/s17-musick-and-dancing.jpeg`
- `assets-realistic-v3/s18-would-not-go-in.jpeg`
- `assets-realistic-v3/s19-father-came-out.jpeg`
- `assets-realistic-v3/s20-the-hurt-poured-out.jpeg`
- `assets-realistic-v3/s21-lo-these-many-years.jpeg`
- `assets-realistic-v3/s22-the-last-words.jpeg`
- `assets-realistic-v3/s23-all-that-i-have-is-thine.jpeg`
- `assets-realistic-v3/s24-the-open-door.jpeg`

The six unlisted frames were intentionally copied byte-for-byte from V2 because
their identities and compositions already passed inspection. The first `s22`
edit was rejected because it hid one father hand; only the corrected two-hand
revision is present in the V3 asset set.
