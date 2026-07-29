#!/usr/bin/env bash
# CLEAN-AUDIO SWEEP — strip the background room tone from audio that was ALREADY
# voiced, then re-render and ship. Costs NO ElevenLabs credits: it only filters
# existing mp3s (highpass + afftdn, same chain as mbm_eleven.clean_clip) and
# re-renders the video. Clips voiced from now on are cleaned at render time.
#
# Cameron, 2026-07-25: "most of them still have the background sound problem."
# Measured: the voices carry room tone (-47 dB between words on scripture vs -80 dB
# on the narrator) and build.py adds ~+8 dB of loudness gain, making it audible.
#
# Safe to re-run: a clip already cleaned is marked with a .cleaned stamp and skipped.
# Duration is preserved bit-for-bit, so caption timing stays in sync.
#
# Usage:
#   bash admin/clean_audio_sweep.sh              # every build with audio
#   bash admin/clean_audio_sweep.sh 27 84 151    # only these
#   NORENDER=1 bash admin/clean_audio_sweep.sh   # clean the audio, don't re-render
set -u
cd "$(dirname "$0")/.." || exit 1
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
MP=media-production
LOG=admin/clean_audio_sweep.log
say(){ echo "[$(date '+%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

if [ "$#" -gt 0 ]; then LIST="$*"; else LIST=$(seq 1 200); fi
CHAIN="highpass=f=75,afftdn=nf=-32:nt=w"
CLEANED=0; RENDERED=0

for n in $LIST; do
  d=$(ls -d "$MP"/build-$(printf '%02d' "$n")-* 2>/dev/null | grep -v _stale | head -1)
  [ -z "$d" ] && continue
  [ -d "$d/audio" ] || continue
  [ -f "$d/.audio-cleaned" ] && continue          # already done

  did=0
  for f in "$d"/audio/*.mp3; do
    [ -e "$f" ] || continue
    # only touch real ElevenLabs clips; never re-encode an old 24000 Hz file
    sr=$(ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate -of csv=p=0 "$f" 2>/dev/null)
    [ "$sr" = "44100" ] || continue
    before=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f" 2>/dev/null)
    if ffmpeg -y -v error -i "$f" -af "$CHAIN" -c:a libmp3lame -b:a 128k -ar 44100 "$f.tmp.mp3" 2>/dev/null; then
      after=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f.tmp.mp3" 2>/dev/null)
      # refuse anything that shifts the timeline (captions are built from these times)
      ok=$(awk -v a="$before" -v b="$after" 'BEGIN{d=a-b; if(d<0)d=-d; print (d<=0.02)?"y":"n"}')
      if [ "$ok" = "y" ] && [ -s "$f.tmp.mp3" ]; then mv "$f.tmp.mp3" "$f"; did=$((did+1));
      else rm -f "$f.tmp.mp3"; fi
    else
      rm -f "$f.tmp.mp3"
    fi
  done
  [ "$did" -eq 0 ] && continue
  touch "$d/.audio-cleaned"
  CLEANED=$((CLEANED+1))
  say "#$n cleaned $did clip(s)"

  [ "${NORENDER:-0}" = "1" ] && continue
  rm -rf "$d/segs"
  if ( cd "$d" && timeout 900 python3 build.py ) >"/tmp/clean-$n.log" 2>&1; then
    RENDERED=$((RENDERED+1)); say "#$n re-rendered"
  else
    say "#$n RENDER FAILED — $(grep -m1 -iE 'error|trace' "/tmp/clean-$n.log" | cut -c1-70)"
  fi
done

say "clean sweep done: $CLEANED build(s) cleaned, $RENDERED re-rendered"
say "next: python3 admin/qc_sweep.py && python3 $MP/gen_site_index.py && firebase deploy --only hosting --project milk-b4-meat"
