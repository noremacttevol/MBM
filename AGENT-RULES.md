# AGENT-RULES.md — MBM Master Manual

> **THIS IS THE ONE FILE TO READ FIRST — every session, on every platform.**
> Claude Code, the Anthropic app, Claude desktop "cowork," Cursor, or any other
> AI tool: read this file top to bottom before touching anything. It is the single
> source of truth for what MBM is, how Cameron wants to work, and the laws that can
> never be broken. If any other rules file disagrees with this one, **this file wins.**
>
> _Last updated: 2026-06-12_

---

## How to use this file (for any AI, any app)

1. **Read this whole file.** Then read `STATUS.md` for the current build state.
2. **Read the code before you change it.** Never rebuild something that exists.
3. **Make one change at a time and commit it with a clear message** (see "Working
   across apps" below). The git history — not chat scrollback — is how Cameron and
   every other app stay in sync. A change that isn't committed effectively didn't
   happen as far as the next app is concerned.
4. **Verify before saying "done"** (typecheck, and bundle/screenshot the UI).
5. **Never re-ask Cameron to explain the vision.** It is written down here.
6. **Read the design-decision records before building the profile/scoring system:**
   - `MBM-SESSION-HANDOFF.md` — the settled two-track design (faith-background
     ladder vs. the Christlike-virtues scale), the honestly-labeled agreement
     meter, the locked "Christlike ___" labels, the build queue, and the one line
     not to cross. Do not re-litigate any of it with Cameron.
   - `CREATION-DILEMMA.md` — the apologetic reasoning the minister uses (meat-only,
     never a debate).

---

## Who Cameron Is

- **Name:** Cameron Lovett. Little River, SC. Industrial electrician (Canfor sawmill).
- **Coding style:** A "vibe coder." He sets the vision and the logic. The AI handles
  the syntax and the build. **Never flip that.** He does not want to become a
  developer; he wants to ramble the idea and have the AI build the best version of it.
- **Faith:** Latter-day Saint (The Church of Jesus Christ of Latter-day Saints).
  This is the heart of the whole project.
- **How he communicates:** He rambles the vision in plain, passionate language. That
  is the input format. Your job is to turn it into working code AND into durable
  written rules so he never has to explain the same thing twice.

### How to treat him
- **Take initiative. Do not cross-examine.** You are the Principal Systems Architect.
  Research, decide, and build the best version that serves the mission — not a weaker
  version because it was the first thing described.
- **Plain language always.** No jargon, no academic lectures.
- **No analogies unless he asks.** And **never** electrical/electrician analogies
  (wiring, panels, relays, breakers, voltage, PLC, ladder logic). He hates these and
  has said so repeatedly. If an analogy is needed and he asked, use universal ones
  (cooking, sports, everyday objects).
- **Explain what changed and why, in plain words, at the END** — after the work.
- **Never make him be the bug reporter.** Verify the work yourself.

---

## What MBM Is

MBM (Milk Before Meat) is a **mobile-first gospel-outreach app** patterned after how
Jesus ministered: meet people exactly where they are, learn them deeply through their
own words, and guide them from foundational truth (**milk**) toward the restored
gospel (**meat**) — only as fast as they are genuinely ready. The goal is
Facebook-level personalization in service of the gospel, with multiple pathways
(feed, dialogue, journal, human connection) all feeding one engine that learns who
the person is and what they need next.

**User statuses (how we talk about people — never shown as "tiers"):** Unbeliever,
Investigator, Calvinist, Other Tradition, Falling-Away LDS, Loyal LDS.

**Feed tags (internal routing only — NEVER shown to a user):**
- **MILK** — foundational Christian content: parables, comfort, invitation.
- **BRIDGE** — apologetics, evidence, skeptic-friendly.
- **RESTORATION** — Joseph Smith, apostasy, priesthood authority (meat).
- **MAINTENANCE** — discipleship content for active members.

**Three phases (build Phase 1 now; design so 2 and 3 slot in without a rewrite):**
- **Phase 1 (now):** Cameron alone. Connection requests go to Cameron. AI handles
  responses; Cameron reviews in admin.
- **Phase 2:** A small team of volunteers receive and respond to requests/threads.
- **Phase 3:** Church partnership. Real missionaries integrated into chat and connect.

---

## The Non-Negotiable Laws

These answer to scripture and to the actual pattern of how Jesus ministered. They
override any implementation that conflicts with them.

### Gospel principles
- Meet people where they are. Do not require a tradition before they are ready.
- Never pressure, shame, or manipulate. Spiritual safety beats conversion metrics.
- Be honest. The app never hides what it is when someone is ready to know.
- **A real human is ALWAYS one tap away.** Not buried. Not gated. Always there.
- The AI speaks only from what it knows. It admits uncertainty and always offers
  the human.
- A person is not a data point. Metrics serve the person, never route them like a package.
- **Jesus let the rich young ruler walk away. This app does too.**

### The Jesus Method (reviewed and confirmed by external review, June 2026)
- **No visible gates.** Sequential visible gates ("pass Gate 2 to see Gate 3") are
  pharisaical hurdles, not Jesus's method. **The app must never make a person feel
  they have not yet qualified for the next step.**
- **Invisible, emergent routing based on love paying attention.** The app listens to
  what a person says and routes silently behind the scenes. Readiness is detected from
  language and engagement — never from checkbox completion. The person never knows
  they have been categorized.
- **Story first. Always.** The first thing a person sees is never a survey about their
  background. It is a story, told beautifully enough that they see themselves in it.
- **Stories are interactive mirrors, not information.** Always follow a story with a
  question that asks which part of it the person recognizes in themselves.
- **Never argue doctrine.** If someone believes God sends people to hell for his glory,
  do not debate. Answer with the words and stories of Jesus from the Bible they already
  accept, and let Jesus correct the error through his own voice.

### The milk-before-meat law (the gate, made invisible)
The restored gospel — the restored church, the Book of Mormon, Joseph Smith — is
**never** mentioned, referenced, or implied until the person has shown BOTH readiness
signals **on their own**, in their own words:
  - (a) they believe God is fundamentally **good**, AND
  - (b) they are **open** to the idea that God might still speak today.
This is not a gate they know they are passing. It is a signal the app detects. The
RESTORATION feed tag and the meat dialogue questions never appear until both signals
are present. In code this is `mayReferenceLds(signals)` in `mobile/src/engine/connect.ts`
— and it is the exact same gate the chat and the question bank use.

### Membership comes only from self-identification (Law 3 / Law 8)
A person is treated as a member **only** when they say so in their own words
(`active_member` / `inactive_member`). **One onboarding tap is never identity.** A
single story tap that hints at faith (`covenant_intent`) is a believer *hint* only —
it can count toward "believes God is good," but it can NEVER mark someone a member.
(A misroute here once lost a tester. Do not repeat it.)

### No come-back wipe, no time cap (Law 5)
The app never locks a person out and never erases what it has learned about them. The
old "5-item screen time cap" and any "reset on return" logic are **retired** — any doc
that still describes them is stale and wrong.

---

## Locked Product Direction (June 2026) — do not regress these

Cameron explained these in full and asked that they be stored so he never re-explains.
They are rules. Build toward them; do not walk them back.

1. **Short onboarding, then a story on every cold open.** First launch is a FAST
   opening that collects only the basics (chiefly a past/present faith-background
   question, enough to seed routing) and then tells ONE great story — told *by the app
   in the name of Jesus, quoting real scripture*, rendered for emotional impact, ending
   in one open question. The user's answer is recorded to the Profile as the founding
   entry of who they are compared to Christlikeness. **Every cold open after the first**
   tells ANOTHER short, powerful Jesus / God's-love story — **never repeating one
   already told** — each recorded to the Profile with the user's answer, until they
   have seen them all. Every story ends with a link into the AI chat to talk about it more.

2. **The story/lesson record lives on the Profile.** The Profile is where the app shows
   it has learned the person: stories experienced, answers given, and a Christlikeness
   read summarized from them. This is the visible payoff for coming back.

3. **The member ("meat") track is easy to enter — and hidden, to respect the mystery.**
   There is **no visible "I'm a member" toggle.** The app infers depth from how the
   person talks and what they engage with, then shifts silently (rides on the existing
   `active_member` / `inactive_member` self-ID signals — never a guessed label). The
   member-helping AI teaches the way Latter-day Saints actually learn and grow — deeper
   doctrine from the four standard works, keeping pace with the living prophet — NOT the
   milk used to win converts. Same Christ, different depth.

4. **The milk AI always defends the goodness of Jesus** and walks others toward the
   Restoration through their OWN scripture. With a Calvinist, Catholic, Baptist, or any
   tradition: use the scripture they already accept to establish that Jesus is good,
   then gently (never by argument) let their own logic begin to align with Latter-day
   Saint theology. This never overrides the milk-before-meat gate.

5. **Multiple-choice answers must not corner people into doubt.** Every belief question
   needs a genuine, well-framed belief/testimony option so a believer can testify
   instead of being boxed into unbelief. Doubt must never be the default-looking choice.

6. **The blessing popup STAYS until it is swiped — and a swipe can open a real talk.**
   The motivation/blessing popup (the one honest word spoken after a dialogue answer, a
   kept heart, or a journal reflection) does **not** auto-dismiss. It rests on screen so
   the person can read it slowly and understand it, and so its **absence is felt** when
   it goes. They control it with a swipe:
   - **Swipe LEFT → let it go** (dismiss).
   - **Swipe RIGHT → talk about it.** This carries the **question, their answer, AND the
     blessing line** into Chat as a pre-filled opening, so a quiet moment can become a
     real conversation about the content they received — more memorable, more impactful,
     and a doorway to reaching out.
   Because the line now persists and can open a conversation, the AI that writes it must
   weigh it like Jesus weighing what He says to someone He knows will carry it:
   **criticize and compliment more carefully and respectfully.** An affirmation must be
   true enough to rest on; a correction must be careful, respectful, and worth opening a
   conversation over. Never careless, never canned, and silence is still valid for a
   non-answer. (Implemented in `BlessingToast.tsx` + the `blessing` BlessingCard /
   `openBlessingInChat` in `useAppStore.ts`; the careful-weighing instruction lives in
   the `generateBlessing` system prompt.)

7. **The app must say, plainly, that it is NOT God.** Subtly but never hidden, near the
   opening, the app declares its own limit: it is not God, it cannot answer a prayer or
   know a person the way Jesus does — it can only point toward Him. What stirs here is a
   **spiritual exercise** to take to God and to trusted people, and to confirm by the
   **Spirit, not the app**, before believing it. This is anchored in Elder Gerrit W.
   Gong's counsel on AI (Quorum of the Twelve, 2025–2026): *"Artificial intelligence can
   answer questions, but it cannot answer prayers… it is not God and cannot be God… it
   can organize information, but it cannot offer revelation, covenant connection or
   divine truth,"* and *"platforms and technologies cannot substitute for authentic
   divine and human connection."* His three guideposts — **rely on the Spirit, practice
   wisdom, choose trusted sources** — and his point that **AI should further, never
   replace, the four relationships (God, self, others, nature)** are the app's own stance
   on itself. (Live in `HookScreen.tsx` as the quiet footer; the fuller treatment for
   devout members lives on the member/MAINTENANCE side, where the app states this stance
   and why it is right.) Never let a person mistake the app for the Lord.

---

## System Guardrails (from `.claudecode.md`)

1. **Never cross-examine or push decisions back onto Cameron.** Take initiative.
2. **Mobile-first: React Native + Expo.** The old Flask/web prototype is reference
   only — never build new features on it.
3. **Local-first.** The routing engine, content, and user data live on-device. The app
   runs with no server terminal.
4. **Zero placeholders.** No `// TODO`, no snippets, no shorthand. Every file fully
   written, end to end, with complete data and error handling.
5. **Code first, talk second.** Deliver complete working code, then a brief plain
   explanation at the end.

---

## Stack & Architecture (what is true today)

- **App:** React Native + Expo (SDK 54). Tested on a real phone via Expo Go over a
  tunnel. Lives in `mobile/`.
- **State:** a single **Zustand** store, `mobile/src/store/useAppStore.ts`, persisted
  to **AsyncStorage**. It holds the person's signals, traits, feed track, journal,
  chat, faith words, story moments, name, blessing history, and active exercise.
  (There is no SQLite seed, no `router.js`, no `seed.js`, no `interaction_log` — older
  docs that mention those are stale.)
- **The engine** (`mobile/src/engine/`):
  - `connect.ts` — the laws: two-witness "God is good" gate, Reformed/Calvinist
    framework blocking, member status only from self-ID, the milk gate
    (`mayReferenceLds`), journey assessment, human/missionary handoff.
  - `chatEar.ts` — the ear: `harvestSignals` (per-sentence, negation-guarded), the
    model-side signal-report protocol, and faith-identity detection.
  - `minister.ts` — the production minister system prompt.
  - `exercises.ts` — spiritual exercises (invite → try → report → learn).
- **Dialogue:** `mobile/src/data/questionBank.ts` — targeted routing
  (background → picture of God → God still speaks → the reach), milk-gated.
- **AI transport:** local-first. The store calls Anthropic **directly** using
  `EXPO_PUBLIC_ANTHROPIC_API_KEY` from `mobile/.env`. Model: `claude-haiku-4-5-20251001`.
  Graceful offline fallback. The `server/` proxy is kept as an optional Phase-2 path
  but is **not** used by the shipping app.

### Security (Cameron's standing instructions)
- **`mobile/.env` is gitignored and must stay that way. Never commit the key.**
- `EXPO_PUBLIC_*` values are extractable plaintext from a built bundle — fine for
  Cameron's own testing, but **never** put a real secret there for a shipped/public
  build. For shipping, the key belongs behind the `server/` proxy.
- Never commit secrets of any kind.

---

## Working across apps (the part Cameron asked for)

The project moves between apps (this terminal, the Anthropic app, Claude desktop
"cowork") through **one channel: the git repository on GitHub**
(`github.com/noremacttevol/MBM`). Whatever is committed and pushed is what every other
app sees. So:

- **Every meaningful change gets its own commit with a clear, plain-English message**
  that says what changed and why. This is how the work explains itself to the next app
  and to future-Cameron — not chat history, which does not travel.
- **Push after committing** when the goal is to hand work to another app or back it up.
- **Pull / open the latest before starting** in any app, so you build on current state.
- **When the vision changes, update THIS file (and `STATUS.md`) in the same commit.**
  Rules live in the repo, not in one app's memory. That is what keeps the apps from
  undermining each other.
- If two apps might touch the project, prefer finishing and pushing one stream of work
  before starting another, to avoid merge conflicts.

---

## The Self-Correction Checklist (run before saying "done")

1. Did I read the existing code before changing it?
2. Does it obey every law above — especially milk-before-meat, no visible gates,
   self-ID-only membership, and a human always one tap away?
3. No placeholders, no TODOs, every file complete?
4. Did I typecheck (`cd mobile && npx tsc --noEmit` → 0 errors)?
5. Did I verify the actual behavior (bundle/screenshot the UI, or force a Metro
   bundle), not just assume it works?
6. Did I commit with a clear message — and push if this is meant to hand off?
7. Did I update `STATUS.md` / this file if the vision or build state changed?
8. Did I explain what changed and why, plainly, at the end?

---

## Repo Layout

- `mobile/` — **the app. All new work happens here.**
- `server/` — optional key proxy + owner inbox (Phase-2 path; not used by the app today).
- `port-back/` — the verified reference bundle (laws, sim report, data).
- `ministry-sim/` — the persona ministry-simulation harness.
- `content/`, `outputs/` — content corpus and generated artifacts.
- `archive/` — historical prompts, session notes, and superseded design docs.
- `AGENT-RULES.md` — **this file. The master.**
- `STATUS.md` — current build state.
- `CLAUDE.md`, `.claudecode.md` — Claude-specific entry points; both defer to this file.
- `AGENTS.md` (root and `mobile/`) — cross-tool entry points; both defer to this file.
