# QC / RUNNER HANDOFF — build-173-dead-shall-hear

Row 173 · John 5:25-29 ("the dead shall hear the voice of the Son of God...
and they that hear shall live... all that are in the graves shall hear his
voice, and shall come forth"). RESTORATION shelf. Authored fresh 2026-08-07
(Machine A `Dev`, Fable-5 author lane, $0).

## COMPLAINT LEDGER
- **OPEN complaint (audio): "Mispronounced live at the end."** — ALREADY FIXED
  AT SOURCE, verified. The homograph "live" (the VERB /liv/, rhymes with give)
  was rendered as the adjective (/lyv/, rhymes with hive) on the closing narrator
  line n2b "To hear him is to live." SPOKEN = {"live": "liv"} is authored in BOTH
  make_narration.py files (V1 dir + V2 dir; Cameron denial #173, 2026-07-22),
  covering every "live" in the build (j1c "shall live", n2b "to live", card
  "and live") — all the verb; the note records it round-trips back as "live" 2/2
  in Eric and Andrew. **Unlike rows 50/51 this is NOT an orphaned fix:** the
  authoritative V1 mp4 (`media-production/build-173-dead-shall-hear/
  john-5_dead-shall-hear.mp4`) was RE-RENDERED 2026-07-29 — AFTER the fix — so the
  delivered audio already carries "liv" (V1 mp4 + V1 segment mp3s both dated
  2026-07-29 09:47, after the 07-22 fix).
  - **RUNNER: do NOT re-voice.** Assemble on the fixed V1 audio (default path;
    `AUDIO_FROM_V1_SEGMENTS` intentionally left unset). The beats.json timing that
    the captions/windows use was extracted from the same fixed V1 segments, so the
    windows already line up.
  - **RUNNER: the review card MUST tell Cameron the ending "live" pronunciation
    was fixed** (LEARNING LAW — the card must say his complaint was addressed).

## SPEAKER LAW (verified)
John's gospel, Jesus in the flesh → RED-LETTER. j1a/j1b/j1c (John 5:25, one
sentence cut three ways for pacing) and j2 (John 5:28-29) are RED captions, and
every red beat pictures JESUS on his own words (row-39 law). Narrator beats are
WHITE; b01/b03/b07 also picture Jesus because they describe him (not a
misattribution). `jesus=True`+`ref=True` on b01,b03,b04,b05,b06,b07,b08,b09; the
shared JESUS lock + JESUS-MASTER-REF inject automatically (confirmed in
ASSEMBLED-PROMPTS.txt). Only Jesus wears cream.

## CONTENT-CARE — the DEAD + the general resurrection (gates before any credit)
The resurrection ground (b10-b13, "come forth" / "every grave will open") is the
general resurrection shown as **DIGNITY and LIFE**: whole, healthy, FULLY-CLOTHED,
living people rising and standing in the dawn light. **NEVER** a corpse, skeleton,
skull, bone, rotting or bandaged flesh, a figure clawing out of the earth, a pit
of bones, gore, or any ghost/mist (row-171 lesson: the grave loses its grip is
DAWN LIGHT, not the walking dead). Graves are plain rock tombs opening to warm
light. No halo/glow/rim-light on anyone.

## Places
- **TEMPLE-COURT** (shared) — Jesus's discourse to the crowd (b01-b09). Plate
  already wired from build-39-pharisee-publican (`PLACE-REF/temple-court.jpeg`,
  committed). No prose architecture needed; scene text is action + light only.
- **RESURRECTION-GROUND** (NEW build-local) — the burial hillside at first light
  (b10-b13).

## 🅿️ RUNNER — build steps (paid image lane)
1. **Generate b10 first** (the RESURRECTION-GROUND establishing wide). QC it hard
   against the content-care bans above (whole living people, NO corpses/bones/
   zombies/gore, dawn light, realistic). Then promote it as the plate:
   `python3 media-production-v2/v2_stash.py --promote build-173-dead-shall-hear RESURRECTION-GROUND build-173-dead-shall-hear/assets/s10-all-of-them.jpeg`
   Re-run `v2_stash.py --wire build-173-dead-shall-hear`, then `--check` (PASS)
   and `--dump`.
2. Generate the TEMPLE-COURT beats (b01-b09) against the wired temple-court plate,
   and the remaining RESURRECTION-GROUND beats (b11-b13) against the promoted plate.
3. **Gates:** `jesus_face_gate.py --dir build-173-dead-shall-hear` must exit 0
   (b01,b03,b04,b05,b06,b07,b08,b09). Content-care sweep every resurrection frame
   for the horror-imagery bans. Scale gate: everyone ordinary-sized (no giant
   Jesus). Face-board: Jesus identical across all his beats.
4. Assemble on the FIXED V1 audio (see COMPLAINT LEDGER — do NOT re-voice).
   Re-audit, then ship with a card that states the "live" pronunciation is fixed.

## Coverage / windows (authored, verified)
13 beats, windows contiguous 0.400 → 58.851 (= card_start), monotonic, each
segment's speech onset inside its window. ~4.5 s/picture. `--check` v4 PASS.

## 🅿️ RUNNER PARK → NEEDS-REBUILD (author-lane) — 2026-08-13, Opus runner, Machine A `Dev`
**All 14 images generated + QC-clean (0 rerolls, $1.88); the row is BLOCKED at
assembly by an authored-timeline / card-window conflict the runner may not fix
(editing beat windows is out of runner scope).**

### What is generated and good (reuse — do NOT regenerate)
- All 13 stills in `assets/` PASS Light QC + FULL-CUT GATE (viewed per-frame in
  the rendered mp4): Jesus one consistent V2 face (green/hazel), cream-only, no
  halo, realistic, correct scale/anatomy on all 8 temple-court discourse beats;
  the 4 RESURRECTION-GROUND beats (b10-b13) are content-care-clean — whole,
  fully-clothed, LIVING people in warm dawn light, ZERO corpses/bones/zombies/
  ghosts/gore. TEMPLE-COURT plate = author's committed build-39 frame (restored
  after `--wire` wrongly re-pointed it to a build-96 crucifixion frame; see note
  below). RESURRECTION-GROUND plate promoted from the v2_story_cast portrait and
  wired. STASH-scan NOT yet run (park before ship).

### The blocker (measured)
- The closing card narration ("He speaks, and death loses its grip. Lean in and
  listen — and live.") is **6.863 s** (`data['card']['seg_dur']`), but the
  authored card window is only **2.744 s** (58.851 → 61.595). `extract_beats`
  therefore fits the full card audio by setting **card_start = total − card_dur =
  61.595 − 6.863 = 54.732 s**.
- `v2_assemble` builds the still chunks from the beats_v2 window `start`s but caps
  the last chunk at `card_start` (54.732). **b13's authored window is
  55.650 → 58.851 — entirely AFTER 54.732**, so b13 gets a negative duration and
  is DROPPED (concat_base has only 12 clips, c000-c011; base.mp4 = 55.667 s). The
  s13 close-up "to hear him is to live" never appears in the video; b12/card ride
  the tail. **A dropped authored beat fails the FULL-CUT GATE → not shipped.**
- The QC.md premise above ("assemble on the V1 mp4, windows already line up") is
  false: the beats_v2 timeline is **61.595 s** but the shipped V1 mp4 is a stale
  **59.396 s** (`ffprobe`), so the default path also trips AUDIO LOCK
  (61.595 vs 59.396). The V1 SEGMENT mp3s (2026-07-29 09:47, carry the "live"→liv
  fix) are correct; `AUDIO_FROM_V1_SEGMENTS = True` is already set and rebuilds a
  correct, coherent 61.595 s track (AUDIO REBUILD PASS 22299b65, no overlap) — the
  AUDIO is fine. Only the VIDEO timeline needs reconciliation.

### Author-lane fix (one of)
1. The card narration is long enough to be a VOICEOVER over the last resurrection
   beats: keep the pictures running their full windows to 58.851 and make the card
   VISUAL short (~2.744 s tail) with the card AUDIO starting earlier (≈54.732) as
   a voiceover — this needs `extract_beats`/assembler support for a card whose
   on-screen duration ≠ its audio duration (NOT a runner edit).
2. OR shorten/trim the card narration so `card_dur ≤ 2.744 s` (card fits its
   authored 58.851→61.595 window; b13 then renders).
3. OR re-window the last beats so all 13 picture windows end at the real
   card_start (54.732) — i.e. re-author b10-b13 windows against the actual audio.
Any of these is a beat/timeline authoring change (Fable-5 author lane), then the
runner re-assembles (AUDIO_FROM_V1_SEGMENTS stays True), FULL-CUT-gates, ships.

### RESUME (after the author fix)
```
cd media-production-v2
python3 v2_prompt.py build-173-dead-shall-hear --check          # must PASS
python3 v2_assemble.py 173                                        # expect 13 clips, AUDIO REBUILD PASS
# FULL-CUT GATE: ffmpeg-extract every beat incl. s13 from the mp4, view all
# then ship (two commits) + firebase deploy + live-verify per PROMPT-OPUS-RUNNER §7
```
Stills are stashed/reusable, so the re-assemble is $0. Note: `--wire` will
re-point TEMPLE-COURT to a wrong build-96 frame — PLACE-WIRING.json is now pinned
`manual:true` to build-39; do NOT re-run `--wire` on this build without
re-restoring `PLACE-REF/temple-court.jpeg` from git.
