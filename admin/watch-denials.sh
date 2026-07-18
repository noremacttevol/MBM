#!/usr/bin/env bash
# MBM denial lookout — polls Cameron's review board and prints a line ONLY when
# the set of active complaints changes. Each printed line becomes a notification
# to the denial-fix machine, so a new "no" from Cameron surfaces on its own — he
# never has to relay it.
#
# Usage:  bash admin/watch-denials.sh [interval_seconds]
set -u
cd "$(dirname "$0")/.." || exit 1
INTERVAL="${1:-90}"
LAST=""
while true; do
  git -c rebase.autostash=true pull --rebase >/dev/null 2>&1 || true
  node admin/sync-reviews.mjs >/dev/null 2>&1 || true
  # signature = every active complaint row (video # + words), stable-sorted
  CUR="$(grep -E '^\| [0-9]' media-production/COMPLAINTS.md 2>/dev/null | sort)"
  if [ "$CUR" != "$LAST" ]; then
    if [ -z "$CUR" ]; then
      echo "BOARD CLEAR — 0 active complaints"
    else
      echo "NEW DENIAL STATE:"
      echo "$CUR"
    fi
    LAST="$CUR"
  fi
  sleep "$INTERVAL"
done
