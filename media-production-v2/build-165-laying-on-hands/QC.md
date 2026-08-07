# QC / RUNNER HANDOFF — build-165-laying-on-hands (Acts 8:14-17)

**AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).**
`beats_v2.py` written from scratch: 25 pictures over 119.61 s (~4.8 s/pic;
lesson-12 movie coverage). `v2_prompt.py --check` PASS. Windows contiguous +
monotonic, first 0.280, last end 119.606 = card seg_start; every segment onset
inside its first beat's window. PETER/JOHN global cast locks resolve in the dump.
Audio column OK on AUTHOR-BOARD. Ready ✅.

## COMPLAINT LEDGER
- **No open Cameron complaint on this row** (`v2_outline.py 165` shows no prior
  review). First V2 authoring, not a complaint fix.

## SPEAKER LAW — no Jesus red-letter, and NO Jesus in this row at all
This is Luke narrating Acts — no red-letter line in the passage. kv14, s15, s16,
kv17 are ALL the **SCRIPTURE voice / light-blue caption**, on the apostles and
believers. Jesus is only NAMED ("baptized in the name of the Lord Jesus", s16)
and is NOT present in the Acts 8 scene — so **every beat is jesus=False,
ref=False** and **nobody wears cream anywhere**.

## HARD GATE #1 — THE HOLY GHOST IS NEVER EMBODIED
Where the gift is received (**b18, b19, b21, b24**) it is **warm light coming
down from above the top of the frame** onto the believers' upturned faces, and
their faces filled with joy — **NEVER a dove, NEVER tongues of flame (that is
Pentecost, a different event — do not import it), NEVER a figure, NEVER a ring
of light around a head.** DRIFT_WORDS glow/halo/rim-light are banned; the scene
text avoids them. Beats b10/b11 deliberately show the air EMPTY ("fallen upon
none of them yet") — nothing may descend in those two.

## THE TWO NEW PLACES — promote from a first good frame (lesson 11)
No beat bears Jesus, so any frame is safe to promote.
1. **SAMARIA-HILL** (the Samaritan hill town — b01, b02, b08, b12, b22). Promote
   the clean **b01** (`s01-samaria-believes.jpeg`) once it passes QC, or the
   calmer **b22** if b01's crowd is busy:

       python3 media-production-v2/v2_stash.py --promote \
           build-165-laying-on-hands SAMARIA-HILL s01-samaria-believes.jpeg

2. **JERUSALEM-ROOM** (the apostles' council upper room — b04, b06, b07).
   Promote **b04** (`s04-not-a-letter.jpeg`):

       python3 media-production-v2/v2_stash.py --promote \
           build-165-laying-on-hands JERUSALEM-ROOM s04-not-a-letter.jpeg

Generate b01/b04 early, QC, `--promote` both, re-run `--check` (it now enforces
the plates on disk), then generate the rest. `--promote BUILD TOKEN ASSET` is
positional.

## COVERAGE MAP (seg → beats)
- n1  → b01 (WIDE establish — Samaria believes) + b02 (baptized in water) + b03 (joy among them)
- n2  → b04 (not just a letter — council) + b05 (Peter & John set out)
- kv14 → b06 (apostles heard) + b07 (they sent Peter & John) — SCRIPTURE
- s15  → b08 (Peter & John come down and PRAY — nothing descends yet) — SCRIPTURE
- n3  → b09 (already believed & baptized) + b10 (gift not yet come — AIR EMPTY)
- s16  → b11 (fallen upon none — AIR EMPTY) + b12 (only baptized in the name of the Lord Jesus) — SCRIPTURE
- n4  → b13 (water alone not enough) + b14 (faith sincere, still waiting) + b15 (waited on the hands of authority — Peter/John's hands)
- n5  → b16 (the deliberate act begins) + b17 (hands laid on a head) + b18 (the gift CAME — light from above)
- kv17 → b19 (the whole verse: hands laid, Holy Ghost received — light from above) — SCRIPTURE
- n6  → b20 (study gem, scroll+lamp) + b21 (travelled by authority — laying on of hands) + b22 (order & gift belong together)
- n7  → b23 (offered to you) + b24 (Comforter given by hands of authority — light from above) + b25 (will you receive it? — open)

## OTHER HARD GATES
2. **PETER + JOHN face/beard board (lesson 13 — Peter is a repeat offender).**
   They appear in b05, b07, b08, b15(hands), b16, b17, b18, b19, b21, b22. Peter's
   iron-grey-streaked beard and John's CLEAN-SHAVEN younger face (per the global
   cast lock) must read as one actor each across all of them. Board + beard-board
   before assembly; b07 or b22 is a clean full-face candidate.
3. **DECEIVERS do not appear** in this row — the only non-cast people are the
   Samaritan BELIEVERS (distinct, glad, varied) and the Jerusalem APOSTLES
   council (distinct, dignified). Keep both varied, never twinned.
4. **The baptizer has no locked face** (b02, b12) — shoot the baptism on the
   WATER and the BELIEVER; the baptizer is hands/back only, so nothing to board.
5. **Realistic only (Law 14):** biblical photography, no cartoon/mixed styles; no
   legible modern text on the scroll (b20); natural stone water-channel, no
   modern font/pool (b02/b12); no modern objects in the Jerusalem room.
6. **Movie coverage (lesson 12):** b01 is the ONLY wide; every other beat is a
   single, two-shot or insert with a SMALL group.

## AUDIO
`AUDIO_FROM_V1_SEGMENTS` NOT set (no re-voice; board Audio column OK). Assemble
with `v2_assemble.py 165` — stream-copies the V1 encoded audio, hash-locked.

## COST
$0 this session (author lane — no Gemini, no ElevenLabs, 0 pictures generated).
Runner budget: 25 beats, reroll budget ≤15% = ~3-4 rerolls. Riskiest frames:
b01/b04 (the two NEW places — spend the plate-promote care there); b18/b19/b24
(the gift-coming light must stay a plain shaft from above, never a dove/flame).
Batch every known fix into ONE re-cut (COST/touch-once law).
