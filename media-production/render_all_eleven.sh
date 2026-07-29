#!/bin/bash
# Full 204-video ElevenLabs re-render (2026-07-23). Resumable: a build that already
# finished on the current script writes .eleven-done and is skipped on re-run.
# Audio (the paid ElevenLabs chars) is generated once; assembly can be re-run free
# when the stills computer lands fixes.
cd ~/Desktop/MBM/media-production || exit 1
export MBM_TTS=eleven
MASTER=ELEVEN-RENDER.log
echo "=== full render started $(date) ===" >> "$MASTER"

done=0; fail=0; skip=0
for d in build-*/; do
  b=${d%/}
  [ -f "$b/make_narration.py" ] || continue
  # skip if finished after the current script version
  if [ -f "$b/.eleven-done" ] && [ "$b/.eleven-done" -nt "$b/make_narration.py" ]; then
    skip=$((skip+1)); continue
  fi
  # sync the new engine into the build (its local module copies are older)
  cp mbm_eleven.py mbm_pronounce.py mbm_caption_timing.py mbm_speakers.py "$b/" 2>/dev/null
  rm -rf "$b/audio" "$b/segs"            # force fresh ElevenLabs audio + reassembly
  ( cd "$b" && MBM_TTS=eleven python3 make_narration.py && MBM_TTS=eleven python3 build.py ) \
      > "$b/eleven.log" 2>&1
  if ls "$b"/*.mp4 >/dev/null 2>&1 && [ -z "$(find "$b" -maxdepth 1 -name '*.mp4' -newer "$b/make_narration.py" -prune -o -print 2>/dev/null)" ]; then
    : # fallthrough
  fi
  # success = an mp4 exists and build.py printed DONE
  if grep -q "^DONE:" "$b/eleven.log" 2>/dev/null; then
    touch "$b/.eleven-done"; done=$((done+1))
    echo "OK   $b  $(grep '^DONE:' "$b/eleven.log" | tail -1 | sed 's/^DONE: //')" >> "$MASTER"
  else
    fail=$((fail+1))
    echo "FAIL $b  (see $b/eleven.log: $(tail -1 "$b/eleven.log" 2>/dev/null | cut -c1-80))" >> "$MASTER"
  fi
  echo "progress: done=$done fail=$fail skip=$skip  last=$b" >> "$MASTER"
done
echo "=== full render finished $(date)  done=$done fail=$fail skip=$skip ===" >> "$MASTER"
