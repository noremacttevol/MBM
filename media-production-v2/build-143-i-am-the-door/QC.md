## ✅ SHIPPED — REALISTIC V2 (2026-08-13, Machine A `Dev`, Opus runner, unattended/headless)

**RESUMED a died-mid-build RUNNING row** (State RUNNING, Claim A-auto): 7 stills (s01–s07)
already existed from the crashed session; portraits/plates already committed (SHEPHERD ref +
FOLD plate present). Ran RUNNER-LESSONS already-shipped check FIRST — no committed mp4, no
segs, card was the old V1 2026-07-29 hash with NO `realistic-v2` wave → genuinely unbuilt →
resumed. `v2_prompt --check` PASS, approvals `approved:false`/`complaint:null`, `v2_outline 143`
shows NO open complaints.

- **COMPLAINT LEDGER: none open.** (`v2_outline.py 143` shows no complaints; `.approvals.json`
  complaint:null.) Nothing to regress.
- **Generated the 3 remaining beats** (b08/b09/b10) at $0.40, ceiling $729, meter $703.37→$704.04.
  Passing frames s01–s07 never re-pulled (COST LAW). **0 rerolls (0% of 10 beats).**
- **Light QC (source):** 10/10 clean. **FULL-CUT GATE 6b (rendered mp4):** extracted one
  mid-window frame per beat + 2 card frames, viewed EVERY one → **10/10 beats + card CLEAN.**
  - Jesus b03/b07: cream ONLY on Jesus, locked face, no halo/glow/rim-light, ordinary scale;
    RED KJV captions exact (John 10:7 b03 "Verily, verily… I am the door of the sheep";
    John 10:9 b07 "by me if any man enter in, he shall be saved, and shall go in and out").
  - SHEPHERD consistent (brown robe, dark beard, ~mid-30s Middle Eastern) across every fold beat.
  - **Gap law held:** open gap in every fold frame, NO gate/bars; b07 Jesus stands framed in the
    opening (the claim embodied); b10 shepherd lies across the opening under stars.
  - Wall-climber b04 non-violent over the FAR wall (no attack/struggle, lit opening avoided).
    Directions correct: flock IN at dusk (b06), OUT at bright morning to green pasture (b08).
  - Realistic-only (Law 14, no cartoon/mix), no modern objects, anatomy/hands clean. Captions
    bottom-band only (narrator WHITE / Jesus KJV RED); reflection card clean serif, no typo-squares.
  - Audio 63.156s ≈ video 63.167s, no ≥1.2s dead tail. concat_base = 10 clips = 10 beats (no
    dropped beat). AUDIO REBUILD PASS (rebuilt from 7 V1 segment mp3s, `AUDIO_FROM_V1_SEGMENTS=True`).
- **Outcome:** shipped `john-10_i-am-the-door.mp4` 19.0 MB / 63.2s. Board → BUILT. Appr stays ⬜.

---

## ✅ AUDIO-FIX DONE → AUTHORED / Audio OK / Ready (2026-08-11, Machine A `Dev`, audio lane)

STALE-V1 class, resolved at **$0, zero Gemini, zero re-voice** — no stills exist
yet, so this hands back to the picture runner (prompt step 5, "no V2 stills" case).

- **Voice-ID:** all segments are 44100 Hz / 128 kbps / mono = ElevenLabs new-voice
  spec (edge-tts would be 24000/48k). NOT the dead old edge-tts — no re-voice.
- **Fix:** `AUDIO_FROM_V1_SEGMENTS = True` added to `beats_v2.py` (timeline 63.16s vs stale 66.15s render, gap 3.00s). When the
  picture runner assembles, the track rebuilds from the segment mp3s instead of the
  stale V1 render, so `v2_assemble.py 143` passes the audio lock.
- **Board:** NEEDS-AUDIO → **AUTHORED / Audio OK / Ready ✅**, claim cleared.

---

## 🅿️ RUNNER $0 PRE-FLIGHT PARK → NEEDS-AUDIO (2026-08-11, Machine A `Dev`, Opus runner)

**Parked at $0 BEFORE any still was generated (row-141 lesson: pre-flight the AUDIO
LOCK even when the board says Audio OK).** This row is STALE-V1: the current V2
audio segments no longer match the old V1 render.

- extract_beats timeline (current `audio/*.mp3` segments) = **63.156s**
- authoritative V1 final mp4 = **66.153s** → gap **2.997s** (past the 0.75s guard); `AUDIO_FROM_V1_SEGMENTS` is NOT set.
- 7 segments, spec 44100/128000/mono = the new-voice ElevenLabs cast spec (Brian narrator / Chris Jesus) — so a re-voice is probably NOT needed, only the flag.

**AUDIO LANE — RESUME (row-200/118/22 template, expected $0/no re-voice):**
1. Voice-ID the segments to confirm they are the new ElevenLabs cast (not old edge-tts); re-voice ONLY any wrong seg first.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `build-143-i-am-the-door/beats_v2.py`.
3. Hand back to the picture runner: `v2_prompt.py build-143-i-am-the-door --check` (PASS) → generate the beats → `v2_assemble.py 143` must print **AUDIO REBUILD PASS** (~63.2s) → FULL-CUT GATE → ship + deploy + live-verify.

The runner does NOT set the flag itself (beats_v2.py is off the runner's allowed-write
list; the runner-prompt step 6 says an AUDIO-LOCK failure = stop the row, log, do not ship).

---

# QC / RUNNER HANDOFF — build-143-i-am-the-door (John 10:1-9)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~55 s. Third I AM row.

## The shepherd IS build-21's shepherd (new cross-video identity)

SHEPHERD lock copied byte-identical from build-21 (lost-sheep) plus
a same-man clause — ONE parable shepherd across both rows. The FOLD
plate (build-21 b12) was ACCEPTED for exactly this reason: the frame
IS the row's picture (gateless gap, shepherd standing in it, flock,
dusk) and the man in it is now this row's locked character.
Face-board 143's shepherd against build-21's frames.

## The gap law

Exactly ONE opening, NO gate, NO bars, ever — the open gap is the
doctrine. A rendered gate is an automatic reject. b07: JESUS himself
stands framed in the gap (the only jesus-in-fold frame — the claim
embodied). b10: the shepherd LYING ACROSS the opening under stars.

## The wall-climber (b04, row-126 unease pattern)

Dark figure over the FAR wall, sheep stirring away — NO attack, NO
struggle. The lit opening visibly avoided.

## Direction law

b06: flock files IN at violet dusk, each under the shepherd's hand.
b08: flock streams OUT at bright morning to green pasture. The
two directions are the verse ("go in and out").

## Coverage shape

One true wide with stated geometry: b01 (camera low on the slope,
fold from the side). Two Jesus beats (b03 teaching slope with the
fold beyond; b07 in the opening). Night/dusk fold frames BY DESIGN.
File order = story order.

- Plates: FOLD accepted (build-21 b12 — see identity note above).
  HILLSIDE promote-first from b03.
- b09: the nuzzle close — nothing transactional in frame.

## QC-VERIFY 2026-08-13 — independent FULL-CUT re-verify (Opus runner, Machine A `Dev`, headless)

Row not approved (approvals.json 143 approved:false) — verify-guard N/A;
independent full-cut check before Cameron's Unwatched queue. Extracted one
frame per beat (mid-window) + the 3 caption/card frames from the RENDERED
mp4 (john-10_i-am-the-door.mp4, live hash 41a4da25…) and viewed all 11
against the 6b defect checklist + RUNNER-LESSONS.

VERDICT: 10/10 beats + card CLEAN. NO re-cut ($0/0 rerolls).
- Jesus b03/b07: locked cream-only face, no halo/glow/rim-light, normal
  scale, KJV John 10:7 + 10:9 word-exact, red-letter captions (his words).
- Shepherd b01/02/05/06/08/09/10: same man every frame (dark brown tunic,
  black hair+beard, ~35), never aged/greyed/shaved, no cream on him.
- Anatomy: every figure two arms/two hands/one head; no extra limbs or
  mangled hands anywhere.
- Doctrine/scene: open gap, NO gate or bars in any frame; wall-climber b04
  non-violent unease only; direction law holds (in at dusk b06 / out at
  bright morning b08); time-of-day arc intentional + consistent.
- Realistic-only: no cartoon/stylised frame; no modern objects.
- Captions bottom-band only; question card clean (no code-squares, art
  uncovered).
COMPLAINT LEDGER: none open on row 143.
