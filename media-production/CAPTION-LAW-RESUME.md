# CAPTION LAW — RESUME / HANDOFF (read this first to pick up the job)

**Job:** Fix + upgrade captions on ALL ~199 MBM story videos, then push each so
the review board (https://milk-b4-meat.web.app/review.html, streams from GitHub
`main`) shows them. Started 2026-07-17.

## STATUS RIGHT NOW
- **The look is APPROVED by Cameron.** Rules are locked in `CAPTION-LAW.md`.
- **Shared engine written + working:** `media-production/mbm_caption_timing.py`
- **Font installed:** `media-production/Jost-Bold.ttf` (+ system `~/.local/share/fonts/`)
- **build-06-two-sons is the reference build** — fully migrated to the new engine.
  ⚠️ Its last render was KILLED mid-encode (tool restart). **First action on
  resume: re-run build-06 and verify the dark band shows, then push it.**
- **Nothing else migrated yet.** ~198 builds still on the old caption code.

## WHAT WAS WRONG (root cause, already fixed)
1. Old caption timer guessed each line's on-screen time by CHARACTER COUNT, not
   real speech → captions drifted out of sync + overlapping lines.
   FIX: capture REAL per-sentence timestamps from edge-tts at narration time
   (`save_narration` writes `<seg>.timing.json`); `timed_windows` maps them per
   character → contiguous, non-overlapping windows.
2. Font was curly serif. Cameron wants a TRUE flat-cross "t". Tested many;
   **Jost Bold** is the winner (geometric, native bold, flat "t").
3. Band/layout upgraded to adaptive (see CAPTION-LAW.md).

## THE APPROVED LOOK (full spec in CAPTION-LAW.md)
- Font **Jost Bold**, flat-cross "t". **Jesus's words RED (0xEE3322), narration white.**
- Band pinned to very bottom, full width, **sized to the text** (thin ~5% for 1
  short line, up to ~13% for 3 lines; MAX 3 lines). Medium-dark `black@0.5`.
- Each line individually centered (`text_align=C`). 56px side margins.
- Real-timing sync, no overlap. Locked 1080x1920 zoom-crop.

## KEY TECHNICAL GOTCHA (cost an hour — don't repeat)
`drawbox` on a TRANSPARENT rgba overlay layer leaves alpha=0 → the band is
INVISIBLE when composited. **The band + text MUST be drawn directly on the
opaque still**, time-gated with `enable='between(t,cs,ce)'`. That's why the API
is now `caption_filter()` (returns a filter string appended to the base chain),
NOT the old `caption_layers()` overlay approach. `caption_layers` now raises on
purpose to catch un-migrated builds.

## HOW TO MIGRATE ONE BUILD (the repeatable recipe)
Per `build-NNN/`:
1. `cp media-production/mbm_caption_timing.py build-NNN/`
2. `make_narration.py`: add `from mbm_caption_timing import save_narration`;
   in `main()` replace `tts=Communicate(...); await tts.save(f"audio/{name}.mp3")`
   with `await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")`
   (use `SPOKEN.get(name, text)` as the text arg if that build has a SPOKEN dict).
3. `build.py`:
   - import: `from mbm_caption_timing import caption_filter`
   - delete the local `caption_layers` + `chunk_caption`/`sentences` if present
     (module provides them). Keep local `LEAD`.
   - in `build_still`, replace the overlay block with:
     ```python
     cap = caption_filter(seg_id, dur, spoken_end, cap_text, kjv)
     tail = ",fade=t=in:st=0:d=1.0" if first else ""
     fc = f"{base}{cap}{tail}[v]"
     run([FF,"-y","-loop","1","-i",f"{A}/{src}","-t",str(dur),
          "-filter_complex",fc,"-map","[v]"]+ENC+[f"{S}/{seg_id}.mp4"])
     ```
4. `python3 make_narration.py` (regens audio + timing sidecars)
5. `python3 build.py` (rebuild mp4; ~2-4 min encode)
6. Verify: grab frames mid-sentence, confirm band shows + text synced + no overlap.
7. `git add build-NNN/ && git commit && git push` — board updates from GitHub.

NOTE: build folders vary. Some have `SERIF_BI`/`POPPINS` leftovers, `SPOKEN`
dicts, different segment names, KJV sets. The recipe holds but READ each build.py
before patching. A rollout script `apply_caption_law.py` should be written to do
this in a loop with verification + a manifest of pass/fail.

## VERIFY-BEFORE-DONE
For each build, an ad-hoc check (see prior /tmp hermes-verify scripts): one
window per chunk, no overlap, monotonic, real timing used, last caption clears
just after speech. Plus eyeball 2 frames (one narration, one KJV-red).

## REPO PATHS
- Engine: `media-production/mbm_caption_timing.py`
- Spec (law): `media-production/CAPTION-LAW.md`
- Font: `media-production/Jost-Bold.ttf`
- Reference build: `media-production/build-06-two-sons/` (build.py + make_narration.py migrated)
- Review board source: videos stream from `github.com/noremacttevol/MBM/raw/main/media-production/build-NNN/<file>.mp4`

## DONE SO FAR ON THE BOARD
- build-65 (help-mine-unbelief) + build-06 (two-sons) were pushed earlier with
  the TIMING fix, but BEFORE the font/band upgrade. Both need a final rebuild
  under the full new law. (65 isn't even on the live board — board skips 65/66/67.)
