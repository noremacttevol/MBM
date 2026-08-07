# QC / RUNNER HANDOFF — build-164-unity-of-faith (Ephesians 4:11-14)

**AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).**
`beats_v2.py` written from scratch: 25 pictures over 124.39 s (~5.0 s/pic,
matches rows 161-163 library density; lesson-12 movie coverage). `v2_prompt.py
--check` PASS. Windows contiguous + monotonic, first 0.280, last end 124.389 =
card seg_start; every segment onset falls inside its first beat's window. Audio
column OK on AUTHOR-BOARD. Ready ✅.

## COMPLAINT LEDGER
- **No open Cameron complaint on this row** (`v2_outline.py 164` shows no prior
  review). First V2 authoring, not a complaint fix — nothing to answer on the
  review card beyond the standard realistic-V2 wave note.

## SPEAKER LAW — no Jesus red-letter in this row
Ephesians is Paul's epistle; a red-letter KJV prints NO red in ch. 4. All three
scripture beats — kv11 (b04/b05), kv13 (b13/b14), s14 (b15/b16) — are the
**SCRIPTURE voice / light-blue caption**, sitting on the people and leaders the
verse describes, NEVER on Jesus's face. kv11's subject is Christ ("he gave") but
Paul says it and it is *about* Christ, not *from* him (same call as build-163).
Jesus's face appears ONLY in b01, b02, b03 (giving the gifts) and b25 (the
closing invitation) — the narrator segments, not the scripture ones.

## THE TWO NEW PLACES — promote from NON-Jesus frames (lesson 11), do NOT promote a Jesus frame
Both recurring places are NEW; the stash has no match, so they are carried by
prose in `LOCKS` for their first frame only. **b01 and b25 are Jesus-bearing —
never promote either as a plate.**

1. **GATHERING-HILL** (the hillside above a first-century town — beats b01, b09,
   b13, b23, b24, b25). Promote the clean NON-Jesus **b13**
   (`s13-unity-of-the-faith.jpeg`) once it passes QC (a real grassy hill above a
   modest town, terraces + olives, a SMALL band, dawn):

       python3 media-production-v2/v2_stash.py --promote \
           build-164-unity-of-faith GATHERING-HILL s13-unity-of-the-faith.jpeg

   Then it auto-attaches to b09, b23, b24 (and b01/b25, which also carry their
   own Jesus lock over the same place text).

2. **JOURNEY-ROAD** (the dirt road toward the far high town — beats b10, b21).
   Promote **b10** (`s10-destination-in-view.jpeg`) once it passes QC:

       python3 media-production-v2/v2_stash.py --promote \
           build-164-unity-of-faith JOURNEY-ROAD s10-destination-in-view.jpeg

**Order for the runner:** generate b10 and b13 early, QC them, `--promote` both,
then re-run `v2_prompt.py build-164-unity-of-faith --check` (it now enforces the
plates are on disk) before spending the rest of the credits, then generate the
remaining stills. `--promote BUILD TOKEN ASSET` is positional; ASSET is the
approved still filename.

## COVERAGE MAP (seg → beats)
- n1  → b01 (WIDE establish, the ONLY wide — risen Lord + small band) + b02 (Jesus pours out gifts, light from above) + b03 (Jesus commissions a minister)
- kv11 → b04 (apostles + prophets) + b05 (evangelists, pastors & teachers at work) — SCRIPTURE, no Jesus
- n2  → b06 (minister mends/matures a believer) + b07 (the body built up strong)
- n3  → b08 (the scattered-crowd contrast) + b09 (knit together, bearing one another up)
- n4  → b10 (the road / destination in view) + b11 (one shared faith, faces to the far light) + b12 (a believer grown to full maturity)
- kv13 → b13 (the gathered church = unity of the faith) + b14 (a perfect man, full stature) — SCRIPTURE, no Jesus
- s14  → b15 (child tossed to and fro in the wind of doctrine) + b16 (deceivers lie in wait) — SCRIPTURE, no Jesus
- n5  → b17 (the leaderless gap — without steady leading) + b18 (believers pulled every different way) + b19 (a deceiver takes a lone believer)
- n6  → b20 (study gem — scroll under a lamp, insert) + b21 (still on the road, town not yet reached) + b22 (a minister keeps a wanderer from drifting)
- n7  → b23 (a single believer apart — the viewer) + b24 (drawn in, grow up together) + b25 (**Jesus** offers an open hand — will you come and grow?)

## HARD GATES FOR THIS ROW (what a reviewer will catch)
1. **THE SON-OF-GOD / HEAVEN IS NEVER EMBODIED for measure or comparison.** At
   "from above"/"returned to heaven" (b01/b02) and at "knowledge of the Son of
   God" / "stature of the fulness of Christ" (b11, b13, b14) there is **no figure
   in the sky and no second giant Christ set up beside a man** — heaven/the goal
   is warm dawn light at the frame edge, and the fullness is read in the grown
   believer himself. DRIFT_WORDS glow/halo/rim-light are banned and the scene
   text avoids them; nothing rings anyone's head.
2. **SCALE GATE (lesson 14):** Jesus is an ordinary-sized man in every frame he
   is in (b01, b02, b03, b25) — never enlarged for emphasis. All believers within
   natural human variation of each other; nobody a giant.
3. **DECEIVERS ≠ MINISTERS (identity + costume board).** The clever men (b16,
   b19) must read as distinctly FINER-dressed and smoother than the plain true
   leaders (b03, b04, b05, b06, b22) — dark wine/grey/umber richer robes vs
   plain earth-toned wool — and never cartoonish, horned, or monstrous. Board
   the two groups so a viewer never confuses a false teacher for a true one.
4. **BELIEVERS face/variety board (lessons 2/3/10/13):** the church band recurs
   in most beats; keep them distinct real people (men and women, varied ages),
   never twinned or a cloned face, beards consistent per person across frames.
5. **Only Jesus wears cream (b01/b02/b03/b25).** No minister, believer or
   deceiver in cream anywhere.
6. **Realistic only (Law 14):** biblical photography, no cartoon and no mixed
   styles; no legible modern text on the scroll (b05/b20), no invented symbols in
   the wind beats (b15/b18), no modern road/buildings on JOURNEY-ROAD.
7. **Movie coverage (lesson 12):** b01 is the ONLY wide; every other beat is a
   single, two-shot or insert with a SMALL band, never the whole congregation.

## AUDIO
`AUDIO_FROM_V1_SEGMENTS` is NOT set (no re-voice needed; board Audio column OK).
Assemble with `v2_assemble.py 164` — it stream-copies the V1 encoded audio and
enforces the hash lock. If the lock ever fails here, that is an audio-lane
matter, not a picture edit.

## COST
$0 this session (author lane — no Gemini, no ElevenLabs, 0 pictures generated).
Runner budget: 25 beats, reroll budget ≤15% = ~3-4 rerolls. Riskiest frames:
b13/b10 (the two NEW places — spend the plate-promote care there so the rest
copy a good hill/road and do not each re-invent it), and b16/b19 (deceivers must
stay visibly distinct from the true ministers). Batch every known fix into ONE
re-cut per the COST/touch-once law.
