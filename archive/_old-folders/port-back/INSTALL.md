# INSTALL — building the real MBM app (hand this folder + repo to Claude Code, or follow by hand)

Everything here is proven in the prototype and by 270 engine-sim trials
(SIM-REPORT.md). Order matters: each step leaves the app working.

---

## STEP 1 — Deploy the key proxy (kills the bundled-API-key problem)

1. Copy `server/index.js` + `server/package.json` over the repo's `server/`
   folder (it already has `railway.json`).
2. Deploy to Railway (or Render/Fly). Set env vars:
   - `ANTHROPIC_API_KEY` = your key (server-side only, never in the app again)
   - `ADMIN_TOKEN` = any long random string (your inbox password)
3. Verify: `GET https://<your-app>.up.railway.app/health` → `{ok:true, key:true}`.
4. Your owner inbox: `GET /api/admin/queue` with header `x-admin-token: <token>`
   — connect requests and fact-checks land there. **This closes Step 5 of the
   original plan: "a human one tap away" is now delivered, not just captured.**

## STEP 2 — Point the app at the proxy (mobile/src/store/useAppStore.ts)

1. Delete `ANTHROPIC_API_KEY`, `ANTHROPIC_URL`, `ANTHROPIC_VERSION` constants
   and the `EXPO_PUBLIC_ANTHROPIC_API_KEY` read. Remove the key from
   `mobile/.env`; add `EXPO_PUBLIC_SERVER_URL=https://<your-app>.up.railway.app`.
2. In `sendChatMessage`, replace the direct Anthropic fetch with:

```ts
const response = await fetch(`${SERVER_URL}/api/chat`, {
  method: 'POST',
  headers: { 'content-type': 'application/json' },
  body: JSON.stringify({ system: systemPrompt, messages: history }),
});
if (!response.ok) throw new Error('proxy ' + response.status);
const { text: rawReply } = await response.json();
```
   Keep the existing graceful-offline fallback messages.
3. In `submitConnectRequest`, after the on-device queue write, POST the entry
   to `${SERVER_URL}/api/connect` (fire-and-forget with .catch — the on-device
   queue stays the source of truth; `delivered` flips true on 200).

## STEP 3 — The engine laws (mobile/src/engine/connect.ts)

```ts
// BEFORE → AFTER (Law 8: one click is never identity)
const MEMBER_SIGNALS = new Set<string>(['covenant_intent', 'inactive_member', 'active_member']);
const MEMBER_SIGNALS = new Set<string>(['inactive_member', 'active_member']);

// covenant_intent becomes a believer HINT:
const GOD_GOOD_SIGNALS = new Set<string>([... , 'covenant_intent']);
```

Replace `believesGodGood` with the two-witnesses + framework-blocking version —
copy it verbatim from the prototype's `mbm-data.js` (function `believesGodGood`,
including `reformed_framework`, `pictures_*`, `nontheistic_framework`,
`rejects_harsh_god` handling).

## STEP 4 — New engine files

- Copy `engine/chatEar.ts` (this folder) → `mobile/src/engine/chatEar.ts`.
- Copy `engine/exercises.ts` (this folder) → `mobile/src/engine/exercises.ts`.

Wire chatEar into `sendChatMessage`:
1. `const heur = harvestSignals(text)` BEFORE building the system prompt; build
   guidance from `[...dialogueSignals, ...heur]` so the gate can open mid-reply.
2. Append `SIGNAL_REPORT_INSTRUCTION` to the system prompt.
3. `const { reply, found } = stripSignalReport(rawReply)`; display `reply`;
   merge `[...heur, ...found]` into `dialogueSignals`; re-derive `routeFeedTag`
   and rebuild the feed only if the track advances; recompute `currentQuestion`
   if null. (This is the prototype's `mergeSignals` — copy it.)
4. If `FAITH_ID_RE.test(text)`, push `{text: text.slice(0,140), ts: Date.now()}`
   into a persisted `faithWords` array.
5. Journal saves and free-text dialogue answers also run `harvestSignals`.

Also add to the system prompt builder (copy blocks from the prototype's
`buildSystemPrompt`): name line, story-so-far moments ("never claim you cannot
see their story"), MINISTERING PLAN with the framework discernment note, the
one-concrete-invitation instruction, and the active-exercise context.

## STEP 5 — Questions (mobile/src/data/questionBank.ts)

- Add question objects with ids 0, 2.5, 61, 62, 63, 64, 66, 67, 68, 69, 70,
  71, 72 — copy verbatim from the prototype's `mbm-data.js` QUESTION_BANK
  (they are valid TS object literals as-is).
- Replace `computeNextQuestion` with the TARGETED version from `mbm-data.js`
  (background → picture of God → God-still-speaks → the reach).
- Add to SIGNAL_LABELS (in useAppStore): the new labels from `mbm-data.js`.

## STEP 6 — Screens (all behaviors proven in the prototype `MBM App.dc.html`)

- `OnboardScreen.tsx`: name input on reflection + the FAITH BACKGROUND page
  (final onboarding step; seeds routing; stores words verbatim; marks q2.5 answered).
- `FeedScreen.tsx`: delete keep-simple/deeper → one "Show me more" (same-track
  refresh); add InvitationCard + FollowUpCard (with the optional "say what you
  noticed" reflection field); ContentCard gains "Reflect on this →" (saves to
  journal + harvests) and "Talk about it →" (prefills chat).
- `ProfileScreen.tsx`: delete CURRENT PATHWAY + "signals active"; keep
  words-only interpretation; add "WHAT'S GROWING IN YOU" (trait bars — owner
  amendment), "YOUR FAITH, AS YOU'VE TOLD IT" (faithWords verbatim), and
  "YOUR STORY SO FAR" (titled moments, each with Ask-about-this → chat).
- New `WelcomeBackScreen.tsx`: name + last-words recall; no cold restarts.
- DELETE `TimeCapScreen.tsx`, its route, the `isTimeCapReached`/`VIEW_CAP`
  logic, and the come-back wipe (Law 5; the wipe destroyed memory).
- Blessing toasts after dialogue/heart/journal/exercise actions (words, never
  numbers — copy pools from the prototype).
- Persist additions: name, moments, faithWords, activeExercise,
  doneExerciseIds, session; rehydrate self-heal (re-derive routeFeedTag, route
  down if state is above what signals justify).

## STEP 7 — Cleanup (the graveyard)

Inside the MBM folder: `git init` + first commit BEFORE deleting anything. Then
delete: root Flask files (app.py, router.py, database.py, ai_guide.py,
connect.py, diagnose.py, templates/, static/, mbm.db, root requirements.txt,
root package.json), the entire `backend/` folder, `mobile/App.js`,
`mobile/test-profile-screenshot.ts`, `ISSUES.md`. Move the old prompt/session
docs into `archive/`. Write a short STATUS.md that matches the code.

## STEP 8 — On your phone (the RustDesk/hotspot workaround)

EAS **cloud builds** bypass your LAN/tunnel problem completely — the build
happens on Expo's servers and your phone downloads it over the internet:

```bash
cd mobile
npx eas-cli login            # ← the one-time step only you can do
npx eas-cli build -p android --profile preview
```
- When it finishes (~10–20 min), EAS prints a build URL with a QR code AND a
  direct .apk download link.
- On your PHONE's browser (hotspot is fine), open the link → download the APK
  → install (allow unknown sources). No LAN, no tunnel, no Metro.
- Record the loop: story → question → reflection → faith page → feed → chat →
  "talk to a real person" → check it lands in `/api/admin/queue`.

## STEP 9 — Acceptance tests (must pass before anything ships)

1. Answer "I'm committed but I hold back" → lands in MILK, zero
   churchofjesuschrist.org links, first question = "Where does that faith live?"
2. Chat "I don't think God still speaks today" → gate stays CLOSED.
3. Chat "a god who does that is not good. God is good though — the real one"
   (after Reformed self-ID) → rejection + affirmation both heard.
4. Chat "I'm LDS, my ward is home" → member track unlocks.
5. Decompile-check: no Anthropic key anywhere in the APK.
6. Re-run ministry-sim 102 personas, seed-locked, with the funnel judge
   (MINISTRY-FUNNEL-SPEC.md).
