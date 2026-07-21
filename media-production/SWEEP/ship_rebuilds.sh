#!/bin/bash
# Ship every OK rebuild to the review board: site/fixed/<num>.mp4 + SERVE-LOCAL
# (repo pushes 500 on mp4-sized commits, so Firebase serves the cuts directly),
# then regenerate the board and deploy.
set -u
MP="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$MP/.." && pwd)"
FIXED="$REPO/site/fixed"
SL="$FIXED/SERVE-LOCAL.txt"
mkdir -p "$FIXED"; touch "$SL"

shipped=0
while read -r b ok mp4; do
  [ "$ok" = "OK" ] || continue
  num=$(echo "$b" | sed -E 's/^build-0*([0-9]+).*/\1/')
  src="$MP/$b/$mp4"
  [ -f "$src" ] || { echo "MISSING $src"; continue; }
  cp -f "$src" "$FIXED/$num.mp4"
  cmp -s "$src" "$FIXED/$num.mp4" || { echo "COPY-MISMATCH $num"; continue; }
  grep -qx "$num" "$SL" || echo "$num" >> "$SL"
  shipped=$((shipped+1))
done < "$MP/SWEEP/rebuild-status.txt"
echo "staged $shipped cuts into site/fixed/"

cd "$MP" && python3 gen_site_index.py || exit 1
cd "$REPO" || exit 1
if ! firebase deploy --only hosting 2>&1 | tail -5; then
  echo "deploy failed — pruning old hosting versions and retrying"
  python3 "$MP/prune_hosting_versions.py"
  firebase deploy --only hosting 2>&1 | tail -5
fi
