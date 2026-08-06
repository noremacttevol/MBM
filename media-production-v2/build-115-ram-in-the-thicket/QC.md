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
