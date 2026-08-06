# QC / RUNNER HANDOFF — build-74-woman-washed-his-feet (Luke 7:36-50)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 36 beats, ~208 s.

## SAME-EVENT LAW — shared cast with build-44 (verified byte-identical)

This is the SAME dinner as build-44-two-debtors. WOMAN/SIMON/ROOM/JAR
locks verified BYTE-IDENTICAL between the two builds this session.
Whichever row builds FIRST defines the faces; the second adds a
build-local `REFS` pointing WOMAN and SIMON at the first's approved
stills (the build-17 mechanism). Same room, same jar, same actors —
a viewer watching both videos must see one dinner.

## Coverage shape

Five true wides with stated geometry: b01 (the correct dinner from the
side), b03 (the entrance — door and table in one side-on frame), b05
(the reclining geometry in profile — the row teaches its own staging),
b10 (the triangle in profile), b23 (the audit — dry basin and washing
feet, both poles in one frame). Seven flips.

## The woman's dignity (the row's own stated law — absolute)

Her lock and the docstring say it: modest dark dress, bound hair at
entry, NOTHING lurid ever; her reputation exists only in the guests'
faces. The loosed hair at his feet is costly humility, reverent. Any
render that codes her otherwise is an automatic reject.

## Cross-row echoes with build-44 (keep them rhyming)

- The unused water jar/basin by the door (the audit's dry pole) is
  the SAME prop in both rows' arrival and audit frames.
- The jar arc: sealed → opened → poured → EMPTY, ending on the HUSH
  beat (b36: the empty jar and the open night door — V1's silent
  breath; person-light frame, do not crowd it).
- The reclining feet-away staging is the row-83-class trap in both
  rows: feet under a table = geometry broken = reject.

- Only Jesus wears cream. Guests varied (90/107), Simon cold-correct.
- ROOM promote-first from b01 (whichever of 44/74 renders first owns
  the room plate — then --take it into the other).

---

## 🅿️ RUNNER PARK — A-auto 2026-08-06 (NEEDS-AUDIO — stale V1 mp4, row-69 class)

Caught BEFORE any credit spent (zero stills generated — COST LAW win). The
assembler's STALE-V1-FINAL guard will refuse the AUDIO LOCK on this row:

- V1 mp4 `luke-7_woman-washed-his-feet.mp4` last committed **2026-07-24 10:15**
  (commit 5bd6b82a9, new-voice ship), never re-rendered since.
- All **19/19** placed narration mp3s in `audio/` are NEWER than that mp4
  (content_time-verified against `v2_assemble.assert_v1_final_is_current`).
- The mp4 runs **171.67s** but the extract_beats timeline sums to **184.57s**
  — the mp4 is **12.9s SHORT** of the current narration. Its audio stream
  predates the current beats, so copying it would ship stale/short audio.

Reproduced the guard exactly (RECENCY tripwire fires: newer_mp3s=19/19). By
contrast shipped rows 68/64 show newer_mp3s=0 and excess≈0. This is the
row-69 stale-V1 class — the runner ships byte-identical V1 audio and does NOT
re-render or edit beats_v2.py, so it cannot fix this.

**RESUME (author/audio session):** either re-render the V1 mp4 from the current
narration, OR add `AUDIO_FROM_V1_SEGMENTS = True` to this build's beats_v2.py so
`v2_assemble` rebuilds the track from the V1 build's own mp3s at the
extract_beats offsets (nothing re-voiced/re-timed; V1 stays read-only). Then
flip AUTHOR-BOARD row 74 State→AUTHORED Audio→OK Ready→✅. No stills exist yet —
the full generate step runs fresh when audio is unblocked. SAME-EVENT LAW: this
row renders the shared WOMAN/SIMON/ROOM/JAR faces FIRST (build-44 is retired),
ROOM promote-first from b01.
