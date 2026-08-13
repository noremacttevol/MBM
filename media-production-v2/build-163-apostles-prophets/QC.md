# QC / RUNNER HANDOFF — build-163-apostles-prophets (Ephesians 2:19-20)

**AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).**
`beats_v2.py` written from scratch: 18 pictures over 116.71 s (6.5 s/pic).
`v2_prompt.py --check` PASS. Windows contiguous + monotonic (0.280 →
116.714 = card seg_start). Audio OK on AUTHOR-BOARD. Ready ✅.

## PARK #1 — 2026-08-13 ~18:25 UTC (Opus runner, Machine A `Dev`, headless) — BOARD-WIDE gemini-3-pro-image OUTAGE, $0/0 gen
Row 163 requested as the next Ready row. Cross-check vs QUEUE.md PASS (Eph 2:19-20,
not a swap). **BLOCKED before first credit by the same self-healing board-wide
`gemini-3-pro-image` outage that parked rows 159/160/162/164 all day:** image
endpoint returned flat **HTTP 503 UNAVAILABLE** ("high demand"), sub-second, on
**12/12 probes** (3 quick + a 9-attempt / ~8-min foreground retry loop, all 503);
`models?list` health probe = instant **HTTP 200** → key HEALTHY, billing FINE,
**NOT the prepay wall**, no top-up / no inbox escalation. Last board-wide frame in
`api-spend.jsonl` = **12:22:14** (row 159 b01); now ~18:25 → **~6 h ZERO frames
from ANY lane** = board-wide, blocks every Ready row identically. $0 spent, meter
unchanged $711.00. Board left AUTHORED / Claim BLANK / Ready ✅ — re-pickable the
instant the endpoint answers. **RESUME COMMAND (from repo root):**
`python3 media-production-v2/v2_story_cast.py build-163-apostles-prophets --ceiling <meter+~5>` (portraits) →
`python3 media-production-v2/v2_gen_api.py build-163-apostles-prophets --ceiling <recompute>` (18 beats, promote the 6 place plates first per §STRUCTURE) →
full-cut gate → assemble → ship (two commits) → deploy → live-verify.

## RUNNER BUILD + SHIP — 2026-08-13 (Opus runner, Machine A `Dev`, headless)
Endpoint RECOVERED (rows 138/160 lanes generating frames ~15:00). Built the row
end-to-end. `v2_prompt.py --check` PASS. Meter at claim ~$712.

**Plates (2 promoted first, the two 8-beat dominant places):**
- HOUSEHOLD ← b03 (door easing open, people-free — anchors the bookend doorway
  arc b04/b16/b18) `--promote`.
- BUILD-SITE ← b07 (establishing wide, incidental mason back — anchors the whole
  construction half) `--promote`.
- FAMILY/OUTSIDERS/BUILDERS/WITNESSES left on lock text (2–5 beats each, per the
  "2–3-beat place is fine on lock text" lesson) — they held.

**QC / rerolls (2 of 18 = 11%, under the ≤15% COST-LAW budget):**
- **b11 cornerstone-set — REROLLED.** Take 1 rendered a small incised CROSS/plus
  mark on the corner stone's face. PROMPT-AUTOPSY = the beat's own `must_not_show`
  ("no invented mark on the stone") was IGNORED (generator drift, verdict 3) — a
  plain `--redo` landed a clean stone (masons aligning with plumb line + mallet,
  no mark). Kept take 2.
- **b16 not-a-stranger (bookend) — reroll ATTEMPTED, REVERTED to take 1.** The
  bookend traveller is text-lock-only (`REFS={}`, no ref), so his face is not
  pinned across b02/b06/b16 (the row-179/142 text-lock-drift class). Take 1 is a
  clearly non-Jesus household man, rested, dark hair/short beard — a reasonable
  "same weary man now at home" match to the b02/b06 anchor (same age bracket,
  colouring, face type; b02↔b06 hold well). The blind `--redo` re-DRIFTED toward
  a longer-haired, fuller-bearded, downcast, pale-mantled figure = a **Jesus-double
  risk** on a `jesus:False` beat (the exact re-drift lesson 13 warns about), so
  reverted to take 1. Minor generic-consistency note only — NOT a Cameron-flag
  identity break (no ethnicity/beard-appears-disappears change); a perfect lock
  would need an author ref pin, not worth stranding the row.
- Everything else passed first take. Jesus b12/b13: cream-only, on-model (green/
  hazel ref eyes, calm gaze — NOT rerolled/edited), hand on the stone, ordinary-
  sized (SCALE GATE pass), no halo, not a literal stone. Witnesses b10/b13 generic
  & distinct (not the named Twelve, no clones). Father never depicted. Realistic
  only (Law 14) — no cartoon/mixed frame. Solid ropes/plumb lines (no ghost ropes).
  No modern tools/tread-prints/utility-wires. No second cream figure anywhere.

**AUDIO:** the V1 final mp4 (2026-07-24) PREDATES this row's narration mp3s
(2026-07-28), so the assembler's staleness guard refused to stream-copy it. Set
`AUDIO_FROM_V1_SEGMENTS = True` (tool-prescribed) → narration rebuilt from the V1
build's OWN 11 segment mp3s at extract_beats offsets; nothing re-voiced, nothing
re-timed, V1 read-only. `AUDIO REBUILD PASS` SHA256=ecf571129df242ea…, 131.006s.
Drop-check (row-173 lesson): `concat_base.txt` = 18 clips == 18 BEATS; last beat
NOT dropped; mp4 = 131.006s == audio. No open pronunciation complaint (board
Audio = OK), so the V1 narration is authoritative.

**FULL-CUT GATE:** extracted one frame per beat from the RENDERED mp4 + the card
and viewed EVERY one — all 18 pass, captions bottom-band only (white narration /
light-blue scripture), question card clean (no tofu), no letterbox on any frame.

**COST:** 20 frames (18 beats + 2 rerolls) × $0.134 ≈ **$2.68**, 0 portraits,
0 TTS. Well under the $6.10/row average; 11% rerolls under the 19% baseline.
Endpoint-recovery build, no overage.

## COMPLAINT LEDGER
- **No open Cameron complaint on this row** (`v2_outline.py 163` shows no prior
  review). First V2 authoring, not a complaint fix.

## THE STRUCTURE (why the beats are shaped this way)
Paul's own move — he "changed the picture from a family to a building" (n4).
So the film does the same:
- **Family half (b01-b06):** outsiders on the far edge → the door thrown open →
  the outsider drawn in → seated as family → "fellowcitizens, household of God."
- **Building half (b07-b15):** the picture becomes construction — foundation →
  apostles/prophets as the foundation → the cornerstone → **Christ at the
  cornerstone** → living people fitted in.
- **Bookend close (b16-b18):** the same weary outsider from b02/b06 now stands
  INSIDE the finished doorway; the last frame offers the open door to the viewer.

**BOOKEND FACE — build it deliberately.** One weary traveller's face is held at
**b02** (longing, outside) and **b06** ("no more strangers", now at rest), and
returns at **b16** (inside the finished doorway) and **b17** (belonging). It must
read as the SAME person across all four — face-board that one traveller like a
named character even though there is no global lock for them.

## NEW PLACES — promote from THIS build's first good frames (do FIRST)
The stash had no matching plate for any place token here, so each is carried by
prose in `LOCKS` for its first frame only, then promoted:

| Token | Generate this beat FIRST, QC it, then `--promote` it |
|---|---|
| HOUSEHOLD  | **b03** (door/threshold) or **b05** (family table) — the warm home |
| FAMILY     | **b05** (family at the lamplit table) |
| OUTSIDERS  | **b01** or **b02** (the travel-worn group / bookend face) |
| BUILD-SITE | **b07** (the establishing wide of the site) |
| BUILDERS   | **b08** (masons setting stone) |
| WITNESSES  | **b10** (apostles + prophets on the foundation) |

Promote syntax (positional `--promote BUILD TOKEN ASSET`):

    python3 media-production-v2/v2_stash.py --promote \
        build-163-apostles-prophets HOUSEHOLD s05-sons-and-daughters-at-home.jpeg

After promoting, re-run `v2_prompt.py build-163-apostles-prophets --check` (it
enforces the plate on disk) before generating the rest.

**OPTIONAL REUSE (lesson 11, runner's call):** the stash suggested
`FAMILY=build-41-counting-the-cost:v2-r041-b09` — a shipped, approved warm
lamplit family-supper frame that closely matches b05/b17. You MAY
`v2_stash.py --wire build-163-apostles-prophets --take FAMILY=build-41-counting-the-cost:v2-r041-b09`
to reuse those family faces instead of promoting b05 — BUT only if that room
coheres with the HOUSEHOLD door/threshold in b03/b04/b16/b18. If it clashes,
skip it and promote b05; internal consistency beats cross-build reuse here.

## HARD GATES FOR THIS ROW
1. **CHRIST AT THE CORNERSTONE (b12, b13)** is the locked V2 Jesus (LOCK v5 +
   REF, both beats jesus=True). Only he wears cream; ordinary-sized, NEVER
   enlarged (SCALE GATE); his hand ON the cornerstone; NO light around his head.
   He is NOT rendered as a literal stone.
2. **The Father is NOT in this passage — do not depict God at all.** No figure,
   no dove, no face in the sky, no light-outline. (Scene text avoids DRIFT words
   glow/halo/pale by design.)
3. **The WITNESSES (b10, b13)** are generic dignified apostles/prophets, distinct
   faces, NOT the named Twelve posed as a roster; no cloned faces.
4. **The bookend traveller** (b02/b06/b16) reads as one person — face-board it.
5. **Realistic only (Law 14):** first-century stonework, timber scaffolding,
   plumb line, oil lamps — no modern tools, no crane, no invented scripture props
   or theological symbols beyond the plain architecture the text names.
6. **Movie coverage:** only TWO wides (b01 family-edge, b07 build-site); groups
   stay SMALL; everything else is a single/two-shot/insert.

## AUDIO
`AUDIO_FROM_V1_SEGMENTS` NOT set (no re-voice needed; board Audio = OK).
Assemble with `v2_assemble.py 163` — it stream-copies the V1 encoded audio and
enforces the hash lock.

## COST
$0 this session (author lane — no Gemini, no ElevenLabs, 0 pictures generated).
Runner budget: 18 beats, reroll budget ≤15% = ~3 rerolls. Spend the plate-
promote care up front so the 6 places stay consistent and the other frames copy
good plates instead of re-inventing them.
