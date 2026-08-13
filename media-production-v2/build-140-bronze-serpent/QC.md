# QC / RUNNER HANDOFF — build-140-bronze-serpent (Numbers 21:4-9 + John 3:14-15)

## ✅ AUTHORED FRESH — Ready for the runner (2026-08-13, Machine A `Dev`, Fable-5 author lane, $0 image spend)

Row 140's story was REPLACED per Cameron (the archived Naaman package carried a
prodigal-duplicate moral he rejected). This is the wholly new, distinct story he
approved by handoff: **The Bronze Serpent** — the wilderness event Jesus HIMSELF
chose to explain his cross (John 3:14). `--check` PASSES (24 beats, zero WARNs);
`audio_audit --rows 140` clean (new ElevenLabs voices). 139.4 s, 24 pictures.

### COMPLAINT LEDGER (the open reviewer complaint this row answers)
- **OPEN — Cameron on the old Naaman cut: "using somebody else's gospel to redo
  the same exact prodigal-son story… did we run out of Jesus stories":** FIXED by
  CUTTING Naaman entirely and authoring a genuinely distinct account. The Bronze
  Serpent is NOT a prodigal/return story and NOT a Nicodemus dupe (#4 is the John
  3 conversation; this is the Old-Testament type it points back to). Its moral —
  *look in faith to God's lifted-up provision and live* — is unique in the 200.
- **Review-card flag for Cameron:** *"You said Naaman repeated the prodigal's
  'coming home' lesson — so I cut it and built the story Jesus used to explain his
  own cross: the bronze serpent lifted on a pole, 'look, and live' (John 3:14).
  Its own lesson, no repeat."*

## Story + speaker map
- 14 narration segments + card. NARRATOR (white) modern; the people's KJV lines
  p1 (Num 21:5) / p2 (Num 21:7) and the narrative verses s1 (21:6) / s2 (21:9) in
  the SCRIPTURE voice (blue); the LORD's command g1 (21:8) in the GOD voice
  (green — OT Jehovah, NOT red-lettered); Jesus's own words j1 (John 3:14-15) in
  the JESUS voice (red). All ElevenLabs (Brian/Roger/Bill/Chris per the cast).
- **AUDIO_FROM_V1_SEGMENTS is NOT set** — this build has no rendered V1 mp4, so
  v2_assemble builds the track from the V1 segment mp3s in
  `media-production/build-140-bronze-serpent/audio/`. (If the AUDIO LOCK asks for
  the flag, that dir is already the source of truth; set it.)

## CARE (hard rails — an autoreject on violation)
- **No divine figure anywhere (OT era).** The LORD (g1/b14-b15) is HEARD, shown
  only as formless brilliant warm light in the sky — never a figure, disc, orb,
  ring, beam or UFO, never a halo/glow/rim-light word. Jesus (j1/b23-b24) is
  HEARD, never shown — those beats hold on the lifted serpent / cross-form.
- **Serpents:** real natural desert vipers, never monstrous/lunging/reared at
  camera. **The bitten and dying:** dignity only — fear, weakness, bound cloth,
  wrapped forms, grief. NEVER a wound, blood, gore, or an exposed corpse.
- **The anchor:** the bronze serpent on a plain straight pole (one short
  crosspiece) whose silhouette reads as an upright CROSS-FORM — the payoff (b17,
  b20, b22, b23, b24). Never a wooden cross with a body; never a live snake on it.

## NEW PLACES — promote-first (lesson 11); no stash plate exists yet
- **WILDERNESS-CAMP:** promote the first good frame (b01 establishing wide) with
  `v2_stash.py --promote`, then generate b02/b03/b07/b08/b10/b11/b13/b17/b20/b24
  with that plate so the camp/terrain stays one place.
- **SERPENT-POLE:** promote from **b17** (the raised-pole hero) BEFORE generating
  b18/b20/b22/b23/b24 so the pole + bronze serpent are byte-identical across the
  climax and the John 3 close. This is the film's payoff — its consistency matters
  most.
- Person locks MOSES and BITTEN-MAN are text-locked here; build the per-character
  face + beard board at assembly (Moses appears b03/b11/b13/b14/b15/b17; the
  bitten father b09/b18/b19). No Jesus/God reference is attached anywhere.

## Coverage / framing notes
- Look-and-live SEQUENCE is three frames (lesson 12): b18 the bitten man TURNS to
  look → b19 he is made WHOLE → b20 the whole camp lifts their faces. Keep them
  distinct; do not collapse.
- Wides (b01/b17/b20/b24) carry the camera-behind-backs geometry in scene text
  (row-14 law) — hold the model to it; reject a posed line-facing-lens frame.

## Resume (runner)
`python3 media-production-v2/v2_prompt.py build-140-bronze-serpent --check` (PASS)
→ promote the two places as above → generate 24 stills at native 2K → face/beard
board → `v2_assemble.py` (AUDIO LOCK from the V1 segment mp3s) → ship. Reroll
budget ≤15% of 24 beats (≈3). Touch once.
