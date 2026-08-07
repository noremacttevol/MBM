# QC / RUNNER HANDOFF — build-63-man-born-blind (John 9)

## §0 🅿️ RUNNER PARK → NEEDS-AUDIO (Machine A `Dev`, 2026-08-07, Opus runner resume)

**The picture runner STOPPED at the audio gate. Cameron's OPEN complaint is
AUDIO-domain — a picture runner may not re-voice, so this row is parked
NEEDS-AUDIO for the audio lane. $0 spent (no Gemini credits), 0 pictures touched.**

**Cameron's OPEN complaint (`v2_outline.py 63`):** `"still wrong its : si-LOH-uhm"`
(the pronunciation of **Siloam** — he wants **si-LOH-uhm**).

**VERIFIED WRONG in the locked V1 audio (faster-whisper base.en + small.en, both agree):**
- **`audio/j2.mp3`** (Jesus: *"Go, wash in the pool of Siloam."*) transcribes as
  **"Go, wash in the pool of Salome."** — this is Jesus's own spoken instruction,
  the most prominent occurrence and the exact context of the complaint. "Salome"
  ≠ si-LOH-uhm (wrong first vowel *sa-*, wrong ending *-mee*). **This is the defect.**
- `audio/n5.mp3` (*"He knelt at the pool of Siloam…"*) transcribes cleaner
  ("siloam") but should be re-checked once j2 is fixed.
- The existing narration override in `make_narration.py:89` is
  `"Siloam": "sih low um"` (added 2026-07-22 for complaint #63). It did NOT
  land — the delivered audio still says "Salome". A better respelling and a
  re-voice through the REAL engine (ElevenLabs, per row 18/19 audio-fix law —
  NOT edge-tts) is needed.

**AUDIO LANE — the fix (spend $0 on Gemini):**
1. Respell **Siloam** in `make_narration.py` so it lands as **si-LOH-uhm**
   (e.g. try `"sih LOAM"` / `"sih LOH um"` / an ElevenLabs phoneme tag) and
   re-voice **j2**, plus **n4/n5** wherever "Siloam" occurs. Ear-check each take
   until it clearly says si-LOH-uhm.
2. Also verify the KJV caption keeps the true spelling "Siloam" (unchanged).
3. Set `AUDIO_FROM_V1_SEGMENTS=True` so the re-cut rebuilds from the fixed mp3s.

**PICTURE STATE (so the handoff is honest):** stills are **41/43** — only two
frames remain to generate: **b42** (`s42-and-he-worshipped-him-right`) and
**b43** (`s43-the-question-of-whose-fault`), est ~$0.27. They were NOT generated
here (gate = stop). After audio is fixed, a picture runner must:
`python3 media-production-v2/v2_gen_api.py media-production-v2/build-63-man-born-blind --ceiling <computed>`
to pull b42/b43, run the full light-QC (the eyes arc b19/b21/b22 first-sight is
the identity law — see below), then `v2_assemble.py 63` and ship.
So: **NEEDS-AUDIO now → after audio fix, AUTHORED+Ready (2 stills + QC + assemble remain), not directly BUILT.**

---


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 43 beats, ~242 s.

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron):

> "still wrong its : si-LOH-uhm"

Audio gate: verify the locked V1 narration says si-LOH-uhm at every
"Siloam." If it does not, mark NEEDS-AUDIO on the board and stop (audio
immutability — never re-voice).

## Coverage shape

Four true wides with stated geometry: b03 (the passing, in profile),
b06 (the street's verdicts crossing behind the beggar's shoulder), b24
(the dispute ring, camera outside the near backs), b25 (the tribunal —
accused and examiners in one profile). TWELVE flips, and the row's soul
lives in three of them being LONE-man frames: b19 (the clay-eyed walk
down the lanes ALONE — staff, wall-touch, strangers' stares), b21 (the
washing), b22 (FIRST SIGHT). Phantom people in the walk would destroy
the obedience-before-sight arc.

## The eyes (the row's identity law)

- BEFORE: his eyes are unfocused/clouded — a real blind man's eyes,
  never milky-horror, never bandaged.
- CLAY ON: the clay is visible over both eyes b12→b21 — continuity
  prop; same clay, drying as he walks.
- AFTER (b22 on): NEW clear seeing eyes in the SAME face — face-board
  him hard; this is the beard-class risk row (32/62/91/102) with eyes
  instead of beards. His first-sight face is joy-shock, not horror.
- The washing pours from cupped hands — Siloam is a stepped POOL
  (promote-first from b21), not a river.

## Other checks

- HALL: stash offered build-22's ROYAL hall — DECLINED (this is a
  Pharisee council chamber, different institution). Promote-first from
  b25.
- LEADERS: exactly THREE examiners (count law), distinct, cold-formal
  not cartoon (row 90/107 variety).
- Direction (row-83): b19 DOWN the lanes to the pool; b23 BACK UP at a
  half-run (staff forgotten — the prop's absence is the story); b31
  OUT through the heavy door.
- The parents' fear beats (if rendered): they edge AWAY from the
  question — spatial, believable.
- Only Jesus wears cream.
