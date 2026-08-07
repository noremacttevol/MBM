# QC / RUNNER HANDOFF — build-163-apostles-prophets (Ephesians 2:19-20)

**AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).**
`beats_v2.py` written from scratch: 18 pictures over 116.71 s (6.5 s/pic).
`v2_prompt.py --check` PASS. Windows contiguous + monotonic (0.280 →
116.714 = card seg_start). Audio OK on AUTHOR-BOARD. Ready ✅.

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
