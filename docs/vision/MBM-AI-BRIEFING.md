# MBM ("Milk Before Meat") — Full Briefing for a New AI

I'm building a mobile app called **MBM (Milk Before Meat)**. Below is everything about the vision, the rules, the architecture, and what's been built so far. After reading it I want you to: (1) tell me honestly whether the approach is sound — spiritually and technically, (2) give me a concrete plan for what to do next, and (3) push hard on how this could actually help members of The Church of Jesus Christ of Latter-day Saints share the gospel more effectively. Be candid; don't just flatter it.

---

## The vision

MBM is a gospel-outreach and discipleship app patterned after the way Jesus Christ actually ministered: meet a person exactly where they are, pay close attention, and lead them gently from foundational truth ("milk") toward the fullness of the restored gospel ("meat"), which I believe is found in The Church of Jesus Christ of Latter-day Saints. The goal is social-media-level personalization, but in service of bringing people to Christ — not to a denomination.

**Core conviction:** Jesus wanted one unified Church, and his teachings have been cherry-picked over centuries into man-made traditions. The app uses scripture people already accept to (a) establish that God is genuinely good, and (b) gently surface the questions that lead back to the restored gospel — always through their own scriptures, never by argument.

**How we talk about people (statuses, never shown to them):** Unbeliever, Investigator, Calvinist, Other Tradition, Falling-Away LDS, Loyal LDS.

**Internal routing tags (never shown to users):** MILK (foundational, comfort, invitation), BRIDGE (apologetics, skeptic-friendly), RESTORATION (Joseph Smith, apostasy, priesthood authority), MAINTENANCE (LDS discipleship for active members).

**Three phases:** Phase 1 (now) — it's just me; the AI handles responses, I review in an admin view. Phase 2 — a small team of volunteers answer connection requests. Phase 3 — Church partnership with real missionaries in the pipeline. Build for Phase 1, design so 2 and 3 slot in.

---

## The non-negotiable laws (the "Jesus Method")

These were validated against scripture and refined; they override anything that conflicts:

- **No visible gates.** Routing is invisible and emergent from what a person says — never "you must pass step 2 to unlock step 3." Jesus offered living water first. The app never makes anyone feel they haven't qualified yet.
- **Story first, always.** Onboarding opens with a beautifully told short story (the Prodigal Son, the Woman at the Well, the woman who touched his cloak), then one open question drawn from that story, then the app reflects the person's answer back so they feel seen.
- **Never argue doctrine.** If someone believes something harsh about God, the response is Jesus's own words from the Bible they already accept — let Jesus correct error in his own voice.
- **The Book of Mormon is never mentioned** until a person has shown they believe God is good AND shown openness to continuing revelation. It's a detected signal, not a gate they know they're passing.
- **A real human is always one tap away** — never buried, never gated.
- **Care for the person before the cause.** Spiritual safety beats conversion metrics. Never pressure, shame, or manipulate. "Jesus let the rich young ruler walk away" — so does the app.
- **The app is honest about what it is** when someone is ready to know, and never pretends to be God. The AI admits uncertainty and always offers the human.

---

## The stack / architecture

- **React Native + Expo** (mobile-first; the real target is an Android app).
- **On-device SQLite** (`expo-sqlite`) + a local Zustand store with persistence — local-first, works offline.
- **Anthropic API (Claude Haiku)** for the AI chat ("Talk it through"), called when online, with graceful offline fallback. The API key lives behind a server proxy, never in the app.
- **Firebase/Firestore** for the two-way "real person" inbox (messages between a user and me/the team).
- **EAS Build** produces the installable Android APK. **EAS Update (expo-updates)** was just added so future code changes push over-the-air without a full rebuild.
- An **admin desk** (Node) where I review and reply to real-person threads.

---

## What's built and working

- **Feed** — a scrolling feed of short scripture cards, with a reflection/dialogue card mixed in, and a "Show me more" that advances through content.
- **Dialogue questions** — multiple-choice questions that quietly read a person's signals and route content. (Being revised so believers always have a genuine "testimony" answer option instead of being boxed into doubt.)
- **Journal** — prompted or freestyle writing, with topic suggestions, editable past entries, "kept notes," and the ability to open a fresh chat about any entry. The app speaks a short personal "blessing" after a sincere entry.
- **AI chat ("Talk it through")** — the minister AI, grounded in the laws above, with a one-tap escalation that copies the conversation to a real human (me) in a separate thread.
- **Profile / Christlikeness read** — seven "spirit levels" (Christlike honesty, openness, humility, hunger for truth, compassion, courage, sincerity, each 0–10). An honest "judge" reads each chat turn and moves the levels both ways; changes are shown to the person's face, never hidden.
- **Multi-thread real-person inbox** + admin desk.

---

## What we changed most recently (this is the current edge of the work)

1. **Typeface** — switched to **Jost** (a real Google Font; its lowercase "t" reads cross-like naturally), embedded and verified.
2. **Journal fixes** — the post-save links ("Another prompt / Write freely / Pick a topic") were dead because an invisible overlay ate the taps; fixed. "Written" → "Saved." "Pick a topic" is now a scrollable popup.
3. **Chat** — message bubbles widened to ~90% of screen.
4. **Virtue scoring fix** — the AI judge no longer rewards a person for *complaining* about their score; and **journaling now earns honest, length-gated credit** (it earned nothing before), so real reflection counts as much as clever questions.
5. **Over-the-air updates** — added expo-updates + EAS Update channels so, after one more build, code changes reach my phone in seconds.
6. **THE BIG ONE — the milk/meat content standard + 200 verses.** See next section.
7. **Footer fix** — the "This app is not God" disclaimer on the opening screen was overlapping the Android home/back bar; lifted by the device's safe-area inset.

---

## The milk/meat content standard (this is the heart of the content engine)

Every content item now carries a `track` (MILK or MEAT) and, for milk, a `milkTrack` (common or restoration). I authored **200 items total**, all verified by an automated test:

- **100 MILK (Bible only, shown to everyone):**
  - **50 "common"** — verses both mainstream Christians and Latter-day Saints already love, all about the goodness of God (Psalm 23, the Prodigal Son, "Come unto me," "Jesus wept," the Good Samaritan, etc.). These build trust and connection.
  - **50 "restoration"** — often-skipped Bible passages that gently raise the questions the restored gospel answers (John 10:34 "ye are gods," 1 Cor 15:29 baptism for the dead, Rev 3:21 sitting in his throne, Matt 3:16-17 the three persons at his baptism, James 1:5, Amos 3:7, Eph 4:11-14, the apostasy passages, etc.). Each carries a hidden `ldsLens` note so the chat can outline the Latter-day Saint perspective *subtly* when asked.
- **100 MEAT (the four standard works, shown only to the meat-ready):** 45 Book of Mormon, 38 Doctrine and Covenants, 17 Pearl of Great Price — the depth a member actually studies (2 Nephi 2:25, Alma 32, Moroni's promise, the three degrees of glory, the First Vision, "this is my work and my glory," etc.).

**Routing rule:** seekers see the 100 milk; meat-ready people (members, or those the restoration has been opened to) see milk **and** meat together — 200.

**The feed never repeats** an item until the person has seen them all, then it starts a fresh shuffled cycle. An automated test proves it: seeker feed = 100 distinct over 20 pages; meat-ready = 200 distinct over 40 pages; every scripture link is well-formed (Bible verses → BibleGateway KJV; LDS scriptures → churchofjesuschrist.org).

---

## Current state / honest gaps

- All of the above type-checks cleanly and passes its tests. None of it is "live" on my phone yet — it requires **one** more EAS build to install (because the currently-installed app predates the over-the-air update system). After that single build, future changes push instantly.
- **Known limitation I want addressed:** content cards currently *link out* to read the actual verse instead of showing the scripture text *in* the app. I believe embedding the text (all of it is public domain) is the single highest-value next step for real discipleship — people shouldn't have to leave to read the word.
- Still to do: wire the `ldsLens` hints into the chat so "Talk about it" gently outlines the LDS view; expand the journaling prompts; and a planned playful feature where, once a person's saved notes repeatedly agree with LDS theology, the AI lovingly points out they already think like a Latter-day Saint.

---

## What I want from you

1. Evaluate this honestly — both the spiritual approach (is it faithful to how Christ ministered, and is it respectful and non-manipulative?) and the technical design.
2. Give me a concrete, prioritized plan for the next phase.
3. Be tough on this question specifically: **is this actually a strong way for Latter-day Saints to help people come to Christ and share the gospel — and if not, what would make it genuinely effective?** I want real strategy, not reassurance.
