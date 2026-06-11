# MBM Agent Startup Protocol
_Every session: read this file first. Do not skip it._

---

## What This App Is
MBM is a mobile gospel-sharing app (React Native / Expo Go) that adapts content to each user based on where they are spiritually. It uses a 4-tier progression — MILK → BRIDGE → RESTORATION → MAINTENANCE — mirroring how Jesus ministered. The goal is to bring users to the Restored gospel of the Church of Jesus Christ of Latter-day Saints through a personal, non-pushy digital experience.

**The active codebase is: `Brain/MBM/mobile/`**
The Flask app in `Brain/MBM/backend/` is a separate web version. Unless told otherwise, work on the mobile app.

---

## Step 1: Read ISSUES.md
File: `Brain/MBM/ISSUES.md`
This is the ground truth for what is broken. Read it before touching any code.

## Step 2: Run the Diagnostic
```bash
cd /home/noremacttevol/Desktop/Brain/MBM
python3 diagnose.py
```
This scans the mobile codebase for known issue patterns and prints a current status report. Run it BEFORE making changes. Run it AGAIN after changes to verify fixes didn't break anything else.

## Step 3: Check FIXES-LOG.md
File: `Brain/MBM/FIXES-LOG.md`
See what was fixed last session. Don't re-fix things that are already done. Don't re-introduce bugs that were already removed.

## Step 4: Check SPEC.md
File: `Brain/MBM/SPEC.md`
This defines what "production ready" means. Every fix should move toward this spec. If you're unsure whether a change is right, check the spec first.

---

## Current Priority Order (as of 2026-06-08)
1. ISSUE-01 — "Start over" crashes the app (CRITICAL)
2. ISSUE-02 — RESTORATION content missing (CRITICAL)
3. ISSUE-03 — more_depth skips RESTORATION (CRITICAL)
4. ISSUE-04 — LOC reveal is a dead end (HIGH)
5. ISSUE-05 — Journal hidden from Seekers (HIGH)
6. ISSUE-06 — positiveCount resets on re-mount (HIGH)
7. ISSUE-07 — content_id=0 logged on signal (MEDIUM)
8. ISSUE-08 — No error handling in router (MEDIUM)

---

## Rules for the Agent

1. **Read before writing.** Use Read tool on every file you're about to edit. Never edit blind.
2. **One issue at a time.** Fix one issue. Mark it done in ISSUES.md. Then move to the next.
3. **Update FIXES-LOG.md after every fix.** Date, issue ID, what changed, what file.
4. **Do not mark an issue closed unless you verified the fix logic is correct.** Re-read the changed code after editing it.
5. **Do not introduce new dependencies** unless absolutely necessary and explicitly approved.
6. **Do not change the visual design** (colors, fonts, layout) unless the issue is specifically about visual design. The aesthetic is intentional.
7. **Do not rewrite working code.** Touch only what is broken.
8. **The 4-tier journey is sacred:** MILK → BRIDGE → RESTORATION → MAINTENANCE. Any routing logic must respect this order.
9. **Content must be doctrinally accurate** to the Church of Jesus Christ of Latter-day Saints. Do not add content that misrepresents LDS doctrine.
10. **After every session, update the priority order** in this file to reflect what was fixed and what's next.

---

## Architecture (quick reference)
```
mobile/
├── App.js                    ← Navigation setup (Stack: Hook → Onboard → Feed → Journal)
├── src/
│   ├── db/
│   │   ├── database.js       ← SQLite setup + seeding
│   │   └── seed.js           ← All content (MILK, BRIDGE, MAINTENANCE — RESTORATION MISSING)
│   ├── engine/
│   │   └── router.js         ← Session creation, feed query, interaction logging, escalation
│   └── screens/
│       ├── HookScreen.js     ← Opening animation (stone rolls away)
│       ├── OnboardScreen.js  ← First question, routes user to feed_tag
│       ├── FeedScreen.js     ← Main experience: card, reactions, signal bar, LOC reveal
│       └── JournalScreen.js  ← Private journal (currently MEMBER-only — should be all users)
```

---

## Key Data Concepts
- **feed_tag:** MILK | BRIDGE | RESTORATION | MAINTENANCE — determines what content is shown
- **resonance_style:** emotional | logical | moral | doctrinal | comfort | personal | foundational | philosophical | historical — secondary sort key for content selection
- **profile:** MEMBER | SKEPTIC | SEEKER | SECULAR | UNKNOWN — set at onboarding
- **LOC reveal:** triggers after 3 thumbs_ups for SEEKER/SECULAR profiles (should include SKEPTIC)
- **more_depth signal:** should escalate MILK→BRIDGE→RESTORATION→MAINTENANCE (currently skips RESTORATION)
- **keep_simple signal:** drops back to MILK/comfort

---

## Last Session Summary
_Update this section at the end of each session._
- Session date: 2026-06-08
- What was done: Fixed all 9 confirmed issues + MISSING-03. Diagnostic scanner shows 10/10 passing.
- diagnose.py passes clean. All critical and high-priority issues resolved.
- Next session: tackle MISSING-01 (AI Q&A in mobile), MISSING-02 (missionary contact), MISSING-05 (returning user experience). Check SPEC.md Must Have list — only those 3 remain for MVP.
