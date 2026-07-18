#!/usr/bin/env bash
#
# next-job.sh — find the next MBM video to build, claim it, and open a fresh
# Claude chat already pointed at it. This is what the cron runs. It is also
# what you can run by hand any time you want to start the next one.
#
#   ./next-job.sh                 # claim next job, open a fresh chat here in this terminal
#   ./next-job.sh --spawn         # claim next job, open it in a NEW terminal window (for cron)
#   ./next-job.sh --dry-run       # just show what the next job is; touch nothing
#   ./next-job.sh --prep-only     # tell the chat to stop at the Flow/browser step (unattended-safe)
#   ./next-job.sh --number 42     # force a specific story number instead of auto-picking
#
# The Flow picture burst needs a human eye (the Jesus-face rule) and only one
# chat can drive Chrome at a time, so unattended runs should use --prep-only:
# the chat does every local step and stops, ready for you to do the burst.

set -euo pipefail

REPO="${MBM_REPO:-$HOME/Desktop/MBM}"
QUEUE="$REPO/media-production/QUEUE.md"
LOCK="$REPO/media-production/.next-job.lock"
MACHINE="$(hostname)"
TODAY="$(date +%Y-%m-%d)"

DRY_RUN=0; SPAWN=0; PREP_ONLY=0; FORCE_NUM=""
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run)   DRY_RUN=1 ;;
    --spawn)     SPAWN=1 ;;
    --prep-only) PREP_ONLY=1 ;;
    --number)    shift; FORCE_NUM="$1" ;;
    *) echo "unknown arg: $1"; exit 2 ;;
  esac
  shift
done

# --- one job per machine at a time ------------------------------------------
if [ "$DRY_RUN" -eq 0 ]; then
  if [ -e "$LOCK" ] && kill -0 "$(cat "$LOCK" 2>/dev/null)" 2>/dev/null; then
    echo "A build session is already running on $MACHINE (lock: $LOCK). Nothing to do."
    exit 0
  fi
  echo $$ > "$LOCK"
  trap 'rm -f "$LOCK"' EXIT
fi

cd "$REPO"

# --- always start from the truth --------------------------------------------
if [ "$DRY_RUN" -eq 0 ]; then
  git pull --rebase origin main
fi

# --- find the next open row -------------------------------------------------
# next job = lowest-numbered row where Built (col 6) is ⬜ and Claim (col 9) is empty.
pick_next() {
  awk -F'|' '
    /^\| *[0-9]+ *\|/ {
      num=$2; built=$6; claim=$9;
      gsub(/[^0-9]/,"",num);
      gsub(/[[:space:]]/,"",built);
      gsub(/^[[:space:]]+|[[:space:]]+$/,"",claim);
      if (built=="⬜" && claim=="") { print num; exit }
    }' "$QUEUE"
}

get_field() { # $1=number  $2=field index -> trimmed value
  awk -F'|' -v n="$1" -v f="$2" '
    /^\| *[0-9]+ *\|/ {
      num=$2; gsub(/[^0-9]/,"",num);
      if (num==n) { v=$f; gsub(/^[[:space:]]+|[[:space:]]+$/,"",v); print v; exit }
    }' "$QUEUE"
}

if [ -n "$FORCE_NUM" ]; then NUM="$FORCE_NUM"; else NUM="$(pick_next)"; fi

if [ -z "${NUM:-}" ]; then
  echo "🎉 Nothing open in the queue — every story is claimed, built, or done."
  exit 0
fi

STORY="$(get_field "$NUM" 3)"
REF="$(get_field "$NUM" 4)"

echo "── Next job: #$NUM — $STORY ($REF) ──"

if [ "$DRY_RUN" -eq 1 ]; then
  echo "(dry run — nothing claimed, no chat opened)"
  exit 0
fi

# --- claim it in the queue, then push, so no other machine grabs it ---------
SLUG="$(echo "$STORY" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//;s/-$//' | cut -c1-30)"
BUILD_DIR="media-production/build-$(printf '%02d' "$NUM")-$SLUG"
mkdir -p "$REPO/$BUILD_DIR"

# stamp the Claim column (field 9) of this row
tmp="$(mktemp)"
awk -F'|' -v n="$NUM" -v claim=" CLAIMED $MACHINE $TODAY " '
  BEGIN{OFS="|"}
  /^\| *[0-9]+ *\|/ {
    num=$2; gsub(/[^0-9]/,"",num);
    if (num==n) { $9=claim; print; next }
  }
  { print }
' "$QUEUE" > "$tmp" && mv "$tmp" "$QUEUE"

git add "$QUEUE" "$BUILD_DIR" 2>/dev/null || true
git commit -q -m "Claim #$NUM $STORY — $MACHINE" || true
if ! git push -q origin main; then
  echo "Push rejected — another machine claimed while we were working. Retrying with the next open row."
  git pull --rebase origin main
  exec "$0" ${PREP_ONLY:+--prep-only} ${SPAWN:+--spawn}
fi

# --- the primed prompt the fresh chat wakes up with -------------------------
STOP_LINE="When the pictures are ready you may do the Flow burst yourself, but ONE chat drives Chrome at a time — ask Cameron first."
[ "$PREP_ONLY" -eq 1 ] && STOP_LINE="Do every LOCAL step (pack, scripture study, prompt sheet, pass jesus_face_gate.py, narration, build.py, assembly of any banked art). STOP before the Flow/browser picture burst and tell Cameron it is prepped and waiting for his picture burst — do NOT drive Chrome unattended."

PROMPT="You are on MBM video production. Your job this session is ONE video: build #$NUM — $STORY ($REF). The row is already claimed for you as $BUILD_DIR. Read media-production/QUEUE.md (the 'HOW A FRESH CHAT STARTS' block) and follow it from step 4. Read PRODUCTION-BIBLE.md and CREW-GUIDE.md first — every law binds you (face-never, two-voice, stills-only, ear-check, no-dead-air, self-revision). Study the KJV passage in full context before storyboarding. $STOP_LINE Tick Prep/Built in QUEUE.md as you go and push each change. When it is built, tell Cameron it is ready for his one yes."

# --- open a fresh chat on that job ------------------------------------------
if [ "$SPAWN" -eq 1 ]; then
  # new window (for cron; needs DISPLAY set — the cron line exports it)
  gnome-terminal --title="MBM #$NUM $STORY" -- bash -lc "cd '$REPO' && claude '$PROMPT'; exec bash"
else
  # right here in this terminal
  cd "$REPO"
  exec claude "$PROMPT"
fi
