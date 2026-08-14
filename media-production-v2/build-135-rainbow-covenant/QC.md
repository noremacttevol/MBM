# QC / RUNNER HANDOFF — build-135-rainbow-covenant (Genesis 8-9)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 44 beats, ~250 s — the batch's biggest row.

## THE EIGHT ARE ALWAYS EIGHT (this row's own complaint class)

Row 135 IS the counts row in the complaint corpus. EXACTLY eight in
every family frame: Noah (white beard, umber), his wife (moss-green),
three sons (rust/slate-blue/brown), three wives (olive/madder/
charcoal). COUNT THEM in b02, b04, b05, b06, b08, b09, b17, b20,
b22, b24, b25, b27, b29, b36, b38 (+1 born-since child ONLY in b38),
b43. A seven or a nine is an automatic reject.

## Content-care gates

- The drowned world is CLEAN AFTERMATH only: mud flats, waterlines,
  driftwood — NEVER bodies or human wreckage, in any frame
  (b01/b03/b08/b12/b26).
- GOD NEVER EMBODIED: blessing/covenant arrive as light over lifted
  faces (b06/b19/b20/b36); the I-will-look vantage (b35) is an
  aerial view above cloud — no figure, no eye imagery.
- b12's flood memory: the ark on grey water at merciful distance —
  endurance, never catastrophe imagery.

## The bow doctrine set (b30-b35, check together)

Real rainbow, no sparkle effects. The battle-bow vignettes: b31 at
rest on its rack, b33 hung on wall pegs by scarred hands, visibly
UNSTRUNG — never a war scene. b32 reads the rainbow's geometry as
the hung-up bow aimed AWAY. b35 is heaven's-side vantage (above the
cloud-tops looking down).

## The fear arc (the row's heart)

b09 (one cloud, one wary wife) → b16 (Noah's stillness) → b17 (real
grey, the eight drawn together — deliberate weather) → b18 (the
wife's grief, unpunishing light) → b19 (the break) → b29 (wonder
before we see the bow) → b43 (the SAME faces transformed).
Face-board the eight across this arc especially.

## Rhyme frames

- b14 bare furrows → b15 same terrace greened (weeks later) → b39
  same valley, later season, bow up again.
- b38: the string around the child's finger beside the bow — the
  row's tenderest frame; the child appears ONLY here.
- b40/b41/b42: timeless later age — period-neutral, NO modern
  objects (row-7); children's delight in b41, not one fearful face.

## Coverage shape

Two true wides with stated geometry: b03 (the stilled ark — camera
low on the slope, hull from the side) and b08 (camera behind the
eight's backs over the washed valleys). File order HEAVILY
scrambled (b02 at 50s, b12 at 1.49s, b25 at 15s, b36 at 25s) —
build by WINDOW.

- Plates: none auto-matched (clean). ARK promote-first from b03,
  MOUNTAIN from b01, ALTAR from b10, FAMILY face-board from b04.
- Animal pairs (b07/b24): orderly, natural species, calm.


---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (19 newer mp3s / +42.3s).** Added `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`
(after `REF = True`). The authoritative track is now rebuilt from the V1 narration mp3s
at the extract_beats offsets instead of copying the stale V1 mp4's AAC stream that failed
`assert_v1_final_is_current`. **Validated ($0, no TTS, no Gemini):** rebuilt track = 263.338s,
delta 0.000s vs the mp3 timeline total (guard needs <0.5s). No re-voice — same voices,
wording, timing.

**Row is buildable.** 0 stills, so per the audio-fix protocol the board is flipped to
**AUTHORED / Audio OK / Ready ✅**; a picture runner generates the stills then runs
`v2_assemble.py 135` → AUDIO REBUILD PASS and ships the full cut on this fixed audio.

---

## 🛑 RUNNER PARK → NEEDS-REBUILD (author beat-text/lock fix) — Opus runner, Machine A `Dev`, 2026-08-13

Resumed the stranded RUNNING build (prior autopilot lane died at 42/44 stills).
Generated the last 2 frames (b43,b44) and ran the FULL-CUT GATE on all 44. **Did NOT
ship** — the row repeats its own OPEN reviewer complaint and the fix is out of runner
scope. Handing to the author lane with the good frames committed for reuse (COST LAW).

### COMPLAINT LEDGER
- **OPEN [MUST BE FIXED] (from `v2_outline.py 135`): "1st picture has 3 girls and 5
  boys that needs to change."** This is a GENDER-BALANCE complaint: the eight must be
  **4 men (Noah + 3 sons) + 4 women (Noah's wife + 3 sons' wives)**, all adults —
  Cameron counted 5 male / 3 female. NOT merely "8 total."
  - Literal 1st people-picture **s04** IS now 4m/4f (fixed).
  - **BUT the same 5m/3f drift still appears in FOUR family frames → shipping would
    RE-FILE the exact complaint (LEARNING LAW: worst possible failure). BLOCKS ship.**

### FULL-CUT GATE result (all 44 viewed from assets, count/gender audited)
- **CLEAN 4m/4f family frames:** s02, s04, s17, s20, s22, s29, s36, s43. (s43 rerolled
  from a 7-count to a correct 8 under a full bow; s08 rerolled to 8 adults / no child.)
- **DISTANT/non-count family frames (acceptable):** s05 (footprints, family a tiny top
  line), s24 (animals wide, eight tiny at top by design).
- **Landscapes/portraits (clean, realistic, no modern objects, no lens-stare):** s01,
  s03, s07(animals natural scale), s10, s11(altar), s12, s13, s14, s15, s16(Noah),
  s18(wife grief), s19(light, no figure), s21(covenant hands), s23(hands), s25(ramp,
  see below), s28, s30–s35(bow doctrine), s37, s39–s42, s44(closing bow, clean).
- **b38 (s38):** children ARE allowed here (the born-since child + string) — correct.

### ❌ FRAMES THAT REPEAT THE COMPLAINT (5m/3f or short-count) — need the author fix
- **s06 (b06)** — 5 men / 3 women.
- **s09 (b09)** — 4 men / 3 women (7 total). Original had a CHILD; 2 rerolls (cap hit)
  removed the child but stayed 7. **Root cause: b09's `must_show` centers "one of the
  wives" and does NOT pin the count** — unlike every clean count frame (b08 "exactly
  eight backs", b27 "count eight", b43 "the eight"). The scene's wife+husband emphasis
  reliably renders a nuclear 7. Runner-legal rerolls cannot fix a missing must_show pin.
- **s25 (b25)** — 5 men / 3 women (8 total on the ramp, wrong split). Not yet rerolled.
- **s27 (b27)** — 5 men / 3 women. Original 7 (4m/3f); reroll1 still 7; reroll2 (cap hit)
  landed 8 total but 5m/3f. The embrace-huddle keeps dropping a wife.

### ROOT CAUSE (systemic — author fix, one edit fixes all four)
The shared **FAMILY lock** (and the intimate/huddle beats b09/b25/b27) describe "eight"
but do NOT pin the **gender composition**, so ~⅓ of family frames drift to 5m/3f. A
runner may not edit locks or beat content (PROMPT-OPUS-RUNNER hard rail #1).

### AUTHOR FIX (touch-once, then a runner re-cuts on the committed audio)
1. Add to the FAMILY lock (and reinforce in b09/b25/b27 `must_show`): **"the eight are
   exactly FOUR men — Noah + his three sons — and FOUR women — Noah's wife + his three
   sons' wives — all adults, no children (except b38); no fewer, no more."** Give b09 a
   real count pin (its must_show currently says only "one of the wives").
2. `v2_prompt.py build-135-rainbow-covenant --check` must PASS.
3. Regenerate ONLY the four violators: **s06, s09, s25, s27** (`v2_gen_api.py
   build-135-rainbow-covenant --only b06,b09,b25,b27 --redo --ceiling …`) — the other 40
   frames are correct and MUST be reused (COST LAW — stills are gitignored but persist
   ON DISK on this one production machine; `v2_gen_api` never re-pulls existing frames).
4. FULL-CUT GATE for 4m/4f on every family frame, then `v2_assemble.py 135`
   (AUDIO REBUILD PASS — audio is already fixed/byte-stable, see the audio block above),
   ship + deploy + live-verify, and answer the "5 boys / 3 girls" complaint on the card.

### Spend this session
7 rerolls total (b43×2, b08×1, b09×2, b27×2) = 15.9% of 44 beats — a small overage vs
the 15% budget, spent hunting the count on the counts row before the systemic gender
cause was identified. ~$0.94 Gemini this session (meter ~$632.4). No audio touched.
**RESUME (author):** do the FAMILY-lock gender pin above, then step 3–4.

---

## CODEX AUTHOR REPAIR — Machine A `Dev`, 2026-08-13

### Prompt autopsy: **ALLOWED**

The rejected outputs did what the old prompt allowed. The shared FAMILY lock fixed the
headcount at eight but did not explicitly fix the sex composition at four adult men and
four adult women. The intimate b09/b27 staging also emphasized one couple while leaving
the remaining six under-specified, so the model could omit a wife or render a fifth man
without contradicting the literal prompt. Blind rerolls therefore repeated the complaint.

Authoring repair applied before spending another generation credit:

- FAMILY now pins **exactly four adult men** (Noah + three adult sons) and **exactly four
  adult women** (Noah's wife + the three sons' wives), with no child except b38.
- b06, b09, b25, and b27 now require all eight adults to remain separate and countable.
- b09, b25, and b27 use explicit four-couple geometry so a wife cannot disappear inside
  an ambiguous huddle; b06 uses a loose countable arc.
- Negative constraints explicitly forbid a fifth man, a missing fourth woman, a child,
  a ninth person, and merged figures.

Next gate: prompt check, then regenerate only b06/b09/b25/b27, visually count 4m/4f in
each result, run the full 44-beat cut gate, and assemble on the existing locked audio.

### Generation gate — attempt 1

- b06: PASS — exactly four adult men and four adult women, eight total, natural arc.
- b09: PASS — exactly four adult men and four adult women, eight total, one cloud.
- b25: PASS — exactly four adult men and four adult women, eight total, wet grass and
  open ark door behind them.
- b27: **REJECTED before assembly** — the people/count passed, but the model composed a
  landscape group inside a horizontal strip and filled the vertical canvas with blurred
  bars. Prompt verdict **ALLOWED**: four-couple semicircle implied a wide composition and
  the beat did not explicitly require continuous full-height portrait geometry. Added
  that positive geometry and explicit no-letterbox/no-blurred-bars constraints; reroll
  only b27.

### Generation gate — final replacements

- b27 reroll: PASS — continuous 9:16 portrait, exactly four adult men and four adult
  women in four readable couples, eight total; physical relief reads clearly; anatomy,
  garments, ground contact, background, and edge closure clean.
- Full asset contact-sheet gate: PASS — all 44 stills re-viewed in order; no cartoon
  frames, panels, modern objects, embodied deity, bodies/wreckage, or new scene-logic
  defects. Every output is native 1536×2752. The family-count audit remains clean in the
  previously accepted family frames; b38's explicitly authored child is the one allowed
  exception.
- Final paid work by Codex: 5 image generations (the four complaint replacements plus
  one b27 format correction), about **$0.67**; cross-session meter $721.05.

Ready for full-cut assembly on the locked V1-segment audio. No audio file, wording,
voice, timing, or story beat was changed by this repair.
