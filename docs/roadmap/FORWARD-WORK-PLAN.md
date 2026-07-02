# Forward Work Plan — everything still to do, in order

**Written 2026-06-29.** One place that answers: *what work is left, who does it, and in
what order?* This pulls together the loose ends scattered across the publishing docs,
`STATUS-AND-ROADMAP.md`, `NEXT-VERSION-EDITS.md`, and `MODEL-ROUTING-AND-OFFLINE-PLAN.md`.

Two columns of work run in parallel: **getting it published** (mostly waiting + Cameron's
human steps) and **making the app better** (mostly the assistant's build work). They don't
block each other.

---

## NOW — the immediate path to "people are using it"

These are the next real moves, in the order they should happen.

1. **Security clean-up (assistant guides, Cameron clicks).** Change the admin desk password
   off the placeholder "JosephSmith"; rotate the Firebase / Anthropic / Railway keys that were
   visible during setup. ~30 min total. Do before sharing widely. *(From PUBLISHING-ROADMAP Stage 5.)*
2. **Upload the 6 Play store screenshots** from `store-assets/` so the Android listing turns
   green. Cameron drags them in once (the in-app uploader can't drive the native file picker).
3. **iPhone beta out now.** Hand the TestFlight link to the first testers. They auto-upgrade to
   the public App Store app the moment Apple approves — no reinstall.
4. **Gather the 12 Android testers** and start Google's 14-day closed-test clock. Over-recruit to
   ~15 so 12 stick for the full two weeks. Assistant sets up the closed track + opt-in link.
5. **When Apple approves:** follow `../publishing/WAITING-ON-APPLE.md` — flip the website iPhone
   card back to live, re-verify, update `START-HERE.md`, log + commit.

## BEFORE A WIDE / PUBLIC PUSH (not needed for friends-and-family)

- **Call the Church Intellectual Property Office** (1-801-240-3959), describe the app honestly,
  and add a one-line trademark attribution to the website footer. *(See `../reviews/CHURCH-REVIEW-2026-06-24.md`.)*
- **Set a hard spending cap** on the Anthropic API key, and decide on Firebase Blaze (paid) to
  remove the free-tier read limit the ministry console hits.
- **Talk it over with a bishop / stake president** (Cameron's own step).

---

## APP IMPROVEMENTS — written/designed but NOT built yet

These are the next engineering wins. None requires Cameron; each ends in a new build.

1. **Tiered model routing (highest-value next build).** Route by signal: crisis / sharp debate →
   strongest model, doubt / hard question → mid, everything else → everyday — with the proxy
   enforcing an allow-list so the phone can never request an expensive model. One API key can call
   any model; a second key is only for budget separation. Confirm current model IDs against
   docs.claude.com before shipping. *(Full design: `MODEL-ROUTING-AND-OFFLINE-PLAN.md`.)*
2. **Prompt-caching restructure — cut AI input costs up to 90% with zero quality change
   (Cameron's call, 2026-07-02).** Anthropic bills cached input tokens at ~10% of the normal
   price, but only when the beginning of the system prompt is byte-identical from request to
   request. Today the app assembles each person's system prompt dynamically, so nothing caches.
   The fix is a restructure: one large FIXED shared prefix (identity, laws, Jesus-method rules,
   story-handling instructions — same bytes for everyone) followed by a small per-person tail
   (their profile, signals, conversation facts), with the proxy marking the shared prefix
   cacheable. **Framing, per Cameron: the current tester phase IS the research phase for this.**
   We are purposefully using the testers to learn what real system prompts and conversations look
   like in practice — which parts stay fixed for everyone and which parts truly vary per person —
   so the restructure is designed from real usage, not guesses. Review tester transcripts with
   that question in mind, then build the split. Pairs with item 1 (tiered routing) since caching
   applies per model. Ship before any wide public push; urgent once the monthly AI bill nears $100.
3. **Belief / testimony answer option in dialogue (Locked Direction #5).** Today's multiple-choice
   answers skew toward doubt, which boxes believers in. Add a genuine, well-framed "testify" option
   to every such question so a believer isn't cornered into unbelief.
4. **Offline AI fallback.** Graceful, measured-quality answers when there's no internet, parked
   behind a quality gate so it never ships a weak answer. *(Design in `MODEL-ROUTING-AND-OFFLINE-PLAN.md`.)*
5. **Small queued edits** in `NEXT-VERSION-EDITS.md` — fold these into the next build.
6. **Optional App Store polish** (additive, no rebuild): 5–8 iOS 6.7" screenshots instead of 2,
   promotional text, keywords. *(See `../publishing/IOS-STATUS-AND-APPLE-READINESS.md`.)*

## Explicitly decided AGAINST (do not build)

- **A "Start fresh" wipe-everything button.** Cameron's call: people control their record by
  *editing/removing* specific items on the Profile (already built), not by nuking the relationship.
- **Christlikeness / virtue scoring of any kind.** Removed deliberately. The app does not grade
  anyone's soul. *(See `SEVEN-SPIRIT-LEVELS-parked.md` in the archive.)*

---

## LATER — the phases beyond v1 (no rush)

The app is designed so these slot in without a rewrite:

- **Phase 2 — a small team.** Volunteers/supporters receive and answer "talk to a real person"
  threads, not just Cameron. The console (`admin/`) and routing already anticipate this.
- **Phase 3 — Church partnership.** Real missionaries integrated into the chat and connect
  pipeline. This is what the church-launch-kit is building toward.
- **Post-beta polish** driven by real feedback: watch the ministry console, note which stories and
  questions land best (the app already records this), and ship small fixes via Expo OTA updates
  when they're JS-only.

---

## The repeatable "ship a new version" runbook (so this never gets fuzzy)

1. `bash scripts/preflight.sh` → must say **ALL CHECKS PASSED** (no secrets in git, typecheck
   clean, server syntax ok).
2. Commit + push.
3. `cd mobile && npx eas build --platform all --profile production`.
4. Wait for **finished** on the Expo builds page.
5. `npx eas submit --platform ios` and `--platform android` (the public step Cameron approves).
6. Update `STATUS-AND-ROADMAP.md` and `START-HERE.md` so the record stays honest.

Remember the one rule that keeps biting: **code committed ≠ code on the phone.** Only a new
build + install (or an `eas update` OTA for JS-only changes) puts a fix on a device.
