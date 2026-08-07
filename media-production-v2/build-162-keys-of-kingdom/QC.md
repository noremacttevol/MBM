# QC / RUNNER HANDOFF — build-162-keys-of-kingdom (Matthew 16:13-19)

**AUTHORED 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).**
`beats_v2.py` written from scratch: 24 pictures over 144.78 s (6.0 s/pic,
matches row 161's library density). `v2_prompt.py --check` PASS. Windows
contiguous + monotonic, first 0.280, last end 144.784 = card seg_start.
Audio column OK on AUTHOR-BOARD. Ready ✅.

## COMPLAINT LEDGER
- **No open Cameron complaint on this row** (`v2_outline.py 162` shows no prior
  review). This is a first V2 authoring, not a complaint fix. Nothing to answer
  on the review card beyond the standard realistic-V2 wave note.

## THE ONE THING THE RUNNER MUST DO FIRST — promote the NEW place plate
`CAESAREA-ROCK` is a **NEW location** (the great rock cliff of Caesarea Philippi
below Mount Hermon — cave-mouth + cold spring at its foot). The stash has no
matching plate (`v2_stash.py --wire` found nothing to wire), so the place is
carried by prose in `LOCKS["CAESAREA-ROCK"]` for the first frame only.

**Generate b01 (`s01-at-caesarea-philippi.jpeg`) FIRST.** When it passes QC
(a real towering pale limestone cliff, dark cave-mouth + spring at the base,
Hermon behind, a SMALL band — not the whole Twelve — Jesus ordinary-sized), then:

    python3 media-production-v2/v2_stash.py --promote \
        build-162-keys-of-kingdom CAESAREA-ROCK s01-at-caesarea-philippi.jpeg

(`--promote BUILD TOKEN ASSET`, positional — ASSET is b01's approved still.)
That writes the plate + PLACE-WIRING.json so it attaches to every other
CAESAREA-ROCK beat (b04, b06, b08, b09, b10, b11, b12, b13, b14, b15, b17, b18,
b22, b23) and the cliff stays the SAME rock across all 24 frames. Only after the
plate is promoted, generate the remaining 23 stills. Then re-run
`v2_prompt.py build-162-keys-of-kingdom --check` (it now enforces the plate is on
disk) before spending the rest of the credits.

## COVERAGE MAP (seg → beats)
- n1  → b01 (WIDE establish, the ONLY wide) + b02 ("Who do you say I am?", Jesus single)
- jv15 → b03 (Jesus red-letter "But whom say ye that I am?")
- s16  → b04 (**PETER's confession — on PETER, NOT Jesus**; row-39 speaker law)
- n2  → b05 (Peter answered for all) + b06 (Jesus: Father revealed it — light from above, NOT embodied)
- n3  → b07 (Peter's expectant face) + b08 (Jesus names him Peter, hand on shoulder, rock behind)
- kv18 → b09 (Jesus "upon this rock I will build my church") + b10 (the cliff + cave = gates of hell not prevail)
- n4  → b11 (Jesus + small gathered church on the rock) + b12 (rock unmoved under gathering storm)
- n5  → b13 (storm at full weight on the cliff) + b14 (storm breaks, dawn on the foundation)
- n6  → b15 (Jesus turns back to Peter) + b16 (specific promise, close two-shot) + b17 ("He called it keys" — two iron keys extended)
- kv19 → b18 (Jesus gives the keys, red-letter) + b19 (**Peter holds the keys — cut to receiver, NOT Jesus**; bind/loose)
- n7  → b20 (iron key turning a wooden door-lock, insert) + b21 (Peter carries authority) + b22 (eyes up, honoured from heaven — light from above, NOT embodied)
- n8  → b23 (closing two-shot: church on rock, keys in Peter's hands) + b24 (the two keys on an OPEN palm toward the viewer — the hopeful question)

## HARD GATES FOR THIS ROW (what a reviewer will catch)
1. **PETER beard/face board (lesson 13 — Peter is a repeat offender).** Peter is
   in b04, b05, b07, b08, b09, b11(?), b15, b16, b17, b18, b19, b21, b22, b23.
   His iron-grey-streaked dark beard and sun-browned face must read as ONE actor
   in every one. Face-board + beard-board him before assembly; identity-edit any
   drift against one anchor (b08 or b18 is a clean full-face candidate).
2. **The KEYS are ONE object: exactly TWO large ancient iron ward-keys**, the
   same in b17, b18, b19, b21, b22, b23, b24. Never one key, never three, never
   modern keys. Board them like a face.
3. **THE FATHER / HEAVEN IS NEVER EMBODIED** (b06, b22): warm light from above
   the top of the frame only — no figure, no face in the sky, no dove, no outline
   of light around anyone's head (DRIFT_WORDS "glow/halo" are banned and the
   scene text avoids them).
4. **SCALE GATE (lesson 14):** Jesus is an ordinary-sized man in every multi-
   figure frame (b01, b06, b08, b09, b11, b15, b16, b23) — never enlarged.
5. **Speaker law:** s16 (b04) is Peter's confession on Peter's face; b19 cuts to
   Peter receiving the keys. The captions stay coloured by segment speaker; the
   pictures illustrate.
6. **Realistic only (Law 14):** biblical photography, no cartoon, no pagan idol
   niches carved in the cliff, no invented scripture props.

## AUDIO
`AUDIO_FROM_V1_SEGMENTS` is NOT set (no re-voice was needed; the V1 mp4 audio is
canonical and the board Audio column is OK). Assemble with `v2_assemble.py 162`
— it stream-copies the V1 encoded audio and enforces the hash lock. If the lock
ever fails on this row, that is an audio-lane matter, not a picture edit.

## COST
$0 this session (author lane — no Gemini, no ElevenLabs, 0 pictures generated).
Runner budget: 24 beats, reroll budget ≤15% = ~3 rerolls. b01 is the single
riskiest frame (NEW cliff place + establishing wide); spend the plate-promote
care there so the other 23 copy a good rock and do not each re-invent it.
