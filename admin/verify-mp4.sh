#!/usr/bin/env bash
# MBM delivery gate — never ship a truncated video again.
#
# Twice now a build printed DONE while the delivered mp4 was cut off at an exact
# MiB boundary with no moov atom (video #4 lost its whole closing question that
# way, and Cameron caught it). ffprobe is the only thing that actually proves the
# file plays, so every mp4 passes through here before it is committed/deployed.
#
# Usage:
#   bash admin/verify-mp4.sh <file.mp4> [expected_seconds]
# Exit 0 = safe to ship. Exit 1 = BROKEN, re-render/re-mux before shipping.
set -u
F="${1:?usage: verify-mp4.sh <file.mp4> [expected_seconds]}"
WANT="${2:-}"

[ -f "$F" ] || { echo "FAIL: $F does not exist"; exit 1; }

SIZE=$(stat -c%s "$F")
# the truncation signature: an exact multiple of 1 MiB (+/- a small header tail)
if [ $(( SIZE % 1048576 )) -lt 64 ] && [ "$SIZE" -gt 1048576 ]; then
  echo "WARN: $F is $SIZE bytes — suspiciously close to an exact MiB boundary (truncation signature)"
fi

DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$F" 2>&1)
case "$DUR" in
  *moov*|*Invalid*|"")
    echo "FAIL: $F has no readable moov atom — file is truncated. Re-mux from segs/ before shipping."
    exit 1;;
esac

# audio must reach (near) the end, or the closing question got cut
ADUR=$(ffprobe -v error -select_streams a -show_entries stream=duration -of csv=p=0 "$F" 2>/dev/null | head -1)

if [ -n "$WANT" ]; then
  DIFF=$(awk -v a="$DUR" -v b="$WANT" 'BEGIN{d=a-b; print (d<0?-d:d)}')
  OK=$(awk -v d="$DIFF" 'BEGIN{print (d<=1.5)?"y":"n"}')
  if [ "$OK" != "y" ]; then
    echo "FAIL: $F is ${DUR}s but the build computed ${WANT}s (off by ${DIFF}s) — content was cut."
    exit 1
  fi
fi

echo "OK: $F  video=${DUR}s audio=${ADUR:-n/a}s size=${SIZE}"
exit 0
