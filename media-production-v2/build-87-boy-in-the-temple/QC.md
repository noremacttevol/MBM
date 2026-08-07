# QC / RUNNER HANDOFF — build-87-boy-in-the-temple (Luke 2:41-52)

## ✅ REALISTIC-V2 SHIPPED — Opus runner, Machine A `Dev`, 2026-08-07 (UNATTENDED/HEADLESS)

**15 realistic painted stills @ native 2K (V1 had 8), 93.9s, 20.4 MB.**
AUDIO REBUILD PASS SHA256=`9cfd37091ef45645085113700051ae031f594bd8307a887dbfb85d447487d847`
(AUDIO_FROM_V1_SEGMENTS, 12 new-voice segments byte-identical — nothing re-voiced).
Row-74 stale-window tripwire CLEAR (captioned 85.900s ≈ card_start 85.826s → full
question card present); mp4 decodes ZERO `-v error`.

**COMPLAINT LEDGER: none open** (`v2_outline.py 87`). Fresh REDO-ALL realistic rebuild
of the old 8-still assembly.

**BOY-JESUS identity law held:** Jesus at TWELVE story-cast as a BOY (child scale,
warm olive, dark wavy hair, warm brown eyes) — the ADULT face ref does NOT apply; BOY
portrait generated + REFS wired and face-boarded across all his frames. **Only the boy
wears cream** at every age. Scale gate BOTH ways PASS — the twelve-year-old is child-
sized beside the seated elders in every frame (b04/b06/b09/b10/b13/b14), and no giant
elders; b12 is the deliberate "small cream figure amid great columns" single (scale
reads). MARY ~30 + JOSEPH ~42 aged from the nativity canon, consistent blue/brown
across the arc. Doctors are distinct astonished elders. Three road beats read three
distinct directions (festival flow b01 → backtrack b02 → home again b15).

**Light QC — 1 sweep (2 contact sheets + 1 reroll zoom + 3 rendered caption frames +
2 stable-point caption checks). 1 reroll / 15 = 6.7% (under the 15% COST-LAW budget):**
- **b11 (s11)** first take = the boy's hero portrait looked STRAIGHT INTO THE LENS
  (lens-stare reroll criterion). Rerolled → he now looks off-camera toward a parent
  (over-shoulder foreground figure); identity held (BOY ref wired).

**Places — ROAD wired from build-79 (`v2_stash.py --wire`, non-Jesus road frame,
3 road beats). PORCH + DOCTORS FORCED NO-PROMOTE:** every PORCH beat carries the boy
in cream (can't promote a cream-bearing frame → row-51/82 rule), and DOCTORS is a
cast group not a place (a place must never carry a character lock). Both left on their
prose locks; uniformity QC'd by eye (all porch frames read the same sunlit temple
colonnade). PLACE-WIRING.json = ROAD only.

**Caption/card QC (rendered mp4, output-seek):** white narrator captions in the bottom
band only; the t=4s "double text" was verified to be a normal caption CROSSFADE (stable
points t=2.5s / t=6.5s show clean single captions). Question card ("Even as a boy he
knew where he belonged. You were made for the Father's house too — come find your
place.") clean — no tofu/square glyphs, good margins.

**FIX-WAVE (kept — subtle, no filed complaint):** minor Joseph garment-tone drift
(brown ↔ rust) between b14 and b15; one seated elder in b10 in pale tan reads near-cream
(the boy is the clear-cream subject). Neither is garbage; rerolling would burn budget.

**Cost:** 2 portraits $0.27 + full run $2.01 + 1 reroll $0.13 = **~$2.41 this row**
(meter $463.91 → $467.79). Well under the $6.10/row average; 6.7% rerolls under the 19%
baseline — COST LAW trend holds DOWN.

---

## ✅ AUDIO FIX DONE — STALE-V1-FINAL lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (duration shortfall), no open Cameron complaint (`v2_outline.py 87`).
Parked only on the AUDIO LOCK: timeline 94.422s vs V1 mp4 93.000s (|Δ|=1.422s > 1.0).
Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler
rebuilds from this build's own 12 mp3 segments (present in the V1 audio/ dir) instead of
copying the stale V1 mp4 AAC. 0 V2 stills → per PROMPT-AUDIO-FIX.md step 6, ship nothing
visual: board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio (the rebuild path passes the lock). No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 15 beats, ~86 s.

## THE BOY JESUS (identity law — one of a kind)

- Jesus at TWELVE per his lock: a BOY (child scale — never a small
  adult), warm olive-brown, wavy dark hair, warm brown eyes, in cream
  (only he wears cream — the law holds at every age). The ADULT face
  ref does NOT apply; story-cast the boy and face-board him across
  his frames. He is earnest and luminous-natured, never precocious-
  smug.
- Scale-gate BOTH ways (row-56/69 class): a twelve-year-old beside
  seated elders — child-sized, and no giant elders.

## Nativity-block continuity

MARY here is ~30 (aged from 84-86's eighteen) and JOSEPH ~42 — FAMILY
RESEMBLANCE to the young canon, aged: same features older. If the
84-86 canon exists at build time, use it as the resemblance reference;
note the aging explicitly to the generator.

## Coverage shape

Three true wides with stated geometry: b01 (the festival road in
profile), b03 (the finding — camera behind the haggard parents toward
the seated circle: the reveal is THEIRS), b15 (the road home, camera
behind the three — subject-unto-them as a walking-away frame). Five
flips including b12 — the small cream figure amid great columns is a
SINGLE (phantom trap; the scale lives in prose).

## Other checks

- The DOCTORS: seated learned elders, listening AND asking (v46-47 —
  "both hearing them, and asking them questions... astonished at his
  understanding"): their faces carry genuine astonishment, not
  indulgence. Distinct men (90/107).
- Mary's line lands as a mother's three-days terror + relief; the
  boy's answer is earnest, not corrective. Both dignified.
- Direction (row-83): festival flow one way (b01); the urgent
  backtrack the other (b02); home again at the close (b15) — three
  road beats, three distinct readable directions.
- PORCH is temple-family — promote-first from b03 or --take the
  build-06 temple frame for family continuity (runner's choice; note
  which in the build log).
- Only the boy wears cream.


## RUNNER PARK (A-auto Machine A `Dev`, 2026-08-06) — NEEDS-AUDIO / STALE-V1-FINAL — $0 SPENT
Pre-flighted at step 2 BEFORE any credit (no stills generated, nothing to reuse-waste).

**BLOCKER — v2_assemble AUDIO LOCK will fail:** timeline total = 94.422s vs authoritative V1 mp4 `luke-2_boy-in-the-temple.mp4` = 93.000s.
Tripwire(s): RUNTIME |Δ|=1.422s > 1.0 (line 531). V1 mp4 SHORTER than timeline (trailing-silence shortfall).
The AUDIO LOCK copies the finished V1 mp4's AAC stream packet-for-packet; it refuses when the mp4 does not match the recomputed timeline.

**Why the runner cannot fix it:** the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py (rebuilds the track from this build's OWN mp3s at the timeline offsets — nothing re-voiced, V1 stays read-only). Editing beats_v2.py is outside the runner's allowed writes (art / QC.md / boards / SESSION-LOG / review card / mp4 only — PROMPT-OPUS-RUNNER.md hard rails). Same class as parked rows 69/74/77/78/80/82/83.

**FIX (author):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py  then this row builds normally.

**RESUME after fix:**
```
python3 media-production-v2/v2_story_cast.py build-87-boy-in-the-temple --ceiling <c>
python3 media-production-v2/v2_gen_api.py build-87-boy-in-the-temple --ceiling <c>
python3 media-production-v2/v2_assemble.py 87
```
