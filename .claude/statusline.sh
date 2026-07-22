#!/usr/bin/env bash
# Status line — always shows WHICH MACHINE this is (hostname -> MACHINE-IDENTITY.md),
# the git branch, and how many uncommitted source files there are. Solves the recurring
# "which computer am I?" confusion at a glance. stdin is Claude Code's session JSON.
set -uo pipefail
input="$(cat)"

DIR="${CLAUDE_PROJECT_DIR:-/home/cameron-lovett/MBM}"
# Prefer the workspace dir from the session JSON if present.
wd="$(printf '%s' "$input" | python3 -c 'import sys,json
try: print(json.load(sys.stdin).get("workspace",{}).get("current_dir",""))
except Exception: print("")' 2>/dev/null)"
[ -n "$wd" ] && DIR="$wd"
cd "$DIR" 2>/dev/null || cd "${CLAUDE_PROJECT_DIR:-/home/cameron-lovett/MBM}" 2>/dev/null || true

# Which machine? hostname -> the row in MACHINE-IDENTITY.md (never trust a doc sentence).
HN="$(hostname 2>/dev/null || echo '?')"
MACHINE="$(grep -i "$HN" MACHINE-IDENTITY.md 2>/dev/null | grep -oiE 'Machine [A-Z]' | head -1)"
[ -z "$MACHINE" ] && MACHINE="Machine ? ($HN)"

BR="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '-')"
# Uncommitted source files (ignore the noisy generated .words.json / fonts / media).
DIRTY="$(git status --porcelain 2>/dev/null | grep -vE '\.(words\.json|ttf|mp3|mp4|jpeg|jpg|png)$' | wc -l | tr -d ' ')"
AHEAD="$(git rev-list --count '@{upstream}..HEAD' 2>/dev/null || echo 0)"

OUT="🖥️ ${MACHINE}  ⎇ ${BR}"
[ "${DIRTY:-0}" != "0" ] && OUT="${OUT}  ✎ ${DIRTY} uncommitted"
[ "${AHEAD:-0}" != "0" ] && OUT="${OUT}  ⇡ ${AHEAD} unpushed"
printf '%s' "$OUT"
