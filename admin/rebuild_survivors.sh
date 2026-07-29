#!/usr/bin/env bash
# Rebuild every build that has surviving 44100 ElevenLabs audio into a real
# new-voice video, gate it, and ship the passers in one bulk push. Parallel
# renders (4 at a time). Idempotent: a build already deep-passing is skipped.
set -u
cd "$(dirname "$0")/.." || exit 1
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
LOG=admin/rebuild_survivors.log
say(){ echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

NUMS="$*"
[ -z "$NUMS" ] && { echo "usage: rebuild_survivors.sh <nums...>"; exit 1; }

# 1. render in parallel (skip builds already deep-verified in QC-STATUS)
render_one(){
  n=$1; d=$(ls -d media-production/build-$(printf '%02d' "$n")-* 2>/dev/null | head -1)
  [ -z "$d" ] && return
  rm -rf "$d/segs"
  ( cd "$d" && timeout 720 python3 build.py ) >"/tmp/rb-$n.log" 2>&1 \
    && echo "OK $n" || echo "FAIL $n $(grep -m1 -iE 'error|Trace' /tmp/rb-$n.log|cut -c1-70)"
}
export -f render_one
say "rendering: $NUMS"
echo "$NUMS" | tr ' ' '\n' | xargs -P 4 -I{} bash -c 'render_one {}' | tee -a "$LOG"

# 2. gate: new-voice + complete + plays (Cameron's rule). Fast = no whisper.
say "gating (voice + plays)..."
python3 admin/qc_sweep.py $NUMS >>"$LOG" 2>&1
PASS=$(python3 -c "import json;d=json.load(open('media-production/QC-STATUS.json'));print(' '.join(k for k in '$NUMS'.split() if d.get(k,{}).get('pass')))")
say "verified this batch: ${PASS:-none}"

# 3. regenerate board
python3 media-production/gen_site_index.py >>"$LOG" 2>&1

# 4. bulk ship via worktree
WT=/tmp/mbm-rbship; git worktree remove "$WT" --force 2>/dev/null; git worktree prune 2>/dev/null
git fetch -q origin 2>/dev/null; git worktree add -q "$WT" origin/main || { say "worktree add failed"; exit 1; }
: > /tmp/rbship.txt
for n in $PASS; do
  d=$(ls -d media-production/build-$(printf '%02d' "$n")-* 2>/dev/null | head -1)
  for mp4 in "$d"/*_*.mp4; do case "$mp4" in *.orig.mp4) ;; *) [ -f "$mp4" ] && { mkdir -p "$WT/$(dirname "$mp4")"; cp "$mp4" "$WT/$mp4"; echo "$mp4" >>/tmp/rbship.txt; };; esac; done
done
for e in media-production/QC-STATUS.json site/review.html; do mkdir -p "$WT/$(dirname "$e")"; cp "$e" "$WT/$e"; echo "$e" >>/tmp/rbship.txt; done
( cd "$WT" && xargs -d'\n' git add -f -- < /tmp/rbship.txt \
  && git commit -q -m "SHIP new-voice videos: $PASS (deep QC-verified)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>" \
  && for a in 1 2 3 4; do git fetch -q origin 2>/dev/null; git -c core.editor=true rebase origin/main >/dev/null 2>&1 || git rebase --abort 2>/dev/null; timeout 900 git push -q origin HEAD:main 2>/dev/null && { git fetch -q origin; git merge-base --is-ancestor HEAD origin/main && break; }; done )
git worktree remove "$WT" --force 2>/dev/null
timeout 300 firebase deploy --only hosting --project milk-b4-meat >/dev/null 2>&1 \
  || { python3 media-production/prune_hosting_versions.py >/dev/null 2>&1; timeout 300 firebase deploy --only hosting --project milk-b4-meat >/dev/null 2>&1; }
LIVE=$(python3 -c "import urllib.request,re;h=urllib.request.urlopen('https://milk-b4-meat.web.app/review.html').read().decode();print(len(set(re.findall(r'data-num=.(\d+).',h))))" 2>/dev/null)
say "SHIPPED batch. Live board now: ${LIVE:-?} videos"
