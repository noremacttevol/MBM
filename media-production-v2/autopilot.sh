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

# --- up to LANES builds in parallel (Cameron, 2026-08-06: "it shouldnt take
# that long") — claim-by-push inside the brief keeps lanes off each other's
# rows; each tick starts at most ONE new lane so starts stay staggered.
LANES="${MBM_LANES:-6}"
LOCKDIR="$V2/.autopilot-lanes"
mkdir -p "$LOCKDIR"
LIVE=0
for f in "$LOCKDIR"/lane-*.pid "$LOCK"; do
  [ -e "$f" ] || continue
  if kill -0 "$(cat "$f" 2>/dev/null)" 2>/dev/null; then LIVE=$((LIVE+1)); else rm -f "$f"; fi
done
if [ "$LIVE" -ge "$LANES" ]; then
  [ "$DRY" -eq 1 ] && echo "(dry) all $LANES lanes busy"
  exit 0
fi
if [ "$DRY" -eq 0 ]; then
  SLOT="$LOCKDIR/lane-$$.pid"
  echo $$ > "$SLOT"
  trap 'rm -f "$SLOT"' EXIT
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
# A RUNNING row claimed 'A-auto' with no build in flight (we hold the lock, so
# nothing autopilot-owned is running) is a stranded row from a dead run.
next_stranded() {
  awk -F'|' '/^\| *[0-9]+ *\|/ {
    row=$2; state=$4; claim=$7
    gsub(/[^0-9]/,"",row); gsub(/[[:space:]]/,"",state)
    if (state=="RUNNING" && claim ~ /A-auto/) { print row; exit }
  }' "$BOARD"
}

# Only resume a stranded row when NO lanes are live (otherwise the "stranded"
# row may be another lane's active build). After a crash/reboot, lanes are 0
# and stranded rows get picked up first.
STRANDED=""
[ "$LIVE" -eq 0 ] && STRANDED="$(next_stranded || true)"
READY="$(next_ready || true)"
UNAUTHORED="$(next_unauthored || true)"

if [ -n "$STRANDED" ]; then
  JOB="resume"; ROW="$STRANDED"
  PROMPT="Read media-production-v2/PROMPT-OPUS-RUNNER.md. A previous autopilot run DIED mid-build on AUTHOR-BOARD row $ROW (State RUNNING, Claim A-auto) — RESUME that row, do not start a new one. Read the build's QC.md for where it stopped; v2_gen_api.py resumes automatically (already-passing frames are never re-pulled — the COST LAW). You are UNATTENDED and HEADLESS: ending your turn kills the session, so run EVERY command in the FOREGROUND to completion; never use run_in_background, never wait for notifications. Finish the row through step 7c DEPLOY + live verification, set the board row BUILT, SESSION-LOG entry, commit, push."
  MODEL_ARGS=(--model opus)
elif [ -n "$READY" ]; then
  JOB="runner"; ROW="$READY"
  PROMPT="Read media-production-v2/PROMPT-OPUS-RUNNER.md and run the next ready rows. You are UNATTENDED and HEADLESS (autopilot): Cameron is not watching and cannot answer — never wait for him, never ask. HEADLESS LAW: the moment you end your turn the session is DEAD — there are no background-task notifications and no next turn. Run EVERY command in the FOREGROUND and wait for it to finish (v2_gen_api.py etc. are synchronous and resume if re-run); NEVER use run_in_background, NEVER end a message with 'waiting for' anything. Before generating, cross-check the row against media-production/QUEUE.md — if the QUEUE says the story was swapped or replaced, do NOT build it: park it on AUTHOR-BOARD (note in Claim, clear Ready), push, take the next row. Also set the row's AUTHOR-BOARD State to RUNNING with Claim 'A-auto <date>' when you claim, and BUILT when shipped. Follow the brief literally including the LEARNING LAW (complaint ledger in QC.md), the COST LAW (reroll budget), and step 7c DEPLOY + live verification. If truly blocked on a row, write the blocker and resume command into that build's QC.md, park the claim, push, and move to the next ready row. Stop cleanly (SESSION-LOG entry, commit, push) when context runs low."
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
