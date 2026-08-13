# QC / RUNNER HANDOFF — build-158-two-sticks (Ezekiel 37:15-19)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 22 beats, ~149.6 s. The two-records row (BRIDGE), kept entirely
in Ezekiel's own frame.

## THE STICKS are the row's props (prop-board them hardest)

Two FLAT wooden writing-rods, forearm length, each carved with one
short INDISTINCT name-line — the SAME wood tone every frame. State
per-beat: TWO separate rods through b09; the JOINING at b10; from b12
on, ONE rod of the same length carrying BOTH name-lines, its grain
merged SEAMLESS — joined, never spliced, never bound with cord, no
join-line. Any visible splice/cord/seam = reject. Script indistinct
always; NO readable text anywhere in the build.

## The joining happens in EZEKIEL'S hand — no divine hand ever

b10 (kv17): the two rods become one as EZEKIEL holds them; the wonder
is carried by the seamless result. "One in MINE hand" (God's, kv19) is
SPOKEN ONLY — no divine hand, arm, or figure is ever depicted. God is
never embodied anywhere: b01's assignment arrives as the arrested
listening posture by the canal, nothing more.

## The exiles are dignified

Displaced Judahite families in earth-toned robes (no cream — only
Jesus wears cream, and there are NO Jesus beats in this row). All
ages, never wretched, never uniform/twinned. Their asking (b02, b09,
b13) is honest hunger to understand — curiosity, not mockery.

## Registers and rhymes

- b21 = the four-word reunion: two long-parted brothers mid-embrace at
  the fire, foreheads together — the rod's joining done in people.
- b22 close = TWO scroll-records side by side in lamplight and ONE
  reaching hand arriving to take BOTH together — the read-them-both
  invitation, exact.
- Time-of-day arc (intentional): grey exile morning (river) → clear
  day (writing/joining) → golden afternoon (proclamation) → warm dusk
  fires (gathering) → lamplight (close).

## Coverage shape

One true wide with stated geometry: b01 (camera low on the bank,
taking the settlement from the side; Ezekiel at the canal's edge).
Everything else singles, two-shots and inserts. File order SCRAMBLED
(b02 sits at 89.10s, b08 at 39.58s, b10 at 61.28s) — build by WINDOW,
never by file order.

## Plates — three NEW places, promote-first

Stash had NO match for any of this row's settings (0 wired):
- RIVER (the Chebar settlement) — promote from b01's first good frame:
  `python3 media-production-v2/v2_stash.py --promote build-158-two-sticks RIVER <frame>`
- EXILES gathering ground — promote from its first good frame the same way.
- STICKS is a PROP lock, not a place — if the stash ever suggests a
  place-frame for it, REJECT (row-157 lesson: person/prop tokens must
  never place-wire). Carry the joined-rod look by prop-board instead:
  compare the rod across b10→b22 side-by-side before assembly.

---

## RUNNER RESUME — 2026-08-13 (Opus runner, Machine A `Dev`, unattended/headless)

Resumed AUTHOR-BOARD row 158 (State RUNNING / Claim A-auto) — a prior autopilot
lane DIED after generating only s01 (the b01 anchor). Already-shipped check FIRST:
NO committed V2 mp4, no mp4 on disk, live review card v158 still the OLD 2026-07-24
cut (`data-hash 356d4dbe`, no realistic-v2 wave) → genuine resume, not shipped.
Verified no live `v2_gen_api` sibling owns 158 (only the sibling agent lanes on
rows 181/142 are alive — different rows). Audio pre-flight PASS (extract total
167.819s vs V1 mp4 167.867s, diff −0.048s, newer_mp3s=0 → standard AUDIO LOCK,
no AUDIO_FROM_V1_SEGMENTS needed). Meter at claim $663.84; ceiling $694
(22 beats × 0.134 × 1.5 + 25 lane buffer).

### COMPLAINT LEDGER
`v2_outline.py 158` shows **NO open complaint** on this row. COMPLAINT LEDGER: none open.

### Face-lock fix applied BEFORE first credit (the #1 predictable failure)
Ezekiel is the story's SPINE — a legible face in 13 of 22 beats. The author
committed `CAST-REF-V2/ezekiel.jpeg` (a clean, dignified ~40 Middle-Eastern man,
full dark beard, dark charcoal-blue wool robe — on-lock) but left it UNWIRED
(no REFS dict), which renders him TEXT-ONLY and flips his face shot-to-shot
(RUNNER-LESSONS rows 52/55/60/63/153/177; rubric lessons 2/10/13). Wired
`REFS = {"EZEKIEL": "CAST-REF-V2/ezekiel.jpeg"}` — a runner-legal FACE-LOCK
(not a beat-content / lock-text edit), done BEFORE any credit so the whole build
renders identity-locked first-attempt (row-177 pattern; avoids the row-179
post-generation park trap). `--check` still PASS; gen log must print
`[+1 char ref: EZEKIEL]` on every EZEKIEL beat.

### PLATES — forced NO-PROMOTE (deliberate, lesson-grounded), plate-free build
The author QC listed RIVER + EXILES as "promote-first" places, but the runner
DECLINES both plates for this row (a "forced no-promote", lesson 675/1028/1211/
1329) — reasons:
- **RIVER spans three times-of-day** — grey exile morning (b01/b08) → golden
  afternoon proclamation (b16) → dusk fires (b17/b19/b20). Promoting the s01
  grey-morning frame as the RIVER plate would BLEED grey morning onto the golden
  and dusk beats (lesson 675: decline a place plate whose token spans two
  times-of-day; the time-of-day law). The RIVER LOCK text ("the same banks and
  settlement throughout") holds the canal/willow/mudbrick look while each beat
  renders its own time.
- **EXILES is a PEOPLE-lock, not a setting** ("the exile families — displaced
  Judahites…"), and its beats include intimate/single-emphasis frames (b02 & b11
  faces, b09 pressing-in, b21 the two-brother reunion). A peopled establishing
  plate forces its crowd composition onto those (lesson 1211/1329 = the "people
  vanish / same picture" failure class). The strong EXILES people-lock text
  (earth-tone robes, dignified, varied, NO cream) + each beat's own scene text
  hold it; QC every exile frame by eye in the FULL-CUT GATE.
- **STICKS is a PROP lock, never place-wired** (author instruction). Rod
  continuity (two flat rods → one seamless joined rod) carried by the prop-board
  eyeball across b03/b04/b06/b07/b08/b10/b12/b14/b15/b20/b22 before assembly.
The real cross-beat consistency risk here is Ezekiel's FACE — solved by the
image ref above, not by place plates. Plate-free build ALSO saves the promote
regens (COST LAW).

### Generation plan
Wire REFS (done) → run the plain skip-existing runner for the 21 missing beats
(`v2_gen_api build-158-two-sticks --ceiling 694`, NO --redo; s01 already on disk
is skipped) → FULL-CUT GATE per RENDERED frame incl. comparing s01's text-only
Ezekiel against the ref-locked majority (regen s01 only if it reads as a
different man) → assemble (standard AUDIO LOCK) → ship + deploy + live-verify.
