# QC / RUNNER HANDOFF — build-108-my-sheep-hear-my-voice (John 10)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 23 beats, ~133 s.

## Two shepherds (identity law)

The custom beats (b01-b03, b17) use the GENERIC olive-mantled shepherd
(SHEP lock); from the I-AM beats the shepherd IS Jesus (cream, ref).
The handover must be clean: never the generic man in cream, never
Jesus in the custom beats. Face-board both.

## Lead-from-the-front (the row's direction doctrine — row-83 class)

Every following frame has the shepherd AHEAD, back to the flock, the
sheep strung AFTER the voice — no one behind the flock, no raised
stick, ever. If a render shows driving-from-behind, the doctrine
inverts; reject.

## The sheep (the row-11 animal class)

A modest MIXED flock — grey-white and brown-black, several lambs,
individually varied so single sheep are recognizable (the by-name
calling depends on it: b06's called individuals must be distinct
animals). Same flock across frames; no sudden herd-size changes.

## Coverage shape

Four true wides with stated geometry: b02 (the invisible leash in one
profile), b03 (the shared fold behind the woolly backs), b06 (the
by-name calling in profile), b15 (the human flock behind the
gathered shoulders). Nine flips including b19's LONE carry through
rough weather (single + lamb — phantom trap) and b09's sheep-only
pool (no people at all).

- The pluck-them-from-my-hand beat rides on the carrying grip —
  contact believable (anatomy law), weather real, no drama beyond
  the wind.
- Dawn → green day → golden evening → night at the gate: one
  direction.
- HILLS promote-first from b09's pool hollow; FOLD from b03.
- Only Jesus wears cream (his beats only).

---

## RUNNER PARK (A-auto Machine A, 2026-08-06) — NEEDS-AUDIO, $0 spent

Pre-flighted the AUDIO LOCK at step 2 (both gates) BEFORE any generation.
**STALE-V1-FINAL — both tripwires fail:**
- RECENCY: V1 mp4 `john-10_my-sheep-hear-my-voice.mp4` rendered 2026-07-24
  10:15:29; all 14/14 narration mp3s are NEWER (2026-07-29 09:44:22). Copying
  the V1 audio stream would ship stale voices/deleted segments.
- DURATION: timeline total 148.623s vs V1 mp4 146.494s, |Δ|=2.129s > 1.0
  (v2_assemble line 531).

The board Audio column read "OK" but the authoritative pre-flight fails — trust
the pre-flight (RUNNER-LESSONS FLEET rule). Runner cannot re-voice/edit beats
under audio-immutability.

**Author fix:** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (narration
then renders from the V1 build's own mp3s at extract_beats offsets — nothing
re-voiced, V1 stays read-only), then this row is BUILDABLE.

**Resume command (runner, after author fix):**
`python3 media-production-v2/v2_story_cast.py build-108-my-sheep-hear-my-voice`
then generate. No stills were generated; nothing to reuse yet.
