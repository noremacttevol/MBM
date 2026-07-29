# PICTURE REDO WORKLIST — apply the locked CAST-REF to every video that needs it

> Started 2026-07-22, Machine C. Cameron approved the locked cast (`CAST-REF/`, Jesus +
> the Twelve). The reference images are BRAND NEW, so no existing video uses them yet —
> every video that shows the disciples needs its disciple stills regenerated with the
> new REF images so Peter and the Twelve are the same faces everywhere.
>
> ## CORRECTED PIPELINE (2026-07-22) — captions must be Jost red-letter
> A rebuild is only to-spec if it ALSO uses the current caption law (`CAPTION-LAW.md`):
> **Jost Bold font, Jesus's KJV words RED, narration white, real edge-tts timing
> (`.timing.json` sidecars), adaptive bottom band.** Builds ≤~99 are mostly NOT migrated
> yet — migrate as part of the rebuild:
> 1. `cp ../mbm_caption_timing.py .` into the build.
> 2. `make_narration.py`: `from mbm_caption_timing import save_narration` + `await
>    save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")` (writes timing.json).
> 3. `build.py`: `from mbm_caption_timing import caption_filter`; in `build_still`,
>    `cap = caption_filter(seg_id, dur, spoken_end, cap_text, kjv)`; `fc = f"{base}{cap}{tail}[v]"`.
> 4. Regenerate narration, rebuild, `/gate`, QC the RED Jesus line.
> Builds ≥100 (and 04/05/06) are already Jost — rebuilding picks it up automatically.
> **Respect `approvals.json`** — approved rows (2,3,5,6,80,89,100-108,111,185-200) get
> redone but PRESENTED for re-approval, never silently overwritten.
> **REDO-STATUS of this session's 6:** #71 ✅ corrected (Jost+cast). #7,#51,#11,#90 need the
> Jost redo (cast stills already done, captions still old). #89 (approved) needs Jost redo + re-approval.
>
> **Method per video:** attach the relevant refs when regenerating each disciple still —
> `--ref CAST-REF/the-twelve.jpeg` for crowd/boat scenes, plus the solo ref(s) for any
> featured man (`CAST-REF/peter.jpeg`, `CAST-REF/john.jpeg`, …), and `--ref
> JESUS-MASTER-REF/jesus-face.jpeg` whenever Jesus shares the shot. Only regenerate the
> stills that actually contain a disciple; Jesus-only / scenery / other-character stills
> are left alone. Then rebuild the mp4 (build.py), full QC, present to Cameron.
>
> Priorities came from an automated disciple-prominence scan of every build's PROMPTS.md,
> then hand-pruned: **John-the-Baptist videos and KJV scripture-citations are NOT the
> disciples** and were removed.

## Progress key: ⬜ todo · 🔄 in progress · ✅ done+shown

---

## P1 — DISCIPLE-DEFINING SCENES (do these first — a viewer WILL notice a wrong Peter/face)
Named disciples or the whole Twelve are the visible subject.

| ✓ | # | Build | Who is featured |
|---|---|---|---|
| ✅ | 7   | build-07-peter-water            | Peter (lead), the Twelve, the boat — REBUILT 2026-07-22, awaiting Cameron's watch |
| ✅ | 51  | build-51-first-catch-of-fish    | Peter, James, John — REBUILT 2026-07-22, awaiting watch |
| ✅ | 11  | build-11-storm                  | the Twelve, the boat — REBUILT 2026-07-22, awaiting watch |
| ✅ | 89  | build-89-the-last-supper        | all Twelve at the table — REBUILT 2026-07-22, awaiting watch |
| ✅ | 90  | build-90-washing-feet           | Peter + the Twelve — REBUILT 2026-07-22, awaiting watch |

## P2 — THE TWELVE PRESENT AS A GROUP (do after P1)
The disciples are in-frame but not the whole subject; regenerate the group/crowd stills.

| ✓ | # | Build |
|---|---|---|

## VERIFY BEFORE TOUCHING (borderline — open the mp4/PROMPTS first)
153 restitution · 190 faith-without-works (Epistle of James?) · 108/134/141/142/143/144/146/159/168/172/173/174 (mostly John-citation verse cards — likely SKIP) · 62 ephphatha · 161 called-of-god.

## EXCLUDE — NOT a cast-redo (scan false positives)
- **John the Baptist, not disciple John:** 69 baptism · 107 john-baptist-doubt · 169 fulfil-righteousness.
- **KJV scripture-citation only** (the closing verse card cites "Matthew"/"John" the book): the ~40 Tier-2 rows scoring 3 on a single citation and nothing else — no disciple is depicted. Skip unless a spot-check shows disciples in the art.

## NOTES
- One video per chat keeps context low (standing rule). This worklist is the shared queue
  so any machine can pull the next ⬜ P1 row, mark it 🔄, and go.
- Credits: disciple stills regenerate on Nano Banana 2 (0 credits) with the refs attached.
