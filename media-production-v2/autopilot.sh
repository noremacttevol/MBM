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
LANES="${MBM_LANES:-4}"
LOCKDIR="$V2/.autopilot-lanes"
mkdir -p "$LOCKDIR"
# Count lanes by LIVE PROCESSES, not pid files — pid files proved deletable
# (a lane's cleanup wiped them on 2026-08-06, which made the counter read 0
# and over-spawn). The timeout wrapper's cmdline is the reliable signature.
LIVE=$(pgrep -fc '^timeout 7200 claude -p' || true)
LIVE=${LIVE:-0}
# pid files kept as a secondary floor + for debugging
FILES=0
for f in "$LOCKDIR"/lane-*.pid "$LOCK"; do
  [ -e "$f" ] || continue
  if kill -0 "$(cat "$f" 2>/dev/null)" 2>/dev/null; then FILES=$((FILES+1)); else rm -f "$f"; fi
done
[ "$FILES" -gt "$LIVE" ] && LIVE=$FILES
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
# Cameron 2026-08-06: "there are some to be just fixed and those would be
# faster and should be done first" — among Ready rows, the one with the MOST
# already-paid banked stills finishes fastest and cheapest, so it goes first.
next_ready() {
  local best="" bestn=-1 row build n
  while read -r row build; do
    n=$(ls "$V2/$build/assets/"*.jpeg 2>/dev/null | wc -l)
    if [ "$n" -gt "$bestn" ]; then best="$row"; bestn="$n"; fi
  done < <(awk -F'|' '/^\| *[0-9]+ *\|/ {
    row=$2; build=$3; state=$4; audio=$6; claim=$7; ready=$8
    gsub(/[^0-9]/,"",row); gsub(/[[:space:]]/,"",build); gsub(/[[:space:]]/,"",state)
    gsub(/[[:space:]]/,"",audio); gsub(/^[[:space:]]+|[[:space:]]+$/,"",claim)
    if (state=="AUTHORED" && audio=="OK" && claim=="" && ready ~ /✅/) print row, build
  }' "$BOARD")
  [ -n "$best" ] && echo "$best"
}
next_unauthored() {
  awk -F'|' '/^\| *[0-9]+ *\|/ {
    row=$2; state=$4; claim=$7
    gsub(/[^0-9]/,"",row); gsub(/[[:space:]]/,"",state)
    gsub(/^[[:space:]]+|[[:space:]]+$/,"",claim)
    if (state=="NEEDS-BEATS" && claim=="") { print row; exit }
  }' "$BOARD"
}
# A RUNNING/A-auto row whose build has NO live v2_gen_api process is stranded —
# its lane died (billing outage, crash). These carry the most banked stills on
# the board, so they resume FIRST even while other lanes work on other rows
# (Cameron 2026-08-06: the just-fix rows should be done first). Per-build
# process check makes this safe alongside live lanes; the resume session also
# verifies shipped-state per RUNNER-LESSONS before spending.
next_stranded() {
  local row build
  while read -r row build; do
    if ! pgrep -f "v2_gen_api.*$build" >/dev/null 2>&1; then
      echo "$row"; return 0
    fi
  done < <(awk -F'|' '/^\| *[0-9]+ *\|/ {
    row=$2; build=$3; state=$4; claim=$7
    gsub(/[^0-9]/,"",row); gsub(/[[:space:]]/,"",build); gsub(/[[:space:]]/,"",state)
    if (state=="RUNNING" && claim ~ /A-auto/) print row, build
  }' "$BOARD")
  return 0
}
# NEEDS-AUDIO rows carry Cameron's open AUDIO complaints (mispronunciations,
# wrong voice, stale V1 renders) — the runner is forbidden to fix them; the
# AUDIO-FIX job (PROMPT-AUDIO-FIX.md) is. Costs $0 Gemini (ElevenLabs/ffmpeg
# only), so it runs even while the Gemini billing breaker is tripped.
next_audio() {
  awk -F'|' '/^\| *[0-9]+ *\|/ {
    row=$2; state=$4; claim=$7
    gsub(/[^0-9]/,"",row); gsub(/[[:space:]]/,"",state)
    if (state=="NEEDS-AUDIO" && claim !~ /AUDIO-FIX/) { print row; exit }
  }' "$BOARD"
}

# --- billing state (checked BEFORE job pick so we can fall back to free work) -
# A depleted Gemini prepayment makes every PAID job die on its first shot.
# Detection: any runner/resume log in the last 25 min reporting depletion.
# Self-heals after top-up (old logs age out of the window). Fail-safe: on any
# find/grep error the flag stays 0 and behavior is unchanged.
BILLING_DOWN=0
if find "$LOGDIR" -maxdepth 1 \( -name '*-runner.log' -o -name '*-resume.log' \) \
     -mmin -25 -print0 2>/dev/null \
   | xargs -0 -r grep -lE 'prepayment credits are depleted|RESOURCE_EXHAUSTED' 2>/dev/null \
   | grep -q .; then
  BILLING_DOWN=1
fi

# Job priority (Cameron 2026-08-06: fastest-to-finish first, complaints get
# fixed, billing-down never idles the loop):
#   billing OK:   stranded-resume (banked stills, cheapest wins) →
#                 audio-fix (MAX ONE audio lane) → ready-build → author
#   billing DOWN: audio-fix → author (paid jobs blocked; free work continues)
STRANDED=""; READY=""
if [ "$BILLING_DOWN" -eq 0 ]; then
  STRANDED="$(next_stranded || true)"
  READY="$(next_ready || true)"
fi
# Audio is capped at ONE lane — it must never starve picture builds
AUDIO=""
AUDIO_LIVE=$(pgrep -fc 'PROMPT-AUDIO-FIX' || true)
[ "${AUDIO_LIVE:-0}" -eq 0 ] && AUDIO="$(next_audio || true)"
UNAUTHORED="$(next_unauthored || true)"

if [ -n "$STRANDED" ]; then
  JOB="resume"; ROW="$STRANDED"
  PROMPT="Read media-production-v2/PROMPT-OPUS-RUNNER.md. A previous autopilot run DIED mid-build on AUTHOR-BOARD row $ROW (State RUNNING, Claim A-auto) — RESUME that row, do not start a new one. Read the build's QC.md for where it stopped; v2_gen_api.py resumes automatically (already-passing frames are never re-pulled — the COST LAW). You are UNATTENDED and HEADLESS: ending your turn kills the session, so run EVERY command in the FOREGROUND to completion; never use run_in_background, never wait for notifications. Finish the row through step 7c DEPLOY + live verification, set the board row BUILT, SESSION-LOG entry, commit, push."
  MODEL_ARGS=(--model opus)
elif [ -n "$AUDIO" ]; then
  JOB="audio"; ROW="$AUDIO"
  PROMPT="Read media-production-v2/PROMPT-AUDIO-FIX.md and fix the next NEEDS-AUDIO rows (lowest first). You are UNATTENDED and HEADLESS (autopilot): Cameron cannot answer — never wait, never ask. HEADLESS LAW: ending your turn kills the session; run EVERY command in the FOREGROUND to completion; never run_in_background, never wait for notifications. Spend NOTHING on Gemini image generation — this job is audio-only (ElevenLabs for re-voiced segments + ffmpeg). Follow each row's QC.md RUNNER PARK note as the per-row authority. Ship through deploy + live verification, answer Cameron's complaint on the review card in his own words, set the board row BUILT with Audio OK, SESSION-LOG entry, commit, push. Stop cleanly when context runs low."
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
  if [ "$BILLING_DOWN" -eq 1 ]; then
    MSG="billing breaker: Gemini prepayment depleted and no free (audio/author) work is open — idle. Top up at https://ai.studio/projects and the loop resumes itself."
  else
    MSG="ALL ROWS BUILT or claimed — nothing to do. If the board is fully BUILT, remove the cron line (see AUTOPILOT.md)."
  fi
  if [ "$DRY" -eq 1 ]; then echo "(dry) $MSG"; else log "$MSG"; fi
  exit 0
fi

if [ "$BILLING_DOWN" -eq 1 ] && [ "$DRY" -eq 0 ]; then
  log "billing breaker active: Gemini paid jobs blocked; running free $JOB work meanwhile. Top up at https://ai.studio/projects to resume picture builds."
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
