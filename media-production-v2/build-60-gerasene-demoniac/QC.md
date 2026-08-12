# QC / RUNNER HANDOFF — build-60-gerasene-demoniac (Mark 5:1-20)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 39 beats, ~226 s.

## Coverage shape

Seven true wides with stated geometry — a big-geography row: b01
(landfall in profile), b05 (the tomb-slope dwelling — one small figure
against the honeycombed face), b10 (THE RUN — camera behind and above
the man, downhill vector to the boat figures), b15 (the fearlessness
geometry — the row-54 distance thesis), b22 (the herd), b25 (the
stampede, bank in profile), b27 (the town's outpouring). Sixteen flips
including four LONE-FIGURE frames (b08 night memory, b32 walking to the
boat, b36 facing the gate, b38 the high road) — phantom people in any
of them break the story's loneliness-to-sending arc.

## CONTENT-CARE — adversary row, laws absolute (same as row 52)

- The afflicted man is a SUFFERING HUMAN: ragged, scarred by the
  broken shackles (marks, not wounds), wild-haired — never a monster,
  never contorted beyond human, no glowing eyes, no smoke.
- Night beats (b08) are misery, not horror — a man crying out alone.
- The entry into the swine is NOT depicted as an effect — the herd
  simply breaks and runs (b25); nothing visible travels.
- The stampede is the ONE violent frame: pigs pouring over the bank —
  no close-up drowning, no floating carcasses afterward.
- THE AFTER PICTURE (b28) is the row's target still: seated, CLOTHED
  (the borrowed tunic), in his right mind, at Jesus's feet. Calm is
  the miracle. Face-board him: SAME man as the wild frames, restored.

## Other checks

- Direction (row-83): b10 he runs DOWN toward the boat (both in
  frame); b26 herdsmen flee TOWARD town; b27 town streams DOWN to
  shore; b35 the commission arm points PAST him toward the town on
  its rise; b36-b39 his mission runs TOWARD/INSIDE the Gentile towns.
- This is GENTILE country — pig herds, a columned shrine, Decapolis
  skylines (b38-b39): the foreignness is stated, keep it; but no
  modern anachronisms (row 7).
- TOWN wired from build-38. SHORE promote-first from b01; HERD from
  b22. (This SHORE is the far/east shore — do NOT reuse row-51's
  Galilee fishing shore if suggested later.)
- The healed man's borrowed tunic is a DISCIPLE's spare — plain dark
  wool, never cream.
- Only Jesus wears cream.

## COMPLAINT LEDGER
- **OPEN (fixed this cut) — C-FIX 2026-08-11 (Machine A `Dev`):** Cameron, against live hash `2ac60fae` — *"2:39 that doesnt look like the man that Jesus just healed. The whole rest of the video has been showing him with black hair."* 2:39 falls on beat **b28** (`s28-sitting-at-his-feet.jpeg`, the after-picture). CONFIRMED on the live mp4: the healed man rendered with **light sandy/greying hair + a light brown beard**, while EVERY other frame of him (s10/s11/s12/s15 afflicted; s29/s30/s33/s34/s35/s37/s38/s39 restored) shows **black hair + a black beard**. **ROOT CAUSE:** the MAN lock TEXT was correct ("long matted black hair and a wild tangled black beard") but the beat rendered TEXT-ONLY — no MAN image was wired — so the earlier Jesus-eyes reroll of this same frame drifted the man's identity to a light-haired stranger. **FIX (durable, per the tight-crop lesson):** wired the already-accepted black-haired MAN portrait (`CAST-REF-V2/man.jpeg`) as an IMAGE character lock (`REFS = {"MAN": ...}` — the author's intended-but-skipped step, see the CAST-REF note in LOCKS) and rerolled ONLY b28. Reroll 1 kept a rough-draft of the old light-haired frame and the hair drifted grey/brown toward the draft; reroll 2 dropped the draft so identity comes only from the FACE + black-haired MAN locks + scene text — the man now renders **solid black hair + black beard**, matching man.jpeg and every other frame. Jesus's warm downcast gaze (prior eyes fix) did NOT regress. Verified in the RENDERED mp4 at 2:40. FULL-CUT GATE 6b: all 39 beats + card re-viewed — s28 was the ONLY complaint-worthy frame; everything else already clean, nothing else touched. 2 rerolls / 39 beats = **5.1%** (budget 15%), spend 2 × $0.134 = **$0.27**, $0 audio (AUDIO LOCK PASS, SHA256 `58abeeb5…` byte-identical). Meter $590.40 → $590.67.
- **CLOSED (prior cut):** Cameron, against live hash `9af3ae30898c` — *"2:39 Jesus eyes do not look good."* 2:39 falls on beat **b28** (`s28-sitting-at-his-feet.jpeg`, the after-picture). In the live cut Jesus's eyes rendered as a flat, pale, staring green — the one frame where the V2 lock's intended "green-amber-gold luminous" iris drifted to an unnatural washed-out light. **FIX:** rerolled ONLY b28 (1 reroll, `--only b28 --redo`); the new take has Jesus looking DOWN at the seated man with a warm, natural, downcast gaze — no pale-green stare. Verified in the RENDERED mp4 at 2:39. Every other Jesus close-up (b12/0:91, b14/1:44, b30/2:52, b32/3:20) was checked and already had correct warm eyes — so this was a true single-frame defect, not a whole-cut drift. All 38 other stills byte-identical; AUDIO LOCK PASS (SHA256 `58abeeb5…`), narration untouched.

## C-FIX 2026-08-07 (Machine A `Dev`)
Reroll of b28 only. 1 reroll / 39 beats = **2.6%** (budget 15%). Spend = 1 × $0.134 = **$0.13**, $0 audio. Touch-once: only open complaint on the row. Meter $419.42 → $419.55, ceiling $445.

## RUNNER LOG — resume 2026-08-06 (Machine A, A-auto)
Prior autopilot died mid-build at 24/39 stills. Resumed: portraits already
set (MAN ref), plates present (TOMBS, TOWN). Generated b25–b39 (15 stills)
under ceiling $441; `v2_gen_api` resumed clean, no re-pull of the 24 good
frames (COST LAW). 0 rerolls. Light QC pass — viewed target b28 (after
picture: man seated clothed & calm at Jesus's feet, only Jesus in cream),
b25 (stampede over the bank — no drowning close-up), b29 (restored face,
matches author's "same gaunt bones, hunted look gone"), b27/b32/b35/b39 and
lone frames b26/b38 (no phantom people, direction correct, columned
Decapolis background — Gentile country stated, no anachronisms).
- FIX-WAVE: b28 Jesus's eyes read slightly light/green — subtle drift, not
  rerolled per COST LAW; flag for the fix wave's face pass.
$ this run: ~$2.01 · rerolls 0/39 (0%).
