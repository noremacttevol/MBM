# build-182-spirit-returns-to-god — QC / runner handoff (Ecclesiastes 12:1,7)

**AUTHORED 2026-08-07, Machine A `Dev` (Fable-5 author lane, $0).** 16-beat V2 map,
`v2_prompt.py --check` PASS (0 warnings), windows contiguous+monotonic 0.400→65.378
(=card_start), every segment onset in-window, audio OK. Picture-only rebuild — do
NOT re-voice.

---

## COMPLAINT LEDGER (LEARNING LAW)

**No open Cameron complaint on file** (`v2_outline.py 182` shows none). Nothing to
re-open; nothing to close. Built to the full rubric (all 15 lessons) and the laws
below.

**Review card:** a plain, gentle summary is fine — e.g. *"Solomon's honest word on
the end of life, and the promise that the spirit returns to the God who gave it —
with mercy, not anger."*

---

## 🅿️ RUNNER — do this (picture-only build on the locked audio)

1. **Audio:** default AUDIO LOCK stream-copy (board Audio = OK). No re-voice, no flag.
2. **Places are ALL NEW — promote-first (lesson 11):**
   - `SOLOMON-CHAMBER` → generate **b01** (establishing wide of the chamber) first,
     QC it, `--promote build-182-spirit-returns-to-god SOLOMON-CHAMBER <b01 frame>`,
     then b08 with the plate.
   - `ELDER-EVENING` → generate **b02** (establishing wide of the elder's home) first,
     QC it, `--promote ... ELDER-EVENING <b02 frame>`, then b04, b06, b09, b11, b16.
   - `YOUTH-MORNING` → generate **b03** (establishing wide of the morning hillside)
     first, QC it, `--promote ... YOUTH-MORNING <b03 frame>`, then b05, b07.
   - `RETURN-LIGHT` → generate **b10** (opening heaven, NO figure) first, QC it,
     `--promote ... RETURN-LIGHT <b10 frame>`, then b12, b13, b14, b15.
3. **SPEAKER LAW — SCRIPTURE, not red-letter, not God-voice.** Only s0 (b03/b04) and
   s1 (b09/b10) are scripture → **light-blue** captions; every other beat is the
   NARRATOR → **white**. There is NO red-letter and NO GREEN God-voice in this row —
   the narration frames the verses as Solomon's *written* words ("wrote", "he says").
   NO Jesus and NO cream anywhere (OT wisdom).
4. **HARD GATE — GOD IS NEVER EMBODIED (default gate).** On every RETURN-LIGHT beat
   (b10, b12, b13, b14, b15) God/the Giver is NOT shown: no figure, face, hand,
   throne or beam-being. Drift-word gate bans halo/glow/rim-light — the light is
   radiant / luminous / brilliant / warm in the SKY, never a ring around a head.
5. **THE SPIRIT IS WARM LIGHT, NOT A GHOST.** The returning spirit (b10, b12, b14,
   b15) is a gentle rising veil of warm luminous light — NEVER a translucent person,
   mist-figure, floating body or ghost (rows 171/172). If a reroll produces a
   ghost-shape, reject it.
6. **CONTENT-CARE — death by RESTRAINT.** The old man's passing (b02, b09, b11, b16)
   is peaceful sleep, dignified and warm — NEVER a corpse pallor, grey death, wound,
   sore, decay, skeleton, bones or gore, and no fear/torment on the face. b16 must
   read as *rest, not terror* (warm merciful light on a serene face).
7. **Face / scale / beard board (lessons 2/10/13/14):** three separate people —
   SOLOMON (aged king, grey-white beard, indigo/wine robe), YOUTH (~18, smooth young
   face, earth-toned tunic), ELDER (~78, white hair/beard, humble earth-brown robe).
   Keep each the SAME person and the SAME age across their frames (SOLOMON and ELDER
   are DIFFERENT aged men — do not blur them); identity-edit drift, recheck the whole
   frame. All ordinary-sized, one ground plane.
8. **Time of day (intentional 3 registers):** SOLOMON + ELDER = long warm GOLD
   evening; YOUTH = fresh clear MORNING; RETURN = warm radiant break of light high in
   the heaven. No flat ordinary sunset that reads as mere scenery (row-11 caution).
9. **Assemble** with `v2_assemble.py` (AUDIO LOCK stream-copy must pass), verify
   captioned length ≈ card_start (65.378) + card, decodes 0 errors, realistic-only
   (Law 14) on all 16. Ship to the reviewer.

## Coverage / windows
16 beats, ~4.0 s/pic. Contiguous window starts: b01 0.400 · b02 3.120 · b03 7.965 ·
b04 12.500 · b05 18.196 · b06 24.800 · b07 29.780 · b08 33.577 · b09 38.560 ·
b10 41.800 · b11 45.530 · b12 48.160 · b13 51.842 · b14 53.970 · b15 57.841 ·
b16 62.982 · (hold to card_start 65.378).
Arc: Solomon writing of life's end → the body grown old → remember thy Creator in
youth → the joyless evil days → remember while young / don't wait → he points where
the breath goes → dust returns to the earth → the spirit returns to God (rising warm
light) → body to the ground / spirit home to Him → death is not the end / the quiet
return → the Giver receives it → with mercy, not anger (peace on the elder's face).

---

## ✅ RUNNER SHIPPED (2026-08-24, Machine A `Dev`, Claude session)

Fresh build: YOUTH + ELDER portraits + all 16 stills, **6 rerolls = 37.5% —
WELL OVER the 15% budget; honest ledger (all law-class ship-blockers):**
- b01 ×2: rendered as a PAINTING twice (law 14 — realistic-only). Scene-level
  "shot as a real photograph" wording was not enough; the fix that worked was
  moving the photographic demand into the **SOLOMON-CHAMBER LOCK** so every
  frame of that place inherits it (real skin pores, woven fibres, lamp falloff,
  sensor grain, shallow DOF; never painting/illustration/gallery religious art).
  **Lesson for the next session: a lamplit-ancient-king interior pulls classical
  illustration style — put the photo demand in the PLACE LOCK, not the scene.**
- b04: ELDER-EVENING plate cloned b02's seated-in-doorway wide (0.941, law 12m)
  → close eye-level portrait, corr 0.085.
- b12/b14/b15: the RETURN-LIGHT plate collapsed FOUR sky beats into one picture
  (0.928-0.982) → re-authored to four genuinely different treatments (horizon
  cloud-break kept on b10, steep vertical light-column b12, abstract close of
  light-meeting-light b14, high-key opening heaven b15). Encoded max now 0.814.
- One unterminated-string syntax error from my own edit caught immediately by
  `--check` (0 wasted gens) and fixed.
Cost $3.22 total — still under the $6.10 average despite the reroll count.

**FULL-CUT GATE — 16 beats + card viewed on the ENCODED mp4: PASS.** SPEAKER
LAW: s0/s1 LIGHT-BLUE (Solomon's WRITTEN words — b03/b04, b09/b10); narrator
white; NO red, NO green (no Jesus, no God-voice), no cream anywhere. **GOD NEVER
EMBODIED** — every RETURN-LIGHT beat is light alone, no figure/face/hand/throne,
source unseen. CONTENT-CARE held: the old man's passing is peaceful covered
sleep in warm light — no corpse pallor, grey, wounds or gore; the spirit is warm
rising LIGHT, never a ghost or translucent person. Three time registers read at
a glance (Solomon/elder gold evening, youth clear morning, return radiant
heaven). Photographic throughout after the b01 fix. Card clean.

**AUDIO:** guard fix `AUDIO_FROM_V1_SEGMENTS` (V1 73.967s vs extract 71.728s,
gap placement; 10 ElevenLabs mp3s) — **AUDIO REBUILD PASS SHA256=b7fe5553df…**,
71.7s, 20.1 MB.
