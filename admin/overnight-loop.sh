#!/usr/bin/env bash
# MBM OVERNIGHT LOOP — the unattended "wake up to the best 200 on the board" run.
# One cycle: pull new stills/audio the still-maker PC pushed -> finish every GREEN
# build (finish_gate: echo-clean AND pictures ok AND laws pass) with fresh captions
# over its existing audio -> ship finished cuts to the review board. Safe to cron:
# flock-guarded, approved-lock enforced by ship-fixes, only green builds finished.
# Does NOT need the ElevenLabs key (captions over existing audio); the voice UPGRADE
# is the only thing that waits on a fresh key in "elevenlabs API KEY.txt".
set -u
# SAFETY INTERLOCK (2026-07-28): this loop was still installed in cron while the
# worktree was tens of gigabytes dirty and in a conflicted rebase state.  It kept
# rebuilding rejected cuts, committing generated scratch, attempting 11+ GB
# pushes, and redeploying the board every 15 minutes.  Cron is disabled too, but
# fail closed here so reinstalling an old crontab cannot restart the damage.
if [ "${MBM_ENABLE_OVERNIGHT_LOOP:-}" != "reviewed-and-enabled" ]; then
  echo "overnight-loop is safety-disabled; set MBM_ENABLE_OVERNIGHT_LOOP=reviewed-and-enabled only after repairing the worktree and ship pipeline"
  exit 0
fi
cd "$(dirname "$0")/.." || exit 1
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
LOCK=/tmp/mbm-overnight.lock
exec 7>"$LOCK"; flock -n 7 || exit 0
LOG=admin/overnight-loop.log
exec >>"$LOG" 2>&1
echo "[$(date '+%m-%d %H:%M:%S')] ---- overnight cycle start ----"
git -c rebase.autostash=true pull --rebase -q origin main 2>/dev/null || true
BATCH="${BATCH:-4}" bash media-production/finish-loop.sh || true
bash admin/ship-fixes.sh || true
echo "[$(date '+%m-%d %H:%M:%S')] ---- overnight cycle end ----"
