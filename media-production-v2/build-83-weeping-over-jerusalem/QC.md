# QC / RUNNER HANDOFF — build-83-weeping-over-jerusalem

## ✅ AUDIO FIX DONE — AUDIO-FIX session, Machine A, 2026-08-06 ($0)

**STALE-V1 audio-lock CLEARED.** Added `AUDIO_FROM_V1_SEGMENTS = True` to
beats_v2.py. V1 mp4 `luke-19_weeping-over-jerusalem.mp4` tripped
`assert_v1_final_is_current`'s runtime tripwire (|Δ|~2.2s vs the summed segment
timeline), so the AUDIO LOCK refused to copy the stale stream. With the flag set,
v2_assemble rebuilds narration from the V1 build's OWN mp3s at the extract
offsets — nothing re-voiced/re-timed, V1 read-only. **Segment parity 10/10
exact.** Validated: `v2_assemble.py 83` now clears the audio gate and stops only
on missing stills (0 V2 stills); `v2_prompt.py 83 --check` PASSES (14 beats).
Board NEEDS-AUDIO → AUTHORED / Audio OK / Ready ✅, claim cleared → picture
runner generates + assembles on corrected audio. Same mechanism as shipped row 69.

---

## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight, generated NOTHING)

STALE-V1 audio class (duration tripwire only). $0 audio-lock pre-flight:
- RECENCY: newer_mp3s=0 (OK).
- DURATION: timeline total vs V1 mp4 → excess=-2.20s (abs>1.0, v2_assemble line 531).
The V1 mp4 runs 2.20s SHORT of the current beats timeline — carries out-of-date
audio. Runner is forbidden to re-render/edit beats_v2.py (audio-immutability).

AUTHOR FIX: add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, OR
re-render the V1 mp4. Then set Ready ✅ + Audio OK on AUTHOR-BOARD.
RUNNER RESUME (after author fix): `python3 media-production-v2/v2_story_cast.py build-83-weeping-over-jerusalem` then `v2_gen_api.py build-83-weeping-over-jerusalem --ceiling …`.
No stills were generated; nothing to reuse yet.
