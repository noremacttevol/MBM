# QC / RUNNER HANDOFF — build-63-man-born-blind (John 9)

## §0-FIXED ✅ AUDIO FIX DONE — Siloam complaint CLOSED (Machine A `Dev`, 2026-08-07, author lane)

**Cameron's OPEN complaint (`v2_outline.py 63`): `"still wrong its : si-LOH-uhm"`
(Siloam) — FIXED at the author level. j2 & n5 re-voiced; row → AUTHORED, Ready ✅.**

### Root cause (verified, not guessed)
The delivered build is **ElevenLabs** (Chris=Jesus, Brian=narrator, all 44.1 kHz —
the park's earlier "just edge-tts" read was wrong; only make_narration.py's *source*
is edge-tts). On the ElevenLabs Jesus voice **plain "Siloam" renders as "Salome"**
(reproduced by faster-whisper base.en+small.en on the delivered j2.mp3, and again on
a fresh ElevenLabs render). The old respell `"sih low um"` rendered as chopped
"silo, um". Neither is Cameron's target si-LOH-uhm.

### The fix (what I did — all committed with the row)
1. **Respell** `make_narration.py` SPOKEN: `"Siloam" → "Siloh-am"`. Measured A/B:
   `Siloh-am` round-trips CLEAN to "Siloam" on BOTH whisper engines for BOTH voices
   AND on BOTH TTS backends (ElevenLabs + edge-tts). Sounds sih-LOH-am = his target.
   Caption keeps the true KJV "Siloam" (unchanged).
2. **Re-voiced j2 + n5 through ElevenLabs** (matching engine — NOT edge-tts, which
   would have made Jesus's voice mismatch the other 21 segments). Both write 44.1 kHz;
   audio-audit A (old-voice) is now **0 of 23**. New durations: j2 3.006 s (was 3.531),
   n5 14.977 s (was 16.721) — the correct pronunciation is a touch tighter.
3. **Timeline coupling remapped.** j2 shrank 0.525 s, n5 1.744 s → n4-region shifts
   −0.525 s, n6-onward −2.269 s. New total **247.692 s**, card_start **240.217 s**.
   All 43 V2 picture windows remapped via a piecewise-linear old→new map anchored on
   the segment onsets (extract_beats). `--check` PASS, windows monotonic + contiguous,
   last_end 239.891 < card_start 240.217.
4. **`AUDIO_FROM_V1_SEGMENTS = True`** added to `beats_v2.py` — the finished V1 MP4 is
   now stale vs the re-voiced mp3s, so the runner rebuilds the track from the V1
   segment mp3s at the extract_beats offsets. audio-audit B (short) is now **0**.

### 🅿️ PICTURE RUNNER — the ONLY remaining steps (a paid picture credit + assemble)
Stills are **41/43**. Generate the last two, then assemble+ship on the fixed audio:
- `python3 media-production-v2/v2_gen_api.py media-production-v2/build-63-man-born-blind --ceiling <meter+2*0.201+25>`
  → pulls **b42** (`s42-and-he-worshipped-him-right`) and **b43**
  (`s43-the-question-of-whose-fault`) only (~$0.27). Run the eyes-arc light-QC below.
- `python3 media-production-v2/v2_assemble.py 63` — AUDIO_FROM_V1_SEGMENTS path,
  AUDIO REBUILD must PASS. Deploy + live-verify, then ship via the C-FIX/ship flow.

### COMPLAINT LEDGER — the review card must tell Cameron, in his words
1. **"still wrong its : si-LOH-uhm"** (Siloam) → Jesus's line "Go, wash in the pool of
   Siloam" and the narrator's "He knelt at the pool of Siloam" now clearly say
   **si-LOH-am** (verified round-trip both engines), no longer "Salome". Same
   ElevenLabs voices as the rest of the video; captions keep the KJV spelling "Siloam".

---

## §0 🅿️ RUNNER PARK → NEEDS-AUDIO (Machine A `Dev`, 2026-08-07, Opus runner resume) [SUPERSEDED by §0-FIXED above — kept for history; its "needs ElevenLabs, not edge-tts" instinct was right, its "just edge-tts" aside was wrong]

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
