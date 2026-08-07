# build-185-many-mansions-member — QC / runner handoff (John 14:1-3)

**AUTHORED 2026-08-07, Machine A `Dev` (Fable-5 author lane, $0).** 14-beat V2 map,
`v2_prompt.py --check` PASS (0 warnings), windows contiguous+monotonic 0.400→53.175
(=card_start), every segment onset in-window. **PARKED NEEDS-AUDIO — NOT Ready.** The
beat map is complete; the row is blocked ONLY on the Jesus-voice audio fix below.

---

## ✅ AUDIO FIX DONE 2026-08-07 (Machine A `Dev`, AUDIO-FIX lane, $0 Gemini)

**Cameron's complaint — *"Old.  That's not the chosen Jesus voice."* — CLOSED.**
The three Jesus red-letter segments were re-voiced through the CHOSEN ElevenLabs
Jesus voice **"Chris"** (`iP95p4xoKVk53GoZ742B`), the exact voice Cameron approved on
rows 50/51/70. Nothing else in the audio was touched — the narrator segments
(n0/n1/n2/n3a/n3b) are byte-identical to before; only jv1/j1/j2 changed.

| segment | text | OLD F0 (wrong) | NEW F0 (chosen Chris) | old sha256 → new sha256 |
|---|---|---|---|---|
| jv1 | "Let not your heart be troubled…" | ≈88.9 Hz | ≈110.3 Hz | `c6d0eb5b…` → `80ef010d…` |
| j1  | "In my Father's house are many mansions… I go to prepare a place for you." | ≈87.0 Hz | ≈105.3 Hz | `7bf19a0c…` → `4b3352cd…` |
| j2  | "And if I go and prepare a place for you, I will come again…" | ≈92.5 Hz | ≈117.6 Hz | `fde043a4…` → `720982ce…` |

Reference proof: a fresh "Chris" render and Cameron-approved row-70 Jesus both read
≈99–100 Hz on the same F0 script; the new 185 Jesus segments read 105–118 Hz — the
approved voice family. The old segments read 87–92 Hz (the wrong/stale voice).

**Mechanics:** rendered via canonical `mbm_eleven.render_segment(..., JESUS)`
(44100 Hz / 128 k, matching the rest of the row), then pitch-preserving
`atempo`-matched back to the ORIGINAL durations (jv1 5.329 s, j1 7.184 s, j2 9.691 s,
within one MP3 frame ≈26 ms) so **no window in beats_v2.py moves**. Captions are
byte-identical (SEGMENT text unchanged); the `.timing.json` sidecars were rescaled to
the matched tempo. `AUDIO_FROM_V1_SEGMENTS = True` set so the picture runner's
`v2_assemble` rebuilds the track from these corrected segments, never the stale
old-voice V1 mp4. Old-voice originals preserved in `audio-oldvoice-backup/`.

**Audio-immutability note:** the audio hash changed on purpose — a Cameron-ordered
re-voice is the sanctioned exception to the drift-protection law (PROMPT-AUDIO-FIX §4).

**Board:** NEEDS-AUDIO → AUTHORED / Ready ✅ (no V2 stills exist yet — this becomes a
picture-only build). The review card the runner ships MUST tell Cameron:
*"Jesus now speaks in the chosen voice — the same one you approved on the other videos."*

---

## COMPLAINT LEDGER (LEARNING LAW) — CLOSED ✅ (was: OPEN, blocked Ready)

**Complaint (now FIXED, see above):** *"Old.  That's not the chosen Jesus voice."*

**Diagnosis (this session, $0):** VALID. The Jesus segments jv1/j1/j2 were rendered
via ElevenLabs (audio-eleven.log) but are **NOT the chosen Jesus voice**. Acoustic
proof (median fundamental frequency, 16 kHz autocorrelation over voiced frames):

| segment | median F0 |
|---|---|
| 185 jv1 (Jesus) | ≈ 93.6 Hz |
| 185 j1 (Jesus) | ≈ 87.7 Hz |
| **70 j1 (Jesus — Cameron-APPROVED chosen voice)** | **≈ 108.1 Hz** |
| 185 n0 (narrator) | ≈ 104.6 Hz |
| 70 narrator | ≈ 103.9 Hz |

The NARRATOR matches the approved build almost exactly (104.6 vs 103.9 Hz), so the
method is sound and the narrator is fine — it is specifically the **JESUS voice** that
is ~15-20 Hz too low/wrong. `mbm_speakers.py` still shows the stale edge-tts EricNeural
trap (the row-70 lesson: migrated builds keep the stale config).

**This session could NOT fix it:** no `ELEVENLABS_API_KEY` in the environment, and a
blind re-voice would be wrong. Handed to the AUDIO LANE.

## 🅿️ AUDIO LANE — do this FIRST (then the row becomes a picture build)

1. Re-voice **jv1, j1, j2** ONLY, through the SAME chosen ElevenLabs Jesus voice as the
   APPROVED row 70 (board note: ElevenLabs JESUS "Chris", 44100/128k) — the same voice
   the rows 50/51/70 audio fixes used. Keep the captions byte-identical.
2. `atempo`-match each re-voiced segment to its ORIGINAL duration (jv1 5.329 s, j1
   7.184 s, j2 9.691 s) so NO window in beats_v2.py moves.
3. Place them in the V1 dir `audio/` and set `AUDIO_FROM_V1_SEGMENTS = True` in
   beats_v2.py so `v2_assemble.py` rebuilds the shipped track from the corrected
   segments (not a stale stream-copy of the old-voice mp4).
4. Verify: the re-voiced Jesus F0 should land near the approved ~108 Hz, and the
   rebuild total == extract_beats total (delta 0.0). Then flip the board to **Ready ✅**.
5. The review card MUST tell Cameron: *"Jesus now speaks in the chosen voice — the same
   one you approved on the other videos."*

## 🅿️ PICTURE RUNNER — after the audio is corrected (do NOT build before)

1. **Places — promote-first (lesson 11):**
   - `FATHERS-HOUSE` → generate **b05** (establishing wide, NON-Jesus) first, QC it,
     `--promote build-185-many-mansions-member FATHERS-HOUSE <b05 frame>`, then b08, b14.
   - `ROOM` → this is the row-89/170 upper room; row 89 shipped it TEXT-ONLY. Promote a
     ROOM plate only from a NON-Jesus frame if you make one — NEVER from a Jesus-bearing
     frame (b01 has Jesus). Text-lock is acceptable (matches row 89).
2. **Jesus:** he speaks (jv1/j1/j2 RED) — Jesus appears on 12 beats (all but b05/b08).
   The assembler injects JESUS LOCK v5 + master REF (jesus=True, ref=True). ONE locked
   face, cream-only, NO halo/glow/rim-light. Run `jesus_face_gate.py --dir
   build-185-many-mansions-member` (exit 0) before any credit. Red-letter stays on
   Jesus's face — the "many mansions/Father's house" imagery lives on the narrator
   beats b05/b08 only.
3. **FATHERS-HOUSE content-care:** a welcoming HOME of many warm-lit dwellings — NO God
   or Father figure, NO throne, NO divine being. It is a home, not a judgment court.
4. **Face/scale board (lessons 2/10/14):** ONE Jesus face across all his beats;
   DISCIPLES are distinct men, none in cream, ordinary-sized on the cushions.
5. **Assemble** (AUDIO LOCK on the corrected audio must pass), verify captioned length
   ≈ card_start (53.175) + card, realistic-only (Law 14) on all 14, decodes 0 errors.
   Ship with the complaint-answer card.

## Coverage / windows
14 beats, ~3.8 s/pic. Contiguous window starts: b01 0.400 · b02 6.752 · b03 10.200 ·
b04 13.559 · b05 17.260 · b06 19.811 · b07 24.790 · b08 28.481 · b09 30.430 ·
b10 35.399 · b11 39.000 · b12 43.000 · b13 46.596 · b14 49.701 · (hold to card 53.175).
Arc (Last Supper night): Jesus comforts them → "let not your heart be troubled / believe
in me" → going but not leaving them → the Father's house being made ready → "many
mansions / I go to prepare a place" → a house with room for everyone → he said it
plainly → "I will come again and receive you unto myself / where I am ye may be also" →
no far-off maybe → he'll come back and carry them home himself.
