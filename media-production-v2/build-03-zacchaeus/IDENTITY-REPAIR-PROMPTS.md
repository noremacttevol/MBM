# Story 3 V3 identity and action-repair record

Mode: built-in image generation, using identity-preserving edits of the existing
Story 3 realistic frames. The first reference was always the target composition;
the remaining references were the canonical Jesus and/or Zacchaeus portraits in
`character-refs-v3/`.

## Common prompt contract

> Preserve the story beat, event order, vertical crop, camera, setting, lighting,
> shadows, colors, clothing, props, people count, spacing, and all already-correct
> anatomy. Match every recurring face to its canonical portrait. Keep natural
> high-resolution live-action photography with real skin, hair, woven cloth,
> stone, and practical clay oil lamps. No illustration, painting, cartoon, CGI,
> glamour retouching, halo, glow, text, watermark, modern object, malformed
> anatomy, invented action, or added or removed principal character.

Zacchaeus remains the same short, slight, normally proportioned middle-aged man:
high receding hairline, closely cropped dark hair, brown eyes, and a dark beard
with gray at the chin. His deep wine-burgundy robe and gold woven borders remain
consistent. Jesus remains the approved green-hazel-eyed man in the global V2
portrait, with the same long dark brown hair, full dark beard, ivory robe, and
calm compassionate presence.

## Scene-specific corrections

- `s09` was rebuilt around the original stated action: Zacchaeus runs ahead in
  profile, both feet airborne, with both fists lifting separate folds of the
  burgundy robe. The accepted frame restores the gold garment borders and keeps
  the crowd watching from behind.
- `s10` was rebuilt around a physically usable sycamore climb: two hands grip
  separate supports, one leg hooks over a broad horizontal limb, and no limb or
  body passes through the trunk.
- `s20` through `s25` preserve the required chronology: Jesus's invitation and
  arrival come before Zacchaeus's vow; the vow itself shows no money; the later
  restitution frame shows the actual coin payment with exactly three people.
- `s24` and `s25` keep Jesus speaking to the witnessed room, not forming an
  artificial worship circle or private aside. `s26` closes at the doorway with a
  single purposeful, naturally posed Jesus and a simple walking staff.

## Accepted output

Twenty-four frames received identity and/or action repairs. `s15` and `s19` were
retained byte-for-byte from the existing realistic draft because their recurring
identity, composition, and action already passed inspection. Early attempts that
introduced a smiling neutral anchor, removed Zacchaeus's gold garment borders,
failed to provide a usable climbing limb, or worsened the `s12` gaze were rejected
and never copied into the final asset directory.

All 26 accepted 1536×2752 frames are stored in `assets-realistic-v3/` and were
reviewed together in `story3-realistic-v3-contact-sheet-a.jpg` and
`story3-realistic-v3-contact-sheet-b.jpg`. The hash-backed face comparisons in
`identity-boards-v3/` record the accepted Jesus and Zacchaeus appearances.
