#!/bin/bash
# Render ONE build on ElevenLabs. Safe to run in parallel (isolated build dir).
b="$1"
cd ~/Desktop/MBM/media-production || exit 1
export MBM_TTS=eleven
[ -f "$b/make_narration.py" ] || exit 0
if [ -f "$b/.eleven-done" ] && [ "$b/.eleven-done" -nt "$b/make_narration.py" ]; then exit 0; fi
cp mbm_eleven.py mbm_pronounce.py mbm_caption_timing.py mbm_speakers.py "$b/" 2>/dev/null
rm -rf "$b/audio" "$b/segs"
( cd "$b" && MBM_TTS=eleven python3 make_narration.py && MBM_TTS=eleven python3 build.py ) > "$b/eleven.log" 2>&1
if grep -q "^DONE:" "$b/eleven.log" 2>/dev/null; then
  touch "$b/.eleven-done"
  echo "OK   $b  $(grep '^DONE:' "$b/eleven.log" | tail -1 | sed 's/^DONE: //')" >> ELEVEN-RENDER.log
else
  echo "FAIL $b  ($(tail -1 "$b/eleven.log" 2>/dev/null | cut -c1-90))" >> ELEVEN-RENDER.log
fi
