# CHURCH-PITCH HANDOFF — everything one chat needs to run the "pitch MBM to the Church" effort

**Written 2026-06-26. Purpose:** Cameron is consolidating the "how do I present this app to my ward / priesthood leaders so they'll let me test it with the congregation" work into ONE dedicated chat. This file is this chat's complete contribution to that handoff. A new chat picking up this task should read this file in full, plus the `church-launch-kit/` folder it describes. This is NOT the app's build-state file (that's `START-HERE.md`); this is specifically about the **pitch / approval / rollout-to-the-ward** effort.

---

## 1. The goal, in Cameron's own framing

Cameron wants to show Milk Before Meat to his ward, who are his intended first real testers — he has their emails. To do it the right way, he wants to go through the **priesthood line** and earn a bishop's blessing to invite the congregation to test it. The sequence he described:

1. Make a **brochure** to show his Bishop for approval/acceptance to try it out.
2. With the Bishop's go-ahead, send a **pre-written email** inviting other priesthood holders to test and give feedback.
3. Before the Bishop, approach two brethren first to get their understanding and support, so he arrives with a friendly chain of priesthood behind him:
   - **Rich Sutherland** — Elders Quorum President.
   - **Kyle Castle** — Second Counselor in the Bishopric, and Cameron's close friend.
4. He wants the whole thing **carefully staged** — his worry, stated directly: "one wrong word and it would make him just doubt it a little and he will say it's probably not a good idea." He wants it presented so a thoughtful leader is comfortable saying yes.

He also expressed conviction that he has the Holy Spirit guiding him on this, and that the app — though it touches things the Church treats as delicate (AI, missionary work) — is a careful, beneficial, cutting-edge use case rather than a violation of any rule.

## 2. His stated concerns and requirements (carry these forward)

- **Careful staging of every word.** The approach must not give a leader an easy reason to doubt. (See the honest-framing note below — the right execution of this is transparency, not slickness.)
- **Follow the priesthood order:** brethren first (Rich, then Kyle), then the Bishop, then the wider invitation.
- **Research what he'd need to present** and **contrast it against the Church's actual rules** to show the app isn't breaking them but is a thoughtful good-faith use.
- **Check what the app is really like** (not just claims) and **check what the Church would have a problem with**, honestly.
- **Delivery mechanics matter:** if the Bishop has an iPhone he can be set up easily; if Android, he needs to be added to the test differently. The plan must account for both.

## 3. The honest-framing principle (important — do not lose this)

Cameron initially framed the goal as making the pitch so airtight the Bishop "can't refute it." The guidance settled on (and that all materials were built around): **the aim is not to make it irrefutable — it is to be so transparent that a careful leader can give an informed yes.** This is also exactly what the app's own principles require (meet people where they are, never manipulate, be honest about what it is). Defensiveness reads as hiding something; calm honesty that names weaknesses and shows how they're handled is what earns a leader's trust. Every material was written to that standard. A new chat should keep this posture: **counsel before approval, name the real risks, let the Bishop see every word before it goes wider.**

## 4. What was BUILT this session — the `church-launch-kit/` folder

Location: `/home/noremacttevol/Desktop/Brain/MBM/church-launch-kit/`

- `00_README-Start-Here.md` — index explaining each file and when to use it.
- `Bishop-Brochure.pdf` — the one-page, designed, hand-to-the-Bishop brochure (the centerpiece). Source is `brochure.html`; re-render with `weasyprint brochure.html Bishop-Brochure.pdf`. **Still has `[your phone]` / `[your email]` placeholders** in the footer — Cameron must fill these before printing.
- `01_App-vs-Church-Review.md` — Cameron's private briefing: every legitimate concern a leader could raise, answered honestly against the app's real behavior and the Church's published guidance. (NOT a handout.)
- `02_Staged-Approach-Plan.md` — the Rich → Kyle → Bishop game plan, with what to say and what to ask for at each step.
- `03_Priesthood-Invitation-Email.md` — two ready-to-send versions (full + short) of the tester-invitation email. Send the Bishop the exact wording first.
- `04_Install-Guide.md` — two-minute install steps for iPhone (TestFlight) and Android (Play internal testing), with the current links.
- `05_FAQ-and-Objections.md` — short, honest, out-loud answers to the pointed questions a Bishop might ask.
- `06_Privacy-One-Pager.md` — plain-language page on what the app collects/protects, for anyone who asks.

**Open polish items for a new chat:** fill the brochure contact placeholders and re-render; optionally produce print-ready PDFs of the other docs; optionally a slide version if he wants to present on a screen.

## 5. Verified facts about the app the pitch relies on (read from the real code this session)

These were confirmed by reading the actual source, so the pitch is honest:

- **Non-affiliation disclaimer** shows on app open (HookScreen) and on the Profile screen: *"This app is not officially affiliated with, endorsed by, or sponsored by any church. It is an independent space to explore who Jesus is."* (`mobile/src/screens/ProfileScreen.tsx`, `HookScreen.tsx`)
- **"Milk Before Meat" note every open** reminds the user the app is "a lantern, not the Light," cannot answer a prayer, and to close the screen and pray to God directly. Anchored in Elder Gerrit W. Gong's counsel that AI "can answer questions, but it cannot answer prayers… it is not God and cannot be God." (`mobile/src/data/milkBeforeMeat.ts`)
- **The AI system prompt** (`mobile/src/engine/minister.ts`): never claims to be Jesus or a spiritual authority; points TO Christ; "never bluff" / admits uncertainty; **discloses immediately and truthfully when asked who made it / whether it's an LDS app** (never denies it); gives milk only and never raises the Restoration/Joseph Smith/Book of Mormon until the person shows readiness AND **asks permission first**; never pressures ("Jesus let the rich young ruler walk away. So do you."); keeps a real human ("the admin team") one tap away; success defined as a person "truly met, unpressured, and free" whether or not they convert.
- **Crisis protocol:** presence first, no diagnosing/therapy, gentle human handoff, and in the US surfaces 988 when there's sign of imminent danger.
- **Data/privacy:** anonymous Firebase sign-in (no name/email/account required); human-inbox messages stored tied only to the anon ID, scoped so a person sees only their own thread; optional self-reported name and faith note; Profile shows what's been noticed with per-item Remove buttons; privacy policy at milkb4meat.org. Honest caveat carried in the materials: conversation is processed by Anthropic's API and messages stored in Firebase (normal, but true).

## 6. The Church guidance anchors (with sources) the materials cite

- **General Handbook AI guidance (added Dec 2025):** use AI in "positive, helpful, and uplifting ways"; AI "cannot replace the gift of divine inspiration"; "interactions with AI cannot substitute for meaningful relationships with God and others"; aim is to "support and not supplant connection between God and His children." Source: newsroom.churchofjesuschrist.org article on Handbook AI guidance.
- **Trademark / name guidance:** members may not use the Church's name/"Mormon"/"LDS" in a way that implies endorsement or affiliation, and not in a product name. The app uses none of these in its name and claims no endorsement. Source: churchofjesuschrist.org/reference/trademark-guidelines.
- **General Handbook Ch. 23 (sharing the gospel):** "love, share, invite"; the effort is positive "whether or not a person meets with the missionaries or joins the Church." Source: churchofjesuschrist.org General Handbook 23.

**Honest caveat baked into the review:** the Church's AI guidance is written for members using AI in their own Church assignments; an AI that ministers to seekers is newer ground the Church has not specifically blessed. That's exactly why the ask is framed as an independent member's local pilot seeking the Bishop's counsel — NOT as a Church-endorsed product.

## 7. The ask, kept deliberately small

For the Bishop meeting the entire ask is: **his blessing to let a few trusted priesthood holders quietly test the app for ~2 weeks and give honest feedback** — plus offering to put it on the Bishop's own phone first. NOT asking the Church to endorse it, vouch for it to the stake, or call it official. Small, reasonable asks are easy to say yes to.

## 8. Current delivery / publishing state (so the pitch's install steps are accurate)

(Source of truth is `START-HERE.md` and `ANDROID-PUBLISH-PATH.md` — both updated 2026-06-26. Summary:)

- **iOS:** Submitted to Apple for public review (v1.0 build 6, WAITING_FOR_REVIEW, auto-releases on approval). App Privacy label published. Also on **TestFlight public link: https://testflight.apple.com/join/cPNpeh3H** — this is the easy way to put it on an iPhone now.
- **Android:** Automated Google Play publishing is now LIVE (service-account key set up 2026-06-26; `eas submit` proven working to the internal track, vc 6). App is on **Play internal testing**; tester opt-in link: **https://play.google.com/apps/internaltest/4700576250998456373**. To install, a tester's Google account email must be in the "MBM Testers" list first.
- **To go PUBLIC on Android** still requires Google's **12-tester / 14-day closed test** — which dovetails with Cameron's ward-testing plan: the 12 priesthood-holder testers can BE the closed-test cohort that unlocks public release. A new chat should connect these two efforts (the church invitation and the 12-tester Google gate are the same people). Store listing still needs 6 screenshots uploaded manually from `store-assets/`.

## 9. What's left / open questions for the new dedicated chat

- Fill the brochure's contact placeholders and re-render the PDF.
- Decide whether to merge the "12 Google testers" requirement with the "priesthood-holder testers" invitation (strongly recommended — same people, two birds).
- Confirm the Bishop's phone type (iPhone vs Android) to pre-stage his install.
- Optionally: print-ready PDFs of the FAQ/plan; a short screen-deck; a one-page leave-behind for Rich and Kyle specifically.
- Gather any additional context from Cameron's OTHER chats (he is pasting his request into several) and reconcile into this single effort.

## 10. Pointers / file hierarchy

- This effort's materials: `church-launch-kit/`
- App current build/publish truth: `START-HERE.md` (highest authority on "what's true now")
- Android path detail: `ANDROID-PUBLISH-PATH.md`
- Vision/laws/how-to-behave: `AGENT-RULES.md`
- An earlier church-angle doc exists: `CHURCH-REVIEW-2026-06-24.md` (historical; reconcile if it conflicts).

---

*Bottom line for the new chat: the pitch package already exists and is honest and accurate. The job now is to finish the small polish items, fold in context from Cameron's other chats, tie the priesthood-tester invite to the Google 12-tester gate, and help Cameron walk the Rich → Kyle → Bishop path with calm, transparent confidence.*
