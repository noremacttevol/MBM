#!/usr/bin/env bash
# PreToolUse(Bash) hook — before any `git commit`, run the Jesus/cast face-consistency
# gate on every build folder whose PROMPTS.md is staged. If the gate fails, block the
# commit (exit 2) so an out-of-spec prompt sheet can never be committed silently.
# Input: JSON on stdin with .tool_input.command. Non-commit commands pass through.
set -uo pipefail

DIR="${CLAUDE_PROJECT_DIR:-/home/cameron-lovett/MBM}"
GATE="$DIR/media-production/jesus_face_gate.py"

# Read the tool command from stdin JSON (robust parse; empty on any error).
CMD="$(python3 -c 'import sys,json
try:
    d=json.load(sys.stdin)
    print(d.get("tool_input",{}).get("command",""))
except Exception:
    print("")' 2>/dev/null)"

# Only act on git commits.
case "$CMD" in
  *"git commit"*) ;;
  *) exit 0 ;;
esac

[ -f "$GATE" ] || exit 0
cd "$DIR" 2>/dev/null || exit 0

# Which build-*/PROMPTS.md are staged for this commit?
STAGED="$(git diff --cached --name-only 2>/dev/null | grep -E '^media-production/build-[^/]+/PROMPTS\.md$' || true)"
[ -z "$STAGED" ] && exit 0

FAILED=""
while IFS= read -r f; do
  [ -z "$f" ] && continue
  bdir="$(dirname "$f")"
  if ! python3 "$GATE" --dir "$bdir" >/tmp/mbm_gate_out 2>&1; then
    FAILED="$FAILED\n=== $bdir ===\n$(cat /tmp/mbm_gate_out)"
  fi
done <<< "$STAGED"

if [ -n "$FAILED" ]; then
  # Exit 2 = block the tool call; stderr is shown to Claude.
  printf 'BLOCKED: the Jesus/cast face gate FAILED on a staged PROMPTS.md. Fix the prompt sheet (JESUS LOCK v3 + REF line, no drift words) and re-run the gate before committing.%b\n' "$FAILED" >&2
  exit 2
fi
exit 0
