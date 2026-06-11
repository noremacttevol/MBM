#!/usr/bin/env python3
"""
MBM Mobile App Diagnostic Scanner
===================================
Run this at the start of every session.
Scans the mobile codebase for known issue patterns and reports status.

Usage:
    python3 diagnose.py

It does not fix anything. It only reports.
"""

import os
import re
from pathlib import Path
from datetime import datetime

MOBILE = Path(__file__).parent / "mobile"
ISSUES_FILE = Path(__file__).parent / "ISSUES.md"

results = []
passed  = []
failed  = []

def check(issue_id, description, ok, detail=""):
    icon = "✓" if ok else "✗"
    line = f"  {icon} [{issue_id}] {description}"
    if not ok and detail:
        line += f"\n       → {detail}"
    results.append(line)
    if ok:
        passed.append(issue_id)
    else:
        failed.append(issue_id)

def read(rel_path):
    p = MOBILE / rel_path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")

print("\n" + "=" * 60)
print("  MBM MOBILE DIAGNOSTIC SCANNER")
print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 60)

# ── ISSUE-01: "Start over" crash ──────────────────────────────────────────────
app_js = read("App.js")
feed_js = read("src/screens/FeedScreen.js")

# Fix: Hook screen registered in both branches of navigator, reset goes via onSessionReset callback
# Check that Hook is registered even in the savedSession branch
saved_session_branch = re.search(r'savedSession\s*\?(.*?):\s*\(', app_js, re.DOTALL)
hook_in_saved_branch = bool(re.search(r'name="Hook"', saved_session_branch.group(1) if saved_session_branch else ''))
uses_session_reset_callback = bool(re.search(r'onSessionReset', feed_js))
check(
    "ISSUE-01", "Start-over button does not crash (Hook screen always registered)",
    hook_in_saved_branch and uses_session_reset_callback,
    "App.js uses conditional navigator (savedSession?) AND FeedScreen resets to 'Hook'. Crash guaranteed."
)

# ── ISSUE-02: RESTORATION content missing ────────────────────────────────────
seed_js = read("src/db/seed.js")
restoration_count = len(re.findall(r"tag:\s*['\"]RESTORATION['\"]", seed_js))
check(
    "ISSUE-02", f"RESTORATION tier has content (found {restoration_count} items, need ≥10)",
    restoration_count >= 10,
    f"seed.js has {restoration_count} RESTORATION items. Need at least 10."
)

# ── ISSUE-03: more_depth skips RESTORATION ───────────────────────────────────
router_js = read("src/engine/router.js")
has_restoration_escalation = bool(re.search(
    r"BRIDGE.*RESTORATION|feed_tag.*RESTORATION.*more_depth|more_depth.*RESTORATION",
    router_js, re.DOTALL
))
check(
    "ISSUE-03", "more_depth escalation includes RESTORATION tier",
    has_restoration_escalation,
    "router.js escalates MILK→BRIDGE→MAINTENANCE, skipping RESTORATION entirely."
)

# ── ISSUE-04: LOC reveal dead end ────────────────────────────────────────────
# Fix: dismissLOC should escalate feed_tag
dismiss_loc = re.search(r"async function dismissLOC.*?^}", feed_js, re.DOTALL | re.MULTILINE)
loc_escalates = False
if dismiss_loc:
    loc_body = dismiss_loc.group(0)
    loc_escalates = bool(re.search(r"BRIDGE|escalat|feed_tag", loc_body))
check(
    "ISSUE-04", "LOC reveal escalates user to BRIDGE tier on dismiss",
    loc_escalates,
    "dismissLOC() sets locDone=true and calls loadFeed(). No tier escalation. Dead end."
)

# ── ISSUE-05: Journal hidden from seekers ────────────────────────────────────
journal_gated = bool(re.search(r"profile.*===.*MEMBER.*Journal|Journal.*profile.*MEMBER", feed_js))
check(
    "ISSUE-05", "Journal accessible to all profiles (not just MEMBER)",
    not journal_gated,
    "Signal bar only shows Journal button if profile === 'MEMBER'. Seekers and Skeptics locked out."
)

# ── ISSUE-06: positiveCount resets on re-mount ───────────────────────────────
# Fix: count persisted via a named AsyncStorage key constant
count_persisted = bool(re.search(r"POS_COUNT_KEY|positiveCount.*AsyncStorage|AsyncStorage.*positiveCount", feed_js))
check(
    "ISSUE-06", "positiveCount persists across screen re-mounts",
    count_persisted,
    "positiveCount is in-memory useState(0). Resets every time screen re-mounts. LOC trigger unreliable."
)

# ── ISSUE-07: content_id=0 on signal ─────────────────────────────────────────
has_fallback_zero = bool(re.search(r"item\?\s*\.\s*id\s*\?\?\s*0|item\.id.*\?\?\s*0", feed_js))
check(
    "ISSUE-07", "Signal actions don't log content_id=0",
    not has_fallback_zero,
    "handleSignal() uses item?.id ?? 0 — logs garbage rows when item is null."
)

# ── ISSUE-08: No error handling in router ────────────────────────────────────
router_has_try_catch = bool(re.search(r"try\s*{", router_js))
check(
    "ISSUE-08", "router.js has error handling (try/catch)",
    router_has_try_catch,
    "Zero try/catch blocks in router.js. Any DB failure freezes the app silently."
)

# ── ISSUE-09: Seed version check ─────────────────────────────────────────────
db_js = read("src/db/database.js")
has_seed_version = bool(re.search(r"seed_version|SEED_VERSION|migration", db_js))
check(
    "ISSUE-09", "Seed uses versioning (not count-based re-seed)",
    has_seed_version,
    "database.js re-seeds based on count < SEED_CONTENT.length. Manual content can be deleted."
)

# ── ISSUE-10: Readiness gate on escalation ───────────────────────────────────
has_readiness_threshold = bool(re.search(r"READINESS_THRESHOLD", router_js))
has_ready_check_in_feed = bool(re.search(r"isReadyToEscalate|ready.*more_depth|more_depth.*ready", feed_js))
check(
    "ISSUE-10", "Take me deeper is gated by readiness (no cold RESTORATION exposure)",
    has_readiness_threshold and has_ready_check_in_feed,
    "User can tap 'Take me deeper' 3x immediately and reach RESTORATION cold. Causes early dropout."
)

# ── MISSING-03: SKEPTIC gets LOC reveal ──────────────────────────────────────
loc_trigger = re.search(r"if.*thumbs_up.*locDone.*profile.*\)", feed_js, re.DOTALL)
skeptic_in_loc = bool(re.search(r"SKEPTIC", loc_trigger.group(0) if loc_trigger else ""))
check(
    "MISSING-03", "SKEPTIC profile included in LOC reveal trigger",
    skeptic_in_loc,
    "LOC trigger checks SECULAR || SEEKER. SKEPTIC excluded despite being a prime candidate."
)

# ── MISSING-01: AI Q&A screen exists ────────────────────────────────────────
ask_js = read("src/screens/AskScreen.js")
has_ask_screen    = (MOBILE / "src/screens/AskScreen.js").exists()
ask_calls_server  = bool(re.search(r"/api/chat|SERVER_URL", ask_js))
check(
    "MISSING-01", "AI Q&A screen (AskScreen.js) exists and calls server",
    has_ask_screen and ask_calls_server,
    "No AI question-answering feature in the mobile app."
)

# ── MISSING-02: Connect screen exists ────────────────────────────────────────
connect_js = read("src/screens/ConnectScreen.js")
has_connect_screen  = (MOBILE / "src/screens/ConnectScreen.js").exists()
connect_wired       = bool(re.search(r"ConnectScreen", read("App.js")))
check(
    "MISSING-02", "Missionary contact screen (ConnectScreen.js) exists and is wired",
    has_connect_screen and connect_wired,
    "No way for user to request missionary contact from the mobile app."
)

# ── MISSING-05: Returning user greeting ─────────────────────────────────────
has_returning_greeting = bool(re.search(r"LAST_VISIT_KEY|returningGreeting|pickGreeting", feed_js))
check(
    "MISSING-05", "Returning user greeting implemented in FeedScreen",
    has_returning_greeting,
    "No acknowledgment when a user returns after being away."
)

# ── File existence checks ─────────────────────────────────────────────────────
print("\n── File Structure ──────────────────────────────────────")
required_files = [
    "App.js",
    "src/screens/HookScreen.js",
    "src/screens/OnboardScreen.js",
    "src/screens/FeedScreen.js",
    "src/screens/JournalScreen.js",
    "src/screens/AskScreen.js",
    "src/screens/ConnectScreen.js",
    "src/engine/router.js",
    "src/db/database.js",
    "src/db/seed.js",
    "package.json",
]
for f in required_files:
    exists = (MOBILE / f).exists()
    print(f"  {'✓' if exists else '✗'} {f}")

# ── Content counts ────────────────────────────────────────────────────────────
print("\n── Content Counts (seed.js) ────────────────────────────")
for tier in ["MILK", "BRIDGE", "RESTORATION", "MAINTENANCE"]:
    count = len(re.findall("tag: '" + tier + "'", seed_js))
    target = {"MILK": 20, "BRIDGE": 20, "RESTORATION": 10, "MAINTENANCE": 10}[tier]
    icon = "✓" if count >= target else "✗"
    print(f"  {icon} {tier}: {count} items (target: {target})")

# ── Results ───────────────────────────────────────────────────────────────────
print("\n── Issue Checks ────────────────────────────────────────")
for r in results:
    print(r)

print("\n" + "=" * 60)
print(f"  PASSED: {len(passed)}  |  FAILED: {len(failed)}")
if failed:
    print(f"  OPEN ISSUES: {', '.join(failed)}")
    print(f"\n  Start with the first CRITICAL issue above.")
    print(f"  Read ISSUES.md for full details and fix guidance.")
else:
    print("  All known issues resolved. Check SPEC.md for remaining features.")
print("=" * 60 + "\n")
