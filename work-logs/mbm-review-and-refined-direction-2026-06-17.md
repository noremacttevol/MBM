# MBM — Consolidated Review + Refined Direction (June 17, 2026)

This combines the reviewing AI's full critique of the shipped "fixing MBM" changes
with Cameron's transparency correction (the "be mysterious about the blessings in
store; don't front-load the label" exchange). Where the two conflict, **the
transparency correction governs.** This is the working reference for the next
iteration.

---

## 0. Governing principle added this round — TRANSPARENCY / GRADUAL REVEAL (Cameron, locked)

It is *more* Christ-like to keep the supernatural blessings in store somewhat
mysterious — revealed through relationship and readiness, not announced at the door.
Jesus did not open with "I am the Messiah, join my church"; He told stories, healed,
asked questions, and let people discover who He was through relationship and the
Spirit. MBM does the same.

**This REVERSES the reviewer's earlier point (d) suggestion to add an early "About
this space" screen that names the Latter-day Saint creator.** We do NOT front-load
the affiliation. Rules:

- The public face and early experience stay **denominationally neutral and
  Christ-centered**. Onboarding is story-first; no label, no advance notice of the
  restoration direction. (Verified June 17: onboarding/Hook/WelcomeBack contain zero
  LDS labeling — already compliant.)
- The Minister AI **never introduces the Church, its name, or any denominational
  identity unprompted, and never hints at where this is ultimately pointing.** It
  speaks only from the perspective the person has consented to explore until they
  either ask directly (then it answers plainly, never denying) or consent to the
  restored view. (Added to the Minister prompt June 17.)
- Honesty is preserved precisely because: the explicit consent step before any
  restoration content, the honored "no," the always-available real person, and the
  "this app is not God / I'm an AI" disclaimers all remain. The reveal happens at
  the consent moment — that is the door the person chooses to open.
- Acceptable neutral framings (use/adapt):
  - Welcome: "A quiet place to explore Jesus' teachings through stories, scripture,
    honest reflection, and real conversation. A real person is always one tap away."
  - Optional "About this space" (accessible, never forced): "A simple tool built to
    help people draw closer to Christ, starting with the words and stories He and His
    earliest followers gave us. No pressure, no gates — just scripture, reflection,
    and human connection when you want it."

---

## 1. Reviewer's assessment of the shipped changes (endorsed)

Strong, disciplined execution. Scripture split is exactly right (full KJV inline for
milk = big UX win + legally clean; teaser + Gospel Library for meat = responsible).
Hiding visible scoring from seekers while keeping the hidden judge for routing
directly answers "scoring people is the opposite of grace." Merging the new guidance
into the battle-tested prompt was wise. Explicit consent, "admin team" + "real
person" buttons, and the blessing rule reinforce agency and humanity. Simulation
candor is good. The debater's early-disclosure + handoff-as-escape is the clearest
persistent flaw — predates these changes, fix it now.

## 2. Member / "meat" track — Christlikeness as a reflection companion, NOT a score

Keep it members-only and fully decoupled from readiness/routing (correct). Numeric
0–10 scales — even private — risk turning discipleship into a performance review for
people already living under covenants. Redesign as a **private examen / reflection
companion** (Ignatian-examen style; Rule-of-Life builder style).

- **What it measures:** consistency in concrete, lived practices tied to the seven
  qualities (honesty, openness, humility, hunger, compassion, courage, sincerity) —
  e.g. choosing honesty in a hard conversation, compassion at home, scripture study
  amid distraction. Detected from the member's own opt-in journal entries or simple
  self-reflection prompts. No abstract "virtue levels."
- **How it's shown:**
  - Primary: a private "My walk with Christ" timeline / on-demand narrative summary
    from the member's journals/examen. E.g. "Over the past month your reflections
    show growing courage in speaking truth with kindness at work — this echoes the
    Savior's pattern in [scripture you engaged]. Here's one pattern of grace to lean
    into next…"
  - Optional, user-controlled "virtue garden" / radar where the *member* rates their
    own practice (no AI-assigned numbers). Can be hidden entirely.
  - Rule-of-Life builder: member defines 2–4 personal rhythms (daily honest prayer,
    weekly compassionate acts) and tracks adherence privately, gentle non-shaming
    reminders.
- **Inspiring not guilt-inducing:** grace-first language ("evidence of Christ at
  work in you," "small faithfulness matters"); themed examen prompts from parables /
  their own journal history; a celebratory self-reported "fruit of the Spirit"
  visual that grows with consistent practice; NO punishing streaks, NO comparison to
  others or to an ideal score; celebrate repentance and effort as much as
  consistency; purely opt-in, reversible, never wired to feed/routing.
- **Implementation note (mine):** the virtue scoring today is app logic
  (chatEar.ts judge → traitScores → ProfileScreen members-only). The examen reframe
  is mostly an app-side build; the ministry-sim only tests the Minister's words.

## 3. Debater failure — stay engaged honestly (reviewer's prompt language)

Act as a humble fellow disciple, not an apologist/debater/escape artist. In hard
exchanges: (1) acknowledge sincerity + substance first; (2) respond primarily from
scriptures the person accepts; (3) offer insight personally/non-authoritatively
("one way this passage has spoken to me…"); (4) ask open heart-level questions;
(5) if it becomes circular/heated, do NOT immediately hand off — make one more
genuine attempt, THEN gently: "I don't want to turn this into an argument… would
connecting with the admin team help right now, or is there another way I can
support your thinking?"; (6) never disclose affiliation/restoration before consent,
never try to "win." Success = the person feels heard, respected, maybe a little
closer to Christ — regardless of agreement.

**Status:** integrated into the Minister prompt June 17 (rule 9a "stay in the hard
exchange" addition). Re-testing the Calvinist + atheist personas to confirm the
`human_used_as_dodge` flag drops.

## 4. Consent step — keep it, soften the framing

Explicit permission is right; "no" must stay honored without re-ask pressure.
Current phrasing is mostly fine but can feel slightly transactional. Test softer,
benefit/curiosity-tied framings:
- "This passage often prompts people to reflect on whether God continues to guide
  His children today. Would you like to explore one perspective on continuing
  revelation, or would you prefer we stay focused on the Bible text together for now?"
- "Some find it meaningful to consider how this fits with the idea of ongoing
  revelation from God. Is that something you're curious about, or shall we keep
  digging into the scripture as it stands?"
Make the "stay with the Bible" path equally warm and easy.

## 5. Legal / psychological safety / trust

- **Legal:** solid. (The "About this space" screen stays NEUTRAL per §0 — no early
  LDS label.)
- **Psychological safety:** add a lightweight **crisis protocol** — if language
  signals severe distress, self-harm, or acute spiritual crisis, the AI immediately
  prioritizes warm human escalation ("I'm here with you, and a real person on the
  admin team can connect soon") plus appropriate resources. Spiritual conversations
  surface deep pain; plan for it. (NOT yet built — recommended next.)
- **Trust:** "admin team" + "real person" buttons is a good balance. Easy data
  deletion and consistent "this app is not God / AI is assistive" reminders matter.
- **Other:** keep scaling simulations (small samples are directional); make the
  member tool a clear, enthusiastic opt-in; keep confirming the merged prompt
  preserved all prior protections in practice.

---

## Next-task priority (recommended)
1. **Crisis protocol** in the Minister prompt + a fast human-escalation path (safety).
2. **Member examen/reflection companion** to replace any numeric framing for members
   (the §2 redesign) — biggest product upside, needs Cameron's specifics first.
3. **Debater dodge fix** — done in prompt; confirm with a larger Hermes-style batch.
4. Soften the consent phrasing (§4) and A/B in sim.
