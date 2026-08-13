# QC / RUNNER HANDOFF — build-153-restitution (Acts 3:1-21)

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
