# QC / RUNNER HANDOFF — build-140-bronze-serpent (Numbers 21:4-9 + John 3:14-15)

## C-FIX LIVE — 2026-08-16 (Machine A `Dev`, Codex + local Ollama)

Cameron's current-cut complaint: *"0:11 the boy has his lips messed up ... at
2:09 there is a picture floating in the sky ... the serpent should not be
pictured on a cross ... a long, weathered wooden staff with no crossbeams.
Redo every picture with the serpent on the cross."*

**Rendered-frame evidence (local `qwen3.5:27b` vision, actual pixels):**
- 0:11 maps to **b02**, not b01. Vision returned **FAIL**: the foreground
  child's lower lip has a dark irregular scab/lesion. Caption and the rest of
  the face are otherwise coherent.
- 2:09 maps to **b24**. Vision returned **FAIL**: a detached semi-transparent
  crowd/tent picture floats in the upper sky, and the pole visibly has a
  horizontal crossbeam.

**PROMPT AUTOPSY:**
- Serpent-on-cross = **CAUSED**. The SERPENT-POLE lock and b17/b20/b22/b23/b24
  prose explicitly demanded a crosspiece / cross-form. All are rewritten to
  one tall bare vertical staff with no horizontal member. The old
  `PLACE-REF/serpent-pole.jpeg` also visibly contains a crossbeam, so b17 must
  be regenerated once with `--no-plates`, vision-gated, then promoted as the
  replacement SERPENT-POLE plate before the remaining pole beats regenerate.
- Child's lip = **CAUSED**. b02 explicitly asked for "cracked lips," which the
  image model rendered as a lesion. The beat now requires dry but smooth,
  healthy, completely unmarked lips.
- Floating sky image = **ALLOWED**. b24 did not prohibit a memory/vision
  overlay. It now requires one unified physical scene and explicitly rejects
  floating, detached, misty or semi-transparent image elements.

**Targeted image work only:** b02 plus every beat carrying SERPENT-POLE
(b17, b18, b20, b21, b22, b23, b24). All other passing images and all narration are
locked. Generation may begin only after `v2_prompt.py --check` passes.

**Anchor gate:** `v2_prompt.py --check` = PASS (24 beats, v4). Regenerated b17
once with `--no-plates` so the old crossbeam plate could not contaminate the
replacement. Local vision = **PASS**: one tall bare vertical staff, no
crossbeam/crosspiece/horizontal bar; bronze serpent coiled around it; canonical
elderly white-haired/full-white-bearded Moses; one realistic coherent scene.
Promoted this passing b17 as the new SERPENT-POLE plate for all seven pole
beats. Cost: one required anchor generation, ~$0.13; meter $721.86→$721.99.

**Changed-frame gate:** the first contact sheet passed Cameron's three named
defects (b02 lips clean; all seven serpent shots use the straight staff; b24
sky is one physical scene), but caught one additional ship-blocker: b21 drew
an elderly grey-bearded dying man while b18/b19 follow the locked young
red-brown-tunic father. Autopsy = **ALLOWED**: b21 omitted `BITTEN-MAN` from its
locks. Added it and targeted b21 for one continuity rerender before assembly.
That continuity rerender exposed a second b21 blocker: blood-like marks on the
man's lips. Autopsy = **CAUSED**: b21 itself still asked for "cracked lips,"
contradicting the character lock's no-wound/no-blood law. Replaced that wording
with smooth, healthy, completely unbroken lips and added explicit no blood,
scab, lesion, cracked/marked lips or mouth injury negatives. One final targeted
b21 rerender is required; no other frame is reopened.

**FINAL C-FIX GATE — PASS:** the final b21 is the same young, dark-haired,
dark-bearded bitten father, with clean uninjured lips and a coherent raised
hand. Local `qwen3.5:27b` vision inspected the actual source pixels and returned
PASS separately for b02, b17, b21 and b24. The complete 24-source-still contact
gate also passes: cast/actions remain coherent, every serpent-pole image uses a
single bare straight staff, and b24 has one physical sky with no overlay.

Assembled `numbers-21_the-bronze-serpent.mp4`: 139.400s video / 139.396s audio,
20,838,830 bytes, SHA-256 `2ae60ecedc80ec218f1b2d2427a38039c45cbc63cb92f3f567a19f91d554dec2`.
`admin/verify-mp4.sh` PASS; full ffmpeg decode PASS. Audio stream remains
byte-identical to the approved narration lock, SHA-256
`90d6b582469c7e87d92adfe96f16df20de4386a3b55fa75c38c69ee526ada425`.
The rendered-frame gate inspected every beat plus the closing card. Exact
complaint frames 0:11 and 2:09, rendered b21, and the closing card all received
an overall and per-frame local-vision **PASS**: clean boy's lips; clean young
man's lips/hand; no crossbeam or cross shape; no floating sky picture; captions
contained in the bottom band; closing text legible, centered and unclipped.

Generation accounting: eight complaint-mandated final images (b02 plus all
seven pole beats) and two b21 blocker corrections = 10 calls, approximately
$1.34 total, meter $721.86→$723.20. No narration or already-passing unrelated
image was regenerated.

## ✅ SHIPPED — 2026-08-13 (A `Dev`, Opus runner, headless) — FIRST V2 CUT, b17 BLOCK CLEARED

`numbers-21_the-bronze-serpent.mp4` · 24 realistic stills · 139.4s · AUDIO REBUILD
PASS `90d6b582…` (built from the 15 V1 segment mp3s, AUDIO_FROM_V1_SEGMENTS=True,
OUTPUT_VIDEO_NAME set by runner — new-story row has no V1 mp4). 1 true reroll
(b21) = **4.2%** (budget 15%); b17 regen was the authoring-block fix, not a reroll.
Spend this session ≈ **$0.26** (b17 $0.13 + b21 $0.13); the 23 banked-good frames
were NOT re-pulled (touch-once / COST LAW). Meter 634.62 → 636.23.

**COMPLAINT LEDGER**
- **OPEN complaint (2026-08-11, story-level):** *"Did we just run out of stories…
  you are using somebody else's gospel to redo the same exact story we told
  earlier of the prodigal son… you shouldn't use 2 different people telling the
  same story."* → **RESOLVED by the story replacement itself.** The Naaman build
  (whose "way back / come home" moral duplicated #2 Prodigal Son) is ARCHIVED in
  `build-140-naaman-washes` and REPLACED by **The Bronze Serpent** — a DISTINCT
  wilderness event (Numbers 21:4-9) that is NOT a repeat of any earlier moral:
  its lesson is *look in faith to God's lifted-up provision and live*. It is the
  event **Jesus himself** chose to explain his own cross (John 3:14-15 —
  "as Moses lifted up the serpent… even so must the Son of man be lifted up"),
  so it is unique in the library and it earns its place. No other cut tells it.
  The review card answers Cameron in his own terms.

**FULL-CUT GATE (6b) — per-rendered-frame pass on all 24 beats + card:**
- b17 hero frame: Moses is now the OLD white-haired / full-white-bearded canonical
  man (matches s03/s11/s12/s13/s14) steadying the serpent-pole — the identity
  BLOCK is FIXED (MOSES ref attached: gen log `[+1 char ref: MOSES]`). Pole stayed
  byte-consistent with b18-b24 via the SERPENT-POLE plate; no plate re-promote
  needed (young-Moses did NOT bleed through).
- Identity: Moses consistent across all his beats; NO Jesus in-frame (OT era, correct);
  no cream robes anywhere. Realistic photography throughout (no cartoon/mix).
- Snakes are real venomous snakes, no horror-gore; the death beat (s10) is a
  dignified shroud; blacksmith (s16) is period tools; anatomy/hands correct; scale
  correct; captions bottom-band only, 4-voice coloring (scripture blue / God green /
  Jesus red / narrator white); question card clean.
- b21 (s21, the ~7.6s dying-man close-up) rerolled once: first take had vivid blue
  eyes on a prominent hold → rerolled to a muted grey-hazel dying man reaching
  toward the distant pole (reads "a dying man" better, hand anatomically correct).
- **FIX-WAVE (non-blocking, logged):** s06 a tiny ambiguous bluish speck by the far
  tents (background, non-subject); s24 a faint semi-transparent "vision" crowd in
  the upper sky (stylistic memory-overlay on the final redemptive frame). Neither
  reaches the "would make Cameron type a complaint" bar; left for the fix wave.


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
  HEARD, never shown — those beats hold on the lifted serpent and its one bare
  vertical staff.
- **Serpents:** real natural desert vipers, never monstrous/lunging/reared at
  camera. **The bitten and dying:** dignity only — fear, weakness, bound cloth,
  wrapped forms, grief. NEVER a wound, blood, gore, or an exposed corpse.
- **The anchor:** the bronze serpent on one plain, long, weathered, straight
  vertical staff with no crosspiece, crossbeam or horizontal member — the payoff
  (b17, b20, b22, b23, b24). It must never read as a cross; never a live snake.

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
