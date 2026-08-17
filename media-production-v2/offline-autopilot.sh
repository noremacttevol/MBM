#!/usr/bin/env bash
# One safe MBM production tick with the reasoning agent running locally.
set -euo pipefail

export MBM_AGENT_BACKEND=codex-ollama
export MBM_LOCAL_MODEL="${MBM_LOCAL_MODEL:-qwen3.5:27b}"
export MBM_LANES=1

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec "$SCRIPT_DIR/autopilot.sh" "$@"
