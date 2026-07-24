#!/bin/bash
# VOICE GATE — proves a build's narration is real ElevenLabs audio (44100 Hz),
# not the old edge-tts voice (24000 Hz). The ship lane (#4) MUST call this and
# refuse to caption/ship any build that fails.
#
# Usage:   verify-eleven-audio.sh build-41-counting-the-cost
# Exit 0 = every audio clip is 44100 Hz and non-trivial (safe to ship).
# Exit 1 = at least one clip is wrong voice / missing / truncated (BLOCK it).
b="${1%/}"
[ -d "$b/audio" ] || { echo "GATE-FAIL $b : no audio/ folder"; exit 1; }
mp3s=$(ls "$b"/audio/*.mp3 2>/dev/null)
[ -n "$mp3s" ] || { echo "GATE-FAIL $b : no mp3 clips"; exit 1; }
bad=0
for f in $mp3s; do
  r=$(ffprobe -v quiet -select_streams a:0 -show_entries stream=sample_rate -of csv=p=0 "$f")
  sz=$(stat -c %s "$f" 2>/dev/null || echo 0)
  if [ "$r" != "44100" ]; then echo "  BAD $f : sample_rate=$r (old edge-tts is 24000)"; bad=1; fi
  if [ "$sz" -lt 2000 ]; then echo "  BAD $f : size=$sz bytes (truncated)"; bad=1; fi
done
if [ "$bad" -eq 0 ]; then
  echo "GATE-OK   $b : all $(echo "$mp3s" | wc -w) clips are 44100 Hz ElevenLabs"
  exit 0
else
  echo "GATE-FAIL $b : has non-ElevenLabs or truncated audio — DO NOT SHIP"
  exit 1
fi
