# MBM CAPTION LAW

**The single source of truth for how captions look and sync on every story video.**
Locked by Cameron 2026-07-17. All builds import `mbm_caption_timing.caption_layers`
— do not hand-roll caption code in a build again.

---

## The Rules (non-negotiable)

### Font
- **Jost Bold** (`media-production/Jost-Bold.ttf`) — geometric sans with a true
  flat-cross lowercase "t" (no hook), native bold for clean readability.
- **Jesus's words → RED** (`0xEE3322`). **Narration → white.**
  (Red-letter Bible convention. `kjv=True` on a segment ⇒ red.)

### Layout — the band adapts to the text
- Caption band is **pinned to the very bottom**, **full width**.
- The band is **sized to fit the text** — never wasteful dark space:
  - 1 short line  → thin strip (~5–6% of screen)
  - 2 lines       → ~9–10%
  - 3 lines       → ~13% (HARD MAX 3 lines)
- Font size auto-picks the **largest** size (40–54px, KJV up to 56) that fits the
  text in the **fewest** lines.
- Text uses the **full usable width** (1080 − 2×56px side margin) so it reaches
  toward the edges, with a **respectful gap** so small phones never clip.
- **Every line is individually centered** (`text_align=C`) — a short second/third
  line centers under the longer ones.
- Band is **medium-dark** (`black@0.5`) — the picture always shows through.

### Timing
- Captions anchor to **REAL spoken timestamps** captured from edge-tts at
  narration time (`<seg>.timing.json` sidecars), mapped per character so each
  chunk appears exactly when its words are spoken.
- Windows are **contiguous and non-overlapping** — one caption clears as the next
  appears. Never two caption blocks on screen at once.
- Fallback: if a timing sidecar is missing, degrade to char-proportional timing
  (never crash a build).

### Framing
- Locked **1080×1920**, `scale=…:force_original_aspect_ratio=increase,crop` — the
  still is zoom-cropped to fill, so **every phone/screen shape sees identical
  framing** with the aspect ratio preserved.

---

## How a build uses it

`make_narration.py`:
```python
from mbm_caption_timing import save_narration
# in main(): replaces `tts.save(...)`
await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
```

`build.py`:
```python
from mbm_caption_timing import caption_layers   # drop-in, same signature
# build_still() already calls caption_layers(seg_id, dur, spoken_end, cap_text, kjv)
```

Each build folder gets a **copy** of `mbm_caption_timing.py` (so it runs
standalone). The font is found automatically in `media-production/`.

## Applying to all builds
Run `media-production/apply_caption_law.py` — it patches every `build-*/` to the
current law, regenerates narration (for timing sidecars), rebuilds the mp4,
verifies (real timing + no overlap), and reports. Then commit + push; the review
board at https://milk-b4-meat.web.app/review.html streams straight from GitHub.

## History
- 2026-07-17: Caption timing rewritten to real edge-tts timestamps (was
  char-count guess that drifted + overlapped). Font → Jost Bold flat-cross "t".
  Jesus red. Adaptive bottom band sized to text. Locked as law.
