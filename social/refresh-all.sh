#!/bin/bash
# ONE command = every posting need for every approved video (Cameron, 2026-09-01:
# "i need all posting needs made for each one when i approve the videos").
# Order matters: exports/covers first, sheet before per-video (per-video marks a
# row APPROVED only when it appears in BOTH POST-QUEUE and the regenerated sheet).
# Gate check G verifies the result — a stale kit fails the public-video gate.
set -e
cd "$(dirname "$0")/.."
python3 social/refresh-postable.py
python3 social/make-thumbnails.py
python3 social/make-youtube-sheet.py
python3 social/make-per-video.py
python3 social/make-post-kit.py
echo "---- kit summary ----"
ls social/exports/row-*.mp4 | wc -l | xargs echo "exports:"
ls social/covers/row-*.jpg | wc -l | xargs echo "covers:"
ls social/thumbs/yt/row-*.jpg | wc -l | xargs echo "yt thumbs:"
ls social/thumbs/vertical/row-*.jpg | wc -l | xargs echo "vertical thumbs:"
grep -c '^### Row ' social/POST-QUEUE.md | xargs echo "post-queue entries:"
echo "NOTE: newly postable rows STILL need a POST-QUEUE entry if the appender was"
echo "not run — make-youtube-sheet prints '!! row N: postable but no POST-QUEUE"
echo "entry' for any such row. Append in the same voice, then rerun this script."
