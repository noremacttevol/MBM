# Claude / AI-Assistant Recommendations for MBM

**Written 2026-06-29.** Cameron asked for my honest recommendations on how this project's
AI setup — the instructions, the context files, scheduled tasks, and memory — could be
cleaned up and improved, "by my understanding." Here it is, in priority order.

The good news first: the bones are excellent. The session-chain protocol (read SESSION-LOG,
verify the commit, recap before working) and the single-truth `START-HERE.md` are genuinely
well-designed and rare. Most of what follows is about *reducing sprawl* so those good systems
aren't drowned out.

---

## 1. The biggest issue: documentation sprawl (now partly fixed)

Before today there were ~34 markdown files in the root, many of them one-off chat handoffs
("CHAT-HANDOFF-CONTEXT", "PITCH-HANDOFF", "CONSOLIDATED-HANDOFF-…") that each claimed to
describe the project. New chats couldn't tell which was current, so they sometimes acted on
stale info — the exact thing that broke trust before.

**Done in this cleanup:** moved everything into `docs/` with a clear split between *current*
(`docs/publishing`, `docs/roadmap`, `docs/vision`, `docs/reviews`) and *historical*
(`docs/archive`), and added `docs/00-PROJECT-MAP.md` as the one index.

**Recommendation going forward:** stop creating per-chat handoff files. The chain is already
`SESSION-LOG.md` (history) + `START-HERE.md` (current truth). A new handoff doc every session
re-creates the sprawl. If a session needs to hand off, add a SESSION-LOG entry and update
START-HERE — that's the whole handoff.

## 2. Update CLAUDE.md to point at the new structure

`CLAUDE.md` and `START-HERE.md` reference docs by their old root paths (e.g.
`STATUS-AND-ROADMAP.md`, `PUBLISHING-ROADMAP`). Those files now live under `docs/`. The
references should be updated to the new locations so the auto-loaded instructions don't send a
future agent to a missing path. (Low effort, high payoff — I can do this on request; I've left
the authority files themselves in place at the root so the chain still works.)

## 3. Slim the instruction set; remove contradictions

There are several overlapping instruction files: `CLAUDE.md`, `.claudecode.md`, `AGENT-RULES.md`,
`AGENTS.md`, plus `.github/copilot-instructions.md` and per-folder `CLAUDE.md`/`AGENTS.md` in
`mobile/` and `port-back/`. They mostly agree, but overlap invites drift.

**Recommendation:** keep `AGENT-RULES.md` as the one vision/laws file and `START-HERE.md` as the
one truth file, and let `CLAUDE.md` be a short pointer to both plus the hard guardrails. Also
reconcile one stale contradiction: `.claudecode.md`/CLAUDE.md still say "do not build new features
on the Flask/web prototype — RN is the target," which is correct, but a few archived docs imply
otherwise. The PROJECT-MAP now states the authority order; following it resolves this.

## 4. Scheduled tasks worth setting up

The project has two time-based things that a human keeps having to remember. Both are good
candidates for a scheduled check so they don't slip:

- **An Apple-approval / build-state check.** A daily (or every-few-days) task that runs
  `cd mobile && npx eas build:list --platform ios` and flags when build 1.0 (6) flips from
  `WAITING_FOR_REVIEW` to ready — then it's time to run `WAITING-ON-APPLE.md`. This removes the
  "did Apple approve yet?" manual polling.
- **The Android 14-day closed-test clock.** Once the 12 testers start, a scheduled reminder that
  counts down the 14 continuous days and warns if the window is at risk, so production unlock
  isn't missed or accidentally reset.

Both are optional conveniences, not blockers — but they fit the schedule tooling cleanly and
match exactly the two waiting-periods this project lives or dies by.

## 5. Memory hygiene

`.auto-memory/MEMORY.md` has grown large and is mostly a running log. The most useful part of it
is already correctly flagged ("this can be stale; START-HERE wins"). **Recommendation:** keep
memory to *stable, repeated* facts (e.g. "Cameron's phone is Android → Google Play path,"
"code committed ≠ code on phone," "one routing source of truth = `routeFeedTag(harvestSignals())`")
and let `SESSION-LOG.md` carry the chronological history. Periodically prune solved-and-shipped
notes out of memory into the SESSION-LOG so memory stays short and high-signal.

## 6. A few files worth adding (by my understanding)

- `docs/00-PROJECT-MAP.md` — **added today.** The index that was missing.
- `docs/roadmap/FORWARD-WORK-PLAN.md` — **added today.** The one prioritized to-do list.
- `docs/publishing/PUBLISHING-VIABILITY-REVIEW.md` — **added today.** The honest go/no-go review.
- A short `CONTRIBUTING`/onboarding note *if* Phase 2 brings other helpers in — how to run the
  console, where secrets live, what never to commit. Not needed while it's just Cameron.

## 7. What NOT to change (it's working)

The session-chain protocol, the `START-HERE.md`-wins rule, the preflight script, keeping the AI
key off the phone, and the "I get you to the exact button, you press it" publishing promise are
all good. Leave them. The recommendations above are about *tidiness and not-drifting*, not about
reworking systems that already serve the mission well.

---

*This is advice, not action. I haven't changed any instruction file except to leave the authority
files (`CLAUDE.md`, `START-HERE.md`, `AGENT-RULES.md`, `SESSION-LOG.md`) untouched at the root so
the chain keeps working. Say the word and I'll apply items 2, 4, and 5.*
