# QC / RUNNER HANDOFF — build-131-scribe-near-the-kingdom (Mark 12:28-34)

AUTHORED FROM SCRATCH (prepped + scaffolded + written this session),
2026-08-05 (Machine A). `--check` PASSES, zero WARNs. 16 beats, ~95 s.

## The scribe is the row's HERO

An honest teacher of the law — open, warm, quick-minded, never
adversarial. He must NOT share a face with the build-06
chief-priests family (he wears fine deep blue, not their robes;
face-board against them to confirm difference). The row's register
is MUTUAL RESPECT: b11 (the look) and b14 (the near-touch word) are
the twin peaks.

## Scripture-exactness

- b04 is the full Shema — gravity, hand at heart, court stilled.
- b10 is the scribe's OWN addition — his gesture at the altar smoke
  ranks love ABOVE offerings; the smoke reverent, never sinister.
- b14: Jesus's hand hovers a BREATH from the shoulder — inches, not
  contact; the nearness is the verse.
- b16: the questioners withdraw QUIETLY — no humiliation theatre.

## The threshold (b12)

A real open temple gate with warm light beyond, the scribe paused
mid-step — invitation architecture (rhymes with rows 125/127's open
doors). Never barred; his pause weighted and hopeful.

## Temple plate — ACCEPTED (family anchor)

TEMPLE wired from build-06 b21 — the SAME frame rows 43 (TEMPLE) and
75 (COURT) already anchor on; family consistency kept. Caveat noted:
that frame carries a near-ground trio (seated recorder + two women).
If they leak into renders as recurring figures, identity-edit them
out — the plate anchors the ARCHITECTURE only.

## Coverage shape

One true wide with stated geometry: b01 (camera past the listening
ring's backs). Eleven Jesus beats — locked face, no halo, warm
throughout; b07's two-fingers-together gesture must read. One
bright Jerusalem morning. File order ≠ story order (b05 at 70s,
b13 at 72s between b05 and b11's windows) — build by WINDOW; note
the scaffold numbers beats b12→b13 skipping a b12-window ordering
(b12 window 87.05, b13 window 72.68).

- LISTENERS varied (rows 90/107 clone check).
- SCRIBE face-board across all 12 appearances.

---

## RUNNER SHIP — Opus runner, Machine A `Dev`, 2026-08-11 (unattended/headless)

**COMPLAINT LEDGER: none open.** `v2_outline.py 131` shows no complaint on top;
REVIEW-LESSONS.json has zero matches for row 131 / "scribe". Fresh first-attempt
realistic-v2 cut.

**Portraits/refs:** SCRIBE portrait generated (`CAST-REF-V2/scribe.jpeg`, tight
face, deep-blue tunic + brown mantle, distinct from Jesus & the build-06
chief-priests family) and `REFS` wired — closes the row-52/55 face-flip class
proactively (QC.md wanted SCRIBE face-board across all 12 appearances).

**Plate:** TEMPLE (build-06 b21) verified period Herodian court, realistic,
daylight, no modern object. Its near-ground trio (seated recorder + two women)
did NOT leak as a recurring named figure — the incidental temple recorder in s08
is a genre figure, not the hero scribe.

**Generation:** 16/16 beats first pass, $2.14, meter $563.74. **0 rerolls (0%),
far under the 15% budget** — strong COST LAW.

**Light QC (source stills) — all 16 pass:** realistic photography throughout,
Jesus cream-only (scribe deep-blue, crowd earth-tones), scale correct (Jesus
ordinary), beards consistent, listeners varied (no twins/clones), no modern
objects, no lens-stare, no rotation/collage, no burned-in text on the KJV/Shema
beats. Twin peaks land: b11 the warm look; b14 Jesus's open hand hovers a clear
few inches from the scribe's shoulder (hover, not contact). b07 two-finger
gesture reads. b12 scribe paused at the open temple threshold (invitation).
Altar-smoke wides (s09/s10/s12) reverent. Jesus green/hazel eyes = systemic ref,
NOT rerolled (RUNNER-LESSONS).

**FULL-CUT GATE (rendered mp4, one frame per beat + card):** all clean. Caught +
FIXED one row-84-class caption defect below.

### CAPTION↔AUDIO FIX (row-84 class) — $0, audio byte-identical
The V1 narration SCRIPT (SEGMENTS) was tightened AFTER the ElevenLabs voices were
cut, so extract_beats printed a newer/shorter NARRATOR draft on screen that the
shipped mp3s do NOT speak. Transcribing the delivered mp4 (faster-whisper
small.en) vs each `audio/<seg>.timing.json` proved 4 narrator segments mismatched
(every KJV/scripture segment + n0a/n3/card already matched):
- n0b caption "which commandment matters most of all?" → audio "Jesus answered from words the scribe had known by heart for years."
- n1 caption "Jesus answered without hesitation…/Everything else hangs on those two." → audio "The answer was not merely an idea to admire. / It measured every other act of devotion."
- n2 caption "The scribe agreed — and added something honest:" → audio "The scribe had not merely repeated Jesus. He understood the weight of the answer."
- n4 caption "Not far. The man was close — a step from the door." → audio "That was both recognition and invitation. / Understanding had brought the man to the threshold; now he had to enter. / And no one dared question Jesus after that."
Fixed with `TEXT_OVERRIDES` in beats_v2.py (spoken timing.json text), re-assembled
→ AUDIO LOCK PASS **same SHA256 5f398642…** (byte-identical, zero re-voice).
Re-extracted the 4 segments' caption frames: all now match the voice, correct
colours (white narrator / blue scripture / red Jesus KJV), bottom-band only.

**Ship:** AUDIO LOCK PASS, 20.5 MB / 101.5s. Board RUNNING→BUILT.
