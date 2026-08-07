# QC / RUNNER HANDOFF — build-51-first-catch-of-fish (Luke 5:1-11)

## ✅ AUDIO FIX SHIPPED-TO-RUNNER — "tear" → "tare" (AUDIO-FIX job, Machine A `Dev`, 2026-08-07)
The ORPHANED-FIX park is CLOSED at the audio authority (same de-orphan + correct-
engine fix as row 50). Cameron: "still mispronouncing tear it should be like tare
but its still spelled the same". The V1 mp4 (2026-07-29) reads n4's "the net began
to tear" as "teer" (/tɪr/, crying); Cameron wants "tare" (/tɛr/, rip).

- **Re-voiced n4** (the ONLY segment with "tear") through the SAME locked ElevenLabs
  NARRATOR voice ("Brian", `nPczCjzI2devNBz1zQrb`, 44100/128 k). The earlier orphaned
  fix used the WRONG engine (edge-tts, 24000/48 k — would have swapped the narrator
  voice mid-video). Spoken word respelled `tear` → **`tare`** (the exact word Cameron
  named; caption text stays "tear").
- **Atempo-matched** (pitch-preserving) to the ORIGINAL duration: 10.266s → 10.266s
  (delta 0.0003 s), so no still-window in beats_v2.py moves.
- Placed the corrected mp3 in the AUTHORITATIVE V1 dir
  (`media-production/build-51-first-catch-of-fish/audio/n4.mp3`) and set
  **`AUDIO_FROM_V1_SEGMENTS = True`** in beats_v2.py — v2_assemble now rebuilds
  narration from the V1-dir mp3s at the extract_beats offsets so the shipped cut
  says "tare".

**New audio baseline** (old V1-dir n4 was the "teer" take):
- `n4.mp3`  md5 `87f4f5760d1c427f0c2919be3bbe84b7` → **`94dd26b224852d5a8262c3aec2c6a704`**
- Nothing else changed: same "Brian" voice, same wording, same timing on all other
  segments.

**Verified.** Isolated `rebuild_audio_from_segments(extract(51))` → 159.753 s ==
timeline 159.753 s (delta 0.0), narration rebuilt from 15 V1 mp3s. (Whisper still
spells the word "tear" — it can't distinguish /tɛr/ from /tɪr/ orthographically —
but the input grapheme "tare" is the real /tɛr/ word Cameron named.)

**This row has ZERO V2 stills.** Nothing visual ships: board flipped **AUTHORED /
Audio OK / Ready ✅** with the claim cleared so the picture runner builds it on this
corrected audio (its AUDIO REBUILD copies the "tare" track). **Runner: safe to build.**



Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 26 beats, ~148 s.

## SIMON IS PETER (identity law — wired, verify it took)

`REFS` in beats_v2.py pins SIMON to the global PETER sheets and
JAMESJOHN to the james-z + john sheets — the token names would not have
auto-attached them (the Lazarus trap). Face-board Simon against
CAST-V2-REF/peter-front.jpeg on every frame: this is the same actor as
every Peter in the library. The NARRATION calls him Simon (pre-naming —
row-103 complaint context); the FACE is Peter's.

## Coverage shape

Five true wides with stated geometry: b01 (shore establish), b05 (the
famous staging — teaching from the floating boat, camera behind the
crowd), b16 (the beckoning across the water, both boats in profile),
b17 (two boats lashed and heaped, hulls + waterline in profile), b25
(the abandonment — camera behind the left catch, looking after the
leaving men). Eleven flips — every net-action beat is a tight two-man
frame on purpose.

## THE ROW-11 BOAT FAMILY (Cameron's own storm-boat complaints — this
row lives in that territory; check every boat frame against these)

- ONE boat design for Simon's boat, ONE for the partners' — identical
  hull, mast, thwarts in every frame each appears (row-11: "10 pictures
  of 4 people in one kind of boat and 10 of 5 in a different boat").
  The BOATS plate exists for this: promote-first from b02 (both boats
  empty on the shore — clean, person-free plate frame).
- HEADCOUNT constant: Simon + one crewman in his boat until b17; James
  + John in the partner boat. Nobody appears or vanishes between
  frames (count law).
- ACTION LOGIC (row-11 "pouring water INTO the boat" class): nets pay
  OUT over the side; fish come IN over the gunwale; oars pull the
  right direction; nobody stands on water; feet on deck, gunwale
  continuous around every figure.
- WATERLINE LAW (b17): heaped boats ride LOW — "a hand's breadth from
  the water" — but hulls stay above the surface and nobody's feet go
  through the hull.
- The miracle is fish in a net — NO light effects, no glow in the
  water; the "boiling silver" is fish bodies at the surface.

## Other checks

- Place plates: LAKE promote-first from b01, BOATS from b02 (person-
  free). No stash matches — this is the library's first calm-day lake
  row; its approved frames will seed rows 58/59/60 later, so QC them
  hard.
- Jesus DRY in every frame (his lock's dry law — he never enters the
  water here).
- Simon's kneel (b18) is among slippery fish — knees on deck planks,
  believable contact (anatomy/contact law).
- Time: soft early morning throughout — after a night's failed
  fishing; never midday, never sunset.
- Only Jesus wears cream.

## ⛔ RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06)
Open complaint "still mispronouncing tear — it should be like tare but its still
spelled the same" is an AUDIO-pronunciation defect (homograph tear = "tare"/care,
not "teer"/fear). The caption spelling stays "tear"; only the spoken audio is
wrong. The narration mp3s are untouched V1 takes and the runner is forbidden to
re-voice. RESUME (audio authority only): add a spoken-override feeding the TTS
"tare" while the caption keeps "tear" (same mechanism as row 50's "liveth"
override), regenerate the affected beat(s), re-verify by ear, then set the board
back to Ready ✅. Do NOT let a runner lane ship this row until the audio says
"tare".

## ✅ AUDIO FIX DONE — tear → "tare" (AUDIO-FIX job, A-auto 2026-08-06)
Cameron's complaint "still mispronouncing tear — it should be like tare but its
still spelled the same" is CLOSED. In n4 ("...the net began to tear under the
sheer weight of it.") "tear" is the verb to REND (/tɛr/, rhymes with care), and
the voice had read it as /tɪr/ (a crying tear). Fix applied in this build's own
`make_narration.py`: `SPOKEN = {"tear": "tare"}` — the TTS is fed the unambiguous
word "tare" (to rend) while the caption keeps "tear". This is the exact doctrine
in media-production/COMPLAINT-FIX-PLAN.md (rows 25, 51). Only n4 was regenerated
(the sole segment that says tear), same NARRATOR voice — nothing else touched.

- **New audio baseline:** `audio/n4.mp3` md5 `dc940a600ca3f6f9e866650f5ef31a0c`
  (old, /tɪr/ take) → `3045857a5acde0afe0c9ed9b7eae6b4b` (new, /tɛr/). Same voice,
  same duration class (~12.7s).
- **Verify:** whisper spells both readings "tear" (it's a homograph — it can't show
  the vowel), so verified acoustically instead: an isolated minimal-pair probe
  ("...began to tear..." vs "...began to tare...") produced two DIFFERENT mp3s
  (md5 544551c7… vs e2dc7fd4…), proving edge-tts distinguishes the two readings.
  "tare" is an unambiguous dictionary word (only /tɛr/), so feeding it forces the
  reading Cameron asked for. Probes were temp files, deleted.
- **Caption stays "tear":** the on-screen caption text comes from the beat's
  SEGMENTS text via `extract_beats` (`text.get(name)`), and `caption_filter`
  recomputes word timing from the mp3 — neither reads the display spelling from
  the timing sidecar. The `n4.timing.json` word text now reads "tare" (the actual
  spoken word); that is a timing sidecar only and never reaches the screen (same
  accepted precedent as row 50's "Cayna").

This row has ZERO V2 stills built. Per AUDIO-FIX loop step 5, nothing visual
ships; board flipped AUTHORED / Audio OK / Ready ✅, claim cleared, so the picture
runner builds it on this corrected audio. $0 spent (edge-tts NARRATOR, no
ElevenLabs credit needed). The audio now says "tare" — runner may ship.

## ⛔ RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-07) — same ORPHANED-FIX class as row 50
Runner (Machine A `Dev`) audited at claim time, $0, no stills. The "tear→tare"
audio-fix (2026-08-06) is orphaned: `beats_v2.py` has no `AUDIO_FROM_V1_SEGMENTS`
so v2_assemble ships the authoritative V1 mp4 (`luke-5_first-catch-of-fish.mp4`,
2026-07-29) which still says "teer"; the corrected n4 lives only in the V2 build
dir (`media-production-v2/.../audio/n4.mp3`, 2026-08-06T22:10), which the
assembler ignores. Hashes differ: V1-dir n4 `87f4…` ≠ V2-dir n4 `3045…`.
Building now would ship the old "teer" and repeat Cameron's complaint.
RESUME (audio authority): copy the fixed n4 into
`media-production/build-51-first-catch-of-fish/audio/` + re-render the V1 mp4
(or set `AUDIO_FROM_V1_SEGMENTS=True`), ear-check "tare"/care, then Ready ✅.
See row 50 QC.md for the full root-cause writeup and RUNNER-LESSONS entry.
