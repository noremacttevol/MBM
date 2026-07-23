# ORDER FOR AGENT #1 — Strip the narrator echo from every transcript

Cameron's standing complaint, still unfixed in **125 of 200 scripts**: a character or
scripture line is spoken, then the **narrator repeats it almost word-for-word**. The
story law already required removing this ("drop the narrator→scripture echo") — it did
not happen. Do it now.

## The job
The full hit-list is **`media-production/ECHO-SWEEP-FOR-AGENT-1.md`** — 232 pairs, grouped
by build, each showing the two adjacent lines and an echo score (`1.0` = word-for-word).

For every pair:
1. Open that build's transcript source: **`media-production/build-NN-*/make_narration.py`**
   (the `SEGMENTS` list — each entry is `(id, speaker, text)`).
2. **Keep** the character/scripture line. **Delete** the narrator line that repeats it —
   OR rewrite the narrator line so it adds *genuinely new* meaning and never restates the
   quote. Never say the same thing twice.
3. Do NOT touch `assets/` (pictures = #3), the caption engine, or `build.py` logic (#4).
   You only edit the words in `SEGMENTS`.
4. Because the words changed, the old audio no longer matches — mark the build for re-voice
   so #2 re-renders it: `rm -f media-production/build-NN-*/.eleven-done media-production/build-NN-*/.audio-eleven-done`
   (deleting the markers tells #2 the audio is stale, and stops #4 from posting the old cut).

## Verify your own work (target: ZERO)
```bash
python3 media-production/echo_scan.py | tail -1
```
Re-run after editing. It prints `TOTAL echo pairs: N`. Keep going until N is 0 (or every
remaining pair is a deliberate keep you can defend to Cameron).

## Hand-off chain
#1 (this) edits words + clears markers → #2 re-voices → #4 auto re-captions & re-posts the
clean cut to the review board. Cameron then reviews it once.
