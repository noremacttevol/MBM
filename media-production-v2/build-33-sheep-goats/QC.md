# QC / RUNNER HANDOFF — build-33-sheep-goats

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before rebuild

"At 1:10 why is the prisoner nails painted black thats weird. And
then at 1:16 it has Jesus speaking something that wasent spoken by
Jesus and makes no sense."
1. b20 (1:10): BOTH hands natural unpainted fingernails — never
   black/dark/painted; ordinary working nails.
2. b21+ (1:16): "Lord, when saw we thee an hungred..." is the
   RIGHTEOUS speaking, not Jesus — yet the built cut carries it in
   the Jesus voice (the row-39 speaker lesson). This is an
   AUDIO-side fix Cameron has explicitly ordered: the righteous'
   question lines must come OFF the Jesus voice before this row is
   re-presented. Route to the audio pass; do not re-present with
   the wrong-voice line intact.

---

## RUNNER PARK — 2026-08-07 (Machine A Dev, C-FIX session) → State: NEEDS-REBUILD, $0, no re-cut

I claimed this row's C-FIX, read `v2_outline.py 33`, and VISUALLY confirmed both
open complaints by extracting the exact frames from the shipped mp4
(`ffmpeg -ss 70` and `-ss 76`). BOTH complaints root-cause to LOCKED author
files, so this is an AUTHOR rebuild, not a runner reroll — I spent $0, touched
no art and no audio, and did NOT ship. Per touch-once, ONE author re-cut must
fix BOTH before this row is re-presented.

### Complaint 1 — "at 1:10 the prisoner's nails are painted black" (PICTURE, but author-locked)
- Frame 70.0 s = beat **`v2-r033-b20`** / `s20-when-i-was-locked-away.jpeg` (seg n4).
- Confirmed: the prisoner's male hand through the bars has clearly BLACK,
  polished-looking fingernails. Exactly Cameron's complaint.
- ROOT CAUSE (why a reroll won't fix it): the beat's own `must_not_show` already
  carries a CAMERON GATE forbidding black nails, **but the `scene` body still
  literally commands** `"...the nails black, a heavy hand-forged iron shackle..."`.
  The prompt contradicts itself, so the model keeps painting the nails black.
  The runner may not edit locked scene text.
- AUTHOR FIX: in `beats_v2.py` beat `v2-r033-b20`, DELETE the phrase
  `the nails black` from the male-hand description (replace with e.g.
  "the nails short, split and unpainted"). Then regenerate ONLY `s20`.

### Complaint 2 — "at 1:16 Jesus is speaking words not spoken by Jesus" (SPEAKER / re-voice)
- Frame 76.0 s = seg **`j37`** ("Lord, when saw we thee an hungred, and fed thee?
  or thirsty, and gave thee drink?", Matt 25:37-39).
- Confirmed: the caption renders in Jesus-RED and is voiced in the Jesus voice —
  but these are the RIGHTEOUS' words, not Jesus's. Under this build's own
  SPEAKER-LAW, "the people inside the stories" = **SCRIPTURE** (light-blue,
  en-US-SteffanNeural), NOT JESUS.
- ROOT CAUSE: `make_narration.py` SEGMENTS declares `("j37", JESUS, ...)`.
- AUTHOR FIX: change that entry to `("j37", SCRIPTURE, ...)` (import SCRIPTURE
  from `mbm_speakers`). This takes the righteous' question OFF the Jesus voice
  AND off the red caption in ONE change. Regenerate `audio/j37.mp3`, then
  re-assemble (AUDIO LOCK hash WILL change — that is expected and correct here;
  the audio is intentionally no longer byte-identical because the wrong voice is
  being removed).

### Ship gate for the rebuild session
- Do Complaint 1 and Complaint 2 in ONE re-cut / ONE re-assembly / ONE ship.
- Review card flag must answer BOTH in Cameron's words: (1) "the prisoner's black
  nails at 1:10 — the frame is regenerated with natural, unpainted nails"; (2)
  "the 1:16 line 'Lord, when saw we thee an hungred' is the righteous, not Jesus —
  it is now off the Jesus voice, spoken in the scripture voice / light-blue caption."
