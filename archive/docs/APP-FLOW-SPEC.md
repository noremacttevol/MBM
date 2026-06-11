# MBM App Flow Spec — The Knowing Engine in Practice

The screen-by-screen flow that turns the six-step attention loop into something you can build.

*Build spec. Reads on top of `KNOWING-ENGINE.md`. Where this conflicts with the "Core User Journey" tier-graduation in `SPEC.md`, this wins — nobody graduates by collecting thumbs-ups anymore.*

---

## The spine

Every screen serves the same six acts of attention Jesus used with every person: perceive what they're carrying, name the real need under the stated one, meet the emotion first, tailor the door to the person, set the pace to theirs, and leave them free. The app is not moving anyone up a ladder. It is doing, through a screen, what Jesus did face to face — and keeping a real human one tap away the whole time.

Two quiet machines run underneath the whole experience:

- **The signal reader.** Listens to what a person says and does, and keeps an internal picture of who they are and what they need next. The person never sees it. There are no tiers, no progress bars, no "unlocked" moments.
- **The approach selector.** Uses that picture to choose *how* to speak to this person — debate-ready for the one who wants to wrestle, gentle questions for the one who doesn't. Same truth, different door.

---

## Screen-by-screen flow

### 1. Sanctuary (open)
One image, one true sentence, no branding, no buttons fighting for attention. Example: *"He is risen. Every piece of genuine peace, beauty, or hope you have ever felt has a source."* A single soft way forward — "I want to understand that." Nothing is asked of the person yet. This is presence before request, the way Jesus was simply *there* before he spoke.

### 2. One story, told well
The first real content is a story, never a question about their background. Three to five sentences, told as narrative, ending on the emotional truth — not a scripture citation. Rotate among a small set: the Woman at the Well, the Prodigal Son, the Woman who touched his cloak. The story does the work of making the person ready to answer.

### 3. The mirror question
One open question that comes *out of the story*, inviting the person to place themselves inside it. Never "what is your religious background?" Instead, after the Prodigal Son: *"Which part feels closest to where you are right now — the son who left, the father waiting, or the older brother who stayed but felt unseen?"* Their answer is the first real signal. Each answer points at a completely different need — and that is the point.

### 4. The reflect-back
Before serving any content, the app echoes what they said in their own words. This is the moment the person feels seen, not processed. *"Thank you for that. It sounds like you've been carrying [X] and wondering if [Y]. That's exactly the kind of thing Jesus paid attention to."* This is the leper being touched before he is healed. It happens every time, never skipped.

### 5. The feed, silently initialized
Now content begins — chosen from the signal the mirror question set, with no label ever shown. Burden and grief lean toward comfort and the parables; questions and analysis lean toward evidence and honest answers; active faith leans toward nourishment. One card at a time, clean. The person can say "this spoke to me" or "not for me," can read the full passage, and can always reach a human. Reactions refine the picture — they do **not** promote anyone to a tier.

### 6. Ask Anything (the AI Q&A)
A place the person can ask any question and get a grounded, honest answer. The AI:
- speaks only from what it actually knows (LDS scripture, official teaching, verified sources), and grounds answers in retrieved content rather than speculating;
- is honest the moment it's uncertain — *"I want to be honest, I'm not fully sure about this"* — and hands off rather than bluffing;
- is honest about being an AI if asked, never letting anyone think they're talking to a person or to God;
- adapts its *manner* to the person (debate-ready or gentle) but never its honesty;
- ends even confident answers by noting a real person is available.

### 7. Talk to a person (the human handoff)
Always one tap away — never buried, never gated behind readiness. When the AI is unsure, or the person pushes back, or they just want a human, the question goes to a real person. **Phase 1: that person is Cameron.** The AI's draft answer is shown to Cameron, who approves it, edits it, or replaces it before it goes back. The helper is introduced simply as a real person who cares — not with a church badge. But if the person asks directly whether this is the LDS church or whether the helper is a member, the answer is the plain truth. Not advertised; never denied.

### 8. The comparison moments
When the signal reader detects that a person's real obstacle is a picture of God that isn't good — a God who damns for his glory, who pre-rejects, who is cruel "for his own ends" — the app does not argue. It sets the Jesus they already accept beside that picture and asks one honest question, then stops. (Full library of these in `KNOWING-ENGINE.md`, Part 4.) The contradiction is theirs to notice. Jesus planted seeds and walked on; so does the app.

### 9. Readiness, sensed (not proven)
Two signals, detected from how the person talks — never a test they see themselves taking:
1. They believe, or want to believe, that God is **fundamentally good**.
2. They show curiosity that God might **still speak today** — that there could be more than they were handed.

Until *both* are present, no LDS-specific reference appears — no Restoration story, no Book of Mormon, no missionary link. This is milk before meat. The father saw the son coming and ran; he did not make him pass an exam at the edge of the property.

### 10. The Restoration introduction (with transparency)
Once both signals are present and the person reaches for more, the app introduces the restored gospel as its own perspective — stated plainly and humbly, never as a sales pitch. It opens with honesty about who built it (the transparency card already in the codebase): *we made this, we didn't lead with it because we wanted to meet you where you were, and we won't hide it from you now.* Then it offers the restored gospel as the thing that makes the genuinely good God they've started to glimpse make sense — we are God's children, here to grow up into his likeness — and points, only if they want more, toward the Doctrine and Covenants.

### 11. The missionary handoff
For a person in whom both readiness signals are present and who wants to go further, the website link to real missionaries is offered — and from that point stays available. Always offered, never pushed. The rich young ruler can still walk away, and the app lets him.

---

## The two approach modes

The same engine, pointed two different directions depending on who the person is. The signal reader picks; the person never chooses a mode or sees one named.

### Debater mode — for the one who wants to wrestle (e.g. a Calvinist friend)
Signals: argument language, "prove it," "what about," doctrinal vocabulary, energy in disagreement. This person is Nicodemus — the intellect is the door, not the enemy. Give them the real material: the actual case, the scriptures, the honest tension, ready to be debated. The app hands them exactly the things Cameron already uses when he teaches them in person — that God is good, argued from Jesus's own words — and lets them push on it. Disagreement here is engagement, not a problem to defeat.

### Gentle mode — for the one who won't fight (e.g. a Baptist mother)
Signals: warmth without argument, study language, quiet devotion, no appetite for confrontation. This person doesn't want a debate; she wants to be gently led to a question she'd never start herself. The app prompts it softly — *"is a God who would send people to hell for his glory actually good?"* — lets her sit with the fact that it isn't, shows that the Jesus of the Bible she already loves would never be that, then shows that the restored Church teaches we're here to become like him, which is right there in scripture. Only if she reaches for more does the Doctrine and Covenants open. No pressure at any step.

---

## What the engine tracks (and what it must never become)

**Track, to know the person better:** which story they responded to, what they said in their own words, what need surfaced, what reopened their picture of God, where they went quiet, when they asked for a human, which approach mode fit. Cameron reviews this the way a minister reviews who he's caring for — to serve the actual person more truly next time.

**Never build:** conversion-probability scores, objection-handling optimization, persuasion A/B tests that treat a person's resistance as a leak to plug, or anything that turns freedom-to-leave into a funnel problem. A person is not a data point. The honest test for any tracking feature: *would Cameron be ashamed to show this person exactly what's recorded and why?* If yes, it doesn't get built.

---

## The human in the loop (Phase 1)

Every human-facing answer in Phase 1 routes through Cameron. The AI drafts; Cameron approves, edits, or rewrites; the answer goes back under the simple identity of "a real person." This keeps the warmth and honesty of a human in every hard moment while the AI carries the volume. The system is designed so Phase 2 (a small team of volunteers) and Phase 3 (real missionaries integrated) slot into this same handoff without a rewrite — the only thing that changes is who's on the receiving end.

---

## What to retire from the current code

- **`FEED_PROGRESSION` + `_auto_graduate` / `canAdvanceToNextTier` / `GRADUATION_THRESHOLD`** — nobody climbs tiers by collecting thumbs-ups. The four tags become invisible signals read from language and emotion.
- **The `ANSWER_MAP` A–E survey branch** — onboarding leads with a story and a mirror question, not a category select.
- **`isRestorationReady()` as a counter** — readiness becomes the two sensed signals (good God + open to ongoing revelation), not an interaction count.

Keep: the transparency card, the always-available human handoff, the AI grounding-and-honesty rules, the journal, and the screen-time cap.

---

## Build order

1. Sanctuary → Story → Mirror question → Reflect-back (the onboarding heart; no survey).
2. Feed initialized from the mirror signal, one card at a time, no visible tiers.
3. Ask Anything AI Q&A with grounded, honest answers and the "talk to a person" escalation routing to Cameron with draft-approval.
4. The signal reader (internal picture) + approach selector (debater / gentle) feeding both feed and Q&A tone.
5. The comparison library wired to fire when a "God isn't good" obstacle is detected.
6. Readiness sensing → transparency card → Restoration introduction → missionary link.
7. Cameron's review surface for drafted human answers and the signal log.

---

## The one line to hold

Do for each person, through a screen, what Jesus did face to face: see what they're really carrying, meet it with the truth of a genuinely good God spoken in his own voice, learn how to approach *this* person specifically — and leave them free the whole way.
