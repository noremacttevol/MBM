# build-09 Rich Young Ruler — REDO progress (pictures-only + face-never)

Owner: Machine C. Started 2026-07-11. Same recipe as build-07 (see build-07/REDO-PROGRESS.md).
Two rules: (1) Jesus's face NEVER shown; (2) pictures + narration only, NO AI clips.
Flow: new project, Nano Banana 2 x2 portrait, camera BEHIND Jesus, download 2K.
Gate every prompt: `python3 media-production/jesus_face_gate.py --dir build-09-rich-ruler`.

## Audit (2026-07-11)
KEEP (these are the YOUNG MAN, not Jesus — his face is allowed):
- s2-kneeling-earnest.jpeg, s3-the-look.jpeg (young man sorrowful), s4-the-one-thing.jpeg
  (young man kneeling), s8-empty-road.jpeg. NOTE: s3 is semi-photoreal — a style nit only.

REGENERATE (Jesus scenes):
- [ ] s7-he-let-him-go.jpeg  — Jesus over-the-shoulder on the right BUT a partial side of
      his face/cheek/eye reads = VIOLATION. Redo: camera fully BEHIND Jesus (back of head
      only), the young man walking away down the road ahead. No glow.
- [ ] s5-words-land.jpeg     — AUDIT (Jesus speaking?); if face/glow, redo from behind.
- [ ] s1-the-run.mp4 (CLIP)  — man runs to Jesus. STILL: young man running toward a Jesus
      seen from behind / at distance, no face. (Rule 2: no clip.)
- [ ] s6-walk-away.mp4 (CLIP) — man walks away. STILL (or reuse the new s7). No clip.

## Rebuild (same as build-07 — which worked)
- Edit build.py: repoint regenerated stills; change the 2 "clip" segments to "still", keep durations.
- Run: `PATH="$PWD/../bin:$PATH" python3 build.py` (ffmpeg/ffprobe in media-production/bin/).
- If the final mux truncates (moov atom), re-mux segs/video_silent.mp4 + segs/audio_mix.m4a.
  SCRIPTURE-NAME: mark-10_rich-young-ruler.mp4. Watch the <25MB law (slow/veryslow preset).
