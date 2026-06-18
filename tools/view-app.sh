#!/usr/bin/env bash
# view-app.sh — the EASY way to see the MBM app in a normal web browser.
#
# It builds a static web copy of the app and serves it on http://localhost:8756.
# No Expo Go, no phone, no logins, no cloud build. Just open that link in Chrome.
#
# Run it from the repo root:   bash tools/view-app.sh
# Then open:                   http://localhost:8756
#
# To see changes later: re-run this script, then refresh the browser tab.

set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PORT=8756

echo "Building a fresh web copy of the app… (about a minute)"
cd "$ROOT/mobile"
npx expo export --platform web --output-dir "$ROOT/web-preview" >/dev/null 2>&1
echo "Built."

# Stop any old viewer, then start a fresh one that keeps running on its own.
pkill -f "http.server $PORT" 2>/dev/null || true
sleep 1
cd "$ROOT/web-preview"
setsid python3 -m http.server "$PORT" --bind 127.0.0.1 < /dev/null > /tmp/mbm-preview-server.log 2>&1 &

sleep 2
echo ""
echo "✅ Your app is now viewable at:  http://localhost:$PORT"
echo "   Open that link in your browser (Chrome). Bookmark it."
