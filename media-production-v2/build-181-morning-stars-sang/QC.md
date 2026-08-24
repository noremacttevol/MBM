# build-181-morning-stars-sang — QC / runner handoff (Job 38:4-7)

**AUTHORED 2026-08-07, Machine A `Dev` (Fable-5 author lane, $0).** 14-beat V2 map,
`v2_prompt.py --check` PASS, windows contiguous+monotonic 0.400→59.869 (=card_start),
onsets in-window, audio OK. Picture-only rebuild — do NOT re-voice.

---

## COMPLAINT LEDGER (LEARNING LAW)

**OPEN complaint:** *"the pictures need to be better made i dont think they fit the
story well."*

**What in this cut fixes it:** every beat is remapped to depict the EXACT narrated
moment, and the two threads are kept visibly distinct so nothing reads as a generic
"Bible sky":
- **JOB thread** (b01, b02, b06, b07, b08, b14): a clear, specific suffering man on
  the ash-heap — questioning → humbled → silent → lifting his eyes off his wreckage →
  comforted. Not a vague figure.
- **CREATION thread** (b03-b05, b09-b13): a clear first-morning cosmos — the forming
  earth, foundations laid, the sky breaking into brilliance, the morning stars
  singing, the host rejoicing, creation as celebration. Not a generic starfield.
- The two never blur: Job is always on his desolate ground in grey storm-dawn light;
  the vision is always the blazing first-light creation.

**Review card MUST tell Cameron:** *"The pictures were rebuilt so each one fits its
exact moment of the story — Job on the ash-heap and the singing first-morning
creation, kept clearly distinct."*

---

## 🅿️ RUNNER — do this (picture-only build on the locked audio)

1. **Audio:** default AUDIO LOCK stream-copy (board Audio = OK). No re-voice.
2. **Places are NEW — promote-first (lesson 11):**
   - `JOB-WHIRLWIND` → generate **b02** (Job small in the whirlwind) first, QC it,
     `--promote build-181-morning-stars-sang JOB-WHIRLWIND <b02 frame>`, then the rest
     of the Job beats (b01, b06, b07, b08, b14) with the plate.
   - `CREATION-DAWN` → generate **b03** (forming earth, NO figure) first, QC it,
     `--promote ... CREATION-DAWN <b03 frame>`, then b04/b05/b09-b13 with the plate.
   - **IGNORE the `--wire` "NEW PLACE" suggestion for `HEAVENLY-HOST`** — it is a
     sky/host text lock, NOT a location. Do not promote a place plate for it.
3. **HARD GATE — GOD IS NEVER EMBODIED (default gate).** GOD-voice beats (g4 b04/b05,
   s1 b10/b11 → GREEN captions) show NO figure/face/hand/beam of God; the voice is the
   whirlwind + the vision. Drift-word gate bans halo/glow/rim-light — the light is
   radiant/brilliant/blazing in the SKY, never a ring around a head.
4. **The "sons of God" (b11):** a DISTANT, small, reverent joyful host of radiant
   light high in the sky — NO detailed faces, NO cherub-with-halo kitsch, and the
   Father is NEVER among them.
5. **Restraint on Job:** weariness and grief only — NO open sores/wounds/lesions in
   close-up (parent test).
6. **Face/scale board (lessons 2/10/14):** JOB is the SAME ~60yo grey-bearded man in
   all his frames; identity-edit drift, recheck the whole frame.
7. **Captions:** g4 (b04/b05) and s1 (b10/b11) render **GREEN**; everything else white
   (no red-letter, no Jesus, OT row). Assemble (AUDIO REBUILD/LOCK must pass), verify
   captioned length ≈ card_start (59.869). Ship.

## Inherited caption/audio desync (do NOT fix — audio locked)
- **n1r** delivered audio opens with a recap line ("Where were you, God asked him,
  when I laid the foundations of the earth.") ahead of the caption's "Tell me, if you
  know." b06 pictures Job humbled under that question, so it reads true.

## Coverage / windows
14 beats, ~4.3 s/pic. Contiguous window starts: b01 0.400 · b02 2.242 · b03 8.641 ·
b04 12.082 · b05 15.402 · b06 20.439 · b07 24.177 · b08 25.547 · b09 36.113 ·
b10 40.428 · b11 43.500 · b12 47.487 · b13 49.542 · b14 54.638 · (hold to card 59.869).
Arc: wreckage → the whirlwind's summons → creation's foundations → Job's eyes lifted →
the singing heavens → comfort home to Job. Whirlwind = grey storm-dawn; vision =
blazing first light; close = warm dawn on Job (no ordinary sunset).

---

## ✅ SHIPPED — Opus runner RESUME (2026-08-13, Machine A `Dev`, unattended/headless)

Prior autopilot session generated all 14 stills + both promoted place plates
($ spent that session) then DIED before assembly (State RUNNING, Claim A-auto).
This session RESUMED per the strand-rescue instruction: already-shipped check first
(no committed mp4; live card v181 still carried the OLD V1 hash `1ac7c026`,
data-built 2026-07-28 — NOT shipped), then finished assembly → gate → ship.

**COMPLAINT LEDGER (LEARNING LAW):**
- OPEN complaint *"the pictures need to be better made i dont think they fit the
  story well."* → **FIXED.** Every beat depicts its exact narrated moment and the
  two threads stay visibly distinct: JOB on the ash-heap (grey storm-dawn: b01
  questioning, b02/b06/b07 humbled+silent, b08 eyes lifted, b14 comforted in warm
  dawn) vs the CREATION vision (blazing first-light cosmos: b03 forming earth,
  b04/b05 foundations, b09 astonishing sky, b10 morning stars, b11 the radiant
  host, b12/b13 stars in song). No generic "Bible sky" stand-ins; Job is one clear
  suffering man throughout. FULL-CUT GATE viewed every rendered frame to confirm.

**AUDIO (assembler-prescribed fix, no re-voice):** default stream-copy tripped the
STALE-V1 guard — the V1 final mp4 runs 67.433s vs the current segment timeline
66.612s (0.821s stale trailing take). Per the assembler's own instruction added
`AUDIO_FROM_V1_SEGMENTS = True`; the track is rebuilt from THIS build's own
ElevenLabs mp3s (audio/*.mp3 = 44100/128000, byte-identical voices to the V1 final,
signature-verified) at the extract_beats offsets. Nothing re-voiced, nothing
re-timed; V1 stays read-only. **AUDIO REBUILD PASS SHA256=7fcd95be2774fa8d…**,
66.6s, 20.0MB. Drop-check: concat_base = 14 clips = 14 beats (row-173 lesson), b14
window 54.638 < card_start 59.869 (no dropped beat).

**FULL-CUT GATE (§6b) on the RENDERED mp4 — 14/14 beats + card PASS:** Job one
consistent grey-bearded ~60 man in torn dark sackcloth on the ash-heap (potsherds
correct), NO open sores (restraint held); creation vision figureless with GOD NEVER
EMBODIED, no halo/glow/rim-light, no cherub kitsch; s11 "sons of God" = distant
small radiant host, no faces, Father absent. Realistic biblical photography
throughout (Law 14), no cartoon/mix, no modern objects, anatomy/scale/beards clean.
SPEAKER LAW pixel-verified: GREEN only on God's exact words (g4 b04/b05, s1 b10/b11
= RGB ~95,219,141); WHITE narrator everywhere else (b06 n1r recap = RGB 242,241,240,
narrator not God); no red (OT, no Jesus). Card clean, no typo squares; captions
bottom-band only.

**Cost this session:** $0 (all frames pre-generated by the died session; resume was
assembly + gate + ship only). Under the $6.10 average — COST LAW downward trend holds.

---

## ✅ C-FIX SHIPPED — complaint fix verified + shipped (2026-08-24, Machine A `Dev`, Claude session resuming the 2026-08-17 offline claim)

**COMPLAINT LEDGER (LEARNING LAW):** open complaint *"0:12 god mispronounced wast
and pictures can't be duplicates with just missing pieces. Make better pictures."*

1. **"wast" pronunciation (0:12) → FIXED at the SOURCE CONTROL (law 12i).**
   g4 is re-voiced through `revoice_wast.py`: ElevenLabs **eleven_flash_v2**
   (supports phoneme tags) with explicit CMU `W AO1 S T` (/wɔst/, rhymes with
   "lost") in the locked Bill God-voice; visible KJV caption spelling unchanged;
   duration-locked to the authoritative V1 segment so no window moved.
   `make_narration.py` (V1 + V2) now routes g4 through this script permanently —
   a plain re-render can never regress it. **Verified in the ENCODED mp4:**
   faster-whisper hears "Where wasst thou…" at 12.24s; LPC formants on the vowel
   F1≈280/F2≈826 Hz = back rounded vowel (a wrong "waste" /eɪ/ would sit F2≈1800+).
2. **Duplicate pictures → FIXED per law 12m (born from this row).** All 14 beats
   re-authored with a SHOT-DIVERSITY lock (each beat's camera geometry unique,
   place plate locks the world not the camera) and regenerated 2026-08-17
   (16 gens / 14 beats = 2 rerolls, 14%, under the 15% budget, $2.14).
   **Verified in the ENCODED mp4:** full contact sheet inspected by eye (14 beats
   + card) — every composition genuinely different (the two Job-whirlwind frames
   b02/b14 differ in angle, light and mood); 64×36 grayscale similarity matrix max
   pairwise correlation **0.652** (b02/b14) — no pair near duplicate territory,
   no suspicious pairs to escalate.

**Gates on the rendered cut:** 66.733s / 19,953,453 B. SPEAKER LAW — GREEN only on
God's exact words (g4 b04/b05, s1 b10/b11), narrator recap b06 stays WHITE, no red
(OT, no Jesus). GOD NEVER EMBODIED (whirlwind + light only); sons-of-God host
distant, no faces; realistic photography throughout, captions bottom-band, card
clean. Cost this session: $0 new spend (all work banked by the 08-17 claim;
this session verified + shipped only).
