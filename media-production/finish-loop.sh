#!/usr/bin/env bash
# AGENT #4 FINISH LOOP — the gated version of caption-and-ship.
# Only finishes GREEN builds (finish_gate.py: echo-clean AND pictures not
# known-bad AND laws pass). As #1 clears echoes and #3 fixes pictures, more
# builds turn green and this loop picks them up on the next run — so it keeps
# going "until there are no more new ones to make" without ever posting a
# known-defective cut.
#
# Usage:
#   bash media-production/finish-loop.sh          # finish every green build now
#   BATCH=3 bash media-production/finish-loop.sh  # cap per run (cron uses this)
set -u
cd "$(dirname "$0")/.." || exit 1
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
GREEN=$(timeout 1200 python3 media-production/finish_gate.py --nums 2>/dev/null)
if [ -z "${GREEN// }" ]; then
  echo "[finish-loop] no green builds — everything left is blocked on #1 (echo) or #3 (pictures)."
  exit 0
fi
echo "[finish-loop] green builds to finish: $GREEN"
exec bash media-production/caption-and-ship.sh $GREEN
