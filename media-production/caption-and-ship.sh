#!/usr/bin/env bash
# MBM CAPTION-AND-SHIP — the dedicated "captions + posting + board" loop.
# Cameron's ask (2026-07-23): other sessions render NEW ElevenLabs audio + new
# Flow stills into build-NN folders; THIS step turns those into freshly-captioned
# videos and posts them to the review website so he can review fresh.
#
# THE GAP THIS FILLS: admin/ship-fixes.sh already auto-ships (cron */15) any
# finished-but-dirty mp4 to GitHub + the Firebase review board. But nothing
# re-runs build.py when new audio/stills land, so the captioned video never gets
# regenerated. This script IS that missing re-caption step.
#
# A build is READY FOR RE-CAPTION when its ElevenLabs marker (.eleven-done or
# .audio-eleven-done, written by the audio session) is newer than the finished
# root .mp4 — i.e. new audio exists but the captioned video is stale. (No mp4 =
# also ready.) build.py reads audio/*.mp3 + assets/ stills and burns fresh
# caption timing, so re-running it is safe and idempotent.
#
# Order per build: render (build.py) -> verify-mp4 (truncated-mp4 gate) -> hand
# to admin/ship-fixes.sh (approved-lock, one small commit, push, board deploy).
#
# Usage:
#   bash media-production/caption-and-ship.sh              # all stale eleven builds
#   bash media-production/caption-and-ship.sh 02 04 05     # only these numbers
#   BATCH=4 bash media-production/caption-and-ship.sh      # cap to 4 per run (for cron)
#   RENDER_ONLY=1 bash media-production/caption-and-ship.sh  # caption, don't ship
set -u
cd "$(dirname "$0")/.." || exit 1
REPO=$PWD
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
LOG=media-production/caption-and-ship.log
LOCK=/tmp/mbm-caption-and-ship.lock
exec 8>"$LOCK"; flock -n 8 || { echo "another caption run in progress"; exit 0; }
say() { echo "[$(date '+%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

root_mp4() { find "$1" -maxdepth 1 -name '*_*.mp4' 2>/dev/null | head -1; }
has_marker() { [ -f "$1/.eleven-done" ] || [ -f "$1/.audio-eleven-done" ]; }
# Newest input signal from the upstream agents: #2's ElevenLabs audio markers +
# audio/*.mp3, and #3's fixed stills in assets/. A rebuild is due when any of
# these is newer than the captioned mp4.
input_mtime() {
  { stat -c%Y "$1/.eleven-done" "$1/.audio-eleven-done" 2>/dev/null
    find "$1/audio" "$1/assets" -type f \( -name '*.mp3' -o -name '*.jpeg' \
      -o -name '*.jpg' -o -name '*.png' \) -printf '%Y@%T@\n' 2>/dev/null | cut -d@ -f2 | cut -d. -f1
  } | sort -rn | head -1
}

# --- pick candidate build dirs ----------------------------------------------
if [ "$#" -gt 0 ]; then
  DIRS=""
  for n in "$@"; do DIRS="$DIRS $(ls -d media-production/build-$(printf '%02d' "$n")-* 2>/dev/null)"; done
else
  DIRS=$(ls -d media-production/build-[0-9]* 2>/dev/null)
fi

# --- which are stale: eleven marker newer than the captioned mp4 -------------
STALE=""
for d in $DIRS; do
  [ -f "$d/build.py" ] || continue
  has_marker "$d" || continue           # only builds that got ElevenLabs audio
  mp4=$(root_mp4 "$d")
  if [ -z "$mp4" ]; then STALE="$STALE $d"; continue; fi
  mt=$(stat -c%Y "$mp4" 2>/dev/null || echo 0)
  em=$(input_mtime "$d"); em=${em:-0}
  [ "$em" -gt "$((mt + 30))" ] && STALE="$STALE $d"
done

# ascending by build number, cap to BATCH if set
STALE=$(for d in $STALE; do printf '%s\t%s\n' "$(basename "$d" | sed -E 's/build-0*([0-9]+).*/\1/')" "$d"; done | sort -n | cut -f2)
if [ -n "${BATCH:-}" ]; then STALE=$(echo "$STALE" | head -n "$BATCH"); fi

if [ -z "$(echo "$STALE" | tr -d '[:space:]')" ]; then
  say "nothing stale — every ElevenLabs build is already captioned into video."; STALE=""
else
  say "re-captioning: $(echo $STALE | xargs -n1 basename 2>/dev/null | tr '\n' ' ')"
fi

# --- re-caption each ---------------------------------------------------------
READY=0
for d in $STALE; do
  b=$(basename "$d")
  say "RENDER $b"
  ( cd "$d" && timeout 900 python3 build.py ) >>"$LOG" 2>&1
  mp4=$(root_mp4 "$d")
  if [ -z "$mp4" ] || ! bash admin/verify-mp4.sh "$mp4" >/dev/null 2>&1; then
    say "BLOCK  $b: render failed or verify-mp4 failed — NOT shipping"
    continue
  fi
  say "OK     $b: $(basename "$mp4")"
  READY=$((READY + 1))
done

# --- ship + refresh the board ------------------------------------------------
if [ "${RENDER_ONLY:-0}" = "1" ]; then say "RENDER_ONLY — captioned $READY, not shipping."; exit 0; fi
if [ "$READY" -gt 0 ]; then
  say "handing $READY verified cut(s) to ship-fixes.sh (push + board deploy)"
  bash admin/ship-fixes.sh
fi
say "done ($READY captioned this run)."
