# QC / RUNNER HANDOFF — build-115-ram-in-the-thicket (Genesis 22)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 32 beats, ~180 s.

## CONTENT-CARE — the hardest story, rendered per its authored laws

- THE BINDING IS NEVER SHOWN. The knife's only close frame is b18:
  FALLING from Abraham's OPENED hand — the release, not the raising.
  No bound child on an altar, no blade near the boy, ever. Any render
  approaching the act itself is an automatic reject with no reroll
  spent.
- Isaac carries the wood UNKNOWING (the not-knowing walk) — trust,
  never fear; his face open through the climb.
- The heavenly call (b14/b16): sky and light per the cloud-law — no
  figure, no visualized voice (the angel of the LORD here is voice-
  only per the authored beats).
- THE RAM (b21): caught by its HORNS in the thorn thicket — the turn
  finds it in-frame behind his shoulder (direction law); the ram is
  real, struggling gently, never anthropomorphic. The substitute
  doctrine is one image: the caught provider.

## Identity

ABRAHAM here is the SAME man as row 114 (locks should match — verify;
face-board across both rows). ISAAC: one age (a boy strong enough to
carry wood), the row-56 child class.

## Coverage shape

Four true wides with stated geometry: b05 (the small pair in
profile), b06 (both loads readable in profile — wood on the boy,
fire and knife with the father: the verse's exact distribution), b21
(the turn to the ram), b28 (the two counts — stars above, hand in
hand below). Ten flips including person-free Moriah frames.

- Grey dawn → white noon light → gold → starlit dusk: one direction.
- b31's far echo (the gaze toward one distant hill) is the quiet
  gospel link — dark hills only, nothing depicted.
- MORIAH promote-first from b01.

## RUNNER PARK — 2026-08-06 (A-auto Machine A `Dev`) — BILLING BLOCK, not audio

**Blocker: Gemini API prepayment credits DEPLETED — hard `429 RESOURCE_EXHAUSTED`
("Your prepayment credits are depleted") that PERSISTS across the mandated 60 s
retry.** This is a GLOBAL key-level block, not a per-row problem — it stops
every concurrent lane, so there is no other Ready row to fall to (the same key
is out of money everywhere). Cameron must top up in Google AI Studio billing
(https://ai.studio/projects → billing) before ANY row can generate again.

**Progress this session (all valid, DO NOT regenerate):**
- Portraits: ABRAHAM + ISAAC generated in `CAST-REF-V2/` (REFS wired into beats_v2.py).
- MORIAH place plate: promoted from b01 (`s01-it-is-one-of-the.jpeg`); PLACE-WIRING.json
  attaches it to 15 beats. b01 eyeballed clean (grey-dawn Moriah summit, stone
  altar cairn, thorn thicket foreground, period-correct, no modern objects, no figures).
- Stills generated: **16 / 32** — b01–b16 present in `assets/`. Stopped mid-b17
  when credits depleted. b17–b32 NOT yet generated (16 remaining).
- Meter at stop: $409.37. This row's spend so far ≈ $2.4 (2 portraits + 16 stills + b01 anchor).

**RESUME (after Cameron tops up Gemini billing) — exactly where it stopped:**
```
cd media-production-v2
python3 v2_gen_api.py build-115-ram-in-the-thicket --ceiling <recompute: meter + 16*0.134*1.5 + 25>
# then Light QC per PROMPT-OPUS-RUNNER step 5 (CARE: knife only FALLS in b18, never raised;
#   no bound child ever; ram caught by HORNS in thicket b21; scale + beard gates),
# then v2_assemble.py 115 (AUDIO LOCK pre-flight already PASSED: |Δ|=0.011s, recency PASS),
# then ship per steps 7a-c (DEPLOY firebase + live-verify), stash --scan, tick BUILT.
```
COMPLAINT LEDGER: none open (v2_outline.py 115 shows no reviewer complaint on this row).

## RUNNER SHIP — 2026-08-13 (A-auto Machine A `Dev`, headless) — BILLING CLEARED, ROW SHIPPED

Resumed the 2026-08-06 billing park. Gemini prepayment credits had reloaded (memory
`gemini-prepay-auto-reload`); dry-run + generation ran with no 429. Generated the
remaining **16 frames b17–b32** (~$2.14) against the banked 16 (b01–b16) + wired
ABRAHAM/ISAAC refs + MORIAH plate.

**COMPLAINT LEDGER: none open.** `v2_outline.py 115` shows no reviewer complaint; the
review card flag states the realistic-V2 change set (14 pics → 32 pics, native 2K).

**Light QC → 2 rerolls (b25, b32), 6.25% of 32 beats (COST LAW ≤15% ✅).** Both were
an ABRAHAM beard-board + head-covering drift (PROMPT-AUTOPSY verdict 3 — generator
ignored the attached ref): they rendered a shorter/fuller beard + draped hood instead
of the ref's long white beard. Rerolls restored the long-white-beard on-model face on
both. (The cap↔mantle-hood head covering alternates uniformly across the whole cut
incl. the banked b01–b16 half — a consistent stylistic variance, face+beard hold; not
an identity break, so not chased further.)

**CONTENT-CARE re-verified in the RENDERED mp4 (§6b FULL-CUT GATE, 32/32 + card):**
THE BINDING IS NEVER SHOWN — the knife only FALLS from Abraham's opened hand (s18),
lies alone/unused (s19/s29); the boy is free-standing, unbound, untouched and SAFE in
every frame; the ram is ALIVE, caught by its horns in the thicket (s21); the altar
smoke (s24) is the RAM burnt offering (Gen 22:13), never the child. No bound child on
an altar anywhere. GOD/THE ANGEL NEVER EMBODIED — heaven = light (s14), the divine
call is caption-only (no figure/beam/disc/halo). Speaker law: God-voice GREEN
(s18 "Lay not thine hand", s26 "in multiplying I will multiply thy seed"), scripture
BLUE (s09 "God will provide himself a lamb"), narrator WHITE, NO red-letter (OT, Jesus
absent). Realistic throughout (no cartoon/mix, Law 14); one Abraham, one Isaac;
ordinary scale; clean anatomy/hands; no modern objects/rotation/collage; captions
bottom-band; card clean. Grey-dawn → day-climb → gold-release → starlit-dusk holds.

Drop-check (lessons 173/89): concat_base = 32 clips == 32 beats; video 191.3s ≈ final
191.27s; AUDIO LOCK PASS SHA256 3ec248cbc1213e41a020588f847035de6a8081c424bc5a4b289cac875b68f718.
Meter at ship ≈ $681.1; this row ≈ $2.41 (16 stills + 2 rerolls this session; portraits
+ 16 stills were spent in the 2026-08-06 park). Under the $6.10 avg — COST LAW trend holds.

## QC-VERIFY — 2026-08-13 (Opus runner, Machine A `Dev`, headless) — CLEAN 32/32 + card, NOT re-cut

Independent FULL-CUT GATE (6b) re-check of the BUILT/unapproved cut before
Cameron's eyes reach it. `.approvals.json` row 115 = `approved:false` (the
`2026-07-18` approvedAt is a void pre-redo timestamp; approved flag governs) →
QC-VERIFY is in-scope, NOT an untouchable release decision. Live-verified the
shipped cut IS what Cameron sees: review.html card data-hash `4453e8aa` == ship
commit; served mp4 HTTP 200 = 20,233,750 bytes == local.

Extracted one frame per beat (mid-window, from the per-beat play-order clips
c000–c031) + 3 caption frames + 2 God-voice caption frames + the question card;
viewed EVERY one against the defect checklist + CONTENT-CARE + RUNNER-LESSONS.

**VERDICT CLEAN 32/32 + card:**
- **CONTENT-CARE fully held** (the hardest law on this story): the knife appears
  ONLY at rest — mid-air/falling toward the ground at the stay of the hand (b18)
  and lying beside the altar at night (b29); NEVER raised, NEVER near the boy.
  No bound child on the altar in any frame. Abraham stands alone at the wood-laid
  altar (b16) — Isaac is never placed on it. Boy safe + unbound + upright in
  every appearance. The ram is a real animal caught by its horns in the thicket
  (b20) / grazing (b21/b23); the altar shows smoke = the RAM's offering, never a
  burning child (b25).
- **GOD / the angel of the LORD NEVER embodied:** the heavenly-call beats are
  carried by light breaking through cloud (b14) and Abraham reacting (b15–b17) —
  no divine figure, no hand-from-sky, no beam-as-God.
- **Identity consistent:** Abraham one elderly man, full white beard, dark cap /
  dark headscarf, rust-brown robe every frame (cap↔scarf both dark, same face —
  not a beard/identity flip). Isaac one boy, dark curly hair, olive-green tunic.
  No cream/white robe on anyone (correct — OT, no Jesus in this story; jesus_face
  gate N/A).
- Realistic biblical photography throughout (Law 14, no cartoon/mix); clean
  hands/anatomy/feet, no extra limbs, no owl-neck; ordinary human scale
  (Abraham never a giant beside Isaac); first-century materials; no modern
  objects; no halo/glow/rim-light/lens-stare. Time-of-day arc holds: grey dawn →
  white noon → gold sunset → starlit night.
- **Captions:** narrator WHITE, God-voice GREEN (b18 "Lay not thine hand upon the
  lad…"; b26 "and in multiplying I will multiply thy seed as the stars of the
  heaven" both pixel-verified green) — SPEAKER LAW honored; bottom-band only,
  clean splits synced to narration, no tofu. Question card clean (cream card,
  dark serif, centered, no code-fault squares).
- **Watch-items (non-blocking, NOT the flagged defect class):** b27 Abraham has
  a faint natural wet tear catching starlight (reads as a real tear, NOT the
  solid painted "white tear" defect Cameron flagged on rows 51/71); b24 embrace
  has a natural kneeling foot at the frame edge (not an extra limb). Neither
  warrants spending a re-cut on a clean, unapproved cut.

**NOT re-cut** — touch-once holds; a re-cut would void nothing-here + re-queue
for no reason. Claim stamped `QC-OK 2026-08-13`. Appr stays ⬜ (Cameron's alone).
**$0 / 0 rerolls / 0 Gemini** (view-only verify).
