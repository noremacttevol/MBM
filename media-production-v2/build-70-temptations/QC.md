# QC / RUNNER HANDOFF — build-70-temptations (Matthew 4:1-11)

## ✅ AUDIO FIX SHIPPED-TO-RUNNER — "proceedeth" → pro-SEE-duhth + ENGINE fix (AUDIO-FIX job, Machine A `Dev`, 2026-08-07)
Both halves of Cameron's complaint are now correct in the audio the assembler
ships. The proceedeth half was ORPHANED **and the earlier fix used the WRONG
ENGINE** — a trap the 2026-08-07 park below missed:

- The authoritative V1 `j1.mp3` is **ElevenLabs JESUS ("Chris", 44100/128 k)** —
  this build migrated to ElevenLabs even though `mbm_speakers.py` still shows the
  stale edge-tts EricNeural scaffold. The 2026-08-06 "fixed" j1 in the V2 build
  dir was rendered in **edge-tts (24000/48 k) = wrong engine**; shipping it (or
  copying it into the V1 dir as the park suggested) would have swapped Jesus's
  voice mid-video.
- **Correct fix:** j1 (the ONLY "proceedeth" segment) re-voiced through the SAME
  locked ElevenLabs JESUS "Chris" (`iP95p4xoKVk53GoZ742B`) with the word respelled
  `proceedeth` → **`proceeduth`** (= pro-SEE-duhth, the /dəθ/ ending Cameron named;
  caption keeps "proceedeth"). Reverent internal pauses shaped with ellipses to
  mirror the original's pacing, then **atempo-matched to the ORIGINAL duration
  (7.837 s)** so NO downstream window moves — **no coupled remap needed** (the
  park expected a +1.083 s edge take; the ElevenLabs take is duration-matched
  instead, which is simpler and safer).
- **n2's "I-S"/"IF"** was ALREADY correct in the shipping ElevenLabs audio
  (verified previously) — untouched. The edge-tts n2 in the V2 dir is likewise a
  wrong-engine orphan and is deliberately NOT used.

**New audio baseline** (old V1-dir j1 was the ElevenLabs Chris take that
mispronounced proceedeth):
- `j1.mp3`  md5 `ab7ae01624180b692e163d939c5eeadd` → **`7f083601811f3c79705c1077adff90a4`**
  (7.837 s → 7.837 s, same voice, same wording, caption unchanged).

Set **`AUDIO_FROM_V1_SEGMENTS = True`** in beats_v2.py so v2_assemble rebuilds
narration from the V1-dir mp3s. **Verified:** isolated
`rebuild_audio_from_segments(extract(70))` → 248.644 s == timeline 248.644 s
(delta 0.0), narration from 20 V1 mp3s; `v2_prompt.py build-70-temptations --check`
PASSES (42 beats, v4 checklist PASS).

**This row has ZERO V2 stills.** Nothing visual ships: board flipped **AUTHORED /
Audio OK / Ready ✅**, claim cleared, so the picture runner builds it on this
corrected audio. **Runner: j1 now says pro-SEE-duhth in the locked Jesus voice —
safe to build.**



Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 42 beats, ~237 s.

## ⚑ A-LAW — THE ADVERSARY IS NEVER DEPICTED (the row's absolute law)

No figure, no shadow-shape, no silhouette, no voice-form, no red glow,
no serpent, no second man — EVER. The temptations arrive as the build
authored them: wrongness in the light, pressure in the silence, the
framing of the offers (stones, the drop, the vista). If any render
contains a second figure in a temptation beat, it is an automatic
reject. The only non-Jesus figures in the row are the two blue-robed
MINISTERS after the victory (b33-b35, restrained: robed figures with
bread and water — reverent, wingless, human-scaled).

## Coverage shape — SOLITUDE IS THE STORY

ONE true wide (b33 — the ministers arriving, three figures in profile:
the tide turning is the one moment company exists). TEN former wides
were Jesus ALONE against vastness (the waste, the pinnacle, the black
summit) — the phantom-people trap at its absolute worst; every one is
re-flagged and the emptiness now rides in the prose. If a render adds
anyone to a solo frame, reject.

## The three temptations (framing laws)

1. STONES (desert): real desert stones that resemble loaves at his
   feet — the resemblance is the temptation; no talking figure.
2. PINNACLE: the temple parapet with the REAL drop below — city small,
   vertigo honest; he never wavers on the edge.
3. SUMMIT: the world's glory as a vista — kingdoms as far lights and
   distant splendors, never a floating montage or globe.
   The dismissal (b31): his arm flung toward the empty air — command
   with no visible addressee, exactly like row 65's b24.

## Other checks

- The fast shows: b05 onward Jesus is visibly leaner, wind-worn,
  sun-dark — but never emaciated-horror (row-15 dignity law); the
  hunger is real and borne.
- Direction (row-83): b01 UP from the green valley into the waste;
  b42 BACK DOWN toward the green at dawn — the arc closes.
- All four places promote-first (DESERT b04, PINNACLE b18, SUMMIT b26
  from their first solo frames; MINISTERS is CAST — no plate).
- Wilderness is Judean badlands — brown, broken; distinct from row
  54's leper wilds and row 59's Decapolis slope (three wildernesses,
  three plates — never cross them).
- Only Jesus wears cream.

---

## ✅ AUDIO FIX DONE — AUDIO-FIX session, Machine A, 2026-08-06

**Both of Cameron's row-70 audio complaints are CLOSED. $0 spent** (edge-tts is
free; no Gemini, no ElevenLabs). Audio is now new-voice-clean and the row is
handed to the picture runner to build on the corrected narration (0 V2 stills
existed, so nothing visual was shipped — same handoff as rows 50/51).

**COMPLAINT LEDGER (picture runner: surface this on the review card when you ship):**
> Cameron: *"The narrator spells out 'I-S' instead of pronouncing the word like
> it should. Also it mispronounced 'proceedeth' it should be pro-see-duhth."*
- **"I-S" spelled out** → FIXED. n2's emphasis-caps `IS`/`IF` ("this **IS** my
  Son", "the little word **IF**") were read letter-by-letter by edge-tts
  (whisper heard caps "IS" as "I asked"). Build-local `SPOKEN` now lowercases
  them **for the TTS only** — the caption still shows the caps. Re-voiced n2
  (narrator/Andrew); whisper now hears "this **is** my son", "the word **if**".
- **"proceedeth" mispronounced (wants pro-see-duhth)** → FIXED. j1 (Jesus/Eric)
  respelled `proceedeth`→`proceeduth` in `SPOKEN`; measured with
  check_pronunciation — "proceeduth" round-trips 100% back to "proceedeth" and
  lands the pro-SEE-duhth target. Caption still shows "proceedeth".

**New audio baseline (audio-immutability sanctioned re-voice — ONLY the two
complained segments changed; the other 20 mp3s are byte-identical, untouched):**

| seg | voice | old md5 | new md5 | old dur | new dur |
|---|---|---|---|---|---|
| n2 | narrator (AndrewNeural) | cbe712b38ed12326241f0978ac837913 | 9167d7ef38376b852737f14df29db716 | 18.437s | 19.891s |
| j1 | jesus (EricNeural)      | 1d777bf6cae1e447fe41dc56a6f8f17e | 730bc3aad189af17efee3925a532ef2a | 7.802s  | 8.928s  |

`SPOKEN = {"IS": "is", "IF": "if", "proceedeth": "proceeduth"}` in
`make_narration.py`. Same voices, same wording, same timing everywhere except
the two fixed segments (which run slightly longer — the runner recomputes the
timeline from the mp3s at assemble time, exactly as it does for a fresh build).
`v2_prompt.py build-70-temptations --check` still PASSES (42 beats). Board:
NEEDS-AUDIO → AUTHORED / Audio OK / Ready ✅, claim cleared.

---

## 🅿️ RUNNER PARK — A-auto Machine A, 2026-08-06 (AUDIO RE-VOICE, out of runner scope) — RESOLVED ABOVE

**Do NOT build this row until the narration is re-voiced.** The lowest-Ready
runner reached row 70 and stopped here on the LEARNING LAW.

**Open reviewer complaint (from `v2_outline.py 70`):**
> "The narrator spells out 'I-S' instead of pronouncing the word like it should.
> Also it mispronounced 'proceedeth' it should be pro-see-duhth"

**Why the runner cannot fix it.** The V2 pipeline ships **byte-identical V1
narration** (v2_assemble.py AUDIO LOCK assembles from the existing mp3s; nothing
is re-voiced or resynthesised). The two defects are baked into those mp3s:

1. `make_narration.py` segment **n2** narration source contains all-caps
   **"this IS my Son"** — the TTS reads the emphasis-caps token `IS` as the
   letters *I-S*. The build's local override dict is **`SPOKEN = {}` (empty)**,
   so nothing respells it. (The lowercase `if`/`is` in the same line are fine;
   only the caps `IS` breaks.)
2. Segment **j1** `"...every word that proceedeth out of the mouth of God."` has
   **no pronunciation override** for `proceedeth` → the voice mispronounces it.

Fixing either one requires **regenerating the narration mp3s** (add a build-local
`SPOKEN` / pronounce override: caps `IS`→`is` respell, `proceedeth`→a `pro-SEE-duhth`
respell, then re-run `make_narration.py` and re-hash the AUDIO LOCK). That is a
re-voice — outside the runner's allowed writes (art / QC / boards / log / review /
mp4 only) and the exact class that parked rows 50 and 51.

**Resume (author/audio track, NOT the runner):**
1. In `build-70-temptations/make_narration.py` add:
   `SPOKEN = {"IS": "is", "proceedeth": "pro-SEE-duhth"}` (tune the proceedeth
   respell against the voice with `mbm_pronounce.audit`; verify caps-IS is only in
   n2 — grep confirms it is).
2. Re-generate n2 + j1 (or the whole track), re-establish the AUDIO LOCK source,
   ear-check both segments (`I-S`→"is"; proceedeth = pro-SEE-duhth), set
   AUTHOR-BOARD Audio back to **OK** + Ready **✅**.
3. Runner then builds normally: `v2_prompt.py build-70-temptations --check` already
   PASSES (42 beats); art has not been generated yet, so no spend was wasted.

Nothing was generated and no credit was spent on row 70 this session.

## ⛔ RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-07) — proceedeth half is ORPHANED (row-50 class)
Runner (Machine A `Dev`) audited at claim time, $0, no stills. Cameron's OPEN
complaint has TWO parts; only ONE is actually fixed in the shipping audio:
- **"narrator spells I-S / IF"** — FIXED. Whisper on the shipping V1 mp4
  (`matt-4_the-temptations.mp4`) n2 window (44-64s) transcribes "if" and "is" as
  WORDS, not letters. (The 2026-07-28 REDO render already said them correctly.)
- **"proceedeth should be pro-see-duhth"** — NOT FIXED in the shipping audio.
  `beats_v2.py` has no `AUDIO_FROM_V1_SEGMENTS` (False) → v2_assemble copies the
  V1 mp4, which was committed 2026-07-28 (90401d7ac), BEFORE the respell
  `{"proceedeth":"proceeduth"}` was committed 2026-08-06 22:30 (baee4b41a). The
  fixed j1 lives only in the V2 build dir (which the assembler ignores). Proof:
  the mp4's j1 segment (64.45-72.4s) cross-correlates **0.757 with the OLD
  V1-dir j1.mp3** and **0.026 with the FIXED V2-dir j1.mp3**; durations 7.95s
  (mp4) ≈ 7.80s (old) vs 8.93s (fixed +1.1s). Building now ships the old
  "proceedeth" → repeats half the complaint (worst failure).

RESUME (audio authority — COUPLED timeline, model it on row 63's Siloam fix):
The respelled j1 already exists at
`media-production-v2/build-70-temptations/audio/j1.mp3` (8.928s, +1.083s vs old
7.802s). Copy it into `media-production/build-70-temptations/audio/j1.mp3`, set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py, remap the beats windows for the
+1.083s j1 shift (piecewise-linear on segment onsets, as row 63 did), re-run
`--check` + the AUDIO REBUILD gate (rebuilt total == extract_beats total), then
Ready ✅. Ear-check j1 says "pro-see-duhth". n2 "if/is" is already correct and
needs no change.
