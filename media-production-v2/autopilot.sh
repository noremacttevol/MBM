#!/usr/bin/env bash
#
# autopilot.sh — the V2 loop: build/fix the next row unattended, repeat until
# all 200 are done. This is what the cron runs. Safe to run by hand.
#
#   ./autopilot.sh            # one tick: if a lane is free and work exists, run one session
#   ./autopilot.sh --dry-run  # show what the next tick WOULD do; touch nothing
#
# THE ROW-CENTRIC DISPATCHER (Cameron, 2026-08-07: "it just did 6 other videos
# before touching 10, 11 — they need to be fixed before i can move past 1-9").
# Priority is by ROW, not by job type: walk the board lowest row first; the
# first row needing complaint-class work defines the next job, WHATEVER kind of
# work it needs (picture re-cut, audio re-voice, author rebuild, resume). Only
# when no complaint-class row is actionable does regular production (resume →
# build → author) run, also lowest row first.
#
# Laws enforced here: COMPLAINT-FIRST (2026-08-06), LOW-NUMBER (2026-08-07),
# COST (reuse banked work, never re-buy), billing-breaker-with-fallback.

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

# --- lanes: count LIVE processes (pid files proved deletable) ----------------
LANES="${MBM_LANES:-4}"
LOCKDIR="$V2/.autopilot-lanes"
mkdir -p "$LOCKDIR"
LIVE=$(pgrep -fc '^timeout 7200 claude -p' || true)
LIVE=${LIVE:-0}
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

# --- billing state (paid jobs blocked while the Gemini prepayment is dry) ----
BILLING_DOWN=0
if find "$LOGDIR" -maxdepth 1 \( -name '*-runner.log' -o -name '*-resume.log' -o -name '*-cfix.log' \) \
     -mmin -25 -print0 2>/dev/null \
   | xargs -0 -r grep -lE 'prepayment credits are depleted|RESOURCE_EXHAUSTED' 2>/dev/null \
   | grep -q .; then
  BILLING_DOWN=1
fi

# --- refresh Cameron's live complaints (stale file still works if this fails)
[ "$DRY" -eq 0 ] && (cd "$REPO/admin" && timeout 60 node sync-reviews.mjs >/dev/null 2>&1 || true)

# --- THE DISPATCHER ----------------------------------------------------------
# Emits "JOB ROW". Caps: audio ≤2 lanes, author ≤1 lane (they run during
# billing-down too — they cost $0 Gemini). cfix/resume/runner are paid.
AUDIO_LIVE=$(pgrep -fc 'PROMPT-AUDIO-FIX' || true)
AUTHOR_LIVE=$(pgrep -fc 'PROMPT-FABLE5-AUTHOR' || true)
PICK="$(BILLING_DOWN=$BILLING_DOWN AUDIO_LIVE=${AUDIO_LIVE:-0} AUTHOR_LIVE=${AUTHOR_LIVE:-0} python3 - <<'PYEOF' 2>/dev/null || echo 'none 0'
import json, re, os, time, subprocess

bd = os.environ.get('BILLING_DOWN', '0') == '1'
audio_live = int(os.environ.get('AUDIO_LIVE', '0') or 0)
author_live = int(os.environ.get('AUTHOR_LIVE', '0') or 0)
V2 = 'media-production-v2'

def active(build):
    # a live gen process OR any file touched in the last 10 min = a lane owns it
    if subprocess.run(['pgrep', '-f', f'v2_gen_api.*{build}'],
                      capture_output=True).returncode == 0:
        return True
    now = time.time()
    for root, _, fs in os.walk(f'{V2}/{build}'):
        for f in fs:
            try:
                if now - os.path.getmtime(os.path.join(root, f)) < 600:
                    return True
            except OSError:
                pass
    return False

try:
    L = json.load(open(f'{V2}/REVIEW-LESSONS.json'))
except Exception:
    L = {}
openc = {k for k, v in L.items() if isinstance(v, dict) and v.get('open')}
try:
    html = open('site/review.html').read()
    # order-independent: data-num and data-hash can appear in either order in a
    # card tag (realistic-v2 cards emit data-review-wave BETWEEN them). [^>]*?
    # keeps the match inside one tag. A rigid "num then hash" regex silently
    # dropped 13 rows and stranded their complaints from the cfix lane (fixed
    # 2026-08-07). Match both orders so every card's live hash is captured.
    cur = {}
    for mm in re.finditer(r'data-num="(\d+)"[^>]*?data-hash="([0-9a-f]{40,64})"', html):
        cur[mm.group(1)] = mm.group(2)
    for mm in re.finditer(r'data-hash="([0-9a-f]{40,64})"[^>]*?data-num="(\d+)"', html):
        cur.setdefault(mm.group(2), mm.group(1))
except Exception:
    cur = {}

rows = []
for line in open(f'{V2}/AUTHOR-BOARD.md'):
    m = re.match(r'\|\s*(\d+)\s*\|\s*(build-\S+)\s*\|\s*([A-Z-]+)\s*\|\s*\d*\s*\|\s*(\S+)\s*\|([^|]*)\|([^|]*)\|', line)
    if m:
        rows.append((int(m.group(1)), m.group(2), m.group(3), m.group(4),
                     m.group(5), '✅' in m.group(6)))

def emit(job, row):
    print(job, row)
    raise SystemExit

# PASS 1 — complaint-class work, LOWEST ROW FIRST, whatever job it needs.
# (Cameron 2026-08-07: row 10's audio fix and row 11's rebuild outrank a
# complaint re-cut on row 22 — the row number decides, not the job type.)
for r, b, st, au, cl, rd in rows:
    k = str(r)
    if active(b):
        continue
    if st == 'NEEDS-AUDIO' and 'AUDIO-FIX' not in cl:
        if audio_live < 2:
            emit('audio', r)
    elif st == 'NEEDS-REBUILD' and 'AUTHOR-LIVE' not in cl:
        if author_live < 1:
            emit('author', r)
    elif (st == 'BUILT' and k in openc
          and not re.search(r'C-FIX \d{4}-\d\d-\d\d', cl)
          and L[k].get('reportedAgainst') == cur.get(k)):
        if not bd:
            emit('cfix', r)
    elif st == 'RUNNING' and 'A-auto' in cl and k in openc:
        if not bd:
            emit('resume', r)

# PASS 2 — regular production, lowest row first.
if not bd:
    for r, b, st, au, cl, rd in rows:
        if st == 'RUNNING' and 'A-auto' in cl and not active(b):
            emit('resume', r)
    for r, b, st, au, cl, rd in rows:
        if st == 'AUTHORED' and au == 'OK' and cl.strip() == '' and rd and not active(b):
            emit('runner', r)
if author_live < 1:
    for r, b, st, au, cl, rd in rows:
        if st == 'NEEDS-BEATS' and cl.strip() == '':
            emit('author', r)
print('none 0')
PYEOF
)"
JOB="${PICK%% *}"; ROW="${PICK##* }"

case "$JOB" in
  cfix)
    PROMPT="Read media-production-v2/PROMPT-OPUS-RUNNER.md — all its laws bind you. THE COMPLAINT-FIRST + LOW-NUMBER LAWS: Cameron filed a complaint against the CURRENT shipped cut of AUTHOR-BOARD row $ROW and it is the lowest waiting row — fixing it outranks all other work. Run 'python3 media-production-v2/v2_outline.py $ROW' to read his complaint in his own words. Claim first: append 'C-FIX <date> LIVE' to the row's board Claim cell, commit, push (rejected push = taken, exit cleanly). Fix ONLY what he named: picture defects = reroll or identity-edit ONLY the offending frames (--only <beat>, reroll budget applies), everything else stays byte-identical; if the complaint is AUDIO-domain, do NOT re-cut pictures — flip the row to NEEDS-AUDIO with a RUNNER PARK note per RUNNER-LESSONS and exit (the audio lane picks it up NEXT tick because low rows go first). Touch-once: batch every open complaint on this row into ONE re-cut. Re-assemble (AUDIO LOCK PASS), redeploy (step 7c, live-verified), review card answers his complaint in his words. UNATTENDED + HEADLESS: everything FOREGROUND to completion, never background, never wait. Board claim -> 'C-FIX <date> SHIPPED', SESSION-LOG, commit, push."
    MODEL_ARGS=(--model opus) ;;
  resume)
    PROMPT="Read media-production-v2/PROMPT-OPUS-RUNNER.md. A previous autopilot run DIED mid-build on AUTHOR-BOARD row $ROW (State RUNNING, Claim A-auto) — RESUME that row, do not start a new one. FIRST run the RUNNER-LESSONS already-shipped check (committed mp4 / live review card) — if it shipped, tick it BUILT and take nothing else. Otherwise read the build's QC.md for where it stopped; v2_gen_api.py resumes automatically (passing frames are never re-pulled — COST LAW). UNATTENDED + HEADLESS: everything FOREGROUND to completion, never background, never wait. Finish through step 7c DEPLOY + live verification, set the board row BUILT, SESSION-LOG, commit, push."
    MODEL_ARGS=(--model opus) ;;
  audio)
    PROMPT="Read media-production-v2/PROMPT-AUDIO-FIX.md and fix AUTHOR-BOARD row $ROW FIRST (THE LOW-NUMBER LAW — it is the lowest waiting complaint row; continue to the next lowest NEEDS-AUDIO rows after). UNATTENDED + HEADLESS: never wait, never ask; everything FOREGROUND to completion. Spend NOTHING on Gemini — audio only. The row's QC.md RUNNER PARK note is the per-row authority. If the row's stills are already generated, re-assemble and ship the full cut through deploy + live verification; the review card answers Cameron's complaint in his own words. Board: NEEDS-AUDIO -> BUILT (shipped) or AUTHORED+Ready (no stills yet). SESSION-LOG, commit, push. Stop cleanly when context runs low."
    MODEL_ARGS=(--model opus) ;;
  runner)
    PROMPT="Read media-production-v2/PROMPT-OPUS-RUNNER.md and run the next ready rows, starting with AUTHOR-BOARD row $ROW (lowest first — THE LOW-NUMBER LAW). UNATTENDED + HEADLESS: ending your turn kills the session — run EVERY command in the FOREGROUND to completion; never run_in_background, never wait for notifications. Before generating, cross-check the row against media-production/QUEUE.md — a swapped/replaced story gets PARKED (note in Claim, clear Ready), never built. Set the board row RUNNING with Claim 'A-auto <date>' when you claim, BUILT when shipped. LEARNING LAW (complaint ledger in QC.md), COST LAW (reroll budget), step 7c DEPLOY + live verification all bind. If blocked, park with the resume command in QC.md and take the next row. SESSION-LOG, commit, push when context runs low."
    MODEL_ARGS=(--model opus) ;;
  author)
    PROMPT="Read media-production-v2/PROMPT-FABLE5-AUTHOR.md and do the next rows, starting with AUTHOR-BOARD row $ROW (THE LOW-NUMBER LAW). If that row's State is NEEDS-REBUILD or NEEDS-AUDIO with a C-FIX/RUNNER PARK note, the park note in its QC.md is your spec — do the author-level fix it names (boat/place plates + REF wiring, PHRASE_SPOKEN pacing, SPOKEN respells + narration regen), then set Ready ✅ (or re-assemble+ship if its stills are done) so Cameron's complaint closes. Mark your claim 'AUTHOR-LIVE <date>' while working. UNATTENDED: never wait for Cameron; spend \$0 on image generation; SESSION-LOG, commit, push when context runs low."
    MODEL_ARGS=() ;;
  *)
    if [ "$BILLING_DOWN" -eq 1 ]; then
      MSG="billing breaker: Gemini prepayment depleted and no free (audio/author) work is open — idle. Top up at https://ai.studio/projects and the loop resumes itself."
    else
      MSG="ALL ROWS BUILT or claimed — nothing to do. If the board is fully BUILT, remove the cron line (see AUTOPILOT.md)."
    fi
    if [ "$DRY" -eq 1 ]; then echo "(dry) $MSG"; else log "$MSG"; fi
    exit 0 ;;
esac

if [ "$BILLING_DOWN" -eq 1 ] && [ "$DRY" -eq 0 ]; then
  log "billing breaker active: Gemini paid jobs blocked; running free $JOB work meanwhile. Top up at https://ai.studio/projects to resume picture builds."
fi

if [ "$DRY" -eq 1 ]; then
  echo "(dry) next tick would start a $JOB session at row $ROW"
  exit 0
fi

log "tick: starting $JOB session (row $ROW) → $LOGDIR/$TS-$JOB.log"
timeout 7200 claude -p "$PROMPT" \
  --dangerously-skip-permissions \
  "${MODEL_ARGS[@]}" \
  > "$LOGDIR/$TS-$JOB.log" 2>&1 || log "run $TS-$JOB exited nonzero ($?) — see its log"
log "tick done: $TS-$JOB"
