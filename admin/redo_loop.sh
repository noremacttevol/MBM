#!/usr/bin/env bash
# REDO LOOP — the robot Cameron asked for (2026-07-24). Takes videos ONE AT A TIME
# and rebuilds each to the whole CRITIQUE-LAW standard: re-voice from the canonical
# transcript with the new Jesus + slowed pacing, re-render the video, gate it hard,
# and ship only if it passes. Resumable: already-done builds are skipped.
#
# Usage:
#   bash admin/redo_loop.sh                 # all 200, in order, skipping done
#   bash admin/redo_loop.sh 10 15 200       # only these
#   FORCE=1 bash admin/redo_loop.sh 10      # redo even if marked done
#
# Progress ledger: media-production/REDO-PROGRESS.txt (one "NN done <date>" per line).
# Re-voicing spends ElevenLabs characters (plentiful now); the loop deletes a build's
# old clips first so it truly re-voices with the current voice + VOICE_SETTINGS.
set -u
cd "$(dirname "$0")/.." || exit 1
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
MP=media-production
LEDGER=$MP/REDO-PROGRESS.txt
LOG=admin/redo_loop.log
touch "$LEDGER"
say(){ echo "[$(date '+%m-%d %H:%M:%S')] $*" | tee -a "$LOG"; }

if [ "$#" -gt 0 ]; then LIST="$*"; else LIST=$(seq 1 200); fi

dirof(){ ls -d "$MP"/build-$(printf '%02d' "$1")-* 2>/dev/null | grep -v _stale | head -1; }
transcript_of(){ grep -l "\"row\": *$1\b" "$MP"/TRANSCRIPTS/*.json 2>/dev/null | head -1; }
is_done(){ grep -q "^$1 done" "$LEDGER"; }

for n in $LIST; do
  if [ "${FORCE:-0}" != "1" ] && is_done "$n"; then continue; fi
  d=$(dirof "$n"); [ -z "$d" ] && { say "#$n: no build dir — skip"; continue; }
  tj=$(transcript_of "$n"); [ -z "$tj" ] && { say "#$n: no transcript — skip"; continue; }
  say "#$n START ($(basename "$d"))"

  # 1. re-voice from the canonical transcript with the new Jesus + slowed pacing.
  #    Delete old clips so voice_from_transcripts can't "skip as already current".
  rm -f "$d"/audio/*.mp3 "$d"/audio/*.timing.json 2>/dev/null
  TR1=$(mktemp -d); cp "$tj" "$TR1/"
  ( cd "$MP" && python3 voice_from_transcripts.py "$TR1" ) >>"$LOG" 2>&1
  rm -rf "$TR1"

  # 2. re-render the video from the fresh clips (wipe caches).
  rm -rf "$d/segs" "$d"/segs_* 2>/dev/null
  ( cd "$d" && timeout 900 python3 build.py ) >"/tmp/redo-$n.log" 2>&1 \
    || { say "#$n RENDER FAILED — $(grep -m1 -iE 'error|trace' /tmp/redo-$n.log|cut -c1-70)"; continue; }

  # 3. gate hard against the law (new voice + render-fresh + complete + no echo).
  if ! python3 admin/qc_gate.py "$d" >"/tmp/redo-qc-$n.txt" 2>&1; then
    why=$(grep -m3 '  - ' "/tmp/redo-qc-$n.txt" | sed 's/^  - //' | tr '\n' '; ')
    say "#$n GATE FAILED — ${why:-see /tmp/redo-qc-$n.txt}"; continue
  fi

  # 4. ship this one via a worktree on origin/main (small, isolated commit).
  WT=$(mktemp -d); git worktree remove "$WT" --force 2>/dev/null; git worktree prune 2>/dev/null
  git fetch -q origin 2>/dev/null
  if git worktree add -q "$WT" origin/main 2>/dev/null; then
    mkdir -p "$WT/$d/audio"
    cp "$d"/*_*.mp4 "$WT/$d/" 2>/dev/null
    cp "$d"/audio/*.mp3 "$d"/audio/*.timing.json "$WT/$d/audio/" 2>/dev/null
    ( cd "$WT" && git add -f -- "$d" \
      && git commit -q -m "REDO #$n ($(basename "$d")): new voice + pacing, re-rendered to CRITIQUE-LAW

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>" \
      && for a in 1 2 3; do git fetch -q origin 2>/dev/null; git -c core.editor=true rebase origin/main >/dev/null 2>&1 || git rebase --abort 2>/dev/null; timeout 900 git push -q origin HEAD:main 2>/dev/null && { git fetch -q origin; git merge-base --is-ancestor HEAD origin/main && break; }; done )
  fi
  git worktree remove "$WT" --force 2>/dev/null; rm -rf "$WT"

  echo "$n done $(date '+%Y-%m-%d')" >> "$LEDGER"
  say "#$n DONE + shipped"
done

# refresh the board once at the end of the run
python3 admin/qc_sweep.py >>"$LOG" 2>&1 || true
python3 "$MP"/gen_site_index.py >>"$LOG" 2>&1 || true
say "run complete: $(grep -c 'done' "$LEDGER")/200 redone so far"
