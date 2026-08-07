# QC / RUNNER HANDOFF — build-166-baptized-properly (Acts 19:1-6)

**AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).**
`beats_v2.py` written from scratch: 24 pictures over 121.22 s (~5.0 s/pic;
lesson-12 movie coverage). `v2_prompt.py --check` PASS. Windows contiguous +
monotonic, first 0.280, last end 121.218 = card seg_start; every segment onset
inside its first beat's window. PAUL build-local lock attaches to all 12 Paul
beats. Audio column OK on AUTHOR-BOARD. Ready ✅. (Direct companion to row 165.)

## COMPLAINT LEDGER
- **No open Cameron complaint on this row** (`v2_outline.py 166` shows no prior
  review). First V2 authoring, not a complaint fix.

## SPEAKER LAW — no Jesus red-letter, and NO Jesus in this row at all
Luke narrating Acts — no red-letter line. s2, s4, kv5, kv6 are ALL the
**SCRIPTURE voice / light-blue caption**; s2/s4 are PAUL's quoted words (still
scripture voice in Acts, NOT Jesus red). Jesus is only NAMED ("Christ Jesus" /
"the Lord Jesus") and is NOT present — so **every beat is jesus=False, ref=False**
and **nobody wears cream anywhere**.

## HARD GATE #1 — THE HOLY GHOST IS NEVER EMBODIED, AND THE TONGUES ARE NOT FLAMES
Where the gift comes (**b17, b23**) it is **warm light down from above the top of
the frame** onto the men's faces. "**They spake with tongues, and prophesied**"
(**b18**) is the MEN'S OWN response — mouths open in praise, a hand lifted in
prophecy, faces alight — **NOT tongues of FLAME** (that is Pentecost — do not
import fire, a dove, or any figure; nothing burns or hovers over a head).
DRIFT_WORDS glow/halo/rim-light are banned; scene text avoids them. Beats
b12/b15 deliberately keep the air EMPTY (baptism done, gift not yet come) —
nothing may descend in those.

## PAUL — reuse the canonical face (cross-video law, lesson 2)
PAUL is NOT in the global cast (only the Twelve are), so his lock is written
build-local — **byte-identical to builds 138 and 155** (compact, wiry, ~50,
balding with a dark fringe, full pointed dark beard, keen deep-set eyes, plain
DARK RUST-BROWN robe — never cream/white). Board Paul's face + beard across all
12 of his beats (b01, b04, b06, b07, b08, b09, b11, b13, b16, b17, b20, b21) so
he reads as the SAME man here and library-wide. b06 or b13 is a clean full-face
candidate anchor.

## THE ONE NEW PLACE — promote from a first good frame (lesson 11)
**EPHESUS-ROOM** (the meeting room — b01, b06, b21). No beat bears Jesus, so any
frame is safe to promote. Promote **b01** (`s01-paul-at-ephesus.jpeg`), or the
calmer **b06** if b01's group is busy:

    python3 media-production-v2/v2_stash.py --promote \
        build-166-baptized-properly EPHESUS-ROOM s01-paul-at-ephesus.jpeg

Generate b01 early, QC it, `--promote`, re-run `--check` (it now enforces the
plate on disk), then generate the rest. `--promote BUILD TOKEN ASSET` is
positional. (The baptism beats b14/b22 are outdoors at the water — no room plate;
shoot on natural stone + the believer, baptizer hands/back only, no locked face.)

## COVERAGE MAP (seg → beats)
- n1  → b01 (WIDE establish — Paul at Ephesus) + b02 (sincere, believed) + b03 (fully in)
- s2  → b04 (Paul: received the Holy Ghost since ye believed?) + b05 (never so much as heard) — SCRIPTURE (Paul's words)
- n2  → b06 (Paul reads the startling answer)
- s4  → b07 (John's baptism of repentance) + b08 (believe on the one to come — Christ Jesus, NOT shown) — SCRIPTURE
- n3  → b09 (what baptism? — only John's) + b10 (a preparation pointing forward — no figure in the light)
- n4  → b11 (good people, something missing) + b12 (not the full ordinance — air empty) + b13 (Paul set it right)
- kv5 → b14 (baptized in the name of the Lord Jesus — the water) — SCRIPTURE
- n5  → b15 (baptism not the final step — air empty) + b16 (one thing more — laying on of hands begun)
- kv6 → b17 (Paul lays hands, Holy Ghost came — light from above) + b18 (tongues & prophesied — the MEN speaking, NOT flames) — SCRIPTURE
- n6  → b19 (study gem, scroll+lamp) + b20 (done right, by one sent) + b21 (sincerity completed by authority)
- n7  → b22 (same pattern — real baptism by authority) + b23 (gift by laying on of hands — light from above) + b24 (will you follow it in? — open)

## OTHER HARD GATES
2. **EPHESIAN-DISCIPLES variety board (lessons 2/3/13):** a SMALL band (~12 men)
   of distinct real faces — never twinned, never a cloned face; beards consistent
   per person across frames.
3. **Realistic only (Law 14):** biblical photography, no cartoon/mixed styles; no
   legible modern text on the scroll (b19); natural stone water, no modern
   font/pool (b14); no pagan idol niche in the Ephesus room.
4. **Movie coverage (lesson 12):** b01 is the ONLY wide; every other beat a
   single, two-shot or insert with a SMALL band.

## AUDIO
`AUDIO_FROM_V1_SEGMENTS` NOT set (no re-voice; board Audio column OK). Assemble
with `v2_assemble.py 166` — stream-copies the V1 encoded audio, hash-locked.

## COST
$0 this session (author lane — no Gemini, no ElevenLabs, 0 pictures generated).
Runner budget: 24 beats, reroll budget ≤15% = ~3-4 rerolls. Riskiest: b01 (NEW
place + establishing wide), b18 (tongues must be the men's speech, never flame),
Paul's face across 12 beats. Batch every known fix into ONE re-cut (COST/
touch-once law).
