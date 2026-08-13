# QC / RUNNER HANDOFF — build-140-bronze-serpent (Numbers 21:4-9 + John 3:14-15)

## ✅ AUTHOR-FIX DONE — 2026-08-13 (A `Dev`, Fable-5 author lane, $0 image spend) — b17 BLOCK CLEARED, back on the RUNNER

The 🅿️ RUNNER PARK below (b17 identity block) is **RESOLVED at the author level**:
- **Root cause fixed:** added `"MOSES"` to b17's `locks` in `beats_v2.py` (was
  `["SERPENT-POLE","WILDERNESS-CAMP"]`, now `["MOSES","SERPENT-POLE","WILDERNESS-CAMP"]`).
  The char ref attaches by `locks` token — b17 is now symmetric with the working
  Moses beats (b03/b11/b13/b15), so `moses.jpeg` will attach on the regen. The
  prose "MOSES LOCK:" now appears in b17's ASSEMBLED prompt. `--check` PASS (24 beats).
- **`assets/s17-lifted-on-a-pole.jpeg` DELETED (git rm).** This is the ONLY frame
  removed — so the runner's `v2_gen_api` resume regenerates **exactly b17** (missing
  frame) and SKIPS the 23 banked-good frames (COST LAW / touch-once). Do NOT
  regen the 23 good frames.

### RUNNER — do this (row is AUTHORED + Ready ✅, complaint-first):
1. `python3 media-production-v2/v2_gen_api.py build-140-bronze-serpent` (resume —
   it fills only the missing s17 with the MOSES ref attached). Budget ≈$0.13, 1 frame.
2. **WATCH b17 in the FULL-CUT GATE:** Moses on the hero frame must be the OLD
   white-haired, full-white-bearded canonical man (matches s03/s11/s12/s13/s14),
   NOT a young brown-bearded man. **Caveat:** the `SERPENT-POLE` plate was
   `--promote`d from the OLD bad s17, so it carries the young Moses as its
   rough-draft. If that young Moses bleeds through the regen, reroll s17, then
   `v2_stash.py --promote build-140-bronze-serpent SERPENT-POLE s17-lifted-on-a-pole.jpeg`
   from the CORRECTED frame so b18/b20/b22/b23/b24 keep a clean pole (they do NOT
   need regen — their pole is fine and Moses isn't their subject).
3. `v2_assemble.py 140` (AUDIO LOCK from the V1 segment mp3s in
   `media-production/build-140-bronze-serpent/audio/`) → FULL-CUT GATE → ship
   (7a/b/c) → live-verify → **RESOLVE the Naaman-dupe complaint** (open→false,
   resolvedBy = ship hash; the Bronze Serpent replaces Naaman — review card carries
   the COMPLAINT LEDGER framing below). Then publish_ledger sync.

---


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

## ✅ RESOLVED 2026-08-13 (author lane) — RUNNER PARK → was NEEDS-REBUILD — 1 AUTHORING BLOCK on b17 (kept for provenance; see AUTHOR-FIX DONE at top)

**Status: all 24 stills GENERATED and FULL-CUT-QC'd (0 rerolls, ~$3.48, meter
624.71→632.88). 23/24 pass. ONE frame BLOCKS the ship and the fix is an AUTHOR
edit the runner is forbidden to make (editing `locks` is a hard rail). Do NOT
re-generate the 23 good frames — they are banked and correct.**

### THE BLOCK — b17 / s17-lifted-on-a-pole (the hero + promoted SERPENT-POLE plate)
b17 renders **Moses as a younger brown-bearded man in a fleece mantle**, but the
canonical Moses (ref-locked in b03/b11/b13/b15, rendered in s03/s11/s12/s13/s14)
is an **old man with long white hair + a full white beard, brown robe + dark
mantle, staff**. This is a lesson-2 (locked cast) / lesson-13 (beard board)
identity break on the single most important frame — exactly Cameron's row-102
"throws people off the story" class. It BLOCKS under the FULL-CUT GATE.

**PROMPT-AUTOPSY verdict = ALLOWED/IGNORED (lesson 2/10):** b17's `must_show`
NAMES "Moses steadying its base" in prose, but b17's `locks` =
`["SERPENT-POLE","WILDERNESS-CAMP"]` — it OMITS the `MOSES` cast token. The char
ref attaches by `locks` token, not by prose, so `moses.jpeg` never attached
(gen log for b17 shows only `[+1 place: WILDERNESS-CAMP]`, no `[+1 char ref:
MOSES]`) and the generator free-invented a non-canonical Moses. Words can't pin a
face; only the ref can.

### AUTHOR FIX (one token) then a $0.13 runner regen — the whole row then ships
1. **AUTHOR LANE (only they may edit beats):** add `"MOSES"` to b17's `locks`
   list in `build-140-bronze-serpent/beats_v2.py` (it already lists SERPENT-POLE
   + WILDERNESS-CAMP; just add the cast token the prose already names). No other
   change — do NOT touch scene text.
2. **RUNNER:** `cd media-production-v2 && python3 v2_gen_api.py
   build-140-bronze-serpent --only b17 --redo --ceiling <meter + 0.13*1.5 + 25>`.
   Because b17's `locks` still include SERPENT-POLE, the redo COPIES the promoted
   pole plate → the pole/bronze-serpent stays byte-consistent with b18-b24, so
   **b18/b20/b21/b22/b23/b24 do NOT need regen** and the touch-once law holds.
   The MOSES ref now attaches → old white-bearded Moses on the hero frame.
3. Eyeball the new b17 (old-Moses face + pole unchanged + no lens-stare), then
   `v2_stash.py --promote build-140-bronze-serpent SERPENT-POLE s17-lifted-on-a-pole.jpeg`
   ONLY IF the pole visibly shifted (it should not). Then `v2_assemble.py 140`
   (AUDIO LOCK from the V1 segment mp3s in media-production/build-140-.../audio/)
   → FULL-CUT GATE → ship (steps 7a/b/c) → publish_ledger sync.

### FIX-WAVE (minor, do NOT block; fold into the b17 re-cut if trivial)
- s21 (only-had-to-lift-his-eyes): the lifted-eyes incidental has notably
  pale/blue eyes — borderline; dark-haired so not a hard fail. Optional reroll.
- s24 (whosoever-believeth): a faint semi-transparent "vision" crowd is
  double-exposed in the upper sky — stylistic, reads as a memory overlay; leave
  unless Cameron flags.
- s06 (bread-called-worthless): a tiny bluish speck sits on the ground by the far
  tents — ambiguous (shadow vs object), background, non-subject. Glance on reroll.

### Board state set this session
QUEUE row 140 claim left in place with PARK note; AUTHOR-BOARD row 140 State →
NEEDS-REBUILD, Ready cleared (author lane picks it up), Claim carries this park.

COMPLAINT LEDGER unchanged (the Naaman-dupe complaint is still correctly answered
by this story — the block is an identity bug, not a story/complaint regression).
