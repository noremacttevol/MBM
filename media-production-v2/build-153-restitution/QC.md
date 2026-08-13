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
