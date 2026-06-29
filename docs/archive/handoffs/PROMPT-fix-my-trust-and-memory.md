# Prompt for a new chat — fix the memory/continuity problem on my project

Copy everything below this line into a fresh chat.

---

I need your help fixing a trust problem, not building a feature. Read this fully before responding.

**Who I am and what I'm building.** My name is Cameron. I don't know much about computers — I rely on the AI to do almost everything technical. I'm building a mobile app called MBM ("Milk Before Meat"), a React Native + Expo gospel-outreach app. The project lives on my computer at `Desktop/Brain/MBM`. There's a `CLAUDE.md` and an `AGENT-RULES.md` in that folder that are supposed to be the source of truth, and there's a memory folder at `.auto-memory/` that the assistant writes notes to between sessions.

**The actual problem — this is what I need fixed.** Across different chats, the assistant keeps losing track of where we already are and makes me re-explain things I shouldn't have to, or worse, tells me things are not done when they are. The pattern repeats and it's destroying my trust. Concrete recent example: we have already built and published multiple versions of this app (iOS is on TestFlight; Android has shipped version 3 and 4 already, and we just built version 5). But in a recent chat the assistant treated publishing Android as if it were brand-new setup, told me I'd need to "create a Google Play account" and pay a "$25 fee," and asked me to do setup steps we finished long ago. That is exactly backwards from reality. It felt like it forgot everything we'd done and wasted my time on stuff that was already handled.

**Other context that should already be "known" every session but keeps getting lost:**
- iOS publishing works end-to-end via EAS cloud builds (no Mac needed). Apple Developer account, certificates, App Store Connect API key — all already set up.
- Android has already been published before (so the Google Play side already exists; this is NOT a from-scratch setup).
- The recurring technical gotcha: writing/committing code does NOT put it on my phone — a new build has to be made AND installed. Fixes have "gone missing" several times purely because the installed build was made from older code.
- I've repeatedly said: take initiative, don't make me be the bug reporter, and don't re-ask things we've settled.

**What I want from you in THIS chat (please actually answer these):**
1. Explain, in plain English with no jargon, WHY an AI assistant keeps losing this context between chats — what are the real mechanisms (and limits) of its memory, and why do good notes still sometimes fail to get read or trusted at the start of a session?
2. Tell me concretely how to set this project up so that EVERY new chat reliably knows the true current state before it does anything — e.g., what should live in the memory file vs. CLAUDE.md vs. a "current status" file, how it should be structured, and what I (a non-technical person) should paste or say at the start of each chat to force the assistant to load reality first.
3. Give me a short, reusable "start every session like this" checklist that I can keep and reuse, so I stop having to re-explain my own project.
4. Be honest about what the AI genuinely cannot do for me (things that truly require me — like entering my own passwords or payment) versus things it has been wrongly claiming it can't do when it actually can. I want the real line, because it keeps moving and that's part of why I don't trust it.

Don't sugarcoat it and don't flatter me. I want straight answers about how the memory actually works and a concrete system so this stops happening.
