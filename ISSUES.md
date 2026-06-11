# MBM — Confirmed Issues
_Last updated by agent: 2026-06-08. Auto-generated from code inspection._
_Target: mobile app (Expo Go). Flask backend is a separate web app — see note at bottom._

---

## 🔴 CRASH / BROKEN FLOW

### ISSUE-01 — "Start over" button crashes the app
**File:** `mobile/src/screens/FeedScreen.js` — `handleReset()`
**What happens:** When the feed is exhausted, the user sees a "Start over with fresh profile" button. Pressing it calls `navigation.reset({ index: 0, routes: [{ name: 'Hook' }] })`. But if the user had a saved session when the app launched, App.js only registers Feed and Journal as screens — Hook and Onboard are not in the navigator. Navigating to a screen that isn't registered crashes React Navigation.
**Fix:** App.js needs to always register all four screens, OR use a state reset pattern that causes App to re-render and re-evaluate the navigator.
**Priority:** CRITICAL — this is a dead end in the core user journey.

---

### ISSUE-02 — RESTORATION tier has zero content
**File:** `mobile/src/db/seed.js`
**What happens:** The seed data has content for MILK, BRIDGE, and MAINTENANCE, but zero RESTORATION entries. The router has RESTORATION in its keyword signals and feed progression, but a user can never reach RESTORATION content because there is none. RESTORATION is the most important tier for the app's core purpose — introducing the specific truth claims of the Restoration. Without it, the app is a generic Christian content app.
**Fix:** Add RESTORATION content to seed.js. Minimum 10 entries.
**Priority:** CRITICAL — the entire purpose of the app depends on this tier.

---

### ISSUE-03 — `more_depth` escalation skips RESTORATION entirely
**File:** `mobile/src/engine/router.js` — `logInteraction()`
**What happens:** When a user taps "Take me deeper," the escalation goes MILK → BRIDGE → MAINTENANCE. RESTORATION is completely skipped. A user who has moved from BRIDGE and is ready to hear about the Restoration gets dumped into MAINTENANCE content (aimed at existing members) instead.
**Fix:** Change escalation to MILK → BRIDGE → RESTORATION → MAINTENANCE.
**Priority:** CRITICAL — breaks the gospel-sharing journey.

---

## 🟠 BROKEN FEATURE

### ISSUE-04 — Light of Christ reveal leads nowhere
**File:** `mobile/src/screens/FeedScreen.js` — `dismissLOC()`
**What happens:** The LOC reveal is a powerful moment — the user has had 3 positive interactions and the app reveals the concept of the Light of Christ. But when they press "I want to know more," it just dismisses the screen and loads the next feed item. No tier escalation. No special content. No transition to BRIDGE. The most important moment in the conversion funnel is a dead end.
**Fix:** After LOC dismissal, escalate the user's feed_tag to BRIDGE and load the first BRIDGE item. Add a brief transition message before the card appears.
**Priority:** HIGH

---

### ISSUE-05 — Journal hidden from Seekers and Skeptics
**File:** `mobile/src/screens/FeedScreen.js` — signal bar render
**What happens:** The Journal navigation button only renders if `profile === 'MEMBER'`. Seekers and Skeptics — the primary target users — can never access the journal even though it exists. Writing is one of the most powerful conversion aids and they're blocked from it.
**Fix:** Show Journal button to all profiles. The journal copy already works for anyone — "A quiet place for thoughts, promptings, and gratitude" is appropriate for any user.
**Priority:** HIGH

---

### ISSUE-06 — `positiveCount` resets every time the screen re-mounts
**File:** `mobile/src/screens/FeedScreen.js`
**What happens:** The `positiveCount` state tracks thumbs_ups toward the LOC trigger (needs 3). But it's in-memory component state. Every time the user navigates away and back, or the app suspends and resumes, the count resets to 0. A user who engaged positively twice, left the app, and came back starts the count over. The LOC trigger will almost never fire.
**Fix:** Persist `positiveCount` in AsyncStorage keyed by sessionId, or compute it from the interaction_log on mount (count rows where action='thumbs_up').
**Priority:** HIGH

---

### ISSUE-07 — `handleSignal` logs content_id=0 when item is null
**File:** `mobile/src/screens/FeedScreen.js` — `handleSignal()`
**What happens:** `await logInteraction(sessionId, item?.id ?? 0, action)` — if the item is null or the user taps a signal button on the exhausted-state screen, it logs a row with content_id=0. There is no content with id=0. This creates garbage rows in the interaction_log and could interfere with the feed's "already seen" exclusion query.
**Fix:** Guard against null item: `if (!item?.id) return; ` before logging, or skip the content_id requirement for signal actions.
**Priority:** MEDIUM

---

### ISSUE-08 — No error handling anywhere in router.js
**File:** `mobile/src/engine/router.js`
**What happens:** Every database function (`createSession`, `getFeed`, `logInteraction`, etc.) has no try/catch. If the SQLite database fails to open or any query throws, the screen freezes on the loading spinner with no feedback and no recovery path. On real devices this will happen.
**Fix:** Wrap all async database calls in try/catch. Return empty/safe values on failure. Add a visible error state to FeedScreen.
**Priority:** MEDIUM

---

### ISSUE-09 — Seed re-runs incorrectly if content is added manually
**File:** `mobile/src/db/database.js` — `openDb()`
**What happens:** The seed check is `if (count < SEED_CONTENT.length)`. This triggers a `DELETE FROM content` + full re-seed if the database has fewer rows than the seed array. But if you ever add content to the database manually (e.g. through an admin panel), and then the count is lower than the seed array somehow, it would delete your manual content. The reverse is also true: if you add to seed.js and the count is already higher from manual additions, the new seed content won't be added.
**Fix:** Use a migration/versioning approach. Track a `seed_version` in a settings table. Only re-seed when version changes.
**Priority:** LOW (won't matter until you have an admin panel for the mobile app)

---

## 🟡 MISSING FEATURES (required for production)

### MISSING-01 — No AI question/answer feature
The Flask backend has a full Q&A endpoint backed by Claude. The mobile app has zero AI. A user who wants to ask "Why do Latter-day Saints use a different Bible?" has no way to do that. This is a critical conversion tool that is completely absent from the mobile experience.

### MISSING-02 — No "Request missionary contact" feature
The Flask backend has a connect endpoint. The mobile app has no way for a user to request to speak with a missionary. This is the entire conversion call-to-action and it doesn't exist in the mobile app.

### MISSING-03 — No SKEPTIC profile gets LOC reveal
The LOC reveal only triggers for SEEKER and SECULAR profiles. A SKEPTIC who engages positively 3 times is probably MORE ready for the LOC moment than a SEEKER, but they never get it. Review whether this is intentional.

### MISSING-04 — ChatScreen, ProfileScreen, TimeCapScreen exist in mobile-expo but not in mobile
Three screens in the TypeScript/Expo version (`mobile-expo/`) don't exist in the active app (`mobile/`). Decide which codebase is the real one and consolidate.

### MISSING-05 — No onboarding for returning users
When a user reopens the app and has a saved session, they go straight to the feed with no context reset or greeting. A returning user gets no acknowledgment that time has passed or that new content might be available.

---

## STATUS

| ID | Description | Status |
|----|-------------|--------|
| ISSUE-01 | "Start over" crashes | ✅ FIXED 2026-06-08 |
| ISSUE-02 | RESTORATION content missing | ✅ FIXED 2026-06-08 |
| ISSUE-03 | more_depth skips RESTORATION | ✅ FIXED 2026-06-08 |
| ISSUE-04 | LOC reveal dead end | ✅ FIXED 2026-06-08 |
| ISSUE-05 | Journal hidden from seekers | ✅ FIXED 2026-06-08 |
| ISSUE-06 | positiveCount resets | ✅ FIXED 2026-06-08 |
| ISSUE-07 | content_id=0 logged on signal | ✅ FIXED 2026-06-08 |
| ISSUE-08 | No error handling in router | ✅ FIXED 2026-06-08 |
| ISSUE-09 | Seed re-run bug | ✅ FIXED 2026-06-08 |
| ISSUE-10 | Take me deeper exposes RESTORATION too early | ✅ FIXED 2026-06-08 |
| MISSING-01 | No AI Q&A in mobile | 🟡 OPEN |
| MISSING-02 | No missionary contact request | 🟡 OPEN |
| MISSING-03 | SKEPTIC excluded from LOC | ✅ FIXED 2026-06-08 |
| MISSING-04 | mobile-expo screens not in mobile | 🟡 OPEN |
| MISSING-05 | No returning-user experience | 🟡 OPEN |

---

## 🔴 ISSUE-10 — "Take me deeper" bypasses spiritual readiness (FIXED)
**File:** `mobile/src/engine/router.js`, `mobile/src/screens/FeedScreen.js`
**What was broken:** The "Take me deeper" button had zero gate. A user could tap it immediately after onboarding and reach RESTORATION content (Book of Mormon scriptures) having never engaged with a single card. Cold exposure to LDS-specific doctrine before trust is built causes early dropout.
**Fix:** Added `READINESS_THRESHOLD` per tier (MILK: 3, BRIDGE: 3, RESTORATION: 2). `isReadyToEscalate()` checks actual engagement (thumbs_up + view actions) against threshold before escalation is allowed. FeedScreen dims the button and shows a brief gentle message ("Spend a little more time here first. There is no rush.") when the user taps before they're ready. MEMBER profile is exempt — no gate for existing members.
**Fixed:** 2026-06-08

---

_Note on Flask: The Flask app (`backend/`) is a separate web app — not what runs in Expo Go. It is API-healthy. Its issues are tracked separately if/when it becomes the target._
