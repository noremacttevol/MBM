# QC / RUNNER HANDOFF — build-177-make-me-a-sanctuary (Exodus 25:8, 25:22)

Authored 2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0). `v2_prompt.py
--check` PASS (19 beats), windows contiguous+monotonic 0.400→90.003=card_start,
every segment onset in-window, audio OK.

## COMPLAINT LEDGER
- **OPEN — "Not real new voice."** REDO-ALL voice-identity complaint: the cut was
  shipped/reviewed on the OLD voice. **FIXED, with certainty:** all 13 segment
  mp3s in `audio/` are ElevenLabs 44100 Hz/128 k (narrator Brian, GOD Bill) —
  ffprobe-confirmed — and `beats_v2.py` sets **`AUDIO_FROM_V1_SEGMENTS = True`**,
  so v2_assemble rebuilds the shipped track FROM those new-voice segments at the
  extract_beats offsets rather than stream-copying any older stream. The V2 cut
  therefore carries the real new cast. **The review card MUST say, in plain words,
  that the voice is the real new voice now** so Cameron can verify in one listen.

## The message (why-law: milk)
God did not ask for a distant palace — He asked for a **tent in the middle of the
camp** so He could dwell among His people in their ordinary days. "Not for his
sake. For theirs." The whole exact pattern — the ark, the mercy seat, the two
carved cherubim — was God giving them an ADDRESS: *right there* is where I will
meet you. It ends by pointing forward: centuries later that promise would take a
face (spoken only — Jesus is NOT shown).

## SPEAKER LAW (do NOT flip)
- **s1 (Ex 25:8)** and **g22 (Ex 25:22)** are the **GOD voice → GREEN captions**
  (Bill). All other segments are the NARRATOR (white). No Jesus red-letter and no
  Jesus anywhere (OT, centuries before the Incarnation).

## HARD GATE — GOD IS NEVER EMBODIED
On b03 (s1), b08/b09 (g22) and the meeting-place beats b11/b12, God speaks and
dwells but is **NEVER shown** — no figure, face, hand, body, throne, or
beam-shaped-being, and no halo/ring of light around anything. His presence is the
biblical **cloud over the tent** (Ex 40:34) — a soft, FORMLESS cloud with no
shape or face — and the meeting place above the mercy seat "between the cherubims"
is the **empty charged space**, carrying at most faint soft light, never a figure.

## CONTENT-CARE gates for the runner
- **Cherubim = carved solid-gold STATUES** on the mercy-seat lid (Ex 25:18-20),
  wings arched toward each other — part of THE-ARK object, NEVER living, flying,
  or mistaken for God. Any living/animate angel fails the still.
- **The sanctuary is the wilderness TABERNACLE** — a plain goats'-hair TENT in the
  middle of the camp — NEVER a stone palace or a permanent temple.
- **b18 ("would take a face"):** show only the tent at dawn. **NO Jesus, NO face
  of God/Christ** — the "face" is spoken foreshadow only.
- Ancient Near-Eastern materials only; no modern object; no rendered writing;
  realistic-only (Law 14). Beard/face-board MOSES across b02/b04/b07.

## PLACES — 3 NEW, promote before generating the rest (lesson 11)
| Place | Beats | Promote from |
|---|---|---|
| WILDERNESS-CAMP | b01, b03-b06, b13-b19 | **b01** (establishing wide) |
| SINAI-MOUNT | b02 | **b02** |
| TABERNACLE-HOLY | b07-b12 | **b07** (establishing wide) |
Generate b01, b02, b07 FIRST; QC each; `v2_stash.py --promote` it as that place's
plate; then generate the remaining beats with the plate attached. None is a Jesus
frame (Jesus not in this row), so all are safe to auto-wire once promoted.

## RUNNER — do this
1. Generate the 19 beats at native 2K (promote-first order above).
2. Audio: `AUDIO_FROM_V1_SEGMENTS = True` — v2_assemble rebuilds from the 13
   new-voice segment mp3s; confirm **AUDIO REBUILD PASS** and decode-clean.
3. Gates before/after assembly: GOD-never-embodied gate on b03/b08/b09/b11/b12
   (no figure/face/beam in cloud or above the mercy seat), cherubim-are-statues
   gate, no-Jesus gate on b18, MOSES face/beard board, scale gate, no-modern /
   no-writing sweep, realistic-only.
4. Caption QC: s1 + g22 captions GREEN, all narrator white; bottom band only.
5. Publish the candidate to the reviewer with a card telling Cameron the voice is
   the real new voice now (closes his open complaint). Reroll budget ≤15% of 19
   (~3). Touch the row once.
