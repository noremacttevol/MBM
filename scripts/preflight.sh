#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# MBM PREFLIGHT — run this before every build/publish.
#
# Plain English: this checks the three things that have bitten us before, so a
# broken or unsafe version can never get shipped:
#   1. No secrets (API keys, service accounts, Apple keys) are tracked in git.
#   2. The mobile app's TypeScript still type-checks (no code errors).
#   3. The admin desk + helper scripts are valid JavaScript (no syntax errors).
#
# How to run it:   bash scripts/preflight.sh
# If everything passes you'll see ALL CHECKS PASSED. If anything fails, it
# stops and tells you exactly what, so you fix it before building.
# ─────────────────────────────────────────────────────────────────────────────
set -u
cd "$(dirname "$0")/.." || exit 1

fail=0
section() { printf '\n\033[1m== %s ==\033[0m\n' "$1"; }
ok()      { printf '  \033[32mOK\033[0m   %s\n' "$1"; }
bad()     { printf '  \033[31mFAIL\033[0m %s\n' "$1"; fail=1; }

# 1) SECRET HYGIENE ───────────────────────────────────────────────────────────
section "1/3  Secret hygiene (nothing sensitive in git)"
SECRET_GLOBS='\.env$|serviceAccount\.json$|AuthKey_.*\.p8$|\.p12$|\.keystore$|\.jks$|\.pem$'
tracked_secrets="$(git ls-files | grep -E "$SECRET_GLOBS" || true)"
if [ -n "$tracked_secrets" ]; then
  bad "These sensitive files are tracked in git and must be removed:"
  printf '       %s\n' $tracked_secrets
else
  ok "No secret files tracked in git."
fi

# Sanity: the known secret files exist locally AND are ignored.
for f in mobile/credentials/AuthKey_M73YLWD8YS.p8 admin/serviceAccount.json admin/.env mobile/.env; do
  if [ -e "$f" ]; then
    if git check-ignore -q "$f"; then ok "Ignored (safe): $f"
    else bad "EXISTS but is NOT git-ignored: $f"; fi
  fi
done

# 2) MOBILE TYPECHECK ─────────────────────────────────────────────────────────
section "2/3  Mobile app type-check"
if [ -d mobile/node_modules ]; then
  if (cd mobile && npx --no-install tsc --noEmit); then ok "TypeScript: 0 errors."
  else bad "TypeScript reported errors (see above)."; fi
else
  bad "mobile/node_modules missing — run 'cd mobile && npm install' first."
fi

# 3) SERVER / SCRIPT SYNTAX ───────────────────────────────────────────────────
section "3/3  Admin desk + script syntax"
for f in admin/inbox.mjs admin/watcher.mjs admin/reset.mjs; do
  [ -e "$f" ] || continue
  if node --check "$f"; then ok "Valid JS: $f"
  else bad "Syntax error in: $f"; fi
done

# RESULT ──────────────────────────────────────────────────────────────────────
echo
if [ "$fail" -eq 0 ]; then
  printf '\033[1;32mALL CHECKS PASSED — safe to build/publish.\033[0m\n'
  exit 0
else
  printf '\033[1;31mPREFLIGHT FAILED — fix the items above before building.\033[0m\n'
  exit 1
fi
