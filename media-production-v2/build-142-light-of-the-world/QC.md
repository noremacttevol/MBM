## 🅿️ RUNNER RESUME → PARK NEEDS-REBUILD (2026-08-13, Machine A `Dev`, Opus runner, headless) — FACE-BOARD BLOCK: the blind man flips age/grey across the healing; text-lock-only (REFS={}) drift, not runner-fixable

**COMPLAINT LEDGER: none open** (`v2_outline.py 142` shows no open reviewer complaint; this is a first V2 cut of the John 8:12 / John 9 story). The block below is an internal FACE-BOARD failure caught BEFORE Cameron — not a re-opened complaint.

RESUMED AUTHOR-BOARD row 142 (State RUNNING / Claim A-auto) — a prior autopilot run DIED after generating s01–s04. Already-shipped check FIRST: **no committed V2 mp4**, live review card v142 still the OLD 2026-07-29 cut (`data-hash 6f8abbf9`, no realistic-v2 wave) → genuine resume, not shipped. Generated the 6 pending beats b05–b10 ($0.80, **0 rerolls**, meter →$662.50); `--check` PASS; jesus_face_gate exit 0.

- **THE BLOCK (FACE-BOARD LAW — one face-board failure blocks reviewer publication).** The born-blind man is the story's spine across b07–b10 and he is **not the same man before vs after the healing**:
  - **s07 / s08 (pre-healing):** ~48–50yo, **grizzled GREY-flecked beard**, weathered/lined face, greying hair. s07 also renders his eyes **open and dark/seeing** — NOT the milk-pale pre-healing eyes the author QC requires (a brown/seeing eye before b09 is an explicit reject in the light-law note below).
  - **s09 / s10 (post-healing):** ~32–35yo, **solid BLACK hair + beard**, smooth younger face, deep-brown eyes (correct post-healing colour).
  - Age + hair-colour flip at the s08→s09 healing = the exact "that's not the same man" Cameron files.
- **Root cause = the row-179 class: `BLINDMAN` is TEXT-LOCK-ONLY (`REFS = {}`).** The committed `CAST-REF-V2/blindman.jpeg` (the canonical build-63 man — lean ~40, **black curly hair, dark beard, MILK-PALE eyes**, rust patched tunic + grey shoulder cloth) was **never wired as a ref to any beat**, so the prose lock alone could not hold him and he drifted grey/old in the first cluster and young/black in the second. Confirmed on disk: `grep -n "REFS = {}" beats_v2.py`.
- **Why NOT runner-fixable:** the durable fix is to pin `blindman.jpeg` as a ref on every BLINDMAN beat and regen the off-model cluster — an author-lane `REFS`/beats_v2 edit the runner may not make. It also exceeds the COST-LAW reroll budget (regen s07+s08 = 2/10 = 20% > 15%), and a blind `--redo` of the same text just re-drifts (row-179 continuity lesson). → **PARK NEEDS-REBUILD**, do not blow the budget, do not ship over a face-board failure.

**PRESERVE (do NOT regen — banked, on-model, verified this session):**
- **All Jesus frames** (s01 temple wide, s02 he-offered-himself, s07/s08/s09/s10): ONE locked V2 face throughout — dark wavy hair, full dark beard, cream-only (crowd browns/greys), ref-true green/hazel eyes (lesson 20, do NOT brown-edit), no halo/glow, ordinary scale, clean hands.
- **TEMPLE** honored (limestone courts, columned porticoes, golden festival lampstands with real physical flames; light physical, none on Jesus).
- **NIGHTROAD** s05/s06: two figures / one low lantern / dark real beyond the ring, faces warm and readable (lesson-22 night floor met), physical flame, no halo; s06 direction correct (bearer AHEAD, follower stepping into the lit footprints).
- **Blind man s09/s10** (young black-haired, deep-brown post-healing eyes): on the young end of the canonical ref and internally consistent with each other; the casting-out is COLD not violent (turned backs, dismissing hands, Jesus arriving at his shoulder), and the b10 sunrise walk is correct (real dawn ahead, no light effects).

**AUTHOR MINIMAL TOUCH-ONCE FIX (regen 2 beats only, then re-gate the full cut):**
1. Wire the ref: `REFS = {"BLINDMAN": "CAST-REF-V2/blindman.jpeg"}` in `beats_v2.py` (the portrait already exists on disk).
2. Delete the off-model cluster: `rm assets/s07-later-as-he-met-a.jpeg assets/s08-he-did-not-leave-the.jpeg`.
3. Regen ONLY those two against the wired ref:
   `cd media-production-v2 && python3 v2_gen_api.py build-142-light-of-the-world --only v2-r142-b07 v2-r142-b08 --ceiling <meter + 2*0.134*1.5 + 25>` — the gen log must print `[+1 char ref: BLINDMAN]` on each. Target ~40yo **black curly hair / dark beard**, and **MILK-PALE eyes** on b07/b08 (pre-healing); keep the discreet fingertip anointing in b08 (earth-dust posture only, nothing clinical/fluid).
4. Face-board all four blindman beats (b07–b10) side-by-side against `blindman.jpeg` — one man, dark-haired throughout; verify the eye-state flip (pale b07/b08 → deep-brown b09/b10). s09/s10 are close to canonical; nudge them only if the four still don't read as one man.
5. Then the normal RUNNER path: `v2_assemble.py 142` (must print AUDIO REBUILD PASS; `AUDIO_FROM_V1_SEGMENTS=True` is already set), FULL-CUT GATE per-rendered-frame 10/10 + card, ship + deploy + live-verify.

**Cost this session:** $0.80, 0 rerolls (6 first-attempt gens; 8/10 stills banked, only 2 re-pulled by the rebuild). Catching the drift before ship saved a voided approval + a re-cut (COST LAW: a defect Cameron finds is far costlier than a park). Review card UNTOUCHED (old cut stays; the redo is not ready). NO deploy (nothing new to serve).

---

## ✅ AUDIO-FIX DONE → AUTHORED / Audio OK / Ready (2026-08-11, Machine A `Dev`, audio lane)

STALE-V1 class, resolved at **$0, zero Gemini, zero re-voice** — audio only; no
stills exist yet, so this hands back to the picture runner (prompt step 5,
"no V2 stills yet" case).

- **Voice-ID:** all 7 segments (n0/n1/n2/n3/j1/j2/card) are **44100 Hz / 128 kbps
  / mono = ElevenLabs new-voice spec** (edge-tts would be 24000/48k). NOT the dead
  old edge-tts — no re-voice needed.
- **Fix:** `AUDIO_FROM_V1_SEGMENTS = True` added to `beats_v2.py`. When the picture
  runner assembles, the track rebuilds from the 7 segment mp3s (~59.4s) instead of
  copying the stale 63.07s V1 render, so `v2_assemble.py 142` will pass the audio
  lock (prints AUDIO REBUILD PASS) instead of failing on the 3.66s divergence.
- **Board:** NEEDS-AUDIO → **AUTHORED / Audio OK / Ready ✅**, claim cleared. The
  picture runner now builds the 10 stills on the fixed audio and ships the full cut.

---

## 🅿️ RUNNER $0 PRE-FLIGHT PARK → NEEDS-AUDIO (2026-08-11, Machine A `Dev`, Opus runner)

**Parked at $0 BEFORE any still was generated (row-141 lesson: pre-flight the AUDIO
LOCK even when the board says Audio OK).** This row is STALE-V1: the current V2
audio segments no longer match the old V1 render.

- extract_beats timeline (current `audio/*.mp3` segments) = **59.409s**
- authoritative V1 final mp4 = **63.067s** → gap **3.658s** (past the 0.75s guard); `AUDIO_FROM_V1_SEGMENTS` is NOT set.
- 7 segments, spec 44100/128000/mono = the new-voice ElevenLabs cast spec (Brian narrator / Chris Jesus) — so a re-voice is probably NOT needed, only the flag.

**AUDIO LANE — RESUME (row-200/118/22 template, expected $0/no re-voice):**
1. Voice-ID the segments to confirm they are the new ElevenLabs cast (not old edge-tts); re-voice ONLY any wrong seg first.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `build-142-light-of-the-world/beats_v2.py`.
3. Hand back to the picture runner: `v2_prompt.py build-142-light-of-the-world --check` (PASS) → generate the beats → `v2_assemble.py 142` must print **AUDIO REBUILD PASS** (~59.4s) → FULL-CUT GATE → ship + deploy + live-verify.

The runner does NOT set the flag itself (beats_v2.py is off the runner's allowed-write
list; the runner-prompt step 6 says an AUDIO-LOCK failure = stop the row, log, do not ship).

---

# QC / RUNNER HANDOFF — build-142-light-of-the-world (John 8:12; John 9)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~53 s. Second I AM row.

## Light law (doubly binding)

Every light physical: festival lampstand flames, the guttering lamp,
the lantern, the sunrise. NO light effect on any person — b03's
lamps burn BESIDE Jesus, never from him. Automatic reject.

## The born-blind man is ROW 63's man

BLINDMAN lock is BYTE-IDENTICAL to build-63 — same face, patched
rust-brown tunic; eyes MILK-PALE in b07/b08, CLEAR DEEP BROWN from
b09. Face-board against build-63's frames. Eye-state is per-beat —
a pale eye after b09 or a brown eye before is a reject.

## Discreet anointing (b08, the row-136 pattern)

Posture only: fingertips (earth-dusted) at the closed lids, head
bent. Nothing clinical, no fluid.

## The casting-out (b09)

COLD, not violent: turned receding backs, a distant dismissing
gesture. The frame's weight is Jesus ARRIVING at his side — found,
not abandoned.

## Real dark (b05/b06)

The night genuinely dark beyond the lantern ring — the light does
not pretend the night is harmless. b06 direction: bearer AHEAD,
follower stepping into the lit footprints.

## Coverage shape

One true wide with stated geometry: b01 (camera past the moving
crowd's backs into the treasury). Eight Jesus beats. b10 closes on
the healed man's FIRST sunrise, walked beside its maker. File
order = story order.

- Plates: TEMPLE accepted (the build-06 b21 family anchor, same as
  43/75/131 — architecture only; identity-edit the frame's
  foreground trio if they leak). NIGHTROAD promote-first from b05.

---

## ✅ AUTHOR-LANE FIX DONE (2026-08-13, Fable-5 author lane, Machine A `Dev`, $0) → row set AUTHORED + Ready ✅ for the runner

Face-board (viewed the ref + s07/s08/s09/s10): the born-blind man drifted because `BLINDMAN` was **text-lock-only** (`REFS` had only TEMPLE). s07 rendered an older ~50yo grey-haired/grey-beard man with eyes not clearly milk-pale; s08 was borderline; s09/s10 were the on-lock ~35 dark-haired healed man. The committed `CAST-REF-V2/blindman.jpeg` (about-35, unruly black hair, short dark beard, MILK-PALE blind eyes) was never wired.

**Author fix ($0, no generation):**
- Wired `REFS["BLINDMAN"] = "CAST-REF-V2/blindman.jpeg"` (kept TEMPLE). `cast_refs_for()` now attaches this face to b07/b08 (both also keep the locked Jesus face via `jesus:True`+`ref`). The BLINDMAN text lock already reads correctly (age 35, black hair, rust-brown tunic + grey cloth never cream, milk-pale-before / clear-after eyes) — no lock rewrite needed.
- Deleted ONLY the two off-model pre-healing stills `s07`, `s08` for regen; kept the 8 banked on-lock frames (s01–s06, s09, s10 — Jesus one locked cream face, TEMPLE/NIGHTROAD good, the healed man consistent).
- Force-added `blindman.jpeg` (CAST-REF-V2 is gitignored) so the ref is reproducible.

`v2_prompt.py --check` = PASS (10 beats). `v2_gen_api --dry-run` = exactly **2 shots (b07/b08), est ~$0.27**, `[face]` (Jesus) + BLINDMAN ref attached. Audio untouched.

### 🅿️ RUNNER — remaining work
1. `v2_gen_api build-142-light-of-the-world` regenerates ONLY s07/s08 — the man must match the ref: ~35, unruly black hair, short dark beard, **milk-pale blind eyes** (pre-Siloam), rust-brown tunic + grey shoulder cloth (never cream). Jesus stays the one locked cream face.
2. FULL-CUT GATE all 10 beats against the ref as the face-board anchor — the born-blind man is the SAME ~35 dark-haired man across s07→s10 (milk-pale before the healing, clear brown after), Jesus one consistent face, realistic throughout.
3. Assemble (AUDIO LOCK), deploy, live-verify. No open Cameron complaint — this was a pre-ship face-board block; the review card presents the finished consistent cut.
