# MBM — Honest Review for "What Will the Church Think?"

*Reviewed 2026-06-24 by reading the actual built app, not just the design docs.*

**One thing up front, in plain words:** I am not a Church authority and I cannot
speak for God or for the Church. What I can do is tell you what I actually found in
the code, point out where it could rub against the Church's real, published rules,
and tell you who can give you the binding answers. The two people who can truly
answer "is this right in God's eyes" and "will the Church be okay with this" are
**your bishop / stake president** (for the spiritual and propriety side) and the
**Church's Intellectual Property Office, 1‑801‑240‑3959** (for the name, trademark,
and content side). I'd encourage you to take it to both. Everything below is to help
you walk in there prepared.

---

## What I actually looked at (so you know I read the real thing)

- The live AI voice — `mobile/src/engine/minister.ts` (the whole system prompt).
- The real onboarding the user sees — `mobile/src/screens/OnboardScreen.tsx` (the 9 stories).
- The scoring screen as coded — `mobile/src/screens/ProfileScreen.tsx`.
- The content corpus — `mobile/src/data/content.ts`.
- A full search of `mobile/src` for any in‑app disclosure ("made by members," "not
  affiliated," "privacy"), and for everywhere the Church is named.
- The shipped config — `mobile/app.json` — and the privacy policy at `site/privacy.html`.

---

## The genuinely strong parts (these will help you with the Church)

These are real, and they're in the code — not just promised in a doc.

- **The app is not named after the Church.** It ships as "Milk Before Meat"
  (`app.json`), package `com.milk_before_meat`. You are not using the Church's name
  or logo as your brand. That's the single most important thing you got right.
- **The "it is not God" stance is real and built in,** anchored in Elder Gong's
  counsel, sitting quietly on the opening screen (`HookScreen.tsx`). This is exactly
  the posture the Church has asked for around AI.
- **The AI never denies what it is or who made it when asked directly.**
  `minister.ts` line 50 forces an honest, immediate answer: *"yes — this was made by
  members of The Church of Jesus Christ of Latter-day Saints."* No lying, no dodging.
- **It never pressures and always leaves the person free** — the rich-young-ruler
  rule, the no‑duck rule, the "ask permission before the Restoration" rule, and real
  crisis-safety handling with 988. This is careful, Christlike ministry, not a
  high-pressure conversion funnel.
- **It honors agency.** Member status only comes from a person saying so themselves.

I want to be clear that the heart of this is good and the safeguards are real.

---

## The real concerns, ranked by how likely the Church is to care

### 1. There is no in-app "we are not officially affiliated with the Church" disclaimer. (Most important.)

When I searched the whole app, the **only** place the Church's name is disclosed to a
user is when the AI is asked point-blank. There is **no standing, visible statement**
anywhere that says, in effect: *"This is an independent app made by members of The
Church of Jesus Christ of Latter-day Saints. It is not owned, endorsed, or sponsored
by the Church."*

This matters because the Church's published trademark guidelines specifically warn
against any third-party use that could imply official endorsement. An app that uses
the full name of the Church, "Book of Mormon," "Joseph Smith," and teaches restored
doctrine, with **no** non-affiliation notice, is the exact pattern that draws a letter
from their IP office. The fix is cheap and protects you: add a short, plain
non-affiliation line in two places — a static spot in the app (an About/Info card)
and on your privacy/landing page.

### 2. Trademarked and copyrighted Church material.

"The Church of Jesus Christ of Latter-day Saints" and "Book of Mormon" are trademarks
held by Intellectual Reserve, Inc. Your own `content.ts` comment already notes that
modern editions of the Book of Mormon are Church-copyrighted — so you're aware. Two
things follow:

- **Scripture text:** the King James Bible is public domain (fine). Modern Church
  editions of the Book of Mormon, and General Conference talks, *Come Follow Me*,
  and Church manuals, are **copyrighted**. Your AGENT-RULES say the member feed should
  grow toward "everything the Church recommends" — if that means reproducing those
  texts in-app, you need permission. Public-domain editions of the Book of Mormon
  (e.g. 1830) exist and are a safer source if you want the text itself.
- **Permission is a real, friendly process.** The Church grants a lot of personal/
  non-commercial use freely, and has a permissions request path. Call the IP office
  and ask before you publish broadly; it's far better than asking forgiveness.

### 3. The silent profiling and the "Christlike score" — a perception risk if it goes public.

I know from `SETTLED-CONCERNS.md` that the ethics of this were worked through and you
hold the line yourself, so I'm not reopening that. I'm raising it only in the exact
frame you asked about — *"what should I worry about when the Church sees this."*

The honest risk is reputational, not doctrinal: a feature that **silently** reads
people's words to categorize them, and assigns a numeric "Christlike compassion /
courage" score that is **capped by whether they accept the theology**, is the kind of
thing that, if a journalist or critic described it from the outside, would read as
"LDS app secretly profiles and grades users' souls." That's a headline the Church
would not want attached to its name.

You've already softened this well — the scores are hidden from seekers and shown only
to members as a striving tool (`ProfileScreen.tsx`, `showVirtues`). Worth considering:
make the fact that the app learns from what you say **disclosed plainly** somewhere
(not hidden), so "silent" never becomes "secret" if someone looks under the hood.

### 4. AI teaching doctrine where the Church coordinates missionary work.

The Church runs proselytizing through called missionaries and official channels. Your
app has an AI teaching restored doctrine and a "talk to a real person" that, in Phase
1, is you (the admin team) — not set-apart missionaries. That's fine as a private,
member-built tool, **as long as it never presents itself as official missionary work
or an official Church channel.** Keep "the admin team" language honest and never let
it imply "the missionaries" or "the Church" institutionally. The Phase 3 "Church
partnership" idea would need actual Church sign-off before any such claim is made.

### 5. Data and privacy (also an app-store requirement).

You collect sensitive spiritual reflections, journal entries, and chat transcripts.
You do have a privacy policy (`site/privacy.html`), which is good and required. Make
sure it plainly covers: that conversations may be sent to a third-party AI provider
(Anthropic), what the admin team can see, and how someone deletes their data. Apple
and Google both scrutinize religious and sensitive-data apps, so this needs to be
airtight for publishing, separate from the Church question.

---

## What I'd actually do next (in order)

1. **Add a plain non-affiliation disclaimer** in the app (a static About card) and on
   the landing/privacy page. I can write that line for you in a sentence or two.
2. **Call the Church Intellectual Property Office (1‑801‑240‑3959)** before a public
   launch. Describe the app honestly and ask about (a) using the Church's name with a
   non-affiliation notice and (b) any use of copyrighted scripture/manuals/talks.
3. **Talk to your bishop or stake president** about the app itself — the silent
   routing and the soul-scoring especially. Their read on whether it honors agency and
   the Church's approach to sharing the gospel is the one that should weigh most for
   you, and it's the best protection you can have.
4. **Make "the app learns from you" disclosed, not hidden** — keep the experience
   gentle, but make sure nothing about it would embarrass you if shown publicly. Your
   own test in `SETTLED-CONCERNS.md` — *"would I be ashamed to show this person exactly
   what we recorded and why?"* — is the right one; apply it to the Church too.
5. **Firm up the privacy policy** on third-party AI, admin visibility, and deletion.

---

*Bottom line: the heart of this is good and a lot of the hard ethical work is already
done. The biggest gaps before the Church sees it are practical and fixable — a
non-affiliation disclaimer, a call to the IP office about names and copyrighted
content, and a conversation with your priesthood leader. None of those require
changing your vision; they protect it.*
