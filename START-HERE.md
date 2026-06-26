# START HERE — MBM Current State (the ONLY file that is allowed to say "now")

**Last verified true: 2026-06-25.**
**If you are an AI assistant: read this whole file before you say ONE word about what is
done, published, built, or pending. Do not trust your memory over this file. If this file
and any other file/your memory disagree, THIS FILE WINS until a human updates it.**

If today's date is more than a few days after the "Last verified true" date above, say so
out loud to Cameron and ask him to confirm anything time-sensitive before acting on it.

---

## Who Cameron is (so you treat him right)
Cameron is non-technical and relies on the assistant to do the technical work. He has
limited time and a low tolerance for being asked to re-explain things or being told to
redo work that is already done. Take initiative. Do not make him be the bug reporter.
Do not re-ask settled questions. Verify before you claim anything is or isn't done.

---

## THE TRUTH RIGHT NOW (do not contradict this)

### Accounts — ALL EXIST. Never tell Cameron to create these or pay setup fees.
- Apple Developer account — exists, paid, set up.
- Google Play Console account — **created, $25 fee already paid, identity verified.**
  NEVER say he needs to "create a Google Play account" or pay "$25." That is DONE.
- Expo / EAS account — `milkb4meat`, logged in, used for cloud builds.
- Railway account — proxy `mbm-proxy` runs here.
- Firebase project — live (Anonymous sign-in on, firestore.rules published).
- Domain `milkb4meat.org` — owned (+ /privacy.html, /support.html).

### Publishing — already shipped before. This is NOT a from-scratch setup.
- **iOS:** Published to **TestFlight** via EAS cloud builds (no Mac needed). Apple
  Developer account, distribution cert, and App Store Connect API key are all set up.
  Public TestFlight link: https://testflight.apple.com/join/cPNpeh3H
- **Android:** Already published to Google Play **internal testing**. Versions **3 and 4
  shipped**; **version 5 built on June 25, 2026.** The Play side already exists.
- **Latest code commit:** `56b41a2` on `main` (always verify with `git log -1`).

### The ONE bug that keeps wasting Cameron's time — check this FIRST every time
**Writing/committing code does NOT put it on the phone.** A fix can be correct in the
files, committed, and pushed — and still not be on any device until a NEW build is made
AND installed. Several "missing fixes" were all this exact thing: the installed build was
made from older code. RULE: when Cameron says a fix "isn't there," first check which
commit the installed build came from (`cd mobile && npx eas build:list`), not whether the
code is right. JS-only changes can also be pushed instantly with `eas update` (OTA), no
rebuild needed.

---

## DONE vs ONLY-WRITTEN vs CAMERON-ONLY
(The full living version is STATUS-AND-ROADMAP.md — but THIS file is the quick truth.
Keep both in sync; update this file's date whenever you change it.)

### Done & shipped (in code, committed, in a build)
Cold-open fade fix, "Talk About It" chat header fix, de-surveilled Profile with Remove
buttons, ministry-console resilience, no-repeat story-on-cold-open, own-words restoration
gate, open/removable signals, non-affiliation disclaimer. All in `e4a2575`/`56b41a2`.

### Written/planned but NOT built yet
Tiered model routing (Haiku/Sonnet/Opus by signal) — see MODEL-ROUTING-AND-OFFLINE-PLAN.md.
"Start fresh" reset button on Profile. Belief/testimony answer option for dialogue.

### Only Cameron can do (human + accounts + money + the public button)
1. **The public store release** — *building* makes the app; *submitting* sends it to
   Apple/Google public review for the world. That is the one irreversible public step.
   The assistant preps everything up to the button; Cameron says go.
2. Firebase Blaze (paid) upgrade, if he wants to kill the free-tier read limit.
3. Any new card/billing caps or new API keys with spend limits.
4. Store listing details Apple/Google require the account owner to confirm.
5. Entering his own passwords / 2FA codes — always handed back to him.

---

## FILE HIERARCHY — which file wins when they disagree
There are too many overlapping docs in this repo. This is the order of authority:
1. **START-HERE.md** (this file) — current state. Highest authority for "what is true now."
2. **AGENT-RULES.md** — the vision, the laws, how to behave. Highest authority for "how/why."
3. **CLAUDE.md** + **.claudecode.md** — operating rules (auto-loaded by the tooling).
4. **STATUS-AND-ROADMAP.md** — the detailed living roadmap. Sync it with this file.
5. **.auto-memory/MEMORY.md** + topic files — accumulated history; CAN BE STALE; do not
   trust it over this file.
Everything else (MISSION-PUBLISH-HANDOFF, PUBLISHING-ROADMAP, NEXT-VERSION-EDITS,
MBM-SESSION-HANDOFF, PUBLISH-PLAN, MESSAGING-SETUP-PLAN, MBM-AI-BRIEFING, etc.) is
HISTORICAL context only. If any of it conflicts with this file, this file is right.
These old files should eventually be moved into an /archive folder so they stop
masquerading as current.

---

## UPDATE RULE (for the assistant — do this, don't skip it)
At the END of any session where something real changed (a build shipped, an account
changed, a feature went from written to built, the public release happened): update the
"Last verified true" date at the top of this file and the TRUTH section, in plain
language. Keep it short. A stale truth file is worse than none — it is exactly what
broke Cameron's trust in the first place.
