# MBM — Diagnostic Report

_Prepared June 10, 2026. Every claim below was verified against the actual files in `/home/noremacttevol/Desktop/Brain/MBM/`, not from memory or from the project's own status docs alone. Where a finding contradicts an existing status doc, that is called out._

---

## 0. One-paragraph summary

MBM is in good shape on **design and simulation**, and weak on the **one thing that matters most: a finished app you can hold and use.** The intended product — a React Native + Expo mobile app in `mobile/` — actually exists, its app code typechecks clean, it has a working four-tab structure (Feed, Journal, Chat, Profile), a live Claude-powered chat, an on-device "talk to a real person" capture, and an invisible-routing engine that obeys the milk-before-meat law. That is real and better than several of the project's own status docs claim. But there is **no verified build running on a phone**, the project is buried under **multiple abandoned codebase generations and duplicate folders**, the **status docs contradict the actual code** (so it's hard to know what's true), the **API key is wired to ship inside the client app**, and the **success metric in the test harness was, until two days ago, pointing away from the app's own mission.** The blocker is not "the app doesn't work" — it's that nobody can currently prove what works, because the signal is drowning in nine generations of notes and three half-built backends.

---

## 1. Core problems (what's actually broken or failing)

**1.1 No proven running app on a device.** This is the single most important failure and the most likely source of the feeling that "nothing good" was built. There is a web export (`mobile/dist/`) and two headless screenshots (`mobile/screenshots/`), but no artifact — build, recording, or device screenshot — proving the app runs end to end on a real phone. The documented path to a phone build (an EAS preview APK) still requires a one-time `eas login` that has not been done. _(Verified: `mobile/screenshots/` contains only `onboard_story.png` and `frontdoor_hook.png`; no `.apk`/`.ipa`; HANDOFF and the audit both concede this.)_

**1.2 The status docs no longer match the code.** `ISSUES.md` (the confirmed-issues tracker) describes and marks "FIXED" a set of bugs in files that **do not exist anymore** — `mobile/src/screens/FeedScreen.js`, `mobile/src/db/seed.js`, `mobile/src/engine/router.js`. The live app is TypeScript (`FeedScreen.tsx`, a Zustand store, `src/engine/connect.ts` + `minister.ts`) with **no `src/db/` and no `router.js` at all.** So an outside reader trying to learn the project's state from its own docs will be reading about a codebase that was thrown away. _(Verified by `find mobile/src` vs. the paths quoted in ISSUES.md.)_

**1.3 The API key is architected to ship inside the app.** Chat calls Anthropic **directly from the client** using `EXPO_PUBLIC_ANTHROPIC_API_KEY`. In Expo, any `EXPO_PUBLIC_*` variable is **baked into the app bundle** at build time, so anyone who installs the app can extract the key and spend on the account. The key is correctly git-ignored (not committed), but the bundling problem is architectural, not a leak. _(Verified: `useAppStore.ts` lines 147 + 568–583; `mobile/.gitignore` contains `.env`.)_

**1.4 The test harness was scoring the app against its own mission (now patched, lightly).** Until 2026-06-10, all 8 faithfulness dimensions measured *restraint* (don't push, don't rush, don't name the Church early). **Not one** measured whether the app actually ministered the restored gospel when a person was ready. Result: of 749 trials, faithfulness on "meat-ready" conversations was *lower* than overall — the optimization gradient literally pointed away from the mission, and a minister that never ministered to anyone could have scored 5/5. A `ministered_when_ready` metric was added two days ago but is verified on only one or two live trials. _(Verified: FIXES-LOG entry 2026-06-10; `trials.jsonl` = 749 lines.)_

**1.5 Recurring behavioral failures the app still commits.** The most recent honest test (`HOW-JESUS-WOULD-APPROVE.md`, 102 simulated people) concludes **"not yet at the bar — and close,"** with six over-reach failures at the *end* of conversations: premature disclosure of the LDS affiliation before trust, answering its own closing questions, pushing the human handoff a beat early, and — in two cases — giving a vague non-answer when asked point-blank what the app is, which violates the app's own first law (honesty). None failed catastrophically, but by the app's own standard a single safety flag is a real failure.

---

## 2. Root causes (why these things are failing)

**2.1 Environment friction, not code, ate the schedule.** `LESSONS-LEARNED.md` documents repeated Expo failures specific to Cameron's setup (RustDesk remote desktop + phone hotspot): blank screens, unreliable LAN/tunnel. Each failed attempt to see the app on a phone pushed work back into simulation, where things *do* run — which is why simulation is rich and the device build is unproven.

**2.2 Generational rewrites without cleanup.** The project has gone through at least three app generations — an early Flask/web prototype, a React Native `.js` generation (the one `ISSUES.md` documents), and the current TypeScript generation — but **old generations were never deleted.** That is why duplicate folders, duplicate entry points, and stale docs coexist. The rule "keep the canonical app in `mobile/` only" exists in `LESSONS-LEARNED.md` precisely because duplicate app folders were created before.

**2.3 Documentation outpaced (and outranked) the code.** There are ~20 top-level markdown docs (CLAUDE, .claudecode, HANDOFF, ISSUES, FIXES-LOG, SPEC, APP-FLOW-SPEC, KNOWING-ENGINE, LEARNING-ENGINE, LESSONS-LEARNED, AUDIT-CONTRARY, HOW-JESUS-WOULD-APPROVE, HERMES-PROMPT, two Gemini transcripts, etc.). Heavy prompt-and-philosophy iteration produced a lot of prose; the prose was not pruned when the code moved on, so the docs now disagree with each other and with the code.

**2.4 Self-grading masked the real gap.** Most "fixes" were verified by the builder's own simulator and the builder's own judge — and the judge was itself proven (item 1.4) to be measuring the wrong thing. So "4.6/5, going great" reports were sincere but measuring restraint, not ministry, while the actual deliverable (a phone app) went unproven.

**2.5 Scope is genuinely hard.** The product goal — minister like Christ to a hundred kinds of hurting, doubting, guarded people, with invisible routing and a hard "milk before meat" law — is ambitious. Much of the iteration is the legitimate cost of getting that voice right, not waste.

---

## 3. Incomplete / half-done / abandoned work

- **Phone build:** unproven; needs a one-time `eas login` then an EAS build. _(Open.)_
- **Real two-way messaging for "Talk to a real person":** the app captures requests into an on-device `connectRequests` queue (`submitConnectRequest`) but there is **no delivery channel** — nothing actually sends them to Cameron. The queue is a TODO with honest UI in front of it. _(Open by design; Cameron owns the channel decision.)_
- **The Flask/web prototype** (`app.py`, `router.py`, `database.py`, `ai_guide.py`, `templates/`) — explicitly "reference only," superseded, but still present and duplicated.
- **Two Node servers** (`server/` and `backend/server/`) — different versions of an admin/conversation server; unclear which (if either) is live.
- **`ministered_when_ready` metric** — added but verified on ~1–2 trials; not yet run across the expanded persona pool.
- **Returning-user experience** — `ISSUES.md` MISSING-05 still open in spirit; the store persists state but there's no "welcome back" acknowledgment.
- **Visual polish** — `FIXES-LOG` 2026-06-10 notes "deeper visual polish still pending"; only the front door got filled-pill buttons.

---

## 4. Technical debt and Band-Aids

- **Duplicate code, verified identical:** root `app.py` == `backend/app.py`; root `router.py` == `backend/router.py`; `mobile/App.js` == `mobile/App.tsx` (and `package.json` `main` points to `App.tsx`, so `App.js` is dead weight).
- **Duplicate, divergent Node servers:** `server/index.js` and `backend/server/index.js` differ — two forks of the same thing.
- **Three `.env` copies** of the same secret across `mobile/`, `server/`, `backend/server/`.
- **`EXPO_PUBLIC_` key bundling** (item 1.3) — the Band-Aid `anthropic-dangerous-direct-browser-access: true` header is in the code, which is a tell that this path was never meant for production.
- **Two synced prompt files kept "byte-in-sync" by hand** — `ministry-sim/minister.py` and `mobile/src/engine/minister.ts` hold the same system prompt and are manually compared after each edit. This will drift the moment someone forgets.
- **Stale tracker (`ISSUES.md`)** pointing at deleted files.
- **MBM is not independently version-controlled.** It lives inside a larger Obsidian "Brain" vault git repo whose recent commits are all ML coursework (DSDT). There is **no MBM-specific commit history**, and the working tree has dozens of unrelated uncommitted changes — so there is no clean way to roll MBM back or see its diff. _(Verified: `git log` shows only coursework commits; `git status` shows unrelated vault churn.)_
- **A broken test helper** (`mobile/test-profile-screenshot.ts`) imports `playwright`, which isn't installed, so `tsc --noEmit` always exits non-zero even though the app's own `src/` is clean. This makes "does it build?" confusing every single time.

---

## 5. Blockers (what's preventing progress right now)

1. **No `eas login` / device build.** The highest-value next step (a real app on the phone) is gated on a one-time interactive login only Cameron can do.
2. **Trust in the record is broken.** Because docs contradict code and the judge was self-serving, it is currently impossible to know "what actually works" without re-verifying by hand — which is exactly what this report had to do. That uncertainty is itself the blocker.
3. **No human-delivery channel** for connect requests means the "always a human one tap away" promise isn't actually wired end to end.
4. **Clutter.** Three backends, duplicate files, and 20 docs make every new agent (or AI reviewer) spend its first hours just figuring out which files are real.

---

## 6. Current state — what actually works (verified)

- **`mobile/` (TypeScript Expo app) — the canonical, current product.** App code typechecks clean (the only `tsc` error is the unrelated Playwright helper). It has:
  - A four-tab structure (Feed, Journal, Chat, Profile) via `AppNavigator.tsx`.
  - **Invisible emergent routing** in `useAppStore.ts` — the old visible gate ladder (`FEED_PROGRESSION`/`GRADUATION_THRESHOLD`) is genuinely **gone** (only a retired-system comment remains). _(Verified by grep.)_
  - The **milk-before-meat law enforced in code** — `RESTORATION` content can only surface when both readiness signals are present.
  - A **live Claude chat** (`sendChatMessage`) with a rich, context-aware system prompt, a member vs. seeker track, graceful offline fallback text, and persisted history.
  - **On-device connect-request capture** (honest UI, no dead-end mailto).
  - Story-first onboarding (`OnboardScreen.tsx`), journal, and a traits/signals dialogue engine.
  - A successful **web export** (`mobile/dist/`) and two real headless screenshots of the front door and first story.
- **`knowing_engine.py`** — the standalone "brain" with a passing self-test (reads signals, recommends a faithful next move, gates LDS references on both signals).
- **`ministry-sim/`** — a real simulator with personas, the minister voice, a judge, a runner, and a learner; **749 logged trials across 300 persona runs**, plus an honest 102-person evaluation report. This is the project's strongest, most real asset after the app shell.
- **Reference Flask prototype** — functional as a web app, but explicitly superseded.

**Strongest verified behaviors** (from the 102-person test): meeting people where they are (4.99/5), milk-before-meat restraint (4.92), wound-before-answer (4.61), letting people walk away (4.72), and **zero** ready people left without a human offered. **Weakest, recurring:** premature LDS disclosure, over-explaining instead of asking, grabbing the wheel at the close, and (until 2 days ago) not ministering the meat when someone was finally ready.

---

## 7. Success criteria — what "fixed" looks like

1. **One app, on the phone, proven.** A single canonical `mobile/` app that launches on Cameron's actual device, walks the full loop (story → question → reflection → feed → chat → "talk to a real person"), captured in a screen recording. No more "it runs in simulation."
2. **The key is server-side.** No `EXPO_PUBLIC` Anthropic key in the bundle; chat goes through a thin proxy (one of the existing Node servers, consolidated) so the secret never ships.
3. **One source of truth.** Dead generations deleted (old Flask, duplicate `backend/`, the extra Node server, `App.js`, stale `ISSUES.md`), MBM committed as its own thing (or its own repo), and a single short STATUS doc that matches the code.
4. **The human promise is real.** Connect requests actually reach Cameron (email/inbox/admin queue), closing the "always a human one tap away" loop end to end.
5. **The metric measures the mission.** `ministered_when_ready` confirmed wired into both judge and learner, run across the full persona pool, and shown to move scores on ready-person conversations — so future "it's going great" is trustworthy.
6. **The six over-reach habits driven to zero** on a re-run of the same 102 people with the seed locked, per the test's own recommendation.

---

## 8. The honest bottom line

The heart of this project — the ministering voice, the invisible routing, the milk-before-meat law, the freedom to walk away — is **built and largely working in code and simulation.** What's missing is not intelligence or design; it's **consolidation and proof.** Cut the project down to the one real app, put the key behind a proxy, wire the human handoff, delete the graveyard of old generations, and get it onto the phone once. That converts a pile of strong-but-unprovable work into a thing Cameron can actually hold — which is the only thing that will make it *feel* like something good was built.
