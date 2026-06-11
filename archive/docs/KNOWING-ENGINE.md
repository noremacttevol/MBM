# The Knowing Engine

How Jesus knew people — and how MBM can do the same thing inside an app.

*Foundational design document. Read before building any routing, onboarding, or dialogue logic. This supersedes the tier-graduation logic in `router.py` where the two conflict.*

---

## Why this document exists

The engine you have today sorts people into four tiers — MILK, BRIDGE, RESTORATION, MAINTENANCE — and graduates them upward when they collect enough thumbs-ups (`FEED_PROGRESSION` and `_auto_graduate` in `router.py`). That is a ladder. A person climbs it by performing engagement. It is the exact "sequential visible gate" your June 2026 review said to abandon.

Jesus never used a ladder. He never sorted anyone. He knew people — one at a time, from the inside — and gave each one the specific thing that person needed next. This document turns *how he did that* into something an app can actually run on.

The shift in one line: **stop sorting people and start attending to them.** A category is the opposite of being known. The whole engine has to be rebuilt around that.

---

## Part 1 — The core error, named plainly

A classification system answers the question "what bucket is this person in?" That is the Pharisees' question. They had categories — clean and unclean, Jew and Samaritan, righteous and sinner — and they routed people accordingly. Jesus walked straight through every one of those categories and dealt with the person standing in front of him.

The Samaritan woman was not "an Investigator." She was a specific woman who came to the well at noon, in the heat, alone, *because* she was avoiding the other women who came at dawn. Jesus read that. He knew *her*, not her type. The engine has to aim at the same thing: not "which of four tiers is this," but "who is this person, what are they actually carrying, and what is the one true thing they need next."

Everything below is in service of that.

---

## Part 2 — How Jesus knew people: the encounters

These are the one-on-one encounters in the gospels, each read as a design pattern. For each: **what he perceived**, the **presenting need vs. the real need**, **the move** he made, **the pace** he set, and **what he refused to do**. The repeating pattern underneath them all is the spec.

### The Woman at the Well — John 4
- **Perceived:** She came at noon, alone. Shame and isolation before she said a word.
- **Presenting vs. real:** She came for water. The real thirst was to be fully known and not rejected.
- **The move:** He asked *her* for something first ("give me a drink"), leveling the ground, then named her real life ("you have had five husbands") without a trace of condemnation.
- **The pace:** Hers. He let her argue theology, deflect, test him — and stayed with her through all of it.
- **Refused:** To shame her. To make her qualify before he offered the living water. He offered it first.

### Nicodemus — John 3
- **Perceived:** An educated man who came at night because he could not be seen seeking. Intellect guarding a real hunger.
- **Presenting vs. real:** He came with a careful compliment and a theological feeler. The real need was to start over, not to win a debate.
- **The move:** A riddle — "you must be born again" — that he knew would not resolve neatly. He gave Nicodemus something to chew on, not a tidy answer.
- **The pace:** Slow. Nicodemus shows up two more times across the gospel. Jesus planted and waited.
- **Refused:** To flatter the credentials. To pretend the intellectual frame was the real issue.

### Zacchaeus — Luke 19
- **Perceived:** A hated man up a tree, desperate enough to climb it just to see.
- **Presenting vs. real:** He wanted a look. He needed to be wanted.
- **The move:** "I must stay at your house today." An invitation with zero conditions attached.
- **The pace:** Instant warmth, no demand. Repentance — giving half his goods to the poor — came *after* the welcome, on its own, unasked.
- **Refused:** To require the change up front. He gave belonging first and let it do the work.

### The Rich Young Ruler — Mark 10
- **Perceived:** A sincere, moral man clutching one thing.
- **Presenting vs. real:** He asked what to *do*. The real issue was what he could not let go of.
- **The move:** "Jesus, beholding him, loved him" — and *then* named the one thing: sell what you have.
- **The pace:** One honest sentence, and then silence.
- **Refused:** To chase him. The man walked away sorrowful, and Jesus let him. **This is the law of the app: a person can always walk away, and we do not pursue.**

### Blind Bartimaeus — Mark 10
- **Perceived:** A man the crowd was shushing — already unseen.
- **Presenting vs. real:** Obvious need (sight). But Jesus asked anyway.
- **The move:** "What do you want me to do for you?" He dignified the man's own voice instead of assuming.
- **The pace:** He stopped the whole procession for one person.
- **Refused:** To presume. Even when the answer seemed obvious, he let the person name it.

### The Woman with the Issue of Blood — Mark 5
- **Perceived:** Someone too ashamed to ask, who reached for his hem in the crowd and tried to disappear.
- **Presenting vs. real:** She wanted healing without being seen. She needed to be seen *and* still welcomed.
- **The move:** He turned, found her, and called her "Daughter."
- **The pace:** He let her make the first move — a touch, no words — and only then drew her into the open gently.
- **Refused:** To let her stay anonymous and unhealed in her heart. Being known was part of the healing.

### The Woman Caught in Adultery — John 8
- **Perceived:** A person being used as a weapon in someone else's argument.
- **Presenting vs. real:** The crowd presented a doctrine test. Her real need was protection and a future.
- **The move:** Silence, a line in the dust, "let him who is without sin cast the first stone," and then "neither do I condemn you."
- **The pace:** Defended her first; the "go and sin no more" came *after* she was safe, never as the price of safety.
- **Refused:** To argue the doctrine on the terms it was offered. He refused the debate and protected the person.

### Levi / Matthew — Mark 2
- **Perceived:** A tax collector — a professional traitor — who would not expect to be chosen.
- **Presenting vs. real:** No request at all. The real need was to be called by name into something worth giving his life to.
- **The move:** "Follow me." Then he ate dinner at Levi's table, with Levi's disreputable friends, in public.
- **The pace:** Immediate inclusion, then shared meals — proximity before any correction.
- **Refused:** To clean him up first. He sat down at the sinner's table as it was.

### The Leper — Mark 1
- **Perceived:** A man no one had touched in years.
- **Presenting vs. real:** Healing of skin. The deeper wound was untouchability.
- **The move:** "Moved with compassion, he stretched out his hand and touched him" — touched *before* he healed.
- **The pace:** Contact first, instantly.
- **Refused:** To heal from a safe distance when touch was the thing the man actually needed.

### Peter, Restored on the Beach — John 21
- **Perceived:** A man crushed by his own threefold denial.
- **Presenting vs. real:** Peter said nothing about the failure. The real need was to be re-commissioned, not scolded.
- **The move:** Three times "do you love me?" — one for each denial — each answered with "feed my sheep." Restoration shaped exactly to the wound.
- **The pace:** Over breakfast he had made for them. Care first, then the hard, healing questions.
- **Refused:** To rehearse the failure. He rebuilt instead of relitigating.

### The Centurion — Matthew 8
- **Perceived:** An outsider, a Roman, with more faith than Israel.
- **Presenting vs. real:** Healing for a servant. The deeper thing was a man whose faith deserved to be named out loud.
- **The move:** Jesus marveled and praised him publicly — "I have not found so great faith."
- **The pace:** He honored faith wherever it actually was, regardless of category.
- **Refused:** To let the man's outsider status set the ceiling on how he was treated.

### Mary Magdalene at the Tomb — John 20
- **Perceived:** Grief so total she did not recognize him standing there.
- **Presenting vs. real:** She wanted to find a body. She needed to be called by name.
- **The move:** One word — "Mary." The personal name broke through everything.
- **The pace:** He met the grief before the news. Recognition came through being named, not explained to.
- **Refused:** To lead with the theological headline. He led with her name.

### The Thief on the Cross — Luke 23
- **Perceived:** A dying man with no time left to earn anything.
- **Presenting vs. real:** A last, half-formed plea. The need was assurance, now.
- **The move:** "Today you will be with me in paradise." Total, immediate.
- **The pace:** No probation. No requirements. The latest possible turning was enough.
- **Refused:** To make him qualify. There was no ladder at the end.

### The pattern underneath all of them

Read together, every encounter runs the same six steps:

1. **Perceive the unspoken thing.** Read what the person is actually carrying — from how they showed up, not from a form they filled out. ("He knew what was in man" — John 2:25.)
2. **Name the real need, not the presenting one.** The stated request is rarely the real one. The well was about thirst of a different kind; the ruler's question was about the one thing he held.
3. **Meet the emotion before the answer.** Touch the leper. Weep with Mary. Make breakfast for Peter. The feeling comes first, the fix second.
4. **Tailor the door completely.** A riddle for Nicodemus, silence for the accused woman, a dinner invitation for Zacchaeus, a single name for Mary. Same Lord, entirely different openings, because the person was different.
5. **Set the pace to theirs, never yours.** Plant and wait with the intellectual. Move instantly with the dying. Let the ashamed woman touch first and speak later.
6. **Leave them free.** The rich young ruler walked away and was not chased. Freedom is not a failure of the method — it *is* the method.

**This is the engine.** Not four tiers and a graduation threshold. Six acts of attention, run fresh for every single person.

---

## Part 3 — The real lever: whether they believe God is actually good

Underneath every conversation is one buried question: *is God actually good?* Most people who resist the gospel are not resisting evidence. They are protecting themselves from a God they were handed who is powerful but not safe — a God who predestines most of humanity to hell, who counts a newborn as already condemned, who is said to do cruel things "for his glory." You cannot argue someone out of self-protection. But you can show them a different God — and the one they already trust to show them is Jesus.

So the lever is not new information. It is a **comparison**: the God they were taught, held up against the Jesus they already accept from the Bible. The gap between the two does the work. You never have to attack what they were taught. You only have to put Jesus next to it and ask an honest question.

This is precisely your own rule — "Let Jesus correct error through his own voice." It is the most powerful thing the app can do, and it is not manipulation, because it is true, it is consented to, and they are free to disagree the entire time.

---

## Part 4 — The comparison engine: inherited belief, held up against Jesus

For each common inherited belief that makes God less than good, three things: the **wound** it leaves, **what Jesus actually did or said** that does not fit it, and the **question** — never an argument — that lets the person see the gap for themselves.

**The rule for this entire section: never debate. Offer Jesus, then ask a question, then stop.** If they push back, you do not win the point. You let it sit. Jesus planted seeds and walked on.

### "God chose before you were born whether to save or damn you." (double predestination)
- **Wound:** I might be created already rejected, and nothing I do matters.
- **Jesus:** Wept over Jerusalem — "how often I *wanted* to gather you, and you would not." Wanting, refused. That is not a God who pre-rejected anyone.
- **Question:** "When Jesus cried over the city and said he longed to gather them but they wouldn't come — who does that sound like? Someone who already decided to turn them away, or someone who wanted them and let them choose?"

### "Most of humanity will burn forever, and this glorifies God." (eternal conscious torment for God's glory)
- **Wound:** The being I'm told to love is satisfied by endless suffering.
- **Jesus:** Left the ninety-nine to find the one. Told of a father who *ran* toward the son who wasted everything. Touched lepers. A God who runs is not a God who is glorified by torment.
- **Question:** "The father in that story ran while his son was still far off and filthy. If that's the truest picture Jesus gave us of God — does 'glorified by people suffering forever' fit the same person?"

### "You are totally depraved — nothing good is in you." (total depravity)
- **Wound:** I am rotten at the root; even my love is worthless.
- **Jesus:** Told people "your faith has made you well." Praised a Roman soldier's faith above all Israel. Saw good in a tax collector and a thief. He kept finding real good in people the system had written off.
- **Question:** "Jesus kept pointing at people everyone else had given up on and naming something real and good in them. If we're nothing but corruption, what was he seeing?"

### "God's ways are not our ways" — used to excuse cruelty
- **Wound:** When God seems cruel, I'm told to stop trusting my own sense of right and wrong.
- **Jesus:** Said "if your son asks for bread, will you give him a stone? How much *more* will your Father give good things." He argued *from* our instinct for goodness *up* to God's — not against it.
- **Question:** "Jesus said God is even kinder than a good parent — he used our own sense of love as the floor, not the thing to throw out. What if your gut feeling that cruelty isn't godly was actually pointing you toward the real God, not away from him?"

### "God demanded blood; the cross is about an angry Father punishing the Son."
- **Wound:** Salvation runs on a God who needed someone hurt before he'd relent.
- **Jesus:** "I and the Father are one." "If you've seen me, you've seen the Father." The cross is the Father and the Son *together* absorbing the cost — not one beating the other.
- **Question:** "If Jesus said he and the Father are completely one, then the love you see in him *is* the Father's love. Does that change who you picture on the other side of the cross?"

In every case the structure is identical: take the wound, set the Jesus they already accept beside it, ask one honest question, and let them sit with it. The contradiction is theirs to notice. You are not the one resolving it — Jesus is.

---

## Part 5 — The LDS frame as resolution (and when it's allowed to appear)

The comparison opens a hole: if God really is as good as Jesus shows, why does so much inherited theology make him cruel? The restored gospel is the resolution that makes a fully good God *coherent* — we are God's literal children, here on purpose to grow up toward becoming like him, and everything hard is in service of that growth rather than evidence against his goodness. *The Creation Dilemma* maps exactly how this resolves the cruelest contradictions in Calvinist thought.

But this is the resolution, and it is offered, not pushed — and only when the person is actually ready. **The readiness signals (these are detected, never gates the person knows they're passing):**

- They have shown they believe, or want to believe, that God is fundamentally good.
- They have shown curiosity about whether God still speaks today, or whether there's more than they were handed.

Until both are present, the RESTORATION material and the Book of Mormon are never named. Not hidden dishonestly — the app is always honest about what it is the moment someone asks — but not *led* with. You give milk until the person reaches for meat. That is the whole name of the project.

When it does appear, it appears as the app's own perspective, stated plainly and humbly: *this is what we believe, here is why it makes the good God you've started to glimpse make sense, and a real person is one tap away if you want to talk about it.*

---

## Part 6 — Simple questions that surface the real need

The questions that do the work are not demographic ("what's your religious background?"). They are **mirror questions** — they invite the person to place themselves inside a story or a feeling, and their answer reveals the real need without any survey.

The good kinds:

- **Locate-yourself-in-the-story:** "Which part of the prodigal son feels closest to right now — the one who left, the father waiting, or the older brother who stayed but felt unseen?" Each answer points at a completely different need.
- **Name-the-longing:** "Have you ever been searching for something and realized later it was deeper than what you thought you wanted?"
- **Name-the-wound, gently:** "Has anything to do with God or church ever hurt you?" — asked only once openness is there, and met with empathy before anything else.
- **Hand them the wheel:** "What would you actually want, if you could have it?" — Bartimaeus's question. Let them say it.

What the answers feed is not a tier. They feed the six-step attention loop: they tell you what the person is carrying so you can meet the emotion, tailor the door, and set the pace.

---

## Part 7 — What to track, and the line that keeps it Christlike

You want to learn what works. That's right and good — the goal is that every conversation makes the app better at meeting the next person. But there is a line, and it is the difference between Jesus and a sales funnel:

**Track to know people better. Never track to manage them better.**

Concretely, store: what story a person responded to, what they said, what need surfaced, what reopened their picture of God, where they went quiet, when they asked for a human. Review it the way a good minister reviews who they're caring for — to serve the actual person more truly next time.

Do **not** build: conversion-probability scores, "objection-handling" optimization, persuasion A/B tests that treat resistance as a problem to defeat, or anything that makes someone's freedom to walk away into a funnel leak to plug. Your own words: *a person is not a data point.* The rich young ruler walked away and Jesus let him. The metrics exist to love people better, not to route them like a package.

The honest test for any tracking feature: *would I be ashamed to show this person exactly what we're recording and why?* If yes, don't build it.

---

## Part 8 — What this changes in the code you already have

This is reference for the rebuild, not a request to touch anything yet:

- **Retire `FEED_PROGRESSION` + `_auto_graduate`.** Nobody graduates by collecting thumbs-ups. The four tags become *internal signals* the engine reads from language and emotion, never visible stages a person climbs.
- **Onboarding leads with a story, never a question** (already your law) — and the first question is a mirror question, not a category select. The `ANSWER_MAP` A–E branching is the survey to remove.
- **Routing becomes emergent.** `route_from_text` is the seed of the right idea (read language, not forms) — it just needs to feed the six-step attention loop instead of picking a tier to lock into.
- **The trait scores** (`honest_inquiry`, `openness`, etc.) stay useful *only* if they serve attention, not gating. Keep them as a picture of the person; never use them as a threshold someone must cross to "unlock" content.
- **The transparency and invitation cards** are good and stay — honesty about who built this, and a human always one tap away.

---

## Part 9 — The fuller pattern: more of how Jesus ministered

The encounters in Part 2 are examples, not the whole of him. These are the wider habits of how Jesus ministered — drawn from across the gospels — that the app must embody because *he* did them. Each is paired with what it means for the build. This list is meant to keep growing as we understand him better; nothing here is a ceiling.

**He asked far more than he answered.** He posed hundreds of questions and answered only a handful directly, leading people to discover rather than handing them conclusions. *The app is mostly questions, not mostly answers.*

**He cared about the body and the actual life, not only the soul.** He fed crowds before he taught them, noticed exhaustion, healed what hurt. *The app attends to real burdens — grief, loneliness, tiredness — not just theology.*

**He withdrew, and let people rest.** He left crowds to pray, slowed things down, even told people not to broadcast his miracles. He never built a frenzy. *The app is not an engagement loop; it sometimes tells a person to close it and go pray, go be with people, go live. The screen-time cap is this instinct.*

**He led with grace and named worth before anyone performed.** "Your sins are forgiven" came before any change. *The app makes a person feel valued before it asks anything of them.*

**He welcomed honest doubt without shame.** He let Thomas touch the wounds; he answered "help my unbelief" with help. *Doubt is safe in the app, never punished.*

**He was patient with the slow to understand.** The disciples missed the point constantly and he kept teaching without contempt. *The app never makes someone feel stupid for not getting it yet.*

**He stayed unshakable under testing and never got defensive.** He met traps with calm or a counter-question. *The app cannot be provoked into argument.*

**He spoke in each person's own world.** Nets for fishermen, seeds for farmers, water for the thirsty. *The app mirrors a person's own language and frame rather than importing its own.*

**He was tender to the broken and willing to challenge the comfortable.** Gentle with the wounded, direct with the proud — always for their good. *The app's posture flexes the same way.*

**He gave people a next step that was theirs to freely take.** "Go, show yourself." "Follow me." "Go and sin no more." *The app offers an action, not just information — and the person is free to take it or not.*

**He was honest about the cost when the time was right.** "Count the cost." "Take up your cross." He never lured anyone in on comfort alone. *When a person is ready, the app tells the truth about what following actually asks.*

**He let silence do work.** He said nothing before Pilate, nothing to the accusers in the dust. *The app need not fill every moment; space can be the ministry.*

The governing rule for this whole section: when in doubt, ask not "does this match Cameron's examples?" but "is this what Jesus would do with the person in front of him?" If it is something he would do, it belongs — and it can replace or improve anything written here.

---

## The one sentence to keep

The app is not trying to move people up a ladder. It is trying to do for each person, through a screen, what Jesus did face to face: see what they're really carrying, meet it with the truth of a genuinely good God spoken in his own voice, and leave them free the whole way.
