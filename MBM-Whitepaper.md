# MBM — Milk Before Meat
## Spiritual Social Media Ministering Platform
### White Paper & Technical Blueprint

---

## What This Is

MBM is a social media platform built to do what Facebook does technically — but with a completely different purpose. Instead of an algorithm that learns what entertains you to keep you scrolling, MBM's algorithm learns what spiritually resonates with you so it can connect you to the Gospel in a way that is personally meaningful.

The name comes from the LDS missionary principle: before teaching the deep doctrines of the Gospel (the "meat"), you build a relationship and teach the foundational truths first (the "milk"). This concept maps directly onto how machine learning recommendation systems work — you start broad, observe what resonates, and progressively tailor toward deeper truth as the person is ready.

The core mission: **show every person how God is personally good for them — using their own life, interests, and struggles as the entry point.**

---

## The Core Insight — The Objective Function

Facebook's algorithm optimizes for: **engagement → time on platform → ad revenue**

MBM's algorithm optimizes for: **spiritual resonance → personal connection to God → transformation**

This single difference changes everything about what the algorithm learns and what it surfaces. Same technical machinery. Completely different outcome.

**The Jesus Pattern:**
Jesus never gave the same message to every person. He met each person where they were:
- To fishermen: "I will make you fishers of men" — their language, their world
- To a tax collector (Zacchaeus): shared a meal first, no sermon, no judgment
- To the Samaritan woman at the well: spoke to her felt thirst before the living water
- To Nicodemus: engaged intellectually and philosophically
- To the rich young ruler: addressed his specific idol directly
- To the disciples after the resurrection: cooked them breakfast on the beach

Each person got a different **entry point** to the same truth. The truth never changed — the approach always did. MBM automates this at scale.

---

## Ethical Design Principle — Personalization vs. Manipulation

This is the most important section. Get this wrong and the app becomes harmful.

**The line:**

| Manipulation (Wrong) | Genuine Personalization (Right) |
|---|---|
| User doesn't know they're being profiled | User explicitly opts in and sees their profile |
| Algorithm optimizes for YOUR conversion metric | Algorithm optimizes for THEIR growth and discovery |
| Truth is withheld strategically without consent | All truth is available; the entry point is personalized |
| Behavioral nudging without transparency | Transparent: "we matched this to your interest in X" |
| "Subdue" people toward a goal they didn't choose | Invite people into a journey they choose to take |

**The rule:** MBM never hides what it's doing. The user always knows the app is learning about them to show them more relevant spiritual content. The profile is visible to the user. The categories they're in are shown to them. This isn't just ethical — it's more effective. People engage more deeply when they trust the platform.

The Gospel doesn't need deception to spread. If it requires hiding what you're doing, something is wrong with the approach.

---

## App Concept — Core Features

### 1. Onboarding — Voluntary Profile
When a user joins, they answer optional questions about:
- Where they are spiritually (seeking, doubting, growing, curious)
- What they're wrestling with in life (purpose, loneliness, grief, identity, fear, forgiveness)
- Their interests and background (work, hobbies, culture, age)
- What kind of content they like (stories, teaching, music, testimony, reflection)

This builds their initial profile vector. Everything after this is learned from behavior.

### 2. The Feed
Personalized content stream including:
- Scripture passages matched to their current life themes
- Short-form testimonies from people with similar backgrounds
- Teachings and devotionals tied to their questions
- Reflection prompts ("How does this apply to your week?")
- Community posts from others on similar journeys

### 3. The Growth Path (Milk → Meat)
Users are placed on a journey track that starts broad (foundational truths about God's character, Jesus's life) and progressively deepens as they engage. The system tracks readiness signals:
- Time spent on deeper content
- Questions asked
- Reactions to challenging teachings
- Voluntary engagement (saves, shares, responses)

The deeper "meat" content is always available — it's never locked. But the algorithm doesn't flood a brand-new seeker with advanced theology on day one.

### 4. Transparent Profile Page
Users can see:
- Their current "spiritual interests" tags
- Their journey stage
- What content categories they engage most
- The option to edit or reset their profile

This transparency builds trust and invites people into the process.

### 5. Community & Connection
- Match users with others on similar journeys for conversation
- Connect seekers with believers who have similar backgrounds
- Small group formation based on life stage and questions

---

## Technical Architecture

### System Overview
```
[User] → [Event Logger] → [Feature Store]
                               ↓
[Content Library] → [Embedding Engine] → [Recommendation Engine] → [Feed]
                               ↑
                        [Feedback Loop]
```

### Layer 1 — Event Logging
Track every meaningful signal:
- `content_viewed` (content_id, user_id, duration_seconds)
- `content_reaction` (content_id, user_id, reaction_type: saved/shared/reflected/skipped)
- `reflection_submitted` (content_id, user_id, word_count, sentiment)
- `search_query` (user_id, query_text)
- `profile_answer` (user_id, question_id, answer)

Do NOT track: location, contacts, external browsing. Only in-app behavior.

### Layer 2 — User Embeddings
Each user is represented as a vector across these dimensions:
- `life_stage` (student / young adult / parent / senior / etc.)
- `spiritual_stage` (curious / seeking / new believer / growing / mature)
- `life_themes` (purpose, loneliness, grief, identity, forgiveness, fear, meaning, relationships)
- `content_style_preference` (story, teaching, music, testimony, reflection, community)
- `depth_readiness` (0.0 → 1.0 — how ready for deeper content based on engagement history)
- `background_context` (cultural markers, interests, profession categories)

These start from onboarding answers and update continuously from behavior.

### Layer 3 — Content Embeddings
Every piece of content is tagged with:
- `primary_theme` (from life_themes above)
- `spiritual_depth` (milk=0.0 → meat=1.0)
- `content_type` (scripture, testimony, teaching, reflection_prompt, community)
- `target_stage` (which spiritual_stage this speaks to)
- `tone` (comforting, challenging, joyful, instructive, narrative)
- `scripture_references` (Bible verses cited)

### Layer 4 — Recommendation Engine
Algorithm matches users to content:

1. **Depth filter:** Only show content where `spiritual_depth <= user.depth_readiness + 0.2` (slight stretch is fine, big jumps aren't)
2. **Theme matching:** Score content by cosine similarity between user's `life_themes` vector and content's `primary_theme`
3. **Style matching:** Boost content matching user's `content_style_preference`
4. **Freshness:** Apply time decay to avoid showing same content repeatedly
5. **Diversity:** Ensure feed has mix of content types, don't over-optimize one theme

**Scoring formula (simplified):**
```
score = (theme_similarity * 0.4) + (style_match * 0.3) + (depth_fit * 0.2) + (freshness * 0.1)
```

### Layer 5 — Feedback Loop
After each content interaction, update the user vector:
- Long view (>60s) + save/share → increase weight on that theme + depth dimension
- Skip (<5s) → decrease weight on that content style/theme
- Reflection submitted → significant positive signal, increase depth_readiness slightly
- "Not for me" explicit feedback → strong negative signal

Use a simple exponential moving average to update vectors gradually. Don't overreact to single signals.

### Layer 6 — The Milk→Meat Progression
`depth_readiness` starts at 0.0 and evolves:
- Increases when: user engages deeply (long views, reflections, saves deeper content)
- Stays stable when: user engages normally
- Decreases slightly when: user consistently skips deeper content

Thresholds (example):
- `0.0 – 0.3`: Foundational content only (God's character, Jesus's life, simple testimonies)
- `0.3 – 0.6`: Intermediate (parables, discipleship, specific life application)
- `0.6 – 0.8`: Deeper doctrine, spiritual disciplines, challenging teachings
- `0.8 – 1.0`: Full depth — theology, apologetics, deep study

---

## Data Model (Database Schema Sketch)

```sql
-- Users
users (id, created_at, spiritual_stage, depth_readiness)

-- User profile vector (stored as JSON or separate columns)
user_embeddings (user_id, life_themes JSON, style_prefs JSON, background JSON, updated_at)

-- Content library
content (id, title, body, content_type, spiritual_depth, primary_theme, tone, created_at)
content_tags (content_id, tag_type, tag_value)

-- Event log
events (id, user_id, content_id, event_type, duration_seconds, created_at)

-- Reactions
reactions (id, user_id, content_id, reaction_type, created_at)

-- Reflections
reflections (id, user_id, content_id, text, word_count, created_at)

-- Feed history (to avoid repeats)
feed_history (user_id, content_id, shown_at)
```

---

## Technology Stack Recommendation

**Backend:**
- Python (FastAPI) — ML-friendly, fast API development
- PostgreSQL — relational data + JSON support for embeddings
- Redis — cache user vectors for fast feed generation
- Celery — async jobs for embedding updates

**ML:**
- scikit-learn or PyTorch — user/content embedding and similarity scoring
- Sentence-transformers — NLP embedding of content text for semantic matching
- Simple collaborative filtering to start, upgrade to neural later

**Frontend:**
- React Native — iOS and Android from one codebase
- Feed component similar to Instagram/TikTok scroll

**Content Moderation:**
- All content reviewed before going live
- Theological review layer — doctrinal accuracy check
- No user-generated content initially (curated library only)

---

## What to Build First — MVP Scope

Do not build everything. Start here:

1. **User onboarding flow** — 5 questions, builds initial profile
2. **Content library** — 50-100 hand-curated pieces, manually tagged
3. **Basic recommendation** — rule-based first (no ML yet), match tags to profile
4. **Feed display** — simple scroll, track views and reactions
5. **Transparent profile page** — show user their tags and journey stage

Once this is live and you have real user data, THEN train the ML model. Don't build ML on zero data.

---

## Instructions for the AI That Continues This Work

Hello. You are picking up a project called MBM (Milk Before Meat). The full concept and technical design is in this document. Here is what to do next:

### Immediate Next Steps:

1. **Create the project folder structure** — Set up a proper project repo with backend and frontend directories

2. **Build the database schema** — Use the schema above as a starting point. Create proper migrations. Use PostgreSQL.

3. **Build the content tagging system** — Create a tool (even just a simple script or admin UI) where content can be entered and tagged with all the dimensions described above. This is the foundation everything else depends on.

4. **Build the user profile system** — Onboarding questions, profile storage, the vector structure described above.

5. **Build the rule-based recommendation engine first** — Simple tag matching before any ML. Get a working feed.

6. **Once data exists, design the ML training pipeline** — Use the event log to train the recommendation model.

### Key Constraints to Honor:
- User data is visible to the user — never hidden profiling
- Depth readiness must evolve gradually, never force deep content early
- Content must pass a theological accuracy review before going live
- No external data collection — only in-app behavior

### Design Philosophy:
This is not a manipulation engine. It is a contextualization engine. The Gospel doesn't change. The entry point does. Every decision you make should serve the user's genuine spiritual journey, not a conversion metric.

Ask: "Would Jesus be comfortable with how this feature works?" If yes, build it. If not, redesign it.

---

*Document created: 2026-06-05*
*Author: Cameron (via Claude Code)*
*Status: Concept phase — ready for development planning*
