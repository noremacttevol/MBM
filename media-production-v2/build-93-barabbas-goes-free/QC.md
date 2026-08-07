# QC / RUNNER HANDOFF — build-93-barabbas-goes-free (Matthew 27:15-26)

## ✅ REALISTIC-V2 BUILT + SHIPPED (2026-08-07, Opus picture runner, Machine A `Dev`, UNATTENDED/HEADLESS)

15 realistic stills, 90.3s, AUDIO REBUILD PASS SHA256=`6df005ef9a84e97bfc8171fefc968899f0808abfe3de3f2fb33f3e14825b191a`.
mp4 = `mark-15_barabbas-goes-free.mp4` (19.8 MB). QUEUE row 93 cross-checked = "Barabbas
goes free / Mark 15" — NOT swapped. `--check` PASS (15 beats). 2 portraits (PILATE +
BARABBAS, $0.27); PAVEMENT promoted from b01 anchor → 10 beats; PRIESTS group-ref reused
from build-06. Meter $476.91→$480.12.

### COMPLAINT LEDGER (LEARNING LAW)
- **No open complaint on this row** (`v2_outline.py 93` shows no OPEN reviewer lesson).
  COMPLAINT LEDGER: none open. Audio safety verified anyway (row was audio-fixed
  2026-08-06): AUDIO_FROM_V1_SEGMENTS=True, V1-dir segments 44100/128k = ElevenLabs
  new-voice (old edge-tts was 24000); AUDIO REBUILD PASS SHA proves the shipped audio.

### Light QC (all 15 frames viewed once against beats + RUNNER-LESSONS)
- Only Jesus wears cream in EVERY frame he appears (s02, s04, s11, s12, s15); Jesus
  face-locked, bound with rope, never beaten/bloodied (content-care held — the abuse is
  off-screen). No second cream, no Jesus double on any jesus:False frame.
- PILATE consistent every shot (Roman, grey short hair, deep-red cloak over bronze
  cuirass); BARABBAS consistent (ragged brown, scarred brow, shackle-marked wrists) across
  s02/s12/s13/s14/s15. PRIESTS present as distinct older dark-robed men (s06/s08/s15).
- The substitution thesis reads at a glance: s12 Barabbas unchained/freed while bound
  cream Jesus is led away by guards; s15 the two men in one frame, opposite directions.
- Mob beats (s08/s10) are shouting fists — intense but NO gore/violence; crowd otherwise
  composed. Chief priests visibly working the crowd in s06 (correct action-logic).
- PAVEMENT plate QC'd first/hardest (empty judgment seat, period columns, Roman guards
  with spears, no modern object) — propagated clean to all 10 PAVEMENT beats.
- **1 reroll = 6.7% (well under the ≤15% COST-LAW budget):** s13 first take was a
  Barabbas lens-stare → `--redo` re-anchored his gaze DOWN to his freed hands. No other reroll.

### Cost
Row 93 = **~$2.41 / 6.7% rerolls** ($0.27 two portraits + $0.13 anchor + $1.88 fourteen
beats + $0.13 one reroll) — WELL under the $6.10/row + 19%-reroll running average
(COST-LAW trend-down satisfied; plate + group-ref reuse). Meter $480.12.

---

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 93`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 14 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 15 beats, ~84 s.

## Coverage shape

Five true wides with stated geometry: b01 (the yard filling, behind
the crowd), b02 (the two presented — both figures in one profile: the
row's thesis pair), b08 (the roar, behind the lifted arms), b12 (the
swap — chains struck off one man as the other is led away, both
motions crossing in profile), b15 (the diverging figures small, from
high behind the emptying yard). Six flips.

## PRIESTS group ref (a documented exception to the no-people-plate rule)

PRIESTS wired (manual --take) to build-06's four-chief-priests frame.
Unlike a crowd plate (which wrongly clones ONE crowd everywhere), the
chief priests are a NAMED RECURRING GROUP — the same four men across
the library is the identity goal, exactly like the temple sharing.
Face-board this row's priests against that frame.

## The two men (the row's identity engine)

- JESUS: bound with rope, silent, upright — cream robe (only he),
  bruised-dignified per content-care: marks of the night's handling
  at most, NO gore (the scourging is never depicted).
- BARABBAS: per his lock — hardened, chained, disbelieving; his arc
  (presented → freed → walking away looking back) is the gospel as
  swap. In b02/b12/b15 the TWO must be instantly distinguishable at
  any size.
- PILATE: authority eroding by stages (offer → stunned → capitulation
  — the turning-away posture, never a literal hand-washing unless
  narrated).

## Other checks

- The crowd's roar is fists and open mouths — fervor, not a riot; no
  weapons in the crowd (content-care).
- Direction (row-83): the swap's two vectors OPPOSE (Barabbas out
  toward the street, Jesus led inward toward the soldiers) and b15
  holds the divergence; if the vectors read parallel, the emblem
  dies.
- Cold morning light throughout.
- PAVEMENT promote-first from b01.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=1.00s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
