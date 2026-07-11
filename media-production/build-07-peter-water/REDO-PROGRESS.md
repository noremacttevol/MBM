# build-07 Peter Walks on Water — REDO progress (pictures-only + face-never)

Owner: Machine C (Cameron Lovett MS). Started 2026-07-11.
Two rules: (1) Jesus's face NEVER shown; (2) Phase 1 = pictures + narration only, no clips.

## How to generate (proven this session)
- Flow project for #07 redo: `231b1a40-f4e1-4e96-b9a1-3ea518306f3b` (Nano Banana 2, x2, portrait).
- Cycle per still: open project → click create box → type the expanded prompt → click the
  submit arrow → wait ~15s → click the tile → zoom-verify face-safe → Download → **2K Upscaled**
  → the file lands in `~/Downloads/<Name>_2K_*.jpeg` → `cp` into `assets/` → gate-check → commit.
- Prompts live in `PROMPTS.md` (gate-passing). Expand [STYLE BLOCK]/[JESUS LOCK] inline when typing.

## RELIABLE no-face rule (learned the hard way)
- **Camera BEHIND Jesus (his back to camera) is the only reliable framing.**
- A distant Jesus FACING forward STILL renders a small readable face — REJECT that. (s5 v1 failed this.)
- Hands-only reach is fine (no face). No glow/halo ever.

## Still status
KEEP as-is (Jesus-free, already fine): s2-boat-storm, s4-over-gunwale, s6-eyes-on-waves.

DONE — regenerated + committed (new look, face-never, no glow):
- [x] s1-mountain-prayer-v2.jpeg  (Jesus from behind, kneeling, moonlit)
- [x] s5-walk-anchor-v4.jpeg      (camera behind Jesus, Peter walks toward him)
- [x] s11-worship-v3.jpeg         (Jesus back-to-camera, disciples' faces the subject)

GENERATED IN FLOW, not yet downloaded (grab from project 231b1a40... next pass):
- [x] s9-walk-back-v2.jpeg  DONE (downloaded).

REMAINING to regenerate (use PROMPTS.md, camera-behind-Jesus):
- [x] s3-figure-on-water-v2.jpeg  DONE (tiny distant dark figure; fishermen's fear fills foreground)
- [x] s7-sink-anchor-v5.jpeg  DONE (Peter sinking; only Jesus's hand+sleeved forearm, no face/glow)
- [x] s9-walk-back-v2.jpeg  DONE (both men from behind, downloaded).
- [x] s12-worship-v2.jpeg   DONE (closing worship, Jesus from behind).
- [!] s8-the-reach         AUDITED old s8-the-reach-v2.jpeg: hands-only/no-face is fine, BUT it has a
                            golden GLOW / light rays from above = BANNED. FIX: reuse the new
                            s7-sink-anchor-v5 for this beat and DROP s8 from build.py (simplest), OR
                            regenerate a night grip with NO glow.
- [ ] s10-calm-sea         AUDIT the banked s10-calm-sea.jpeg (not yet checked this pass); regenerate
                            only if a face or glow reads on the Lord.

DONE this pass (7 stills, all committed): s1-v2, s3-v2, s5-v4, s7-v5, s9-v2, s11-v3, s12-v2.
ONLY remaining before rebuild: resolve s8 (reuse s7) + audit s10.

## After all stills: rebuild pictures-only
1. Edit `build.py`: change the two `"clip"` segments (CLIP_WALK, CLIP_SINK) to `"still"` using the
   new anchors (s5-walk-anchor-v4, s7-sink-anchor new); repoint S1/S11 (+ any others) to the new files.
2. Run with the local static ffmpeg on PATH: `PATH="$PWD/../bin:$PATH" python3 build.py`
   (ffmpeg + ffprobe are in `media-production/bin/`).
3. Full self-revision QC (ear-check already 15/15; frame-strip for any face/glow), then present to Cameron.
