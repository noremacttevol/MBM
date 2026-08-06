# QC / RUNNER HANDOFF — build-93-barabbas-goes-free (Matthew 27:15-26)

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
