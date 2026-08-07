# QC / RUNNER HANDOFF — build-83-weeping-over-jerusalem

## ✅ RUNNER SHIP — realistic-v2, A-auto Machine A `Dev`, 2026-08-07

**COMPLAINT LEDGER (3 open, from `v2_outline.py 83` — all addressed):**
1. **"first picture they are walking the wrong way... away from Jerusalem rather than toward it."** → FIXED at b01: authored camera BEHIND the procession's shoulders, so every walker moves AWAY from the lens and TOWARD the revealed city; the road streams down to the gate with Jerusalem + temple filling the background. Verified in the rendered s01 — the whole procession visibly heads toward the city.
2. **"the second picture Jesus looks like a giant."** → FIXED: lesson-14 scale gate applied to EVERY multi-figure frame (b02/b09/b11/b14). Jesus renders at the SAME height as the men beside him in all of them — ordinary-sized, never enlarged. b02 (the complaint frame) verified head-to-head against the flanking disciples: proportionate.
3. **"at the end... the question is asked but then it stays going for an extra 13 seconds."** → FIXED by the STALE-V1 audio rebuild (AUDIO_FROM_V1_SEGMENTS=True): the dead tail was V1's stale over-long stream. Tail check at assembly: captioned.mp4 duration ≈ card seg_start (±0.2s) and final mp4 ≈ audio length — NO trailing dead air after the question card. (See ASSEMBLY block below for the measured numbers.)

**Light QC (1 pass, all 14 frames + skyline zoom on b02 + 3 rendered caption frames): 1 reroll / 14 = 7% (COST LAW, under 15%).**
- b02 REROLL: first take had a MODERN skyline behind the temple (high-rise tower block + antenna masts + construction crane) — modern-object fail on the hero "he stopped" frame. One `--redo` cleared it: all-period limestone city + temple, no modern structures. $0.13.
- Beard board: full dark beard + shoulder-length wavy dark hair identical across every Jesus frame (s01-s14). Scale gate: Jesus ordinary-sized in every multi-figure frame. Only-Jesus-cream held (crowd in earth-brown/rust/olive; s08/s12 jesus:False frames carry no cream figure, no Jesus-double). No lens-stare, no burned-in subtitle on the quote beats (s04/s07), anatomy clean, city INTACT every frame (off-screen-ruin law), green/hazel Jesus eyes are the baked V2 ref (not rerolled).
- FIX-WAVE (kept, non-blocking): s06 (gate-traffic wide) has a faint hazy distant structure top-left that could read modern at full zoom — distant, non-hero, borderline; COST-LAW FIX-WAVE rather than a reroll (a reroll re-seeds the whole landscape for one hazy far element).

---


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
