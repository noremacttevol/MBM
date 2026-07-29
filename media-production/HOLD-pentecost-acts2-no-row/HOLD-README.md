# PARKED — Pentecost (Acts 2). NOTHING DELETED.

**Why this is here (2026-07-25):** Row 44 in QUEUE.md = **"The two debtors" (Luke 7),
APPROVED 2026-07-17**. The complete, canonical build lives in
`../build-44-two-debtors/`.

This directory (`build-44-pentecost`, renamed to `HOLD-pentecost-acts2-no-row`) was
mislabeled as row 44. It is:
- **Incomplete** — no `build.py`, cannot render.
- A **genuinely distinct video** — Acts 2 Pentecost (rushing wind, tongues of fire,
  Peter's sermon, 3,000 baptized). It is **NOT** a duplicate of row 197
  ("Your sons and your daughters shall prophesy," Joel 2) — verified by comparing the
  two transcripts. Row 197 quotes Joel; this quotes Acts 2.
- **Homeless** — there is no Pentecost / Acts 2 row anywhere in QUEUE.md.

Because it's a real distinct story with no queue row, it was **parked, not deleted**,
so `redo_loop.sh` stops picking it (its `dirof()` globs `build-44-*` and its
`transcript_of()` greps `"row": 44`). The transcript was moved to
`../TRANSCRIPTS/HOLD-pentecost-acts2.json` with `"row": null`.

## Decision for Cameron
Pentecost (Acts 2) needs an intent call — it's not on the 200 list:
1. **Give it a real QUEUE row** (its own number) and finish the build, OR
2. **Fold it into row 197** as the same message, OR
3. **Drop it.**

Until you decide, everything is preserved here and fully reversible.
