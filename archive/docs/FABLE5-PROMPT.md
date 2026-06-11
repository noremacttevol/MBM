# Copy-paste this whole block to Claude Fable 5

---

You are taking over as the Principal Systems Architect for a project called **MBM (Milk Before Meat)**. I need decisive, hands-on help getting it from "lots of work, nothing proven" to "one real app I can hold and use." Read this whole brief, then do the work in the order I lay out. Do not push decisions back on me unless I genuinely have to make a business/account choice. Take initiative.

## What MBM is (goal and scope)

MBM is a **mobile-first React Native + Expo app** that ministers the way Jesus did: it meets each person exactly where they are, learns who they are from what they say, and guides them gently from foundational Christian truth ("milk") toward the restored gospel of The Church of Jesus Christ of Latter-day Saints ("meat") — without ever pressuring, shaming, sorting them into visible tiers, or gating them.

Hard, non-negotiable rules baked into the product:
- **No visible gates, tiers, or progress bars.** Routing is invisible and emergent from what the person says. They must never feel they "haven't qualified."
- **Story first, always:** a story they see themselves in → one open question → the app reflects their words back → then content. No survey-style onboarding.
- **Milk before meat is a hard law in code:** nothing LDS-specific (Joseph Smith, Book of Mormon, Restoration, missionaries, or even who built the app) until the person shows BOTH signals — believes God is fundamentally good, AND is open to God still speaking today.
- **Faithfulness is the only success metric, never conversion.** A person met honestly, unpressured, who walks away freely, is a success. Jesus let the rich young ruler go; so does the app.
- **A real human is always one tap away** (Phase 1 = me, the owner).

Scope right now is Phase 1: just me behind it; AI handles responses; I review. Design so a small volunteer team (Phase 2) and real missionaries (Phase 3) slot in later without a rewrite.

## Current state (honest, already verified by me)

What actually works:
- `mobile/` is the canonical TypeScript Expo app. Its app code typechecks clean. It has a four-tab structure (Feed, Journal, Chat, Profile), invisible emergent routing in a Zustand store (`mobile/src/store/useAppStore.ts`), the milk-before-meat law enforced in code, a **live Claude-powered chat**, story-first onboarding, a journal, a traits/signals dialogue engine, and an on-device "talk to a real person" capture queue. A web export and two headless screenshots exist.
- `knowing_engine.py` is a standalone "brain" with a passing self-test.
- `ministry-sim/` is a real simulator (personas, minister voice, judge, runner, learner) with **749 logged trials across 300 persona runs** and an honest 102-person evaluation that rates the app "not yet at the bar — and close."
- The old **visible gate ladder is genuinely removed** (only a comment remains).

What is broken or unproven:
1. **No app has ever been verified running on a real phone.** Only a web export + headless screenshots. The EAS build path needs a one-time `eas login` I have not done.
2. **The Anthropic API key is wired to ship inside the app.** Chat calls Anthropic directly from the client using `EXPO_PUBLIC_ANTHROPIC_API_KEY`, which Expo bakes into the bundle — anyone who installs the app could extract and spend the key. (The key is git-ignored, so it's not leaked in source; the problem is architectural.)
3. **The project is a graveyard of old generations.** There are three app generations layered on top of each other and never cleaned up: an old Flask/web prototype (`app.py`, `router.py`, `database.py`, `ai_guide.py`, `templates/`), an older React Native `.js` generation that the docs still describe, and the current TypeScript app. Verified duplicates: root `app.py` is identical to `backend/app.py`; root `router.py` identical to `backend/router.py`; `mobile/App.js` identical to `mobile/App.tsx` (and `package.json main` is `App.tsx`, so `App.js` is dead). Two divergent Node servers exist (`server/` and `backend/server/`). Three copies of the same `.env` secret.
4. **The status docs contradict the code.** `ISSUES.md` marks bugs "FIXED" in files that no longer exist (`mobile/src/screens/FeedScreen.js`, `mobile/src/db/seed.js`, `mobile/src/engine/router.js`). The live app has none of those paths.
5. **The "talk to a real person" feature captures requests on-device but has no delivery channel** — nothing actually sends them to me.
6. **The test harness was, until 2 days ago, scoring the app against its own mission** — all 8 faithfulness metrics measured restraint, none measured whether the app actually ministered when someone was ready. A `ministered_when_ready` metric was just added but is verified on only 1–2 trials.
7. **MBM is not independently version-controlled** — it sits inside a larger Obsidian vault git repo whose commits are unrelated coursework. There's no clean MBM history to diff or roll back.
8. **Recurring app behavior failures** from the latest 102-person test: it discloses the LDS affiliation too early in ~2 cases, answers its own closing questions, pushes the human handoff a beat early, and twice gave a vague non-answer when asked point-blank "what is this app?" (which violates its own honesty rule).

## What I've already tried

- Many rounds of prompt-tuning the ministering voice via the simulator (749 trials), with an honest 102-person evaluation.
- Removing the old visible gate/graduation system (confirmed gone from live code).
- Building the chat, the member-vs-seeker tracks, and the on-device connect-request queue.
- Repeated attempts to preview the app on my phone via Expo LAN/tunnel — unreliable in my setup (I use RustDesk remote desktop + phone hotspot), which is why everything keeps falling back into simulation instead of a real device build.
- Adding the `ministered_when_ready` metric to fix the mission-blind test harness.

## What I need you to do, in this exact order

**Step 1 — Establish ground truth (do this first, before changing anything).** Read `mobile/`, `MBM-DIAGNOSTIC-REPORT.md`, `CLAUDE.md`, and `.claudecode.md`. Then give me a short, plain-language confirmation of what is real vs. what the old docs falsely claim. Don't trust any status doc over the actual code.

**Step 2 — Consolidate to one app.** Propose (then, once I say go, execute) a cleanup that deletes or archives the dead generations: the old Flask prototype, the duplicate `backend/` Flask copy, the redundant Node server, `mobile/App.js`, and the stale `ISSUES.md`. Keep exactly one canonical thing. Replace the pile of ~20 docs with a single short `STATUS.md` that matches the code. Tell me precisely what you'd remove and what you'd keep before you touch anything destructive.

**Step 3 — Secure the API key.** Get the Anthropic key out of the client bundle. Stand up (or consolidate one of the existing Node servers into) a thin proxy that holds the key server-side, and point the app's chat at it. Keep the graceful-offline fallback. Show me the before/after of how the key flows.

**Step 4 — Get it on my phone, once, proven.** Walk me through the exact minimum to produce an installable build I can run on my actual device, given my RustDesk + hotspot constraint. I will do the one-time `eas login` myself when you tell me to. The deliverable is a screen recording or device screenshots of the full loop: story → question → reflection → feed → chat → "talk to a real person." Until that exists, nothing is "done."

**Step 5 — Wire the human handoff for real.** Make the on-device `connectRequests` queue actually deliver to me (email/inbox/admin endpoint — recommend the simplest reliable option and build it). This closes the "always a human one tap away" promise end to end.

**Step 6 — Make the test trustworthy, then re-run.** Confirm `ministered_when_ready` is genuinely wired into both the judge and the learner and that it moves scores on ready-person conversations. Then re-run the same 102 personas with the seed locked and report whether the six over-reach failures (early LDS disclosure, answering its own questions, pushing the handoff, vague "what is this app" non-answers) drop toward zero.

## How to work with me

Deliver working code first, then a brief plain-language explanation — no jargon, no lectures. Verify your own UI work with screenshots; never ask me to be your bug reporter or paste error logs. When in doubt about a product call, don't ask "does this match an example?" — ask "is this what Jesus would do with the person in front of him?" and decide. The only decisions that are genuinely mine are account/login actions and where the human handoff should deliver. Everything else, own it.

Start with Step 1 and report back before changing files.

---
