# Publishing Viability Review — is the plan actually going to work?

**Written 2026-06-29 as a fresh, honest second look at how MBM is being published.**
Plain language. The job here is not to cheerlead — it is to tell Cameron where the plan
is solid, where the real risks are, and what to do about each one.

---

## The verdict in one paragraph

The publishing plan is **sound and is already most of the way done.** iPhone is effectively
finished (submitted to Apple, auto-releases on approval, and already installable today via
TestFlight). Android is also in good shape technically — it is live on internal testing and
fully automated for uploads — and the *only* real thing standing between it and a public
release is a Google waiting-period rule (12 testers for 14 days), not anything broken in the
app. The plan's strategy — soft-launch to a beta crowd, get the church comfortable, then flip
to public — fits both stores well. The honest risks are not "will it publish"; they are three
softer things: a security clean-up that should happen before wide sharing, the trademark/"don't
look official" posture with the Church, and ongoing cost control. None of these is a blocker.
All three are manageable. **Recommendation: proceed.**

---

## What is genuinely strong (keep doing this)

The architecture was chosen correctly for a one-person publisher. Cloud builds (Expo/EAS)
mean no Mac is needed and every build is repeatable from one command. The AI key lives on a
server, not the phone, which is exactly right and is the thing that would otherwise get an app
pulled. The app is native (not a thin web wrapper), type-checks clean, and has a real feature
set — so it clears Apple's "minimum functionality" bar that kills a lot of small apps. Both
store sides were driven through official APIs, so future updates follow the same proven path.
And the hardest store item — Apple's privacy "nutrition label" — is already published and
correct. That is the part Apple most often rejects over, and it is done.

## The real risks, ranked by how much they matter

**1. The 12-tester / 14-day Android gate (schedule risk, not technical risk).**
Google requires personal developer accounts to run a closed test with at least 12 testers who
stay opted in for 14 continuous days before production unlocks. This is a hard clock and the
single biggest thing between MBM and a public Android release. The risk is not the rule — it is
*people*: getting 12 real humans to install and keep the app for two unbroken weeks. If a tester
drops out, it can reset progress. **Do this:** over-recruit (line up ~15 so 12 stick), start the
clock the day they're ready, and use the same church-beta pool for both platforms so one outreach
feeds both. This is already Cameron's plan; it just needs the 12 names.

**2. Security clean-up before wide sharing (real, quick, important).**
The roadmap honestly flags two items: the admin reply-desk password is still the placeholder
"JosephSmith," and some keys (Firebase / Anthropic / Railway) were visible in setup logs and
should be rotated before the app is shared widely. Neither blocks a small friends-and-family
beta, but both should be closed before any public push. These are 30-minute jobs (make a new
key, paste it, delete the old) and the assistant can walk each one through.

**3. The Church trademark / "don't look official" posture (reputational, not store).**
For a Latter-day Saint outreach app, the biggest non-technical risk is *looking like the Church
built or endorsed it.* That is already well-handled: the app is branded "Milk Before Meat" (not
the Church's name), uses a neutral icon (no logo, no Angel Moroni), and now carries a standing
non-affiliation disclaimer on the first screen, the Profile, and the privacy page. Referring to
Church terms in text is fine; looking official is not. **Do this before any *wide/public* launch
(not needed for friends-and-family):** call the Church Intellectual Property Office
(1-801-240-3959), describe the app honestly, and add a one-line trademark attribution on the
website footer. The strongest protection is being upfront, not staying unseen — and the changes
already made are exactly what make the app safe to be looked at. (Full detail:
`../reviews/CHURCH-REVIEW-2026-06-24.md`.)

**4. Running cost as usage grows (budget risk).**
Two costs scale with users: the Anthropic API (every AI reply) and Firebase (the ministry
console already brushes the free-tier read limit). Today this is tiny. Before a real public
launch, set a hard spending cap on the API key and decide whether to move Firebase to the paid
Blaze plan. Put a billing cap in place *before* growth, not after a surprise bill. These are
account/billing actions only Cameron can take, but they are simple.

**5. Apple's content review (low risk, worth naming).**
Apple permits religious apps. The realistic rejection angles are the trademark/official-look
issue (mitigated above) and the privacy label (already published correctly). Given the app is
already submitted with everything Apple asks for, the expected outcome is approval within about a
day. If Apple does come back with a question, it is almost certainly a quick metadata clarification,
not a redesign.

## What is NOT a risk (so nobody re-worries about it)

The app compiling, the AI responding, the website loading, secrets being shipped in the app, and
"is there even a build" are all settled and verified. The member-recognition fix and the
meat-leak fix are in code and in build 6. The earlier Android "is it really on internal testing?"
unknown is resolved — it is. Don't spend worry there.

## Bottom line / recommendation

Publish as planned. The sequence that makes sense: (a) finish the quick security clean-up,
(b) hand the TestFlight link to the iPhone beta crowd now, (c) gather the 12 Android testers and
start the 14-day clock, (d) make the Church IP call before any wide push, (e) set billing caps,
then (f) flip both stores to public. Every one of these is a known, bounded task. There is no
hidden blocker. The work that remains is *waiting periods and human coordination*, not engineering.

---

*Cross-references: `START-HERE.md` (current truth), `IOS-STATUS-AND-APPLE-READINESS.md`,
`ANDROID-PUBLISH-PATH.md`, `WAITING-ON-APPLE.md`, `../reviews/CHURCH-REVIEW-2026-06-24.md`,
`../roadmap/FORWARD-WORK-PLAN.md`.*
