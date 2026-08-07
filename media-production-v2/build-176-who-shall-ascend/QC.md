# QC / RUNNER HANDOFF — build-176-who-shall-ascend (Psalm 24)

Authored 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0). `v2_prompt.py
--check` PASS (17 beats), windows contiguous+monotonic 0.400→65.068=card_start,
every segment onset in-window, audio OK. No open Cameron complaint.

## COMPLAINT LEDGER
- `v2_outline.py 176` shows NO open complaint on this row. Nothing to close;
  first V2 picture build on the SPEAKER-LAW-corrected narration (audio OK).

## The message (why-law: milk)
The gate of the house of the Lord opens on **clean hands and a pure heart** — not
bloodline, not rank, not a price paid. Purity does not purchase the blessing; it
only describes the person ready to receive what God gives. A humble worshipper
climbs, is found worthy to stand, and receives the blessing freely.

## SPEAKER LAW (do NOT flip)
Psalm 24 is David at the pen the whole way — a psalmist asking about the LORD and
answering himself; the LORD never opens his mouth in it. So **every scripture
beat (s1, s2, s3, s4, s5) is the SCRIPTURE voice → LIGHT-BLUE caption. NO
red-letter and NO God-voice anywhere.** (V1 wrongly painted s1/s2 Jesus-red; the
make_narration.py rebuild already moved them to blue — leave it.)

## HARD GATE — GOD / THE KING OF GLORY IS NEVER EMBODIED
This is the make-or-break of the row. "The King of glory shall come in" (b09),
"Who is this King of glory?" (b11), "The LORD strong and mighty, mighty in
battle" (b12), and "he is the one who comes in" (b13) are carried by the
**flung-wide everlasting doors, the radiant dawn light through the open gate, and
the awe on the worshippers' faces — NEVER a divine figure, face, hand, throne, or
a beam shaped like a being, and NEVER a halo/ring of light around a head or in
the gateway.** The open gate stays EMPTY of any figure on every one of those
beats. "Mighty in battle" (b12) = MAJESTY AND AWE only — **no army, soldier,
weapon, armour, battle or gore anywhere.** No Jesus and no cream in this row (OT
psalm, Deity not embodied). If any Jesus/King figure appears in the gate or the
light, the still fails.

## CONTENT-CARE
Ancient biblical architecture in the manner of the Jerusalem temple (dressed pale
stone, broad steps, tall plain columns, great timber-and-bronze everlasting
doors) — NEVER a modern building and NEVER a specific present-day temple. No
rendered writing anywhere (captions live in the bottom band only). One humble
WORSHIPPER we follow across b03/b05/b06/b07/b10/b13/b14/b15/b16/b17 — beard-board
him so his face and beard hold across every frame.

## PLACES — 3 NEW, promote before generating the rest (lesson 11)
| Place | Beats | Promote from |
|---|---|---|
| HILL-OF-THE-LORD | b01-b03, b05-b07, b10 | **b01** (establishing wide) |
| ANCIENT-GATES | b04, b08-b13 | **b04** (establishing wide) |
| TEMPLE-COURT | b14-b17 | **b14** (establishing wide) |
Generate b01, b04, b14 FIRST; QC each; `v2_stash.py --promote` it as that place's
plate; then generate the remaining beats of the place with the plate attached so
the architecture holds. None of the three is a Jesus frame (Jesus not in this
row), so all are safe to auto-wire once promoted.

## RUNNER — do this
1. Generate the 17 beats at native 2K (promote-first order above). No audio touch
   — `AUDIO_FROM_V1_SEGMENTS` is unset (default): v2_assemble stream-copies the
   authoritative V1 audio, which is current (segments OK).
2. Gates before assembly: GOD-never-embodied gate on b09/b11/b12/b13 (empty gate,
   no figure/beam/halo), no-violence gate on b12, face+beard board on the
   WORSHIPPER, scale gate, no-modern / no-writing sweep, realistic-only (Law 14).
3. `v2_assemble.py`, confirm AUDIO LOCK PASS + decode-clean, run the caption/color
   QC (all scripture light-blue, narrator white), then publish the candidate to
   the reviewer with a card noting there was no open complaint — fresh V2 build.
4. Reroll budget ≤15% of 17 beats (~2). Touch the row once.
