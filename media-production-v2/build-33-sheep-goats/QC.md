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

## ✅ AUTHOR DONE — 2026-08-07 (Machine A `Dev`, Fable-5 author session), $0

**Both complaints are now fixed in the author files, and the coupled timeline was
verified by a full local assemble.** Only ONE image credit remains — the s20 reroll —
which the author may not spend. RUNNER: reroll ONLY s20, re-assemble, ship. Details:

### What the author did (all committed with this row)
1. **Complaint 2 (SPEAKER) — DONE + verified.** V1 `make_narration.py`: `import ...
   SCRIPTURE`; `j37` speaker `JESUS → SCRIPTURE`, and the docstring rewritten to record
   Cameron's ruling so it is never flipped back. Regenerated ONLY `audio/j37.mp3`
   (free edge-tts, SteffanNeural −18%) → the righteous' question is now the SCRIPTURE
   voice / light-blue caption, OFF the Jesus red voice. **Verified in the assembled mp4
   at 0:77 — caption is light-blue "Lord, when saw we thee an hungred…" on the woman
   (s21), not red on Jesus.**
2. **TIMELINE COUPLING — measured, remapped, verified.** NOTE: the earlier park's
   estimate was BACKWARDS. The real old JESUS `j37` was **16.901 s**; the SCRIPTURE
   render is **19.512 s**, so `j37` seg_dur grew 18.331 → **20.942 s** (`is_kjv =
   spk != "narrator"` in extract_beats keeps the 1.15 s KJV gap for SCRIPTURE too, so
   only the mp3 duration changed). Everything from n5 onward shifts **+2.611 s LATER**;
   new card_start **175.790 s**, total **182.585 s**. All 25 windows b21–b45 in
   `beats_v2.py` were remapped: b21–b25 anchored to the 5 real phrase onsets from
   `j37.timing.json` (74.465 / 79.367 / 82.510 / 86.141 / 88.995), b26–b45 shifted
   +2.611 s and snapped to the exact extract_beats segment boundaries. Contiguity
   check: 0 gaps, last_end 175.790 = card_start. **Verified at 2:05 (t=125): j2
   "Inasmuch as ye have done it…" is still red on Jesus and in sync — no drift.**
3. **`AUDIO_FROM_V1_SEGMENTS = False → True`** (the V1 mp4 is now stale vs the re-voiced
   j37) so v2_assemble rebuilds audio from the V1 segment mp3s. Local assemble printed
   **AUDIO REBUILD PASS SHA256=91b16db5…**, 182.585 s.
4. **Complaint 1 (nails) — author half DONE.** `beats_v2.py` beat `v2-r033-b20` scene
   text: the self-contradicting phrase **"the nails black"** DELETED → now "the nails
   short, split and unpainted" (the `must_not_show` CAMERON GATE already forbade black
   nails; the scene body was the reason the model kept painting them). The `must_show`
   / `must_not_show` are unchanged and already correct.

### 🅿️ RUNNER — the ONE remaining step (a single reroll, then ship)
- **Reroll ONLY `s20-when-i-was-locked-away.jpeg`** against the now-fixed b20 scene text
  (`v2_gen_api … --only s20` or the build's reroll path). The prisoner's fingernails
  must be natural/unpainted. Do NOT regenerate any other still — the other 44 are
  accepted and byte-identical; a full regen would blow the reroll budget.
- **Re-assemble** (`python3 v2_assemble.py 33`) — this overwrites the verification mp4
  below with the clean s20. AUDIO REBUILD must PASS (from-segments path).
- **⚠️ DO NOT SHIP the mp4 currently on disk** — it was assembled for timeline
  verification and still carries the black-nail s20. Ship only AFTER the s20 reroll +
  re-assemble.
- Deploy + live-verify, then set Appr/Post per the C-FIX flow.

### COMPLAINT LEDGER — the review card must tell Cameron, in his words, both are fixed
1. **"at 1:10 why is the prisoner's nails painted black"** → the frame is regenerated
   with natural, unpainted working nails; the prompt no longer commands black nails.
2. **"at 1:16 Jesus is speaking something that wasn't spoken by Jesus"** → that line
   ("Lord, when saw we thee an hungred…") is the RIGHTEOUS, not Jesus. It is now OFF the
   Jesus voice — spoken in the scripture voice, light-blue caption — while Jesus's own
   words (j1, j2) stay red.

---

## RUNNER PARK — 2026-08-07 (Machine A Dev, C-FIX session) → State: NEEDS-REBUILD, $0, no re-cut
## [superseded by the AUTHOR DONE block above — kept for history]

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

### ⚠️ TIMELINE COUPLING measured 2026-08-07 (author lane, Machine A `Dev`) — READ BEFORE re-cutting
Complaint 2 is NOT a free swap: the JESUS voice j37 is **19.51 s**, but the same
words in the SCRIPTURE voice (en-US-SteffanNeural, -18%) render at **~16.90 s**, so
j37 gets **~2.6 s SHORTER**. `extract_beats` times every segment from the LIVE mp3
duration (line ~244), so the audio + captions for j2, n7, n8, n9 and the card all
move ~2.6 s EARLIER — but `beats_v2.py` still-windows are STATIC and
`v2_assemble.py` silently places stills on them (no validation; a collided tail beat
is dropped at the `dur<=0.05` guard). **Result if you only swap j37 + regen + assemble:
every still after j37 drifts ~2.6 s LATE — the exact row-42 caption/picture-drift
defect, a NEW complaint.** So Complaint 2 is a THREE-part author job, all in ONE ship:
  1. `make_narration.py`: `from mbm_speakers import ... SCRIPTURE`; `("j37", SCRIPTURE, …)`.
  2. Regenerate ONLY `audio/j37.mp3` (free edge-tts; mp3s are gitignored).
  3. **REMAP all beat windows after j37 to the NEW `extract_beats` timeline** (row-42
     monotonic piecewise-linear method, anchored on the segment boundaries) so stills
     stay on the voice. Measured anchors on the OLD timeline: card_start 173.179 s,
     total 179.974 s — recompute both after the swap and remap.
Because the final cut can only be verified by ASSEMBLING (and s20 must be rerolled
first, which spends an image credit the author cannot), the author reverted the
partial changes rather than hand the runner an unverified coupled timeline change.
Do all three (+ the s20 nails reroll) together, assemble, verify the still/caption/voice
agree at ~155-180 s, then ship.
