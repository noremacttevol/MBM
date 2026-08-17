# QC / RUNNER HANDOFF — build-153-restitution (Acts 3:1-21)

## C-FIX LIVE — 2026-08-16 (Machine A `Dev`, Codex + local Ollama)

Cameron's current-cut complaint: *"1:52 is double picture in 1 frame thats no
good replace it."* Exact rendered-frame tracing maps 1:52 / 112s to **b20**
(109.42–118.09), not a transition or neighboring beat. Local `qwen3.5:27b`
vision inspected the actual 112s pixels and returned **FAIL**: two distinct
temple scenes stacked vertically, joined by a diffuse semi-transparent band.

**PROMPT AUTOPSY = CAUSED.** b20 demanded an empty sky-only temple view while
also attaching the `TEMPLE` place plate. That plate visibly contains a crowded
close temple scene with two foreground women. The generator preserved that
incompatible reference as the upper picture and invented a separate empty
temple/sky picture below it. The old prompt also omitted explicit anti-diptych
language. Fix: remove `TEMPLE` from b20's locks so the crowded plate cannot
contaminate the empty composition, and require one single-exposure low-angle
photograph with one unbroken roofline, one uninterrupted sky, no people, and
explicitly no diptych/collage/split/stack/overlay/ghost/blend/inset/panel or
montage. Regenerate **only b20**; all other images and all audio remain locked.

### ✅ C-FIX FINAL GATE — SHIP CANDIDATE

- Generated **only b20**: 1 still, $0.13, meter $723.20 → $723.33. The other
  25 source stills remain byte-identical.
- Source-still inspection: PASS — one continuous sky and one unbroken temple
  roofline; no people and no diptych, collage, split, stack, overlay, ghost,
  blend band, inset, panel, or montage.
- Exact rendered 112s complaint frame: local `qwen3.5:27b` vision **PASS** —
  one seamless temple-and-sky shot, no double picture, readable caption wholly
  inside the bottom band.
- Exact rendered 72s regression frame: **PASS** — Peter visibly addresses the
  restored formerly lame man in one coherent temple scene; the prior fix held.
- Full-cut gate: all 26 chronological rendered scene midpoints inspected;
  closing question card inspected and independently vision-checked **PASS**
  (centered, readable, unclipped).
- `verify-mp4.sh`: PASS; full FFmpeg decode: PASS. Duration 161.566667s,
  20,442,101 bytes. MP4 SHA256
  `259753df57eac4180033668ce50d56a99f6e7cabee909075b16672ba1b38ac55`.
- Audio stream SHA256
  `25b1a0e3507cf767910bb88df6747d310bf3e1c0be6f5112254de787a8ecfb8e`
  exactly matches the pre-fix approved audio stream. No narration changed.

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 26 beats, ~148 s. The restitution-of-all-things row (BRIDGE
tone, kept entirely inside Acts' own frame).

## Peter is the shared cast token

Same peter face as CAST-V2-REF sheets across 8 appearances —
face-board. Fisherman's build; preacher's fire EARNEST, never angry
(b12).

## The lame man (row-15 dignity, strictly)

Lame from birth: thin wasted legs BEFORE, strong legs/ankles AFTER
(the verse names ankles) — never grotesque, begging with a held-out
bowl, never abject. b05's lift is by the RIGHT hand (scripture-
exact). Leg-state is per-beat: wasted b03/b04/b05-start, strong
from b05's rise on. Face-board him b01/b03/b05/b06/b13.

## Absolute gates

- b19 prophets' relay: indistinct varied silhouettes, ONE scroll
  travelling the line — NO named/depicted prophet.
- b20: the vast waiting sky over the temple ONLY — no figure, no
  ascension depicted.
- b14's all-things healing: ONE continuous landscape, ruin
  becoming whole left-to-right.

## Rhymes and registers

- Refreshing = REAL rain: first dark coins on cracked dust (b09) →
  full soaking + lifted faces, NOBODY running for cover (b10/b11).
- b17: the shadow NEAR the mark, not on it.
- b23: new vessel FLAWLESS + shards retired — no glued patchwork.
- b26: the FULL turn (feet, shoulders, face) toward the bright
  valley — the 117/133 reversal rhyme.
- b22: the giving-BACK exact — the very ewe to the very arms.

## Coverage shape

One true wide with stated geometry: b01 (camera across the
flagstones past the runners' backs). No Jesus beats. TEMPLE plate
ACCEPTED (build-06 b21 family anchor, same as 43/75/131/142 —
architecture only; identity-edit the frame's foreground trio if
they leak). File order ≠ story order (b15 at 32s, b21 at 142s
before b22's 119s) — build by WINDOW.

- LAMEMAN promote-first from b03.

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**$0 spent. NO stills generated. Parked at the two-part audio PRE-FLIGHT before touching the meter.**

STALE-V1: the picture runner copies the V1 mp4's audio (no `AUDIO_FROM_V1_SEGMENTS` flag), but the V1 mp4 no longer matches the current narration timeline:
- `extract_beats.extract(153)` total = **161.553s**
- V1 mp4 `acts-3_restitution-of-all-things.mp4` duration = **204.428s** (the old 3:24 cut)
- `abs(total − mp4) = 42.875s` (≫ 1.0s guard; excess mp4−total = +42.875 ≫ 0.75s assembler guard)
- **13/13** V1-dir `audio/*.mp3` are NEWER than the V1 mp4 (re-recorded new-voice narration over the old render)

Either tripwire alone blocks the AUDIO LOCK; both fire here. This is the row-141/147/118 STALE-V1 class.

**FIX = audio lane (NOT runner — beats_v2.py is off the runner's write-list):**
1. Voice-ID the 13 V1-dir mp3s (`media-production/build-153-restitution/audio/*.mp3`) — confirm new-voice ElevenLabs cast (Brian narrator / Roger scripture; no Jesus segment in this Acts row).
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` so the cut rebuilds audio from those 13 mp3s (~161.5s), NOT the stale V1 mp4. No re-voice, $0.
3. Since **0 stills exist**, hand back to the picture runner: board State `NEEDS-AUDIO → AUTHORED`, keep `Ready ✅`, Claim BLANK (per audio-fix prompt "AUTHORED+Ready (no stills yet)").

**RESUME (audio lane):**
```
python3 media-production-v2/v2_assemble.py 153   # will still refuse until AUDIO_FROM_V1_SEGMENTS=True is set
```
After the flag is set, the picture runner builds all 26 stills fresh and full-cut-gates.

**COMPLAINT LEDGER (carried forward for the eventual picture build):**
- OPEN: "1:12 is weird picture — needs Peter" → the author already fixed this in the beat map: **b13** (window 69.58–73.66s, covers 1:12/72s) now shows **Peter's arm sweeping from the healed leaping man out across the whole court/city/sky** (must_show: "Peter's arm lifting FROM the healed man TO the whole court"). Peter is present and the subject — no longer a Peter-less "be blotted out" still. The picture runner MUST verify b13 renders Peter at ~1:12 in the FULL-CUT GATE before shipping.

## ✅ AUDIO-FIX DONE — 2026-08-13 (Machine A `Dev`, audio lane, headless)
STALE-V1 resolved, $0, 0 re-voice:
1. Voice-ID'd all 13 V1-dir mp3s (n1,n1b,n2-n8,kv19,kv21,s6,card) = **44100 Hz / 128 k = the chosen ElevenLabs new-voice cast** (no old edge-tts segment).
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild from the newer mp3s; nothing re-voiced/re-timed; V1 read-only). The stale 204.4s V1 mp4 is now irrelevant — the segment timeline (161.6s) is authoritative.
3. Pre-flight PASS: `extract_beats 153` = 161.6s / 12 beats; `--check` v4 PASS (26 beats); `audio_audit --rows 153` = **0 old-voice segments**.
4. Handed to the PICTURE RUNNER: board State NEEDS-AUDIO → AUTHORED, Ready ✅, Claim cleared. Runner builds the 26 beats on the now-valid audio and MUST verify b13 shows Peter at ~1:12 in the FULL-CUT GATE (see COMPLAINT LEDGER above) before shipping. $0 / 0 Gemini / 0 re-voice.

## 🅿️ RUNNER PARK → NEEDS-REBUILD — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**26/26 stills generated (~$3.48, 0 rerolls) — NOT SHIPPED. Peter is off-model in every frame he appears in. Root cause is an AUTHORING gap the runner may not fix (editing a beat's `locks`/`ref` is off the runner write-list).**

### The defect (FACE-BOARD LAW / rubric lesson 2)
Peter — the PROTAGONIST of this row — renders as an **older grey-haired man in a charcoal/brown robe**, a different actor from his canonical sheet. Canonical PETER (`media-production/CHARACTERS/peter/`, `character_refs.lock_text('peter')`) = **mid-thirties, thick DARK curly hair, full DARK beard, weathered olive skin, BLUE-GREY wool tunic + rope belt, dun-brown mantle.** Verified against the SHIPPED fleet: build-103 s11 shows exactly that dark-haired mid-30s Peter. build-153's Peter is unrecognizable next to it, and even his robe drifts (charcoal in s02/s12, brown in s03/s13). Cameron reads this as "that's not Peter / the character changed" — the exact repeat-complaint class the LEARNING LAW forbids shipping.

### PROMPT-AUTOPSY (verdict = ALLOWED + IGNORED)
Pulled b02's assembled prompt: the ONLY reference attached is `PLACE-REF/temple.jpeg`; **no Peter reference image is attached and the canonical PETER LOCK text is never injected** — because PETER is not in any beat's `locks` list and every Peter beat is `ref:False`. Peter is carried by prose only ("PETER per the cast sheets — fisherman's build, weathered", "the cast-token face exact"), and the b02 line **"the weathered face that three years of following and one terrible weekend remade"** actively nudges the model toward an aged, weathered man. Words cannot pin appearance (lesson 2); only the reference image can. Peers build-19-shore (PETER in locks, 15 beats `ref:True`) and build-103 (PETER×20 in locks) do it correctly — build-153 is the anomaly.

### AUTHOR FIX (NEEDS-REBUILD, author lane)
For EACH of the 10 Peter-bearing beats — **b02, b03, b04, b05, b06, b07, b12, b13, b15, b18** — add `"PETER"` to the beat's `locks` list AND attach Peter's reference (set `ref:True` with the peter canonical ref, or `v2_stash --promote`/wire a PETER plate), exactly as build-19/build-103. Also soften the b02 "weathered face ... remade" prose so it stops pushing an aged Peter (keep him mid-30s per the lock). Leave the LAMEMAN plate (already promoted this session from s03) and all non-Peter beats untouched.

### TOUCH-ONCE / COST
The 16 non-Peter frames (refreshing b09/b10/b11, kv b12 is Peter... actually b12 is Peter; non-Peter = b08 partial, b09, b10, b11, b14, b16, b17, b19, b20, b21, b22, b23, b24, b25, b26) already pass and are byte-identical carryover — the rebuild regenerates ONLY the 10 Peter beats, so this session's ~$3.48 mostly carries forward. LAMEMAN plate = `PLACE-WIRING.json` (promoted from s03, wired to b01/b03/b04/b05/b06/b13).

### OPEN COMPLAINT still open (not shipped)
"1:12 is weird picture — needs Peter" → b13's composition already puts Peter gesturing from the leaping healed man across the court at ~1:12 (compositionally fixed), but Peter's identity must be corrected in the rebuild before it can ship. The complaint stays OPEN until the fixed cut is approved.

**RESUME (after author adds PETER lock+ref to the 10 beats):**
```
python3 media-production-v2/v2_gen_api.py build-153-restitution --only v2-r153-b02 v2-r153-b03 v2-r153-b04 v2-r153-b05 v2-r153-b06 v2-r153-b07 v2-r153-b12 v2-r153-b13 v2-r153-b15 v2-r153-b18 --redo --ceiling <meter+~4>
# then FULL-CUT GATE (face-board Peter against character_refs peter), v2_assemble 153 (AUDIO LOCK must pass), ship+deploy+verify.
```

---

## ✅ AUTHOR-FIX DONE — 2026-08-13 (Machine A `Dev`, Fable-5 author lane, headless) — Peter identity root-caused & fixed, State→BUILT for paid cfix regen

**$0. No stills generated. Author-lane edits only (beats_v2.py locks + prose). The park's "add ref:True" instruction was WRONG and is corrected here.**

### The mechanism (verified in code, not guessed)
- `v2_gen_api.py` `GLOBAL_CAST` maps `"PETER" → "peter"`; `CAST-V2-REF/peter-front.jpeg` + `peter-quarter.jpeg` both exist (3.2 MB each, ≫50 KB). So **putting `"PETER"` in a beat's `locks` auto-attaches the peter reference SHEET *and* injects the canonical PETER lock TEXT** (`v2_prompt.py` `CAST_LOCKS['PETER']`: mid-thirties, thick dark curly hair, full dark beard, weathered olive skin, BLUE-GREY tunic — never cream — + dun-brown mantle).
- The `ref` flag is **the Jesus face lock ONLY** — `face_b64 = b64_file(JESUS_REF)` (v2_gen_api.py:367), attached only when `beat.get("ref")` is truthy (line 422); `check()` ties `ref` to `jesus:True`. **Setting `ref:True` on a Peter-only beat would inject JESUS's face into an Acts scene that has no Jesus — a defect, not a fix.** The park note conflated the two. Left `ref:False` everywhere (correct; matches peer build-103 b04/b06, which render Peter correctly with `PETER` in locks + `ref:False, jesus:False`).
- TRUE root cause was therefore SINGLE, not double: **PETER absent from every beat's `locks`** → no sheet, no lock text, prose-only → the model invented an older grey man and drifted the robe (charcoal/brown vs locked blue-grey).

### The fix (author lane)
1. Added `"PETER"` to `locks` on the **9 REAL Peter beats**: b02, b03, b04, b05, b06, b07, b12, b13, b15. `ref` stays False (no Jesus in this row).
2. **b18 EXCLUDED (park note was wrong to list it).** b18 is scrolls-only — its `must_show`/`must_not_show`/scene all say "No people are needed in this frame." It renders no Peter figure; adding PETER would force a person into a no-people frame. `locks` stays `[]`.
3. Softened b02's aging prose: dropped "the weathered face that three years of following and one terrible weekend **remade**" (which nudged an aged Peter) → "the broad net-hauling frame of the **mid-thirties fisherman the cast sheet fixes, thick dark curly hair and full dark beard, sea-tanned but unmistakably young**…". Verified: assembled b02 now contains `PETER LOCK` + `mid-thirties` + `BLUE-GREY`, and no longer contains `remade`.
4. `python3 v2_prompt.py build-153-restitution --check` → **v4 checklist PASS** (26 beats).
5. LAMEMAN plate (PLACE-REF/lameman.jpeg, promoted from s03 last session) + temple.jpeg force-added to the repo (PLACE-REF is gitignored). PLACE-WIRING.json already tracked.

### Handoff — State NEEDS-REBUILD → **BUILT** (paid cfix/runner lane owns the targeted re-cut)
Only a PAID targeted regen remains (this session is $0-image by law), so per PROMPT-FABLE5-AUTHOR "When your author work on a NEEDS-REBUILD row is DONE" the board State is flipped to **BUILT** (complaint stays OPEN, no literal `C-FIX <date>` in Claim). The 16 non-Peter frames are byte-identical carryover; only the 9 Peter beats regenerate (~$1.2, spend mostly carries from the parked $3.48).

**RESUME (paid lane) — regenerate ONLY the 9 Peter beats:**
```
python3 media-production-v2/v2_gen_api.py build-153-restitution --only v2-r153-b02 v2-r153-b03 v2-r153-b04 v2-r153-b05 v2-r153-b06 v2-r153-b07 v2-r153-b12 v2-r153-b13 v2-r153-b15 --redo --ceiling <meter+~2>
# gen log must show "[+1 char ref: PETER]" on each. Then FULL-CUT GATE:
#   - face-board Peter across all 9 vs CAST-V2-REF/peter-front.jpeg (mid-30s, dark curly hair, dark beard, blue-grey tunic — NOT grey/old, NOT charcoal/brown robe)
#   - VERIFY b13 renders Peter at ~1:12 sweeping FROM the healed man TO the court (closes the OPEN "1:12 needs Peter" complaint)
# then v2_assemble.py 153 (AUDIO_FROM_V1_SEGMENTS already True; AUDIO LOCK must pass), ship + deploy + live-verify.
```

### OPEN complaint still open (do NOT close until the fixed cut is approved)
"1:12 is weird picture — needs Peter" → b13 compositionally puts Peter's arm sweeping from the healed leaping man across the court; identity is now fixable via the PETER lock. Stays OPEN until the regenerated cut ships and Cameron approves.

---

## ⚠️ HANDOFF CORRECTION — 2026-08-13 (same author session): State → AUTHORED + Ready ✅ (RUNNER lane), NOT BUILT/cfix

My "AUTHOR-FIX DONE" section above first flipped State→BUILT for the cfix lane. **That would STRAND this row.** I re-checked `autopilot.sh`: the cfix picker (PASS 1, lines 248-250) fires only when `cur.get(row) is not None` — i.e. the row has a **LIVE PUBLISHED cut** and the complaint's `reportedAgainst` matches that live hash. **Row 153 was never published in V2** (fresh rebuild, no review card, `cur['153']` is None), so cfix would never fire and the complaint would sit forever (the "cfix hash-gate strands rebuilds" class; cf. row-140 precedent — an unpublished rebuild is built by the RUNNER, not cfix).

**Correct route (done):** State **AUTHORED** + Audio **OK** + Claim **empty** + Ready **✅** → the RUNNER lane (autopilot PASS 2, lines 292-297) picks it up, **complaint-first** (row 153 is in `openc`), lowest-number-first.

Because the runner **skips existing stills >50 KB** (`v2_gen_api.build_todo`, line 321), I **DELETED the 9 off-model Peter stills** (s02,s03,s04,s05,s06,s07,s12,s13,s15) so the runner regenerates exactly those 9 with the now-attached PETER sheet+lock. The 16 good frames + b18 (scrolls) are kept byte-identical (touch-once; the parked $3.48 mostly carries; ~$1.2 to regen 9). Asset count on the board is now 17 (will return to 26 after regen).

**RUNNER must, before shipping:** face-board Peter across the regenerated 9 vs `CAST-V2-REF/peter-front.jpeg` (mid-30s, dark curly hair, full dark beard, BLUE-GREY tunic — NOT grey/old, NOT charcoal/brown robe); confirm gen log prints `[+1 char ref: PETER]` per frame; **VERIFY b13 renders Peter at ~1:12** sweeping FROM the healed man TO the court (closes the OPEN "1:12 needs Peter" complaint); assemble (AUDIO LOCK PASS), ship + deploy + live-verify; card answers the complaint in Cameron's words.

---

## ✅ RUNNER SHIP — 2026-08-13 (Machine A `Dev`, Opus runner, headless, UNATTENDED) — RESUMED the dead build, 26/26 Peter fixed, SHIPPED + LIVE

**Resumed row 153 (State RUNNING / Claim A-auto) after the prior autopilot session was SIGTERM'd mid-regen (RUNNER-LESSONS line 61 — background gen killed under lane concurrency; resume is idempotent).** RUNNER-LESSONS already-shipped check first: no committed V2 mp4, live card `65427b73` was the OLD 8-still cut, complaint still OPEN → genuine resume, not already-shipped.

- **On-disk audit before spending:** 21/26 stills present. Viewed s02–s05 — a prior session had ALREADY regenerated them correctly (mid-30s dark-haired Peter matching `CAST-V2-REF/peter-front.jpeg`, blue-grey tunic), NOT the old off-model grey man. Only **5** were missing (s06,s07,s12,s13,s15). Used the PLAIN runner (auto-skips existing >50 KB frames) — NOT `--redo` — so I regenerated EXACTLY the 5 missing and did NOT re-pull the 4 already-fixed Peter frames (COST LAW / touch-once).
- **Generated 5 beats, $0.67, 0 rerolls (0% vs 15% budget), meter $662.63→$664.10, ceiling $689.** Every one attached `[+2 char ref: PETER:front, PETER:quarter]` — the PETER lock+sheet now reach the model (the whole point of the author fix).
- **FULL-CUT GATE per-asset (all 9 Peter beats) + per-RENDERED-frame:** Peter is the canonical mid-30s dark-haired man in the blue-grey tunic across s02–s07/s12/s13/s15 — face-board consistent, no grey-old-man drift, no charcoal/brown robe. **b13/s13 VERIFIED at 1:12 in the rendered mp4** (Peter's arm sweeping FROM the leaping healed man TO the whole court/city/sky — closes the OPEN "1:12 needs Peter" complaint). Realistic throughout, no Jesus/cream, no halo, anatomy/hands/scale clean, no modern objects. Captions bottom-band (white narrator / blue KJV scripture, no red — correct, Peter is not Jesus). Question card clean, no typo squares. No trailing dead-air (closing question segment fills to end).
- **AUDIO REBUILD PASS** SHA256 `25b1a0e3507cf767…` (rebuilt from 13 V1 segment mp3s per `AUDIO_FROM_V1_SEGMENTS=True`; this is a STALE-V1 rebuild with no prior V2 mp4 to hash-lock, so REBUILD PASS not LOCK — expected). Duration 161.6s, 20.6 MB.
- Ship = two commits (mp4 force-added + boards + QUEUE + this note; then review card repointed + SESSION-LOG), firebase deploy, live-verify. Complaint "1:12 needs Peter" CLOSED-pending-approval (stays OPEN until Cameron approves the fixed cut).
