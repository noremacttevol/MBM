# QC / RUNNER HANDOFF — build-99-flesh-and-bone-thomas (Luke 24/John 20)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 99`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 15 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 14 beats, ~79 s.

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron):

> "Old audio needs updating and i belive the thomas character is off"

1. AUDIO: REDO-ALL gate — verify the rendered MP4 carries the verified
   new-voice stream (rows 92's law).
2. THOMAS: he has a GLOBAL sheet (thomas-front/quarter) — the token
   auto-attaches it. Face-board every Thomas frame against the sheet;
   "the character is off" means his V1 face drifted from the cast —
   this build must nail the sheet's man exactly.

## The risen body (rendering laws)

- NATURAL warm flesh-and-bone — cream robe, real weight; NO graphic
  wounds ever (the hands are offered OPEN; the marks are never
  detailed); no shining, no materialization effects — he is simply,
  solidly THERE with the bar still in its brackets (both appearances).
- Thomas NEVER TOUCHES (John 20:28-29 — the offer is enough): his
  confession comes at the sight of the offered hands; if a render
  shows the finger in the wound, it is scripturally wrong — reject.

## Coverage shape

Three true wides with stated geometry: b01 (the first standing, behind
the huddled shoulders), b07 (the second standing, behind the circle's
backs — the mirror), b11 (the meeting — doubter and doubted in one
profile). Five flips; b14's closing is candid-safe by its own text
(hands offered "out of the picture entirely" — never into the lens).

## Other checks

- The BARRED DOOR with its beam is in frame at both appearances — the
  locked-room fact is the miracle's frame.
- Disciples distinct (row 90's gate applies); Peter/John sheets.
- Lamplit evening both scenes; eight days pass BETWEEN b06 and b07 —
  same room, same bar, the only change is Thomas present.
- ROOM promote-first from b01 (it is NOT rows 89/90's supper room —
  a different hiding room; do not take their plate).
- Only Jesus wears cream.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=9.28s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.

---

## ✅ REALISTIC-V2 SHIPPED — Opus picture runner, Machine A `Dev` (A-auto 2026-08-07, UNATTENDED/HEADLESS)

**14 realistic stills @ native 2K, AUDIO REBUILD PASS `6e928ade4a0f...`, 88.7s, john-20_flesh-and-bone-thomas.mp4 (18.9 MB).**
ROOM promoted from b01 (this hiding room, NOT rows 89/90's supper room) -> wired to 10 beats.
0 portraits (THOMAS/PETER/JOHN sheets already exist). Meter ~$492.05.

### COMPLAINT LEDGER — Cameron's open complaint on this row:
> "Old audio needs updating and i belive the thomas character is off"

1. **AUDIO ("old audio needs updating") — FIXED.** `AUDIO_FROM_V1_SEGMENTS=True`
   makes the assembler rebuild narration from this build's 9 V1 segment mp3s
   (the new-voice takes), NOT the stale 2026-07-24 V1 mp4. Result: 88.7s (the
   old mp4 was 79s — the |Delta|=9.28 STALE gate is exactly why it needed the
   rebuild). **AUDIO REBUILD PASS `6e928ade4a0f3a09...` is the cryptographic
   proof the delivered mp4 carries the rebuilt segment audio.**
2. **THOMAS ("thomas character is off") — FIXED.** The THOMAS lock auto-attaches
   `CAST-V2-REF/thomas-front.jpeg` to every Thomas beat. Face-boarded all six
   Thomas frames (b05/b06/b08/b10/b11/b12) side-by-side against the sheet: dark
   tousled hair, practical furrowed brow, medium dark beard, warm olive skin —
   the sheet's man in every frame, in a consistent teal-blue robe. The V1
   face-drift that read "off" is gone; this is one Thomas across the cut.

### Rendering-law checks (all PASS):
- Only Jesus wears cream (checked every multi-figure frame; no second cream robe,
  no Jesus double on the jesus:False frames b02/b05/b06).
- NO graphic wounds/gore — hands offered open; a faint pale/red risen-mark shows
  on Jesus's hand in b04/b09/b10 (small, never detailed) -> within the "risen
  wounds = gentle marks, never gore" law.
- Thomas NEVER TOUCHES — enforced. b10's first take had Thomas clasping Jesus's
  forearm (contradicted the beat narration "he never did reach out and touch
  anything") -> **rerolled once**; the shipped take has Thomas's hand raised but
  stopped short, eyes on the face. No finger-in-wound anywhere.
- Barred door + beam in brackets present at both appearances (b01/b07/b13/b14).
- Lamplit evening both scenes; calm warm Jesus eyes (rubric lesson 18) — no
  crazy/lens-stare; b14 closing outward-address is candid-safe by its own text.

### COST — 1 reroll / 14 beats = **7.1%** (under the 15% budget). Row ~= **$2.01**
(15 stills incl. the b01 anchor + 1 reroll, 0 portraits). Under the $6.10 avg —
cost-law DOWN trend holds.

### FIX-WAVE (non-blocking, no filed complaint):
- Faint risen-mark on Jesus's hand (b04/b09/b10) — deliberate restraint call,
  not blind-rerolled.
