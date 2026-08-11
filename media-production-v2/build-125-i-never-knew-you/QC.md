# QC / RUNNER HANDOFF — build-125-i-never-knew-you (Matthew 7:21-23)

AUTHORED FROM SCRATCH (scaffolded + written this session), 2026-08-05
(Machine A). `--check` PASSES, zero WARNs. 15 beats, ~85 s.

## CONTENT-CARE — the library's most sobering sermon row

The narration's own frame governs every render: "this is not a
threat to scare you. It is an invitation to be known."

- "THAT DAY" = a great door + warm morning light. NO fire, NO
  engulfing darkness, NO wrath-face, NO falling figures, in ANY
  frame. Automatic reject, no reroll spent.
- b12 ("I never knew you") is GRIEF: Jesus's face carries sorrow and
  loss, never fury; the pleaders turn away across ordinary dim
  ground — distance is the tragedy, not torment.
- The row ENDS on the door WIDE OPEN with Jesus's hand extended
  (b15) — the final image is welcome. If the closing render reads as
  anything but invitation, reject.

## The pleaders (sympathy law)

Earnest, respectable, genuinely accomplished — the viewer must see
THEMSELVES, not fools or villains (b09's face especially: "somebody's
beloved teacher"). Scroll-lists indistinct period script, never
readable text.

## The full-arms doctrine (b10)

The missing thing is made visible by composition: arms stacked to
the chin, NO hand free to be held. b13 answers it: the balance
retired empty, two hands clasped. b11/b14 answer it on the road:
the companion's hands visibly FREE and EMPTY. These four frames are
one argument — check them as a set.

## Jesus beats

b01, b03, b11, b12, b14, b15 — locked face, no halo. b12 grieving,
b15 welcoming; b11/b14 walking WITH a companion (matched stride,
easy conversation — direction and gaze law: heads inclined toward
each other).

## Coverage shape

One true wide with stated geometry: b01 (camera past the seated
crowd's backs). Short row — mostly closes and symbolic frames. File
order = story order except b04/b05 vignette inserts.

- Plates: ROAD auto-match REJECTED again (build-38 b39 road-through-
  doorway — second rejection of this same frame). DOOR promote-first
  from b02 (the door must be the SAME door in b06-b09, b12, b15 —
  closed until b15, then open), ROAD from b11, HILLSIDE shared with
  121-124.
- b04 street vignette: the declaimer is SINCERE, the doer unnoticed
  — no cartoon contrast.

---

## ⛔ RUNNER PARK — NEEDS-AUDIO (Opus runner, Machine A `Dev`, 2026-08-11, $0)

**Audio pre-flight FAILS the STALE-V1 guard — generated nothing.** `v2_assemble`'s
`assert_v1_final_is_current` refuses the AUDIO LOCK: the V1 mp4
(`matthew-7_i-never-knew-you.mp4`) runs **92.717s** but the timeline summed from the
current mp3s on disk is **91.824s** → **excess +0.893s > the guard's 0.75 threshold**
(newer_mp3s=0). An excess means the V1 mp4 carries ~0.9s of audio (a trimmed/deleted
segment or a longer take) that the current narration mp3s no longer contain, so copying
its AAC stream would ship stale audio. This is NOT trailing-silence noise: the shipped
sibling rows land ~0.04s excess (121 +0.038, 122 +0.047, 123 +0.015, 124 +0.073); only
125/126/127 carry ~0.9s.

**Runner cannot fix this** — the documented fix is `AUDIO_FROM_V1_SEGMENTS = True` in
`beats_v2.py`, which is an author/audio-lane edit (editing beats_v2.py is outside runner
writes; audio-immutability law). Rebuilding from the V1 mp3s at the extract_beats offsets
re-voices nothing and drops the stray ~0.9s tail.

**Audio-lane resume:**
```
# set AUDIO_FROM_V1_SEGMENTS = True in build-125-i-never-knew-you/beats_v2.py, then:
python3 media-production-v2/v2_assemble.py 125   # must print AUDIO REBUILD PASS
```
After AUDIO REBUILD PASS the row is buildable — a picture runner then generates the 15
stills (DOOR promote-first from b02, ROAD promote-first from b11, HILLSIDE plate shared
with 121-124) and ships per the normal loop.

**BATCH FINDING (same excess-tail defect):** rows **126** (+0.969), **127** (+0.889) share
the identical >0.75 excess (newer=0) and **128** (−1.778, **8 newer mp3s** — a genuine
un-rendered re-voice / the story-replacement) ALL need the same `AUDIO_FROM_V1_SEGMENTS=True`
audio-lane fix. All four parked NEEDS-AUDIO this session so no picture lane burns credits
rediscovering the wall. Row **129** was BUILDABLE (excess +0.380, newer=0) and is being
built this session.

COMPLAINT LEDGER: none open (v2_outline.py 125 shows no complaint block).
