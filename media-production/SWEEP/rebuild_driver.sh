#!/bin/bash
# Rebuild every build in SWEEP/rebuild-list.txt: narration -> video -> verify.
# One line per build lands in SWEEP/rebuild-status.txt (OK/FAIL + mp4 name).
set -u
MP="$(cd "$(dirname "$0")/.." && pwd)"
LIST="$MP/SWEEP/rebuild-list.txt"
LOGD="$MP/SWEEP/rebuild-logs"; mkdir -p "$LOGD"
STATUS="$MP/SWEEP/rebuild-status.txt"; : > "$STATUS"
export MP LOGD STATUS

cut -f1 "$LIST" | xargs -P4 -I{} bash -c '
  b="{}"
  log="$LOGD/$b.log"
  cd "$MP/$b" || { echo "$b FAIL cd" >> "$STATUS"; exit 0; }
  if ! python3 make_narration.py > "$log" 2>&1; then
    echo "$b FAIL narration" >> "$STATUS"; exit 0
  fi
  if ! python3 build.py >> "$log" 2>&1; then
    echo "$b FAIL build" >> "$STATUS"; exit 0
  fi
  mp4=$(ls -t *.mp4 2>/dev/null | head -1)
  if [ -z "$mp4" ]; then echo "$b FAIL no-mp4" >> "$STATUS"; exit 0; fi
  if bash "$MP/../admin/verify-mp4.sh" "$mp4" >> "$log" 2>&1; then
    echo "$b OK $mp4" >> "$STATUS"
  else
    echo "$b FAIL verify" >> "$STATUS"
  fi
'
echo "DRIVER DONE $(wc -l < "$STATUS")/$(wc -l < "$LIST")" >> "$STATUS"
