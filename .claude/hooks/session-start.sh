#!/usr/bin/env bash
# SessionStart hook — prints the session-chain orientation into context at the start of
# every chat, so the session-chain protocol in CLAUDE.md happens mechanically instead of
# depending on Claude remembering to do it. stdout is added to the model's context.
set -euo pipefail

DIR="${CLAUDE_PROJECT_DIR:-/home/cameron-lovett/MBM}"
cd "$DIR" 2>/dev/null || exit 0

echo "===================== MBM SESSION ORIENTATION (auto) ====================="

# --- Which machine am I? (hostname -> MACHINE-IDENTITY.md; never trust a doc sentence) ---
HN="$(hostname 2>/dev/null || echo unknown)"
echo "hostname: $HN"
if [ -f MACHINE-IDENTITY.md ]; then
  MATCH="$(grep -i "$HN" MACHINE-IDENTITY.md 2>/dev/null | head -1 || true)"
  if [ -n "$MATCH" ]; then
    echo "machine : ${MATCH}"
  else
    echo "machine : NOT LISTED in MACHINE-IDENTITY.md — ask Cameron which machine this is and add it."
  fi
fi
echo

# --- Session chain: top SESSION-LOG entry + last commits (verify the hash appears) ---
echo "--- Top of SESSION-LOG.md (recap the last session to Cameron first) ---"
if [ -f SESSION-LOG.md ]; then
  awk 'NF{p=1} p{print} /^---[[:space:]]*$/ && seen{exit} /^##/{seen=1}' SESSION-LOG.md 2>/dev/null | head -25 || head -25 SESSION-LOG.md
else
  echo "(no SESSION-LOG.md)"
fi
echo
echo "--- git log --oneline -5 (confirm the SESSION-LOG 'Commit:' hash is here) ---"
git log --oneline -5 2>/dev/null || echo "(git log unavailable)"
echo

# --- Next open video job (lowest-numbered unbuilt, unclaimed row) ---
if [ -f media-production/QUEUE.md ]; then
  echo "--- media-production/QUEUE.md: reminder ---"
  echo "For 'next'/'do the next video': git pull, then take the lowest-numbered row where"
  echo "Built is empty AND Claim is empty; claim-by-push BEFORE generating anything."
fi
echo "=========================================================================="
exit 0
