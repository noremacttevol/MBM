#!/bin/bash
# Drive the full 204-build ElevenLabs render, 4 builds in parallel. Resumable.
cd ~/Desktop/MBM/media-production || exit 1
echo "=== parallel render started $(date) ===" >> ELEVEN-RENDER.log
ls -d build-*/ | sed 's#/##' | xargs -P 4 -I{} bash render_one_eleven.sh {}
d=$(ls build-*/.eleven-done 2>/dev/null | wc -l)
echo "=== parallel render finished $(date)  done=$d/204 ===" >> ELEVEN-RENDER.log
