#!/usr/bin/env bash
# MBM AUTO-SHIP — the missing link Cameron asked for (2026-07-21):
# "why doesn't it do that automatically?"
#
# Every run: find finished-but-uncommitted video cuts, gate them, ship them to
# GitHub (where the review board plays from), record WHAT each cut changed in
# FIXNOTES.json so the board can tell Cameron exactly what to check, then
# refresh the board. Designed for cron — silent when there is nothing to do.
#
# HARD GATES (each one exists because of a real incident):
#   1. verify-mp4.sh          — truncated-mp4 bug: DONE printed, file unplayable
#   2. approved-lock          — 2026-07-20: 9 APPROVED videos got overwritten by
#                               a recovery push; approved cuts NEVER ship over
#   3. small commits          — 8k-file pushes die with HTTP 500 on this repo
#
# Fix notes: a session that fixes a video drops a one-line plain-English
# build-NN-*/FIXNOTE.txt. This script uses it (then removes it) and also
# auto-describes the changed files (new pictures / new narration / script fix).
set -u
# cron strips PATH down to /usr/bin:/bin — firebase lives in ~/.npm-global/bin
export PATH="$HOME/.npm-global/bin:/usr/local/bin:$PATH"
cd "$(dirname "$0")/.." || exit 1
REPO=$PWD
LOCK=/tmp/mbm-ship-fixes.lock
LOG=admin/ship-fixes.log
exec 9>"$LOCK"; flock -n 9 || exit 0   # another run in progress
exec >>"$LOG" 2>&1

say() { echo "[$(date '+%m-%d %H:%M:%S')] $*"; }

# ---- 0. sync down (never clobber local work) --------------------------------
git -c rebase.autostash=true pull --rebase -q origin main 2>/dev/null || true

# ---- 1. approved-lock: numbers Cameron approved (unfiltered, from Firestore) --
APPROVED=$(node admin/dump-approvals.mjs 2>/dev/null | python3 -c "
import json,sys
try: d=json.load(sys.stdin)
except Exception: sys.exit(1)
print(' '.join(n for n,v in d.items() if v.get('approved') and v.get('approvedHash')))") || {
  say "SKIP RUN: cannot reach Firestore for the approved-lock list"; exit 1; }

is_approved() { case " $APPROVED " in *" $1 "*) return 0;; *) return 1;; esac; }

# ---- 2. find candidate cuts: dirty finished mp4s in build folders ------------
SHIPPED=0
for line in $(git status --porcelain media-production/ | awk '$2 ~ /^media-production\/build-[0-9]+-[^/]+\/[0-9a-z-]+-[0-9]+_[^/]+\.mp4$/ {print $2}'); do
  mp4=$line
  dir=$(dirname "$mp4"); b=$(basename "$dir")
  num=$(echo "$b" | sed -E 's/^build-0*([0-9]+)-.*/\1/')

  if is_approved "$num"; then
    say "HOLD  #$num ($b): video is APPROVED — locked, not shipping"
    continue
  fi
  if ! bash admin/verify-mp4.sh "$mp4" >/dev/null 2>&1; then
    say "BLOCK #$num ($b): verify-mp4 FAILED — needs re-render"
    continue
  fi

  # ---- what changed, in plain English ---------------------------------------
  # HOLD-FOR-NOTE (2026-07-22): a cut whose FIXNOTE.txt has not been written yet
  # used to ship with only the auto-generated filename list, and the human note
  # that arrived seconds later was lost — it happened twice on #10 in one night,
  # because a session writes the mp4 first and the note last, and cron fires in
  # between. If the mp4 is newer than 3 minutes and there is no FIXNOTE yet, the
  # session is still mid-write: leave it for the next run.
  if [ ! -f "$dir/FIXNOTE.txt" ] && [ -n "$(find "$mp4" -mmin -3 2>/dev/null)" ]; then
    say "WAIT  #$num ($b): fresh cut, no FIXNOTE yet — holding for the next run"
    continue
  fi
  note=""
  [ -f "$dir/FIXNOTE.txt" ] && note=$(head -1 "$dir/FIXNOTE.txt" | tr -d '\n')
  auto=$(git status --porcelain "$dir/" | awk '{print $NF}' | python3 -c "
import sys
parts=[]
files=[l.strip() for l in sys.stdin if l.strip()]
pics=[f.rsplit('/',1)[-1] for f in files if f.endswith(('.jpeg','.jpg','.png')) and '/assets/' in f]
if pics: parts.append('new picture(s): '+', '.join(sorted(pics)[:6]))
if any('/audio/' in f for f in files): parts.append('narration re-recorded')
if any(f.endswith(('build.py','make_narration.py')) for f in files): parts.append('build script updated')
print('; '.join(parts))")
  [ -n "$auto" ] && note="${note:+$note — }$auto"
  [ -z "$note" ] && note="re-rendered (audio + captions)"

  # ---- record the note so the board can show it -----------------------------
  python3 - "$num" "$note" <<'EOF'
import json, sys, datetime, os
num, note = sys.argv[1], sys.argv[2]
p = 'media-production/FIXNOTES.json'
try: d = json.load(open(p))
except Exception: d = {}
d.setdefault(num, []).append({'date': datetime.date.today().isoformat(), 'note': note})
tmp = p + '.tmp'
json.dump(d, open(tmp, 'w'), indent=1)
os.replace(tmp, p)
EOF
  rm -f "$dir/FIXNOTE.txt"

  # ---- ship: one small commit per video, verified on origin -----------------
  git add -A -- "$dir/" media-production/FIXNOTES.json
  git diff --cached --name-only | grep -E '\.orig$' | xargs -d'\n' -r git restore --staged --
  git commit -q -m "#$num $b: $note

Auto-shipped by admin/ship-fixes.sh (verify-mp4 passed, approved-lock checked).

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>" || continue
  # Before pushing, say how big the push actually is. On 2026-07-22 a single
  # commit carrying 12 GB of qc/ scratch made every push hang until it timed
  # out; the errors went to /dev/null, so the log only ever said "push did not
  # land" and five finished cuts sat unshipped for hours while Cameron watched
  # a board that never changed. Never swallow the reason again.
  payload=$(git rev-list --objects origin/main..HEAD 2>/dev/null | awk '{print $1}' \
            | git cat-file --batch-check='%(objectsize:disk)' 2>/dev/null \
            | awk '{s+=$1} END {printf "%.0f", s/1048576}')
  nobj=$(git rev-list --objects origin/main..HEAD 2>/dev/null | wc -l)
  if [ "${payload:-0}" -gt 500 ]; then
    say "WARN  #$num ($b): push payload is ${payload} MB across ${nobj} objects — \
something rebuildable is being committed. Check for qc/ or segs/ scratch."
  fi
  ok=0
  for try in 1 2 3; do
    # 15 min is generous for a normal cut (~20 MB) and still fails fast enough
    # that a wedged push cannot eat the whole cron slot.
    if ! timeout 900 git push -q origin main 2>>"$LOG"; then
      say "WARN  #$num ($b): push attempt $try failed or timed out (${payload:-?} MB)"
    fi
    git fetch -q origin
    if git merge-base --is-ancestor "$(git rev-parse HEAD)" origin/main; then ok=1; break; fi
    git -c rebase.autostash=true pull --rebase -q origin main || break
  done
  if [ $ok -eq 1 ]; then say "SHIP  #$num ($b): $note"; SHIPPED=$((SHIPPED+1));
  else say "FAIL  #$num ($b): push did not land (${payload:-?} MB, ${nobj:-?} objects) — see errors above"; fi
done

# ---- 3. refresh board state + page (deploy only when the page changed) -------
node admin/sync-reviews.mjs >/dev/null 2>&1 || say "WARN: sync-reviews failed"
cp site/review.html /tmp/mbm-review-before.html 2>/dev/null || true
python3 media-production/gen_site_index.py >/dev/null 2>&1 || say "WARN: gen_site_index failed"
if ! git diff --quiet -- media-production/COMPLAINTS.md media-production/approvals.json 2>/dev/null; then
  git add -- media-production/COMPLAINTS.md media-production/approvals.json
  git commit -q -m "Board sync (auto)" && git push -q origin main 2>/dev/null || true
fi
if ! cmp -s /tmp/mbm-review-before.html site/review.html 2>/dev/null; then
  git add -- site/review.html && git commit -q -m "Review board refresh (auto)

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>" && git push -q origin main 2>/dev/null || true
  if ! firebase deploy --only hosting --project milk-b4-meat >/dev/null 2>&1; then
    python3 media-production/prune_hosting_versions.py >/dev/null 2>&1 || true
    firebase deploy --only hosting --project milk-b4-meat >/dev/null 2>&1 \
      && say "DEPLOY: board redeployed (after quota prune)" \
      || say "WARN: firebase deploy failed"
  else
    say "DEPLOY: board redeployed"
  fi
fi
[ "$SHIPPED" -gt 0 ] && say "DONE: $SHIPPED cut(s) shipped"
exit 0
