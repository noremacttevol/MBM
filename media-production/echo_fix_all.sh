#!/usr/bin/env bash
# Fix the narrator echo across EVERY flagged build: echo_fix.py (trim repeat +
# re-voice via ElevenLabs) -> build.py (re-caption) -> verify-mp4. Leaves each
# rebuilt cut dirty for the ship step. Resumable: skips builds already clean.
set -u
cd "$(dirname "$0")/.." || exit 1
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
LOG=media-production/echo-fix.log
LOCK=/tmp/mbm-echo-fix.lock
exec 7>"$LOCK"; flock -n 7 || { echo "echo-fix already running"; exit 0; }
say() { echo "[$(date '+%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

NUMS=$(python3 media-production/echo_scan.py 2>/dev/null | grep -oE '^## build-0*[0-9]+' | grep -oE '[0-9]+' | sort -n | uniq)
[ -z "$NUMS" ] && { say "no echoes left — all clean."; exit 0; }
say "echo builds to fix: $(echo $NUMS | tr '\n' ' ')"

ok=0; fail=0
for n in $NUMS; do
  d=$(ls -d media-production/build-$(printf '%02d' "$n")-* 2>/dev/null | head -1)
  [ -z "$d" ] && continue
  b=$(basename "$d")
  if ! python3 media-production/echo_fix.py "$n" >>"$LOG" 2>&1; then
    say "SKIP  $b: echo_fix found nothing / errored"; continue
  fi
  ( cd "$d" && timeout 900 python3 build.py ) >>"$LOG" 2>&1
  mp4=$(find "$d" -maxdepth 1 -name '*_*.mp4' | head -1)
  if [ -n "$mp4" ] && bash admin/verify-mp4.sh "$mp4" >/dev/null 2>&1; then
    say "FIXED $b"; ok=$((ok+1))
  else
    say "BUILD-FAIL $b (restoring script from .pre-echo)"
    [ -f "$d/make_narration.py.pre-echo" ] && cp "$d/make_narration.py.pre-echo" "$d/make_narration.py"
    fail=$((fail+1))
  fi
done
say "echo pass done: $ok fixed, $fail failed. Remaining: $(python3 media-production/echo_scan.py 2>/dev/null | tail -1)"
