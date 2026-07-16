# MBM — Master Instructions for Claude Code

> 🖥️ **KNOW WHICH COMPUTER YOU ARE — do this FIRST, before the session chain.**
> All of Cameron's computers run Claude Code on this same repo, so a "this machine
> is X" note inside any shared file is read by ALL of them and CANNOT be trusted.
> Run `hostname` and look it up in [`MACHINE-IDENTITY.md`](./MACHINE-IDENTITY.md)
> to learn which machine (A/B/C/etc.) you are. If your hostname isn't listed, ask
> Cameron and add it. Only THAT table decides your identity — never a sentence in
> the session log or claim board.
>
> 🔗 **SESSION-CHAIN PROTOCOL — THIS IS YOUR VERY FIRST ACTION IN EVERY NEW CHAT.**
> Before you do ANY other work, before answering anything else:
> 1. Read the TOP entry of [`SESSION-LOG.md`](./SESSION-LOG.md).
> 2. Run `git log --oneline -5` and confirm the entry's "Commit:" hash APPEARS in the
>    history (proving that session was saved). If it does NOT appear, tell Cameron
>    something wasn't saved instead of guessing.
> 3. Make your FIRST message to Cameron a short recap of that last session AND the
>    matching commit hash — this proves to him you read the chain and that the last
>    session was saved. Only after that do you begin new work.
> At the END of any session where something happened: add a new entry at the TOP of
> SESSION-LOG.md, commit it, and push to GitHub (origin/main). That commit is the new
> link in the chain that the next chat will verify.
>
> 🛑 **ALSO READ [`START-HERE.md`](./START-HERE.md) at the start.** It is the ONLY
> file that states the CURRENT state of the app (what's built, what's published, what
> accounts exist). Your memory and every other doc can be stale; START-HERE.md is the
> truth and overrides them on "what is true right now." Do NOT tell Cameron to set up
> accounts or pay fees that START-HERE.md says are already done.
>
> **For the VISION, LAWS, and HOW TO WORK, the source of truth is [`AGENT-RULES.md`](./AGENT-RULES.md) — read it first,
> every session, on every platform (Claude Code, the Anthropic app, Claude desktop,
> any tool).** It consolidates the full vision, the laws, the architecture, the current
> build state, and how to work across apps. If anything in this file conflicts with
> `AGENT-RULES.md`, that file wins. The detail below remains valid and is kept for
> Claude Code's auto-loaded context.
>
> Read this every session. This is the operating manual.
> Also read `.claudecode.md` — it contains the permanent system guardrails that override all defaults.

---

## 🎬 VIDEO DUTY — when Cameron says "do the next video" (or "next")

This is a standing job. When Cameron says **"do the next video," "next,"** or
**"make my next video,"** that short phrase is the WHOLE instruction — he never
re-explains. Do this, in order:

1. `git pull --rebase origin main`.
2. Open [`media-production/QUEUE.md`](media-production/QUEUE.md). The next job is
   the **lowest-numbered row where `Built` is ⬜ and `Claim` is empty.** (If
   Cameron named a number, build that one instead.)
3. **Claim it immediately** so no other computer takes it: create
   `media-production/build-NN-slug/`, write your machine + today's date into that
   row's `Claim` column, commit, and **push before generating anything**. If the
   push is rejected, another computer grabbed it while you read — pull and take the
   next open row. This claim-by-push is the ONLY thing keeping all 4 computers off
   each other's video; never skip it.
4. Read `media-production/PRODUCTION-BIBLE.md` and `CREW-GUIDE.md`. Every law binds
   this session (face-never, two-voice, stills-only, ear-check, no-dead-air,
   self-revision, full-story). Study the KJV passage in full context first.
5. **Build the whole video yourself — including the Google Flow photo burst in
   Chrome, the same way it's been done. Cameron does NOT make the pictures.** Pass
   `jesus_face_gate.py` before any Flow credit. Tick `Prep`/`Built` in QUEUE.md as
   you go and push each change. Do the full Self-Revision QC before you show him.
6. Show Cameron the finished video. He watches it once and says yes. Then tick
   `Appr` (and `Post` once it's published). Add a SESSION-LOG entry, commit, push.

Cameron should be able to run this loop by only ever saying **"looks good, next."**
Keep each video to ONE chat so context stays low — that is the whole point. On
each of his 4 computers he just opens a chat and says "next"; the QUEUE claim keeps
them from ever colliding. (Optional: `media-production/next-job.sh` auto-opens a
primed chat, and `SCHEDULER.md` can put it on a timer — but "just say next" is the
everyday way and needs neither.)

---

## System Guardrails (from .claudecode.md — enforced every session)

1. **Never cross-examine or push decisions back onto Cameron.** Take initiative as Principal Systems Architect. Research, decide, build.
2. **Target: React Native + Expo.** Mobile-first. The Flask/web prototype is reference only — do not build new features on it.
3. **Local-first architecture.** Routing engine, content corpus, and user data live on-device in embedded SQLite. App runs with no server terminal.
4. **Zero placeholders.** No `// TODO`, no snippets, no shorthand. Every file fully written, end-to-end, with complete data and error handling.
5. **Code first, talk second.** Deliver complete working code blocks first. Brief explanation at the end only.
6. **Use Playwright** to screenshot and verify all UI before declaring anything done. Never ask Cameron to be the bug reporter.
7. **For ALL video/media production work, [`media-production/PRODUCTION-BIBLE.md`](./media-production/PRODUCTION-BIBLE.md) is the permanent law** — locked animation style block, hybrid stills+motion pipeline, story-fit rule, QC checklist, credit accounting. Read it before any media work. Cameron never writes prompts or edits clips; the AI runs the whole assembly line and presents finished videos.
8. **The Jesus-framing laws (PRODUCTION-BIBLE §1, "The Standing Laws") are non-negotiable and Cameron has rejected finished videos over each of them. THE #1 LAW: never prompt or show Jesus's face — see (f)/(g).** (The old numbered "Corrections #1–#18" were consolidated into the un-numbered Standing Laws on 2026-07-11; the numbered history is archived in media-production/CORRECTIONS-HISTORY.md, provenance only.) The ones violated most: (a) reverence and non-specificity govern how he is framed — his FACE is NEVER shown (f/g below); (b) NEVER a small detached Jesus at the frame edge while the crowd's eyes wander — gazes must visibly converge on him; (c) NO rim-light, halo, or glow that outlines his face or head — a glowing silhouette highlights him, the opposite of the goal; (d) still BEFORE motion clip when a beat has both; (e) the anti-panel sentence is mandatory in every wide multi-figure still prompt; (f) **JESUS'S FACE IS NEVER PROMPTED OR SHOWN (Cameron, 2026-07-11). We do not know his face; a constructed face — different every story — pulls the viewer onto the artwork and is not good worship. NO prompt may name his face, eyes, gaze, expression, smile, cheek/jaw/nose/mouth/brow, a portrait, a close-up, a three-quarter view, or a profile. Hide by ANGLE only: from BEHIND, OVER-THE-SHOULDER (camera behind him, the people facing past the camera at him), or true DISTANCE. Run the mechanical gate before any credit: `python3 media-production/jesus_face_gate.py --dir <build-folder>` must exit 0**; (g) **He IS still a real, warm, painted human (Middle Eastern hands and hair may show), NOT a hooded void / black cutout / "Assassin's Creed" ghost, and his skin is warm MIDDLE EASTERN tan/olive-brown, NEVER white/Caucasian. Never hide the face with halo/glow. Other characters DO show faces — kept consistent within a story; only Jesus's face is withheld. THE JESUS LOOK STANDARD (Cameron, 2026-07-11 — standardize across ALL videos): LONG dark hair past the shoulders (never short, never changing length); ONE plain undyed off-white/cream wool robe every scene and every video (never a fur/fleece look, never changing); warm Middle Eastern skin; from BEHIND / back-of-head is the default because a side profile shows too much of his face; see PRODUCTION-BIBLE §1 'THE JESUS LOOK STANDARD' (Cameron, 2026-07-11)**; (h) ACTION-LOGIC LAW — every figure's action must read correctly at a glance (storm V1 rejected: fishermen appeared to pour water INTO their own boat and pull a rope leading outside the hull); bailing throws water OUT over the gunwale, ropes connect to rigging inside the boat; QC every frame by asking "what does this person appear to be doing?"; (i) TIME-OF-DAY LAW — scene lighting must match the scripture's stated time of day; Mark 4:35 is night: limited light, moon/stars/lightning, NEVER sunset or sunrise coloring (Cameron, 2026-07-10, storm-11 V2 rejection); (j) figures stay visibly INSIDE the boat — deck under feet, gunwale connecting around them; nobody stands on the water unless the scripture puts them there; (k) CYCLICAL-MOTION LAW — repeated actions in clips must visibly cycle (scoop-lift-fling for bailing), never a static pose with a continuous hose-like stream.** Whenever Cameron gives a new correction, write it into PRODUCTION-BIBLE §1 AND this list in the same session.
9. **Multi-machine claim law (Cameron, 2026-07-10 — PRODUCTION-BIBLE §0 Law A).** Cameron runs Claude on multiple computers, all on this same project. Before ANY video work: `git pull`, open `media-production/VIDEO-ASSIGNMENTS.md`, claim an UNCLAIMED video, commit + push the claim BEFORE generating anything. Never touch a video claimed by another machine. This prevents two machines burning credits on the same video.
10. **Never hold Cameron's computer hostage (Cameron, 2026-07-10 — PRODUCTION-BIBLE §0 Law C).** Browser automation steals his mouse and window focus while he's working on the same machine. Announce each Chrome burst in the message right before starting it, then START IMMEDIATELY — never stop to ask permission or wait for a "go" (Cameron, 2026-07-10: asking again after he has set work in motion is itself the failure; his protection is that any message from him stops the browser instantly). Prepare everything (prompts, scripts, QC) in files/terminal first, then do the clicks in one short announced burst. If Cameron sends any message mid-burst or says he's using the computer, STOP the browser immediately. All non-browser work (writing, audio, assembly, git, QC on downloaded files) never touches his screen — do as much as possible there.
11. **Run to completion — never stop mid-video (Cameron, 2026-07-11 — PRODUCTION-BIBLE §0 Law D).** Once Cameron says go, build the ENTIRE video end to end (every still, every motion clip, narration, assembly, QC) and present ONE finished video. Do not stop partway to report progress-and-wait or ask "keep going?" — he already answered. The only allowed stops are: the video is DONE, or a real blocker you cannot resolve yourself and must ask about (a genuine question, not a permission check). Give progress updates WHILE continuing to work. (Law C still holds: if Cameron himself messages, yield the browser instantly — that is his interrupt.)
12. **PHASE 1 IS STILLS-ONLY — NO AI motion clips for now (Cameron, 2026-07-11 — PRODUCTION-BIBLE §0 Law E, current version, which REVERSED the earlier "motion required" rule).** Every video is produced as narrated painted STILLS with slow Ken Burns drift, serif captions, KJV verse card, and closing question card — and NO Veo/Flow motion clips at all. Why: the AI-animated clips are where nearly every error, hours of rework, and credit burn came from; a still costs ~0 and regenerates in seconds. Get all 200 done as picture-and-narration videos FIRST. A delivery containing any AI-animated clip is OUT OF SPEC. PHASE 2 (later, only when Cameron says so): go back through the finished library and add motion only to the specific beats that genuinely need it. The §3 Story-Fit clip counts are SUSPENDED for Phase 1.

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

---

## Locked Product Direction — June 2026 (do not lose this)

> Cameron explained these four directions in full and asked that they be stored so he never has to re-explain. They are now rules. Build toward them; do not regress them.

### 1. Onboarding is short — then a story on every cold open
- **First launch:** a FAST opening, quicker than the old onboarding. It collects only the basics — chiefly a faith background question (past or present faith), enough to seed routing — then tells ONE great story.
- **The first story** is the app's strongest, told **by the app in the name of Jesus, quoting real scripture**, rendered for emotional impact, ending in one open question. The user's answer to that first question is recorded to the Profile as the founding entry of who they are in comparison to Christlikeness.
- **Every cold open after the first** (app opened from a fully closed state): the app tells ANOTHER short, powerful Jesus/God's-love story — **never repeating one already told**. Each is recorded to the Profile with the user's answer, until they have seen them all.
- This is the engine of return: a growing, personal record of stories seen, answers given, and lessons learned. The Profile **accumulates** these, records the answers, and **summarizes the traits learned** from them.
- Every story ends with a link into the AI chat to talk about it more.
- Stories are short-form, scripture-grounded, and high-impact — not recitation. Track completion so the user is motivated to keep coming back and finish them all.

### 2. The story/lesson record lives on the Profile
The Profile is where the app shows it has learned the person: the stories they've experienced, the answers they gave, and a Christlikeness read summarized from them. This is the visible payoff for coming back.

### 3. Member ("meat") track must be easy to opt into — and hidden, to respect the mystery
- A person who is baptized, saved, or curious about The Church of Jesus Christ of Latter-day Saints needs their experience tailored deeper — toward the four standard works and prophet-aligned discipleship — distinct from the milk/convert track.
- **How the app learns to go deeper: detection from their own words (Cameron's choice, June 2026).** There is no visible "I'm a member" toggle. The app infers depth from how they talk and what they engage with, then shifts silently — which already respects the mystery, since nothing is ever waved in front of seekers. (This rides on the existing self-ID signals — `active_member`/`inactive_member` from Law 3 — never on a guessed label.)
- The member-helping AI must be trained to teach the way Latter-day Saints actually learn and grow — deeper doctrine, keeping pace with the living prophet — NOT the milk used to win converts. Same Christ, different depth.

### 4. The milk AI always defends the goodness of Jesus, and walks others toward the Restoration through their OWN scripture
- The AI's fixed center: **always and only defend the true goodness of Jesus.**
- With a Calvinist, Catholic, Southern Baptist, or any tradition: use the scripture **they already accept** to establish that Jesus is good, then carefully navigate their own logic — gently, never by argument — so it begins to align with the theology of The Church of Jesus Christ of Latter-day Saints. Expose the contradiction by letting Jesus's own words do the correcting (see "Never argue doctrine" and the BOM law above — this does not override the milk-before-meat gate).
- The whole app, milk and meat alike, acts the way our version of Jesus would want an AI to act.

### 5. Multiple-choice answers must not corner people into doubt
- Current dialogue answer options skew negative — they make "I don't believe because X" look like the expected answer, which demeans and discourages believers.
- Every such question needs a genuine, **well-framed belief / testimony** answer option, so a believer can testify instead of being boxed into unbelief. Framing matters: give people a good reason to testify, don't make doubt the default-looking choice.

### Testing note
The on-device store is reset for a clean test by bumping the persist key `name` in `useAppStore.ts` (currently `mbm-app-store-v3`). This is a one-time wipe of local data only and does NOT change how often real users' memory persists. A self-serve "Start fresh" reset for the testing phase may be added to the Profile screen.
