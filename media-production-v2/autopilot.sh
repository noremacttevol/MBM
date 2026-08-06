#!/usr/bin/env bash
#
# autopilot.sh — the V2 loop: build the next ready row unattended, repeat
# until all 200 are done. This is what the cron runs. Safe to run by hand.
#
#   ./autopilot.sh            # one tick: if idle and work exists, run one builder session
#   ./autopilot.sh --dry-run  # show what the next tick WOULD do; touch nothing
#
# Design (Cameron, 2026-08-06 — "make this into a loop process until its done"):
# - ONE build at a time (PID lock). A tick while a build runs does nothing.
# - Each run is a FRESH headless Claude session reading PROMPT-OPUS-RUNNER.md,
#   so every run starts from the laws (learning law, cost law, complaint
#   ledger, deploy step) with clean context — the "one video per chat" rule.
# - Claim-by-push inside the runner brief keeps this loop and any interactive
#   chat off each other's rows.
# - When no Ready rows remain but NEEDS-BEATS rows exist, the tick runs an
#   AUTHOR session instead. When the whole board is BUILT, ticks do nothing
#   and say so — then remove the cron line (see AUTOPILOT.md).
# - 2-hour hard timeout per run so a wedged session can never hold the lock.

set -euo pipefail
export PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin"

REPO="${MBM_REPO:-$HOME/Desktop/MBM}"
V2="$REPO/media-production-v2"
BOARD="$V2/AUTHOR-BOARD.md"
LOCK="$V2/.autopilot.lock"
LOGDIR="$V2/autopilot-logs"
TS="$(date +%Y%m%d-%H%M%S)"
DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1

mkdir -p "$LOGDIR"
log() { echo "[$(date '+%F %T')] $*" | tee -a "$LOGDIR/autopilot.log"; }

# --- one build at a time -----------------------------------------------------
if [ -e "$LOCK" ] && kill -0 "$(cat "$LOCK" 2>/dev/null)" 2>/dev/null; then
  [ "$DRY" -eq 1 ] && echo "(dry) a build is already running (lock $LOCK)"
  exit 0
fi
if [ "$DRY" -eq 0 ]; then
  echo $$ > "$LOCK"
  trap 'rm -f "$LOCK"' EXIT
fi

cd "$REPO"
[ "$DRY" -eq 0 ] && git pull --rebase --autostash origin main -q

# --- what work exists? -------------------------------------------------------
# AUTHOR-BOARD columns: | Row | Build | State | Stills | Audio | Claim | Ready |
next_ready() {
  awk -F'|' '/^\| *[0-9]+ *\|/ {
    row=$2; state=$4; audio=$6; claim=$7; ready=$8
    gsub(/[^0-9]/,"",row); gsub(/[[:space:]]/,"",state); gsub(/[[:space:]]/,"",audio)
    gsub(/^[[:space:]]+|[[:space:]]+$/,"",claim)
    if (state=="AUTHORED" && audio=="OK" && claim=="" && ready ~ /✅/) { print row; exit }
  }' "$BOARD"
}
next_unauthored() {
  awk -F'|' '/^\| *[0-9]+ *\|/ {
    row=$2; state=$4; claim=$7
    gsub(/[^0-9]/,"",row); gsub(/[[:space:]]/,"",state)
    gsub(/^[[:space:]]+|[[:space:]]+$/,"",claim)
    if (state=="NEEDS-BEATS" && claim=="") { print row; exit }
  }' "$BOARD"
}

READY="$(next_ready || true)"
UNAUTHORED="$(next_unauthored || true)"

if [ -n "$READY" ]; then
  JOB="runner"; ROW="$READY"
  PROMPT="Read media-production-v2/PROMPT-OPUS-RUNNER.md and run the next ready rows. You are UNATTENDED (autopilot): Cameron is not watching and cannot answer — never wait for him, never ask, follow the brief literally including the LEARNING LAW (complaint ledger in QC.md), the COST LAW (reroll budget), and step 7c DEPLOY + live verification. If truly blocked on a row, write the blocker and resume command into that build's QC.md, push, and move to the next ready row. Stop cleanly (SESSION-LOG entry, commit, push) when context runs low."
  MODEL_ARGS=(--model opus)
elif [ -n "$UNAUTHORED" ]; then
  JOB="author"; ROW="$UNAUTHORED"
  PROMPT="Read media-production-v2/PROMPT-FABLE5-AUTHOR.md and do the next rows. You are UNATTENDED (autopilot): never wait for Cameron; spend \$0 on generation exactly as the brief says; stop cleanly with the chain (SESSION-LOG entry, commit, push) when context runs low."
  MODEL_ARGS=()
else
  log "ALL ROWS BUILT or claimed — nothing to do. If the board is fully BUILT, remove the cron line (see AUTOPILOT.md)."
  exit 0
fi

if [ "$DRY" -eq 1 ]; then
  echo "(dry) next tick would start a $JOB session at row $ROW"
  exit 0
fi

log "tick: starting $JOB session (next open row $ROW) → $LOGDIR/$TS-$JOB.log"
timeout 7200 claude -p "$PROMPT" \
  --dangerously-skip-permissions \
  "${MODEL_ARGS[@]}" \
  > "$LOGDIR/$TS-$JOB.log" 2>&1 || log "run $TS-$JOB exited nonzero ($?) — see its log"
log "tick done: $TS-$JOB"
