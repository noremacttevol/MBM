#!/usr/bin/env bash
#
# run_queue.sh — the unattended driver for MBM videos.
#
# Builds the queue one video at a time, each in a BRAND-NEW headless Claude
# session, with permissions pre-approved so Cameron is never asked yes/no.
#
# Why one video per session and not a batch of 3-5:
#   PRODUCTION-BIBLE: "Keep each video to ONE chat so context stays low — that is
#   the whole point." A session that builds 5 videos is choking by the 5th, which
#   is exactly the context-death this script exists to kill. One video, fresh
#   context, every time. Cameron clicks nothing either way, so it costs him nothing.
#
# Why bash and not Python: every step is already a shell action — git, claude,
# python scripts, ffmpeg, notify-send. Bash calls them directly with no wrapper.
#
#   ./run_queue.sh                 # run until the checkpoint, then wait for approval
#   ./run_queue.sh --from 38       # start at a specific video
#   ./run_queue.sh --to 200        # stop after a specific video
#   ./run_queue.sh --checkpoint 38 # which video to STOP after for review (default 38)
#   ./run_queue.sh --no-checkpoint # never stop; run straight through (after 38 is approved)
#   ./run_queue.sh --approve       # release a waiting checkpoint from another terminal
#   ./run_queue.sh --status        # print progress and exit
#   ./run_queue.sh --dry-run       # show what it WOULD build; touch nothing
#
set -uo pipefail

REPO="${MBM_REPO:-$HOME/Desktop/Brain/MBM}"
QUEUE="$REPO/media-production/QUEUE.md"
LOGDIR="$REPO/media-production/logs"
APPROVE_FLAG="$REPO/media-production/.APPROVED"
LOCK="$REPO/media-production/.run-queue.lock"
MACHINE="$(hostname)"

CHECKPOINT=38
FROM=""; TO=200; DRY_RUN=0; NO_CHECKPOINT=0; STATUS=0

while [ $# -gt 0 ]; do
  case "$1" in
    --from)          shift; FROM="$1" ;;
    --to)            shift; TO="$1" ;;
    --checkpoint)    shift; CHECKPOINT="$1" ;;
    --no-checkpoint) NO_CHECKPOINT=1 ;;
    --dry-run)       DRY_RUN=1 ;;
    --approve)       touch "$APPROVE_FLAG"; echo "✅ Approved. The waiting run will continue."; exit 0 ;;
    --status)        STATUS=1 ;;
    *) echo "unknown arg: $1"; exit 2 ;;
  esac
  shift
done

mkdir -p "$LOGDIR"

# ── the manifest is QUEUE.md. Columns: | # | Story | Ref | Prep | Built | Appr | Post | Claim |
#    field:  2    3       4     5      6       7      8      9
q_field() { awk -F'|' -v n="$1" -v f="$2" '
  /^\| *[0-9]+ *\|/ { num=$2; gsub(/[^0-9]/,"",num);
    if (num==n) { v=$f; gsub(/^[ \t]+|[ \t]+$/,"",v); print v; exit } }' "$QUEUE"; }

# next job = lowest row where Built is ⬜ and nobody has CLAIMED it.
#
# NOTE: the Claim column is not only used for claims. Rows 181-200 carry the
# delivery note "§IX post-signal" (the Restoration track — produced like any
# other video, but never SURFACED to a viewer until the milk-before-meat signals
# fire, per the BOM law). Treating any non-empty Claim as "owned" made the driver
# skip all 20 of them and stop at #180 while reporting success. A row is only
# claimed if it actually says CLAIMED.
next_open() { awk -F'|' '
  /^\| *[0-9]+ *\|/ { num=$2; built=$6; claim=$9;
    gsub(/[^0-9]/,"",num); gsub(/[ \t]/,"",built);
    if (built=="⬜" && claim !~ /CLAIMED/) { print num; exit } }' "$QUEUE"; }

progress() {
  local built done_ total
  built=$(grep -cE '^\| *[0-9]+ *\|[^|]*\|[^|]*\|[^|]*\| *✅ *\|' "$QUEUE" 2>/dev/null || echo 0)
  done_=$(awk -F'|' '/^\| *[0-9]+ *\|/ { b=$6; gsub(/[ \t]/,"",b); if (b=="✅") c++ } END{print c+0}' "$QUEUE")
  total=$(awk -F'|' '/^\| *[0-9]+ *\|/ {c++} END{print c+0}' "$QUEUE")
  echo "$done_/$total"
}

notify() {  # desktop popup + terminal bell; never fatal if the desktop isn't there
  local title="$1" body="$2"
  command -v notify-send >/dev/null && notify-send -u critical "$title" "$body" 2>/dev/null || true
  printf '\a'
}

if [ "$STATUS" -eq 1 ]; then
  echo "MBM queue: $(progress) built"
  awk -F'|' '/^\| *[0-9]+ *\|/ { n=$2; b=$6; c=$9;
      gsub(/[^0-9]/,"",n); gsub(/[ \t]/,"",b); gsub(/^[ \t]+|[ \t]+$/,"",c);
      if (b!="✅" && c ~ /CLAIMED/) printf "  in flight: #%s — %s\n", n, c }' "$QUEUE"
  echo "  next open: #$(next_open)"
  exit 0
fi

# Everything below this line WILL claim and build. --dry-run just lists.
if [ "$DRY_RUN" -eq 1 ]; then
  echo "Would build, in this order (nothing claimed, nothing spent):"
  awk -F'|' -v to="$TO" -v from="$FROM" '/^\| *[0-9]+ *\|/ {
      n=$2; s=$3; r=$4; b=$6; c=$9;
      gsub(/[^0-9]/,"",n); gsub(/[ \t]/,"",b);
      gsub(/^[ \t]+|[ \t]+$/,"",s); gsub(/^[ \t]+|[ \t]+$/,"",r); gsub(/^[ \t]+|[ \t]+$/,"",c);
      if (n+0 > to+0) exit;
      if (from != "" && n+0 < from+0) next;
      if (b=="⬜" && c !~ /CLAIMED/) printf "  #%s — %s (%s)\n", n, s, r }' "$QUEUE"
  exit 0
fi

# ── one driver per machine ───────────────────────────────────────────────────
if [ "$DRY_RUN" -eq 0 ]; then
  if [ -e "$LOCK" ] && kill -0 "$(cat "$LOCK" 2>/dev/null)" 2>/dev/null; then
    echo "A driver is already running on $MACHINE (lock: $LOCK)."; exit 0
  fi
  echo $$ > "$LOCK"
  trap 'rm -f "$LOCK"' EXIT
fi

cd "$REPO" || exit 1

# ── the prompt each fresh headless session wakes up with ─────────────────────
build_prompt() {
  local num="$1" story="$2" ref="$3" dir="$4"
  cat <<EOF
You are on MBM video production, running headless and unattended. Your entire job
this session is ONE video: #$num — $story ($ref). Build it end to end and stop.

The queue row is already claimed for you. Your build folder is: $dir

READ FIRST, they are law and they bind you:
  media-production/PRODUCTION-BIBLE.md  (all of it — §0 operating laws, §1 Standing Laws)
  media-production/CREW-GUIDE.md
Every law binds this build: Jesus's face is NEVER prompted or shown; two-voice
(narrator modern, Jesus exact KJV only); Phase 1 is STILLS-ONLY (no Veo/Flow motion
clips); the ear-check on every narration segment; no dead air over 2.5s; the full
Self-Revision loop before you call it done; the whole story through the final verse.

Study the KJV passage ($ref) in full context BEFORE storyboarding.

BUILD STEPS:
 1. Write the production pack + storyboard (8-16 beats, each beat its own picture).
 2. Write $dir/PROMPTS.md — the still prompts, Master Style Block byte-identical,
    character/wardrobe locks in every prompt the character appears in.
 3. Run: python3 media-production/jesus_face_gate.py --dir $dir
    It MUST exit 0. If it fails, rewrite the prompts and re-run. No image is
    generated until it passes.
 4. Generate the art: python3 media-production/gen_stills.py --dir $dir
    (This calls the official Gemini image API. There is NO browser and NO Google
    Flow any more — do not open Chrome, do not ask Cameron to make pictures.)
 5. QC every still: anatomy count, action reads right, time-of-day matches the
    scripture, style matches the painted gold standard, no baked-in text.
    Regenerate any miss: python3 media-production/gen_stills.py --dir $dir --only <slug>
 6. Narration (edge-tts: en-US-AndrewNeural narrator, en-US-ChristopherNeural Jesus,
    never a Multilingual model), then the ear-check against the script.
 7. Assemble: Ken Burns drift, serif captions, KJV verse card, closing question card.
    Export 9:16 1080x1920 H.264 under 25MB, named book-chapter_story-name.mp4.
 8. Run the full Self-Revision QC loop until a clean pass finds nothing.
 9. Tick Prep and Built in media-production/QUEUE.md for row $num.
10. Commit and push everything to origin main. Cameron never touches git.

You are unattended. Do NOT ask for permission, do NOT stop to check in, do NOT wait
for a go. Cameron has already said go. Run to completion (Law D/F). The only reason
to stop early is a genuine technical blocker you cannot solve yourself — if that
happens, say exactly what is blocked and why.
EOF
}

# ── build one video in a fresh headless session ──────────────────────────────
run_one() {
  local num="$1"
  local story ref slug dir log
  story="$(q_field "$num" 3)"; ref="$(q_field "$num" 4)"
  slug="$(echo "$story" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//;s/-$//' | cut -c1-30)"
  dir="media-production/build-$(printf '%02d' "$num")-$slug"
  log="$LOGDIR/video-$(printf '%03d' "$num").log"

  echo "── #$num $story ($ref) → $dir"
  if [ "$DRY_RUN" -eq 1 ]; then echo "   (dry run — nothing claimed, nothing built)"; return 0; fi

  # claim by push BEFORE generating anything (PRODUCTION-BIBLE §0 Law A).
  # If the push is rejected, another machine took it while we were reading.
  git pull --rebase --autostash -q origin main
  mkdir -p "$REPO/$dir"
  local tmp; tmp="$(mktemp)"
  awk -F'|' -v n="$num" -v c=" CLAIMED $MACHINE $(date +%F) (driver) " 'BEGIN{OFS="|"}
    /^\| *[0-9]+ *\|/ { num=$2; gsub(/[^0-9]/,"",num); if (num==n) { $9=c; print; next } }
    { print }' "$QUEUE" > "$tmp" && mv "$tmp" "$QUEUE"
  git add -A "$QUEUE" "$dir" 2>/dev/null
  git commit -q -m "Claim #$num $story — $MACHINE (driver)" 2>/dev/null
  if ! git push -q origin main 2>/dev/null; then
    echo "   push rejected — another machine claimed #$num. Skipping."
    git pull --rebase --autostash -q origin main
    return 2
  fi

  # ── the fresh session. --dangerously-skip-permissions is what stops the
  #    hundreds of yes/no clicks. It is scoped to this repo by cwd.
  local attempt=0
  while [ $attempt -lt 5 ]; do
    attempt=$((attempt + 1))
    build_prompt "$num" "$story" "$ref" "$dir" \
      | claude -p \
          --dangerously-skip-permissions \
          --fallback-model sonnet \
          >"$log" 2>&1
    local rc=$?

    # Subscription rate limit → wait it out and retry the SAME video.
    if grep -qiE "usage limit reached|rate limit|429|too many requests" "$log"; then
      local wait_s=1800
      # If Claude tells us when the limit resets, honor it.
      local reset
      reset=$(grep -oiE "resets? at [0-9]{1,2}(:[0-9]{2})? ?(am|pm)?" "$log" | head -1)
      echo "   ⏳ rate limit hit (${reset:-no reset time given}). Waiting ${wait_s}s, then resuming #$num."
      notify "MBM paused" "Rate limit. Auto-resuming #$num in 30 min."
      sleep "$wait_s"
      continue
    fi

    if [ $rc -ne 0 ]; then
      echo "   ❌ session exited $rc — see $log"
      return 1
    fi
    break
  done

  # Did the session actually tick Built? Trust the manifest, not the chat.
  git pull --rebase --autostash -q origin main
  local built; built="$(q_field "$num" 6)"
  if [ "$built" != "✅" ]; then
    echo "   ⚠️  #$num finished but Built is still '$built' — not counting it done. Log: $log"
    return 1
  fi
  echo "   ✅ #$num built. Queue now $(progress)."
  return 0
}

# ── the checkpoint: stop dead after the first video and wait for Cameron ─────
wait_for_approval() {
  local num="$1"
  rm -f "$APPROVE_FLAG"
  notify "MBM — video #$num is ready for your review" \
          "The run is PAUSED. Watch it, then approve to continue through 200."
  cat <<EOF

════════════════════════════════════════════════════════════════════
  🛑  CHECKPOINT — VIDEO #$num IS BUILT AND THE RUN IS PAUSED
════════════════════════════════════════════════════════════════════

  Watch it against your old videos. Does the art match? Same warm gold
  palette, same painted storybook feel, no Jesus face anywhere?

  The video is in:  $REPO/media-production/build-$(printf '%02d' "$num")-*/

  ▶ To continue through video 200:   type  approve   and press Enter
                                     (or from any other terminal:
                                      ./run_queue.sh --approve)

  ▶ To stop and change something:    press Ctrl-C. Nothing else runs.

  Nothing will be built until you decide. Waiting...

EOF
  # Accept a typed "approve" on a real terminal, or the flag file from anywhere.
  while true; do
    [ -e "$APPROVE_FLAG" ] && { echo "✅ Approved — continuing through the queue."; rm -f "$APPROVE_FLAG"; return 0; }
    if [ -t 0 ]; then
      read -r -t 5 answer || continue
      case "${answer,,}" in
        approve|approved|yes|y|go) echo "✅ Approved — continuing through the queue."; return 0 ;;
        stop|no|n|quit)            echo "🛑 Stopped at your word. Nothing further built."; exit 0 ;;
        "")                        : ;;
        *) echo "   (type 'approve' to continue, or Ctrl-C to stop)" ;;
      esac
    else
      sleep 5
    fi
  done
}

# ── main loop ────────────────────────────────────────────────────────────────
echo "MBM driver on $MACHINE · queue at $(progress) · checkpoint after #$CHECKPOINT"
echo

while true; do
  if [ -n "$FROM" ]; then NUM="$FROM"; FROM=""; else NUM="$(next_open)"; fi
  [ -z "${NUM:-}" ] && { echo "🎉 Nothing open — every story is claimed, built, or done."; break; }
  [ "$NUM" -gt "$TO" ] && { echo "Reached --to $TO. Stopping."; break; }

  run_one "$NUM"; rc=$?
  if [ $rc -eq 1 ]; then
    echo "🛑 #$NUM failed. Stopping so it doesn't burn the whole queue on a broken step."
    notify "MBM stopped" "Video #$NUM failed. See media-production/logs/."
    exit 1
  fi

  if [ "$NO_CHECKPOINT" -eq 0 ] && [ "$NUM" -eq "$CHECKPOINT" ] && [ $rc -eq 0 ]; then
    wait_for_approval "$NUM"
    NO_CHECKPOINT=1   # approved once — run unattended from here on
  fi
done

echo
echo "Done. Queue at $(progress)."
notify "MBM finished" "Queue at $(progress)."
