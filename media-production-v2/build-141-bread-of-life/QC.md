# QC / RUNNER HANDOFF — build-141-bread-of-life (John 6:26-51)

## 🅿️ RUNNER PARK → NEEDS-AUDIO (2026-08-11, Machine A `Dev`, Opus runner)

**All 10 V2 realistic stills are DONE + FULL-CUT-clean on disk — do NOT regen
(row-118 template). The row is blocked only at the AUDIO LOCK: `v2_assemble.py 141`
refuses because the V1 final mp4 is STALE.**

Measured (all $0):
- Extracted V2 timeline (from the current `audio/*.mp3` segments) = **61.022s**.
- Authoritative V1 final mp4 (`media-production/build-141-bread-of-life/john-6_i-am-the-bread-of-life.mp4`) = **68.700s** → a **7.68s** divergence, far past the 0.75s guard. The V1 mp4 is the OLD 7-still 1:09 cut; its audio no longer matches the current segments.
- The current segments are IDENTICAL in both dirs (`media-production/build-141/audio/` == `media-production-v2/build-141/audio/`), sum 49.92s raw, and are spec **44100/128000/mono** (= the chosen ElevenLabs new-voice cast spec, matching rows 200/22). So the narration on disk is almost certainly already correct; the mp4 is just an out-of-date render.

**Why the RUNNER parks instead of fixing (row-200 / row-118 / row-22 precedent):**
the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this row's `beats_v2.py` — beats_v2.py
is NOT on the runner's allowed-write list, and the runner prompt step 6 says an
AUDIO-LOCK failure = STOP the row, log, do not ship. It is an AUDIO-LANE decision
because it requires a **voice-ID verification** the picture runner does not do:
confirm the segments are the NEW ElevenLabs voice (Narrator "Brian" / Jesus "Chris",
not old edge-tts) before flipping the flag — exactly what the audio lane did for
rows 200/118 before those shipped.

**AUDIO LANE — RESUME (all $0, zero Gemini, zero re-voice expected):**
1. Voice-ID the segments (transcribe / cross-check the cast) — confirm Brian narrator
   + Chris on `audio/j1.mp3`/`j2.mp3`/`j3.mp3` (the three red-letter John 6:35/48/51
   lines). If genuinely old/wrong, re-voice ONLY the wrong segs through the locked
   ElevenLabs cast first.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `build-141-bread-of-life/beats_v2.py`.
3. `python3 media-production-v2/v2_assemble.py 141` → must print **AUDIO REBUILD PASS**
   (~61.0s from the 8 segments; silent-card handling already fixed row-128).
4. Hand back to the picture runner (or continue): FULL-CUT GATE §6b on the rendered
   mp4 (transcribe + caption↔`audio/<seg>.timing.json` diff per row-131), then ship +
   deploy + live-verify. The 10 stills are already gated clean this session (below).

**The 10 stills, FULL-CUT-QC'd 2026-08-11 (0 rerolls, ~$1.34):** all realistic,
Jesus locked-face + cream-only across b01/b02/b03/b05/b08/b10, no halo, natural
scale, correct hands/anatomy, period props only (boats/nets/clay lamp/wooden
board/baskets), bread state machine correct (whole display loaf b04 → broken
b08/b10, no cross/passion imagery), manna vignette b06 carries no death imagery.
Nothing to reroll.

---

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~54 s. First of the I AM rows (141-146).

## The given-flesh foreshadow is BROKEN BREAD ONLY (b08/b10)

No cross imagery, no wounds, nothing of the passion — Jesus's hands
slowly breaking one loaf carry the whole weight. Automatic reject
otherwise. b10's close: the broken loaf open across his two extended
hands, face warm and resolved.

## Loaf state machine (prop-board)

One barley loaf: whole/torn-open on the board in b04 (a DIFFERENT
display loaf), the teaching loaf whole until b08, broken open from
b08 through b10 — same loaf b08/b10.

## Manna vignette (b06)

The gathering morning ONLY — pale desert dawn, robed ancestors,
baskets. NO graves, no death imagery — mortality is the narration's.

## Appetite dignity

The crowd's hunger is human and gently drawn (b01/b07) — no greed
caricature. b09's deeper hunger: a FULL table + searching eyes —
interior, dignified.

## Coverage shape

One true wide with stated geometry: b01 (camera up the shore past
the crowd's hurrying backs; boats freshly beached). Six Jesus beats
(b01, b02, b03, b05, b08, b10) — locked face, no halo; b05's hand
flat at his own chest. File order ≠ story order (b07 at 4.53s, b09
at 19.36s) — build by WINDOW.

- Plates: none auto-matched. SHORE promote-first from b01.
- The bread must look GOOD everywhere (the literal kind's goodness
  makes the deeper kind mean more).
