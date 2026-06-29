# MBM — Full context handoff for the new (publishing + pitch) chat

*Written June 25, 2026. This is a complete, self-contained record of everything one
of Cameron's recent chats worked through, so a fresh chat can pick it up knowing what
Cameron has asked for, what he's worried about, what is already done, and what is left.
Cameron is gathering one of these from each recent chat and feeding them all into a
single new chat whose job is to keep the app moving and to figure out how to pitch it
to people. Read this, then read the project files it points to.*

---

## 0. First, orient yourself in the repo
Work in `/home/noremacttevol/Desktop/Brain/MBM`. Read, in order: `AGENT-RULES.md`,
`CLAUDE.md`, `STATUS.md`, `PUBLISHING-ROADMAP.md` (esp. "Stage 5.5" and "Next
mission"), and `MISSION-PUBLISH-HANDOFF.md`. Do not ask Cameron to re-explain the
vision — it is all written down. Cameron is a "vibe coder": he sets the vision and the
logic; the AI handles the build. Plain language, no jargon, take initiative, never
make him be the bug reporter.

## 1. What MBM is (one paragraph)
"Milk Before Meat" (MBM) is a React Native + Expo mobile app patterned after how Jesus
ministered — meet each person exactly where they are, give "milk before meat," and let
people discover Jesus through stories, an AI "minister," a feed, a journal, and a real
human one tap away. It is built on restored-gospel (Latter-day Saint) theology, but it
is deliberately an **independent app, not an official Church product**.

## 2. Cameron's philosophy (in his own intent — honor this)
He wants an **honest environment with NO Church endorsement** — a free place for anyone
to see what Jesus is really like, powered by restored-gospel theology, where the AI does
its best to convey what Jesus would want. If it helps someone reach out to the admin
team (who can point them toward the Church), good — but it is all on the person and
their own relationship with God. The app never hides what it is when someone asks, never
pressures, and leaves people free (Jesus let the rich young ruler walk away). A person
is not a data point.

## 3. What Cameron asked for in this chat — and what was DONE
He gave four directives; all four are complete and committed (git `fea4add`):

1. **Add a "not officially affiliated with any Church" disclaimer** on the first screen
   "and anywhere else needed." → Done: it's on the first screen (`HookScreen`), the
   Profile (`ProfileScreen`), and the privacy page (`site/privacy.html`).
2. **Swap Church-copyrighted material for official Church links / public-domain text.**
   → Already true by design and re-verified: all 100 "meat" cards link to the official
   Gospel Library (churchofjesuschrist.org); restored scripture is NEVER embedded; only
   the public-domain King James Bible is bundled inline. Nothing to change.
3. **Remove ALL Christlikeness / virtue "soul-scoring."** → Done: the "seven spirit
   levels," `traitScores`, `christlikeCap`, the hidden judge — all removed everywhere.
   The app does not grade anyone's virtues.
4. **Broadcast/record on the person's profile every piece of info used to know them —
   all of it visible, editable, removable.** → Done: a "What the app has noticed" card
   on the Profile lists every recorded signal in plain language, each with a **Forget**
   button (`forgetSignal`) that truly un-learns it and re-routes the feed. Nothing
   hidden or un-removable.

Related decision he confirmed earlier: the restored-gospel gate is decided by **their
own words only** — no hidden scoring of anyone. In code the gate is
`mayReferenceLds(signals)` / `restorationReady(signals)`: the Church is named only once
the person has shown, in their own words, BOTH that they believe God is good AND that
they're open to God still speaking today.

## 4. How it was verified (so the new chat can trust the state)
- Typecheck clean: `cd mobile && node_modules/.bin/tsc --noEmit` → exit 0.
- The full minister AI prompt (`mobile/src/engine/minister.ts`) was read and is sound:
  points to Jesus (never plays Him), meets emotion before answer, the "comparison
  method" (never argue doctrine), the **no-duck rule** (always answer + offer a human
  in addition), **ask permission before the Restoration**, crisis safety (presence
  first, 988), and a separate **member track** that teaches deeper instead of converting.
- The gate engine (`mobile/src/engine/connect.ts`) was stress-tested with 12 adversarial
  profiles — **12/12 passed**: fresh visitors never get the Church named; a Calvinist/
  harsh-God picture stays blocked even when the person says "God is good"; a single soft
  signal is never enough (two witnesses required); "how do I get baptized" with no
  readiness routes to a real person, not a fast-tracked missionary referral; members are
  never gated as seekers.

## 5. The Church / trademark question Cameron keeps asking ("would the Church have
anything to say?")
Plain answer: **the only real worry is not making the app look like the Church built or
endorsed it** — and that is already handled. It's branded "Milk Before Meat" (not the
Church's name), no Church logo or Angel Moroni, neutral icon, and now a non-affiliation
disclaimer. Intellectual Reserve, Inc. owns "The Church of Jesus Christ of Latter-day
Saints," "Mormon," "Book of Mormon," the Church logo/wordmark, and program brands (Come
Follow Me, Liahona, FamilySearch, CTR). Referring to them in text is fine; looking
official is not. **Rule for publishing AND for any pitch/marketing:** never put those
names or logos in the app title, icon, store listing, or marketing materials, and never
imply it's an official Church app. Two steps only a human can do, recommended before any
*wide/public* launch (not needed for friends-and-family testing): call the Church
Intellectual Property Office (1-801-240-3959) and describe the app honestly, and talk it
over with his bishop / stake president. I am not a lawyer or a Church authority — those
calls give the binding answers.

> Note for the new chat: Cameron got frustrated when this point was over-repeated. Don't
> belabor it. He has already done the thing that matters. State it once, clearly, and
> move on.

## 6. Cameron's urgency and intent about publishing
He wants the improved version live ASAP and has talked about getting it updated quickly.
The honest framing to keep: being upfront IS the protection — these very changes (the
disclaimer, removing the soul-scoring) are exactly what make the app safe to be seen.
Publishing the improved build is the move; nothing here needs to be hidden to be okay.

## 7. Current publishing state + the immediate "update the apps" mission
- Commits on `main`: `fea4add` (the four directives) and `558f705` (roadmap update).
- iOS: build 1.0.0 (3) uploaded to TestFlight, submitted for Beta App Review (was
  "Waiting for Review"); public link https://testflight.apple.com/join/cPNpeh3H.
- Android: `.aab` built; Play internal-testing rollout was UNCONFIRMED — verify it.
- **Fastest update path:** the June 25 changes are JavaScript-only (no native code), so
  an **Expo OTA update** (`eas update`) lands on already-installed apps instantly with
  no store review. EAS CLI is installed and logged in as account `milkb4meat`; channels
  are `preview` (internal testers) and `production`. Recommend pushing `preview` first,
  confirm, then `production`. Get Cameron's explicit yes before pushing — it publishes
  to real phones.
- Cameron has Chrome tabs open and already signed in / trusted for Apple App Store
  Connect and Google Play Console, and wants the Claude Chrome extension to drive those
  to finish store steps. Use `tabs_context_mcp` to find and reuse those signed-in tabs;
  NEVER enter his password/2FA or change account/security settings; get explicit
  approval before any Submit/Publish/Send-to-testers click. (Full instructions:
  `MISSION-PUBLISH-HANDOFF.md`.)
- Still open from Stage 5: change the admin desk password from the placeholder
  "JosephSmith" to a strong one, and rotate the Firebase/Anthropic/Railway keys that
  were exposed in setup logs. These are Cameron's account steps — walk him through them.

## 8. The new chat's added job: how to pitch the app to people
Cameron wants the new chat to figure out how to pitch/present MBM to people. Context that
must shape any pitch: (a) it's an honest, no-pressure space to encounter Jesus, not a
conversion funnel; (b) it is independent and must never be marketed as official Church
work or use Church names/logos in its branding; (c) it's currently in testing
(TestFlight + Play internal), so the near-term "pitch" is to friends, family, and first
testers, with a wider public pitch later; (d) the app honestly tells people what it is
when asked. A good pitch leans on the genuine product strengths (meets people where they
are, leaves them free, a real human one tap away, nothing hidden, gentle) — not on
implying institutional backing it doesn't have.

## 9. Key facts table
- App: "Milk Before Meat" (shows "Milk B4 Meat"), version 1.0.0.
- iOS bundle `org.milkb4meat.app`; Android package `com.milk_before_meat`.
- Website milkb4meat.org (+ /privacy.html, /support.html). Proxy: Railway `mbm-proxy`.
- Feedback/contact email: noremacprojects@gmail.com. EAS account: `milkb4meat`.
- Stack: React Native + Expo (SDK 54), local-first, Zustand store to AsyncStorage,
  Anthropic (claude-haiku-4-5-20251001) for the minister AI via the proxy.

## 10. Guardrails for the new chat
- Don't commit the loose binaries/sensitive files in the repo root (`*.apk`, `*.aab`,
  `*.pem`, `*.backup.gz`) — suggest adding them to `.gitignore`.
- Get Cameron's explicit approval before publishing anything (OTA update, store submit,
  posting public/marketing content) or any irreversible action.
- Never enter Cameron's credentials or change account/security settings — hand those
  back to him.
- Verify before saying "done" (typecheck, and where relevant a real test or screenshot).
- Keep the app branded as Cameron's independent app; never imply it's official Church work.
