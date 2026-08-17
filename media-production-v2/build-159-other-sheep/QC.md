# QC / RUNNER HANDOFF — build-159-other-sheep (John 10:14-16)

## C-FIX LIVE — 2026-08-16 (Machine A `Dev`, Codex + local Ollama)

Cameron's current-cut complaint: *"0:59 picture is bad redo it."* Exact
rendered-frame tracing maps 0:59 / 59s to **b10** (57.40–60.90), not b09 or
b11. Local `qwen3.5:27b` vision inspected the actual rendered pixels and
returned **FAIL**: Jesus is shown only from behind, his identity and expression
are hidden, the prominent raised hand has fused/malformed fingers and an
oversized thumb, and the background contains an artificial horizontal haze
band with melted-looking structures.

**PROMPT AUTOPSY = CAUSED.** b10 explicitly required an over-the-shoulder view
from behind, made the raised hand the dominant foreground action without
pinning its anatomy, and asked for vague far haze. Fix: replace that staging
with a clean medium-wide three-quarter side view that keeps Jesus's locked face
visible and in focus at frame-left, keeps his fully natural five-fingered hand
small in the frame, preserves the required gesture toward frame-right, and
uses one continuous dry slope, distant hills and open sky with no haze band or
premature settlement. Regenerate **only b10**; all other pictures and all audio
remain locked.

### ✅ C-FIX FINAL GATE — SHIP CANDIDATE

- Generated **only b10**: 1 still, $0.13, meter $723.33 → $723.47. The other
  19 source stills remain untouched.
- Replacement source inspection: local `qwen3.5:27b` vision **PASS** — one
  coherent hillside scene; one correctly locked Jesus with his face visible;
  one natural right hand with one thumb and four separate fingers; gesture
  exits frame-right; no duplicate Jesus, haze band, melted structure, halo,
  modern object, malformed person, or composite defect.
- Exact rendered 59s complaint frame: independent local vision **PASS** on the
  final pixels; the caption is readable and wholly inside the bottom band.
- Full-cut gate: all 20 chronological rendered scene midpoints inspected;
  Jesus, shepherd, travel direction and fold continuity hold. Closing question
  card independently vision-checked **PASS** (centered, readable, unclipped).
- `verify-mp4.sh`: PASS; full FFmpeg decode: PASS. Duration 142.366667s,
  19,416,706 bytes. MP4 SHA256
  `6c6fc490c2d7d7f2a82676cdfc011e1373009615a2dc0f99b6239b0962ac54fb`.
- Audio stream SHA256
  `8bcd7cab6b2d13748ac22f3161c544ac3bf6369d59f24b2eb0f7717378198c5d`
  exactly matches the pre-fix approved audio stream. No narration changed.

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 20 beats, ~127 s. Same John 10 shepherd discourse as row 143
(i-am-the-door) — this row EXTENDS 143's canon.

## The shepherd IS build-21's/143's shepherd (cross-video identity)

SHEPHERD lock byte-identical with rows 21/143 — ONE parable shepherd
across the library. He appears in b02-b06, b14, b17-b20. He is the
parable's shepherd, NOT Jesus: dark earth-brown tunic, never cream.
Face-board him against build-21's frames AND 143's.

Jesus appears as HIMSELF only in the five teaching beats (b01, b07,
b09, b10, b15) — jesus/ref flags set; he wears cream; hand-flat-at-
chest on kv14's "I am" (the I AM series signature, b07).

## The fold law (143's gap law holds)

FOLD lock byte-identical with 143; the FOLD plate (build-21 b12) is
wired to b14/b20. Exactly ONE opening, NO gate, NO bars, ever — a
rendered gate is an automatic reject.

## Direction law (row-14) — the row's geography

Home world (hillside, fold) = frame-LEFT; far country = frame-RIGHT.
- b10: Jesus's pointing arm exits RIGHT.
- b16: the lone sheep's ears/gaze turn LEFT toward the unheard call.
- b17/b19: the shepherd travels LEFT-TO-RIGHT (going out to them).
- b14/b20: arriving sheep move RIGHT-TO-LEFT into the fold.
Check every travel/gaze against this before assembly.

## The far country is UNNAMED (content care)

b11/b12: a different hill country at warm dusk — NO map, NO
recognizable geography, NO doctrine props. The row says only "other
places." Dusk kept WARM, never ominous.

## Registers and rhymes

- b05 (sheep lifting heads) → b12 (far-country PEOPLE lifting heads)
  — the promise rhyme; both must read as the same motion.
- b13: TWO converging flocks EQUAL in size and light — any
  favoured/forgotten grading = reject.
- b08: listeners stopped COLD — arrested attention, never anger.
- b16: the outsider sheep is FAR, never injured/trapped/pitiful.
- b20 close: the far sheep one MID-STRIDE step from the gateless
  opening, the shepherd's hand out — arriving, not arrived.

## Coverage shape

One true wide with stated geometry: b01 (camera low behind the
seated listeners, frame climbing the rise to Jesus; fold small
beyond frame-left). File order = story order; windows contiguous
0.28–126.74.

- Plates: FOLD auto-wired (build-21 b12 — the frame 143 accepted;
  the man in it IS this row's locked shepherd). NEW places:
  HILLSIDE promote-first from b01's first good frame, FAR-COUNTRY
  promote-first from b11's:
  `python3 media-production-v2/v2_stash.py --promote build-159-other-sheep HILLSIDE <frame>`
  `python3 media-production-v2/v2_stash.py --promote build-159-other-sheep FAR-COUNTRY <frame>`

---

## COMPLAINT LEDGER (LEARNING LAW)
- `.approvals.json["159"]` = NO ENTRY → never approved, never complained.
  `v2_outline.py 159` shows no open complaint. **COMPLAINT LEDGER: none open.**
- QUEUE.md cross-check: row 159 = "Other sheep I have" (John 10:16), all-columns
  ✅ — NOT a swapped/replaced story. The dupe that was purged was row **134**
  (its old build WAS other-sheep, archived, replaced with today-in-paradise);
  #159 is the canonical keeper. Safe to build.

## RUNNER PARK — 2026-08-13 12:44 (Opus runner, Machine A `Dev`, headless)
**Status: RUNNING/claimed, generation blocked by a TRANSIENT GOOGLE-SIDE IMAGE-ENDPOINT OUTAGE (NOT billing, NO Cameron action needed).**

Work banked this session (valid, do NOT regen):
- `CAST-REF-V2/shepherd.jpeg` — SHEPHERD story portrait generated + wired into
  `beats_v2.py REFS` (defuses the #1 RUNNER-LESSON cross-location-drift block:
  SHEPHERD spans 9 beats across HILLSIDE/FAR/FOLD; QC'd on-lock — Middle-Eastern
  ~35, black hair+beard no grey, deep-brown skin, dark-brown rough wool tunic
  (NOT cream), olivewood staff, clean anatomy).
- `assets/s01-on-a-hillside-surrounded-by.jpeg` — b01 establishing wide.

Blocker diagnosis (definitive, so nobody re-diagnoses on the meter):
- Last successful gen board-wide = my s01 @ 12:22. As of 12:44, **16+ min of ZERO
  frames on EVERY lane** (build-154 sibling frozen at 12:16 too).
- `gemini-3-pro-image:generateContent` **HANGS** — 3 direct curl probes each
  `HTTP 000 / time_total 45–90s` (no response body, no 429, no error).
- **Key is HEALTHY / billing is FINE**: a text-model probe returned an *instant*
  404 ("model no longer available") — proves the key reaches Google and is NOT
  billing/permission-blocked. This is an IMAGE-ENDPOINT infrastructure outage on
  Google's side, self-healing — it is NOT the prepay-depleted wall and needs NO
  top-up / NO inbox escalation.

## RUNNER PARK #2 — 2026-08-13 13:54 (Opus runner, Machine A `Dev`, headless)
**Task = RESUME row 159. Did the diligent resume; endpoint STILL down → re-parked clean, $0/0.**
- Ran the RUNNER-LESSONS already-shipped check FIRST: no committed V2 mp4, review
  card `id="v159"` is the OLD V1 (data-built 2026-07-28, no `data-review-wave`),
  so row 159 is NOT shipped — correct to resume, not tick BUILT.
- Endpoint verified STILL walled ~91 min after the 12:44 park: last board-wide
  frame in api-spend.jsonl = **12:22:14** (my own s01); now 13:54. Probes this
  session: image-model returned **503 UNAVAILABLE ("high demand")** ×3 then
  **HTTP 000 (30s hang)** — oscillating, still not serving images. A text-model
  probe returned an **instant 404** ("model no longer available") → key reaches
  Google, authenticated, **NOT a billing/prepay wall, NO top-up needed** (same
  self-healing Google-side image-endpoint outage as the 12:44 park + row 160).
- **Real resume attempt made (not just probes):** ran
  `v2_gen_api.py build-159-other-sheep --ceiling 739.82` in the FOREGROUND for a
  full 9.5 min. It resumed correctly (kept s01 + shepherd portrait, tried s02–s20)
  and produced **0 new frames / $0** — every beat hit the 503/000 wall and was
  skipped per-beat. Confirms the outage, not a per-row problem.
- Banked work still valid, do NOT regen: `CAST-REF-V2/shepherd.jpeg` + s01.
- No inbox escalation: transient endpoint outage self-recovers, needs nothing
  from Cameron (row 159/160 precedent). Board handed back AUTHORED + blank claim
  so autopilot/next runner re-picks it the instant the endpoint answers.

## RUNNER PARK #3 — 2026-08-13 18:15 (Opus runner, Machine A `Dev`, headless)
**Task = RESUME row 159 (lowest Ready). Endpoint STILL down → re-parked clean, $0/0.**
- Same self-healing Google-side image-endpoint outage, now **~6 h board-wide** (last
  frame in api-spend.jsonl = **12:22:14**, my own s01; now 18:15). Probes this
  session: **4/4 image-model = HTTP 503 UNAVAILABLE ("high demand"), sub-second**;
  a `models?list` probe = **instant HTTP 200** → key HEALTHY, authenticated, billing
  FINE, **NOT a prepay wall / NO top-up / NO inbox escalation** (rows 159/160/162/164
  precedent — all four sit AUTHORED empty-claim, re-pickable). Board-wide → NO row
  is buildable, so this is a genuine truly-blocked stop, not a per-row skip.
- Did NOT re-burn a full `v2_gen_api` run: the 4/4 flat sub-second 503 + the 13:54
  real 9.5-min foreground resume (0 frames / $0) already prove the endpoint, not the
  row. Banked work still valid, do NOT regen: `CAST-REF-V2/shepherd.jpeg` + s01.
- Meter unchanged **$711.00**. $0/0 gen, 0% rerolls.

## RUNNER PARK #4 — 2026-08-13 18:45 (Opus runner, Machine A `Dev`, headless)
**Task = RESUME row 159 (lowest Ready, LOW-NUMBER LAW). Endpoint STILL down → re-parked clean, $0/0.**
- Same self-healing Google-side image-endpoint outage, now **~6 h 23 m board-wide**
  (last frame in api-spend.jsonl = **12:22:14**, my own s01; now 18:45). Probes this
  session: **11/11 image-model = HTTP 503 UNAVAILABLE ("high demand") / one HTTP 000**,
  sub-second — 1 initial single-probe + a 6-attempt loop (18:41→18:43) + a 4-attempt
  loop (18:43→18:45), full JSON body confirmed the 503 UNAVAILABLE error; a
  `models?list` probe = **instant HTTP 200** → key HEALTHY, authenticated, billing
  FINE, **NOT a prepay wall / NO top-up / NO inbox escalation** (rows 159/160/162/163/164
  precedent — all sit AUTHORED empty-claim, re-pickable). Board-wide → NO Ready row
  is buildable, so this is a genuine truly-blocked stop, not a per-row skip.
- Did NOT set row 159 RUNNING or re-burn a full `v2_gen_api` run: 11/11 flat sub-second
  503 across ~4 min + the 13:54 real 9.5-min foreground resume (0 frames / $0) already
  prove the endpoint, not the row; setting RUNNING with only 1 banked frame would
  falsely strand it from the resume lane. Banked work still valid, do NOT regen:
  `CAST-REF-V2/shepherd.jpeg` + s01.
- Meter unchanged **$711.00**. $0/0 gen, 0% rerolls. (Note: api-spend.jsonl carries 1
  pre-existing malformed line from a concurrent-write race — left untouched, another
  lane's shared file; meter math skips it.)

RESUME (once the image endpoint responds again — a text/image probe returns 200,
or a sibling lane's frame lands in api-spend.jsonl):
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
# resumes automatically, re-pulls ONLY s02–s20 (s01 + portrait are kept)
M=$(python3 -c "import json;print(round(sum(json.loads(l).get('est_cost',0) for l in open('api-spend.jsonl') if l.strip()),2))")
python3 v2_gen_api.py build-159-other-sheep --ceiling $(python3 -c "print(round($M+19*0.201+30,2))")
```
Then: Light-QC each frame (SHEPHERD identity board across b02-06/b14/b17-20;
NO gate/bars in FOLD b14/b20; direction law home-LEFT/far-RIGHT; scan jesus=False
beats for a stray cream/Jesus-double; scale/anatomy/modern-object/letterbox/
rotation). **Plates:** FOLD plate is committed — do NOT `--wire` (it overwrites);
HILLSIDE (all-Jesus beats) + FAR-COUNTRY (2 beats) stay TEXT-LOCK, do NOT promote
from a Jesus/subject frame (row-152/row-1050 precedent). Then `v2_assemble.py 159`
(AUDIO LOCK PASS) → FULL-CUT GATE 20/20+card from the RENDERED mp4 → ship (two
commits) → deploy + live-verify → stash --scan → publish_ledger sync.

---

## RUNNER BUILD + SHIP — 2026-08-13 (Opus picture runner, Machine A `Dev`, headless)

**Endpoint RECOVERED** (other lanes gen'ing frames ~1 min before claim; api-spend
last frame in EDT clock). Claimed row 159 RUNNING (`A-auto 2026-08-13`), built the
19 remaining beats on the banked SHEPHERD portrait + s01, shipped.

### COMPLAINT LEDGER (LEARNING LAW)
- `.approvals.json["159"]` = NO ENTRY, `v2_outline.py 159` shows no open complaint,
  QUEUE cross-check PASS (John 10:16 "Other sheep I have" = build-159-other-sheep,
  NOT the purged row-134 dupe). **COMPLAINT LEDGER: none open.**

### Plates
- HILLSIDE promoted from banked s01 (manual) → wired to the 5 Jesus beats
  (b01/b07/b09/b10/b15). FAR-COUNTRY promoted from b11 (after reroll) → wired to
  b11/b12. FOLD kept as the committed build-21 plate (did NOT `--wire`, per lesson).

### Light QC — every source frame viewed (20/20)
- SHEPHERD identity consistent across b02/04/06/14/17/18/19/20 (Middle-Eastern ~35,
  black hair+beard, brown wool NOT cream, olivewood staff). Jesus consistent +
  cream-only across b01/07/09/10/15; hand-flat-at-chest on kv14 (I-AM signature).
- Direction law held: home-world/fold frame-LEFT, far-country frame-RIGHT; b10
  Jesus points RIGHT, b16 outsider sheep gazes LEFT, b17/19 shepherd travels L→R,
  b20 far sheep mid-stride to the gateless opening. Two flocks EQUAL (b13). FOLD =
  open stone enclosure, NO gate/bars (b14/b20). Realistic photography, no cartoon/mix.

### Rerolls (COST LAW: budget 15% of 20 = 3; used 2 = 10% ✓)
- **b11 FAR-COUNTRY (reroll 1):** first take put the far-country children in bright
  RED tracksuit + GREEN modern jersey = historical-coherence fail (lesson 6). Autopsy
  = ALLOWED (FAR-COUNTRY lock is "unnamed/universal", never pinned first-century garb).
  Reroll landed period earth-toned hooded cloaks, warm dusk, no map/doctrine props.
- **b10 (reroll 2):** first take rendered a DUPLICATE JESUS (second long-haired
  bearded cream-robed figure in the far country, in a glowing mist) = second-cream +
  duplicated sacred figure + glow. Autopsy = ALLOWED (nothing forbade a background
  figure across the water). Reroll: single Jesus, back to camera, pointing RIGHT to
  the far country, no double, clean anatomy.

### FULL-CUT GATE (6b) — from the RENDERED mp4
- concat_base.txt = 20 files = BEATS (no dropped-beat; card_start check OK). AUDIO
  LOCK PASS SHA256=8bcd7cab6b2d13748ac22f3161c544ac3bf6369d59f24b2eb0f7717378198c5d,
  142.4s / 19.3 MB.
- Caption law verified on rendered frames: narrator WHITE (n7), Jesus red-letter RED
  (kv14 "I am the good shepherd…", kv16 "And other sheep I have…" — both speaker=jesus,
  correct red-letter, NOT blue), all in the bottom band, two-line synced, never over
  the art. Closing card clean serif on cream, no typo-squares, correct margins,
  question "When you hear his voice, will you follow?"

### FIX-WAVE (non-blocking, logged; not rerolled — COST/recurrence)
- Small yellow plastic livestock EAR-TAGS appear on some sheep across several frames
  (b02/04/05/06/13/14/16/20) — a modern object (lesson 6). Tiny at Ken-Burns/phone
  scale, background only, never a foreground/named-complaint subject; rerolling won't
  reliably remove them (model's sheep carry them) and would blow the 15% budget.
  Durable fix is an AUTHOR-lane `must_not_show` "no ear tags / no plastic livestock
  tags" clause on every sheep beat. Logged to RUNNER-LESSONS.

### COST
- This session: **2 rerolls / 20 beats = 10%** (≤15% ✓, under the 19% baseline).
  ~24 paid images this session (s01 was pre-banked; b11 ×2, b10 ×2, +18 batch) ≈
  **~$2.68**. Meter moved $713.42 → ~$718.91 (shared with concurrent lanes). $/row
  well under the $6.10 average — cost trending DOWN per COST LAW.
