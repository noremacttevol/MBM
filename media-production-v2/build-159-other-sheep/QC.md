# QC / RUNNER HANDOFF — build-159-other-sheep (John 10:14-16)

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
