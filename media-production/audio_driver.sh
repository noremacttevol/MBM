#!/bin/bash
# Drive ElevenLabs AUDIO-ONLY generation across all builds, 6 in parallel. Resumable.
cd ~/Desktop/MBM/media-production || exit 1
echo "=== audio-only render started $(date) ===" >> AUDIO-RENDER.log
ls -d build-*/ | sed 's#/##' | xargs -P 6 -I{} bash audio_one_eleven.sh {}
d=$(ls build-*/.audio-eleven-done 2>/dev/null | wc -l)
echo "=== audio-only render finished $(date)  done=$d ===" >> AUDIO-RENDER.log
