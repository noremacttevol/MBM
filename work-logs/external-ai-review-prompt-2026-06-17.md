# Prompt to take back to the reviewing AI (MBM, June 17 2026)

Copy everything below the line into the AI that gave me the original "fixing MBM"
feedback, so it can review what got built and weigh in on what's next.

---

I had a developer AI implement the full revised roadmap you helped me with for MBM
(Milk Before Meat — a React Native gospel-outreach app patterned after how Jesus
ministered: meet people where they are, milk before meat, a real human always one
tap away, invisible routing, never pressure). Here is exactly what shipped, the
judgment calls that were made, and where I want your honest critique. Push back
hard where you think it's wrong.

## What was built (all committed, verified: type-checks clean, automated tests pass)

1. **Scripture split for legal safety + UX.** The ~100 "milk" items are Bible-only
   and now render the full **public-domain King James Version text inline** in the
   app (bundled, works offline), so a seeker never leaves for a foundational verse.
   The ~100 "meat" items (Book of Mormon, Doctrine & Covenants, Pearl of Great
   Price) show only a short teaser plus an "Open in Gospel Library" link — we never
   embed the copyrighted modern LDS scripture text.

2. **Killed visible gamification — but only for seekers.** The 0–10 "Christlikeness"
   virtue scores and bars are now hidden from seekers/milk users entirely (being
   scored is the opposite of grace). A hidden judge still reads the conversation to
   guide content routing and to privately inform the AI — it just shows no numbers.
   The visible virtue scale is kept **only for self-identified members**, as a
   chosen discipleship striving tool, not a verdict.

3. **Merged (not replaced) the Minister AI system prompt.** Rather than overwrite a
   prompt that had been tuned over 740+ simulation trials, the new guidance was
   merged in: an explicit "ask permission before sharing the Restoration" rule, an
   "admin team" name for the human help (never a personal name), and a
   "speak a blessing when someone shares something sacred" rule. All prior
   protections were preserved.

4. **Explicit consent before restoration content.** When the AI senses someone is
   ready, it now asks first ("Would it help if I shared the restored perspective —
   or would you rather stay with the Bible view for now?") with yes/no buttons.
   Restoration-tagged content will NOT surface in the feed until the person says
   yes; a "no" is honored and not re-asked.

5. **"Admin team" everywhere for human help**, with one deliberate exception: the
   two primary buttons still say "Talk to a real person" / "Send to a real person"
   because that best signals *a human, not the bot*. Everything around them says
   "admin team." No personal name appears anywhere in the app.

## Simulation results so far (small sample — directional, not statistical)

- A "ready seeker" persona: the consent rule worked perfectly — the AI asked
  permission, and only taught the Restoration after she said yes. Solid pass.
- A grieving seeker: normal pass.
- A **Calvinist debater scored low**: it disclosed the LDS affiliation too early
  (before trust was built) and leaned on "talk to a real person" as an escape hatch
  when the argument got hard. This is the *same* weak spot this persona has always
  had, not something the new changes introduced — but it's the clearest remaining
  problem. A larger batch is running now to see if it's real or just noise.

## Where I specifically want your critique

a) **The member / "meat" track and the Christlikeness measurement.** Now that the
   virtue scale is members-only and decoupled from "are they ready for the restored
   truth," I want it to become a more honest, more *inspiring and even fun* tool for
   a faithful member to grow in Christlikeness — measured and kept over time, just
   to encourage devoted discipleship (not to gauge conversion-readiness). How would
   you design that so it inspires without becoming the very "scoring people"
   dynamic we just removed for seekers? What should it measure, how should it be
   shown, and what would make it genuinely motivating rather than guilt-inducing?

b) **The debater failure** (early affiliation disclosure + using the human handoff
   to dodge a hard question). How would you instruct an AI minister to stay in a
   hard theological exchange — answering honestly, never manipulating, offering the
   human only as a supplement — without either retreating or starting to "win"?

c) **The consent step.** Is asking explicit permission before sharing the
   Restoration the right call, or does it risk feeling like a sales prompt? Any
   better framing?

d) **Anything we missed** on legal exposure, psychological safety, or trust — the
   three lenses you reviewed before.

Be specific and concrete. Assume the goal is always: do for the person what a
faithful disciple of Jesus would do — meet them where they are, leave them free,
and keep a real human reachable — never optimize for conversions.
