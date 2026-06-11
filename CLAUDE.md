# MBM — Master Instructions for Claude Code

> Read this every session. This is the operating manual.
> Also read `.claudecode.md` — it contains the permanent system guardrails that override all defaults.

---

## System Guardrails (from .claudecode.md — enforced every session)

1. **Never cross-examine or push decisions back onto Cameron.** Take initiative as Principal Systems Architect. Research, decide, build.
2. **Target: React Native + Expo.** Mobile-first. The Flask/web prototype is reference only — do not build new features on it.
3. **Local-first architecture.** Routing engine, content corpus, and user data live on-device in embedded SQLite. App runs with no server terminal.
4. **Zero placeholders.** No `// TODO`, no snippets, no shorthand. Every file fully written, end-to-end, with complete data and error handling.
5. **Code first, talk second.** Deliver complete working code blocks first. Brief explanation at the end only.
6. **Use Playwright** to screenshot and verify all UI before declaring anything done. Never ask Cameron to be the bug reporter.

---

## What MBM Is

MBM (Milk Before Meat) is a mobile-first gospel outreach platform patterned after Christ's method of ministering — meeting users exactly where they are, learning them deeply, and guiding them from foundational truth (milk) to the restored gospel (meat).

The goal is Facebook-level personalization in service of the gospel. Multiple pathways — feed, dialogue, journal, human connection — all feeding one engine that learns who the person is and what they need next.

**User statuses (how we talk about people — not tiers):**
- Unbeliever
- Investigator
- Calvinist
- Other Tradition
- Falling Away LDS
- Loyal LDS

**Feed tags (internal routing — never shown to users):**
- MILK — foundational Christian content; parables, comfort, invitation
- BRIDGE — apologetics, evidence, skeptic-friendly
- RESTORATION — Joseph Smith story, apostasy, priesthood authority
- MAINTENANCE — LDS discipleship content for active members

**Three phases:**
- **Phase 1 (now):** Cameron alone. Connection requests go to Cameron. AI handles all responses; Cameron reviews in admin.
- **Phase 2:** Small team of volunteers/supporters receive and respond to connection requests and threads.
- **Phase 3:** Church partnership. Real missionaries integrated into chat and connect pipeline.

Build for Phase 1 now. Design so Phases 2 and 3 slot in without rewriting.

---

## Stack

**Primary (build everything new here):**
- React Native + Expo
- SQLite on-device via `expo-sqlite`
- Anthropic API (claude-haiku-4-5-20251001) for AI — called when internet available, graceful offline fallback
- Expo SecureStore for session data

**Reference only (do not add features):**
- The Flask/Python prototype in this folder — useful for understanding the routing logic, question bank, and content schema. Logic can be ported to RN.

---

## How to Work With Cameron

Cameron sets the vision. AI — not Cameron — is responsible for knowing how to build it right.

- **Take initiative.** Build the best version that serves the mission. Do not implement a weaker version just because it was the first description.
- **Never ask Cameron to test, debug, or report bugs.** Screenshot and verify everything with Playwright or device preview before reporting done.
- **Explain what changed and why**, in plain language, at the end of the output — after the code.
- **Plain language always.** No jargon, no lectures, no analogies unless Cameron asks.

---

## Build Protocol

**Before touching any file:**
1. Read CLAUDE.md and .claudecode.md
2. Read every file relevant to the task
3. Understand what already exists

**When building:**
- Write every file completely. No stubs, no partial implementations.
- Screenshot and verify UI with Playwright after every change.
- If something adjacent would make it significantly better, build that too and explain it.

---

## Gospel Principles — Non-Negotiable

Every design decision answers to these:

- Meet people where they are. Do not require a tradition before they are ready.
- Never pressure, shame, or manipulate. Spiritual safety matters more than conversion metrics.
- Be honest. The app never hides what it is when someone is ready to know.
- Always keep a real human one tap away. Not buried. Not gated. Always there.
- The AI speaks only from what it knows. It admits uncertainty. It always offers the human.
- A person is not a data point. Metrics exist to serve them better, not route them like a package.
- Jesus let the rich young ruler walk away. This app does too.

---

## The Jesus Method — Reviewed and Confirmed by Grok + Gemini (June 2026)

These rules were validated by two external AI systems asked to critique MBM honestly against scripture and the actual pattern of how Jesus ministered. They override any earlier implementation that conflicts with them.

### The core error to never repeat
Sequential visible gates — "you must pass Gate 2 before seeing Gate 3" — are pharisaical hurdles, not Jesus's method. They replace a corporate survey with a theological test. Jesus did not demand ideological compliance before offering connection. He offered the living water first (John 4). The father ran while the son was still far off (Luke 15). The woman touched the cloak before she said a word. **The app must never make a person feel they have not yet qualified for the next step.**

### What replaces the gate system
**Invisible, emergent routing based on love paying attention.**

The app listens to what a person says and routes silently behind the scenes. The person never knows they have been categorized. There are no visible gates, no progress bars for spiritual readiness, no "you haven't unlocked this yet" moments. Readiness is detected from language patterns and engagement — not from checkbox completion.

Grok's exact words, confirmed: *"The gates become emergent from conversation, not prerequisites."*

### The onboarding law: Story first. Always.
The first thing a person sees is never a question about their background. It is a story, or a fragment of one, told beautifully enough that they see themselves in it. Jesus never opened with a survey. He told stories to crowds who hadn't asked for them. The story does the work of making the person ready to answer.

**Onboarding flow (this is the law, not a suggestion):**

1. **Sanctuary open.** A single visual + one true statement. No branding, no explanation. Just presence. Example: "He Is Risen. Every piece of genuine peace, beauty, or hope you have ever felt has a source."

2. **One story told well.** The Woman who touched his cloak. The Prodigal Son. The Woman at the Well. Told in 3–5 sentences as narrative, not scripture recitation. Ends with the emotional truth of the story: desperate, seen, welcomed, called daughter, running toward.

3. **One open question that honors their reality.** Not "what is your religious background?" The question comes from the story. Examples:
   - After the Woman at the Well: *"Have you ever been searching for something and realized later it was deeper than what you thought you wanted?"*
   - After the Prodigal Son: *"Which part feels closest to something you have experienced — the son far away, the father waiting, or something else?"*
   - After the Woman with the cloak: *"Have you ever been that desperate for something in your life to change?"*

4. **Reflect back immediately before serving any content.** The app echoes what they said in their own words. This is not a chatbot transition. It is the moment the person feels seen. Example: *"Thank you for that. It sounds like you have been carrying [X] and wondering if [Y]. That is exactly the kind of thing Jesus paid attention to."*

5. **Feed initializes from their response, silently.** No label is ever shown to the user. The routing signal is set internally:
   - Burden + grief + desperation → MILK
   - Questions + doubt + analytical → BRIDGE
   - Active faith + wanting more → MAINTENANCE
   - Free text → NLP sentiment detection, defaulting to MILK until signals emerge

### Stories as interactive mirrors — not information
When a story is used, it must invite the person to place themselves inside it. Never tell a story and move on. Always follow it with a question that asks which part they recognize in themselves.

**Prodigal Son:** After the story — *"Which character feels closest to where you are right now — the son who left, the father waiting, or the older brother who stayed but felt unseen?"* Each answer reveals a different spiritual need and routes to different content and dialogue.

**Woman at the Well:** After the story — *"She came for water and ended up talking about her real life. Have you ever been searching for something and realized later it was deeper than what you thought you wanted?"*

**Woman who touched his cloak:** After the story — *"She didn't even ask. She just reached. Jesus turned and found her and called her daughter. What would it mean to you if someone saw you like that?"*

### What signals readiness for deeper content
These are language patterns to detect — not gates to pass:

**Ready for more (go one layer deeper):**
- Curiosity language: "I've always wondered…", "That makes sense but what about…"
- Ownership of pain or longing: "I feel like the son who left…"
- Openness, even tentative: "I want to believe God is good but life has been hard"
- Request for more: "Tell me the rest of the story"

**Stay gentle, do not advance:**
- Strong resistance or anger without curiosity
- Surface agreement with no personal connection ("Yeah that's nice")
- Trauma language — empathy before anything else: "I was hurt by church people…"
- Defensiveness or testing — respond with Jesus's words, never debate

**Never argue doctrine.** If someone believes God sends people to hell for his glory, the response is not an argument. It is the words and stories of Jesus from the Bible they already accept. Let Jesus correct error through his own voice. The book *The Creation Dilemma* maps out how LDS theology resolves the cruelest contradictions in Calvinist thought — but this is only introduced after a person has shown they are willing to examine whether God's character matches what they have been told.

### The BOM law
The Book of Mormon is never mentioned, referenced, or implied until a person has:
- Shown they believe God is fundamentally good
- Shown curiosity or openness about continuing revelation or God still speaking today

This is not a gate they know they are passing. It is a signal the app detects and responds to. The RESTORATION feed tag never appears until these signals are present.

### For active LDS members
Separate track from the moment they identify. They never see the skeptic or seeker onboarding. Their feed is MAINTENANCE: spiritually nourishing content that replaces doom scrolling. Covenant deepening, general conference, scripture study patterns. They can also be shown the outreach content if they want to share the app with someone they know.

### Data collection for refinement
Every story response, every dialogue turn, every signal detected is stored. The goal is that every conversation makes the app better at doing what Jesus did — meeting the exact person in front of it with exactly what they need. Cameron reviews what is working. Nothing is thrown away.
