# PORT-BACK — bring `mobile/src` up to the proven prototype (hand to Claude Code)

Every change below is already implemented and verified in the prototype
(`MBM App.dc.html` + `mbm-data.js` — copy logic from there verbatim where noted).
Work top-to-bottom: items are ordered by how badly the live app is violating the
laws in CLAUDE.md right now.

---

## 1. `src/engine/connect.ts` — ONE CLICK IS NEVER IDENTITY (Laws 2, 3) ⚠ HIGHEST

The live bug that lost a tester: `covenant_intent` (set by a single story tap
like "I'm committed but I hold back") counts as membership → MAINTENANCE track →
churchofjesuschrist.org links on screen one.

```ts
// BEFORE
const MEMBER_SIGNALS = new Set<string>(['covenant_intent', 'inactive_member', 'active_member']);

// AFTER — membership only from explicit self-identification in their own words
const MEMBER_SIGNALS = new Set<string>(['inactive_member', 'active_member']);

// AND add covenant_intent as a believer HINT (counts toward signal (a), never identity):
const GOD_GOOD_SIGNALS = new Set<string>([
  'believes_god_good', 'believes_in_jesus', 'drawn_to_jesus',
  'open_to_god', 'had_spiritual_experience', 'covenant_intent',
]);
```

## 1b. `src/engine/connect.ts` — ONE HINT IS NEVER BELIEF (Law 8 extension)

`believesGodGood` must not return true from a single soft signal (one story tap
like "something has been pulling me" currently marks a brand-new user as
believing God is good). Port the two-witnesses rule verbatim from `mbm-data.js`:
explicit `believes_god_good` always counts; `pictures_harsh_god` /
`pictures_distant_god` block until contradicted; otherwise ≥2 independent soft
witnesses required.

## 1c. `src/data/questionBank.ts` — TARGETED `computeNextQuestion`

Port the priority layer from `mbm-data.js`: background → picture of God →
God-still-speaks → the reach. The next question is always the one the engine
most needs answered to move this person along the designed path — never list
order.

## 1d. Framework discernment — the affirmation is not the signal (Law 8, owner direction)

A person inside a framework that denies God's goodness (Reformed determinism:
election, damnation for God's glory; the creation-dilemma: an ex nihilo creator
owns the evil that follows) often loyally SAYS "God is good." That affirmation
must NOT open readiness signal (a). Port from `mbm-data.js`/prototype:
- New signals: `reformed_framework`, `rejects_harsh_god` (+ chat harvest
  patterns and signal-report tokens).
- `believesGodGood`: framework/harsh-picture signals BLOCK until the person
  rejects the harsh picture in their own words AND affirms goodness.
- Framework probes in the question bank: id 70 (which church/tradition + what
  it taught about God — verbatim into faithWords), id 71 (does everyone get a
  real chance — the Calvinist-revealing question), id 72 (1 Pet 4:6-shaped:
  would universal chance be better news, gated on pictures_harsh_god).
- Chat captures faith self-descriptions verbatim into `faithWords` (the app
  must KNOW it is talking to a Calvinist/Baptist/etc.).
- Ministering plan gains the internal discernment note (comparison method
  against the framework, 1 Tim 2:4 / 1 Pet 4:6 milk-safe scriptures, never
  exposed, never named).

## 2. `src/data/questionBank.ts` — confirming question + belief probes + faith tradition (Laws 2, 6, 9)

Port from `mbm-data.js` QUESTION_BANK, verbatim:
- **id 0** `faith_home` (ENTRY, prereq `covenant_intent`) — "Where does that faith
  live right now?" Asked FIRST for anyone whose tap hinted faith. Names no church.
- **id 2.5** `faith_tradition` (ENTRY) — "Do you have a faith tradition today?"
  Third question for everyone. `active_faith_tradition` signal.
- **id 66** `faith_home_named` (EARLY, prereq `active_faith_tradition`, FREE_TEXT) —
  "Which church or tradition is home for you?" Their own words → harvested →
  this is where an LDS member self-identifies (Law 3) and a Baptist gets
  `believes_in_jesus`.
- **ids 61, 62, 63, 64** — belief probes (picture-of-God): what God thinks of
  you / describe the God you don't believe in / Jesus in your situation /
  score-keeper vs leaning-in. New signals `pictures_harsh_god`,
  `pictures_distant_god` (add to SIGNAL_LABELS; the minister uses them for the
  comparison method).

## 3. `src/store/useAppStore.ts` — the chat ear + whole-app learning (Law on hearing)

In `sendChatMessage`, port from the prototype logic class:
1. `harvestSignals(text)` — conservative regexes (copy from prototype, includes
   member self-ID phrases "I'm LDS / my ward / served a mission" and Christian
   denominations → `believes_in_jesus`). Run on the user's message BEFORE
   building the system prompt; merge into a `liveSignals` array used for the
   guidance block so the gate can open mid-conversation.
2. Append the `[SIGNAL REPORT]` instruction to the system prompt (fixed token
   vocabulary; copy the exact block). Strip `<signals>…</signals>` from the
   reply before display; merge valid tokens.
3. `mergeSignals(newSignals)` — dedupe, re-derive `routeFeedTag`, rebuild feed
   ONLY if the track honestly advances, recompute `currentQuestion` if null.
4. ABOUT THIS PERSON block additions: first name; recent moments list with the
   instruction "You DO have this context — never claim you cannot see their
   story"; active exercise; the one-concrete-invitation instruction line.
   (Copy `buildSystemPrompt` from the prototype.)
5. `answerQuestion`: support `'__own'` answer value (own-words on CHOICE
   questions → generic sincerity/courage traits) and harvest every free-text
   answer through `harvestSignals`.
6. `addJournalEntry`: harvest signals from the entry text + sincerity/courage
   nudges. `thumbsUp`: trait nudges by content tag. `markOpened`: hunger/openness
   nudges.
7. Rehydrate self-heal (Law 7): on store rehydration, `routeFeedTag(signals)`;
   if persisted feedTag is MAINTENANCE/RESTORATION but signals don't justify it,
   downgrade and rebuild the feed.
8. Persist additions: `name`, `moments`, `activeExercise`, `doneExerciseIds`,
   `session` (increment per rehydration).
9. DELETE `keepSimple` / `goDeeper` actions (Law 1) → replace with `refreshFeed`
   (same-track rebuild only). DELETE `VIEW_CAP` / `isTimeCapReached` (Law 5).

## 4. New `src/engine/exercises.ts` — the spiritual exercise loop (Law 9)

Copy `EXERCISES` + `pickExercise` from `mbm-data.js`. Loop: invitation card in
feed → accept ("I'll try it") / pass (free, no guilt) → on NEXT session a
follow-up card asks what came back, with an optional own-words reflection field
(harvested) + 4 outcome options mapping to signals
(`had_spiritual_experience`/`open_to_god` / honest-nothing honored). Log both
accept and report as moments.

## 5. Screens

- **`FeedScreen.tsx`**: remove the keep-simple/deeper buttons → one "Show me
  more →"; add FollowUpCard (top of feed when due) and InvitationCard (below
  content). Copy markup/behavior from the prototype feed.
- **`ProfileScreen.tsx`** (Law 4): DELETE trait bars and CURRENT PATHWAY /
  "N signals active". Keep: words-only interpretation, activity counts, privacy
  footer. ADD "Your story so far" — titled moments, newest first, each with
  "Ask about this →" that opens Chat with the prefilled draft.
- **`OnboardScreen.tsx`**: optional first-name input on the reflection step
  ("A first name is plenty — or skip it"), then a dedicated FAITH BACKGROUND
  page as the final onboarding step (owner direction): "Where does faith live
  for you — today, or in your past?" — five options + open field, seeds
  routing signals before the first feed, stores their words verbatim in the
  faith record, marks the in-feed faith-tradition question answered. Copy from
  the prototype's `phaseFaith` block + `enterApp`.
- **New `WelcomeBackScreen.tsx`**: on launch with persisted main-state, show
  "Welcome back{, Name}." + recall of their last journal line, "Pick up where
  you left off →". No more cold restarts.
- **`TimeCapScreen.tsx` + its route + the `resetSession` come-back wipe**:
  DELETE (Law 5; the wipe also destroyed identity/memory).
- **`ChatScreen.tsx`**: "Talk to a real person" opens the in-app connect
  capture (not mailto), same as the prototype.
- **Blessing toasts**: after dialogue answers, hearts, journal saves, exercise
  accept/report — words only, copy the pools from the prototype. Journal's
  "Written." state gets a blessing line.

## 6. `src/engine/minister.ts` (+ keep `ministry-sim/minister.py` byte-synced)

Add to the system prompt the standing invitation instruction (one small
concrete thing to DO, offered once, never assigned) — copy the line from the
prototype's `buildSystemPrompt`.

## 7. `ministry-sim` — make the harness measure the mission

Implement MINISTRY-FUNNEL-SPEC.md: F1–F5 funnel stages + V1–V5 vetoes in
`judge.py`, objective in `learn.py`, seed-locked 102-persona re-run, plus the
new F2 check (did the engine HEAR chat-expressed readiness before the end?).

## Acceptance test (the one that lost the tester — must pass before anything ships)

1. Fresh install → story → answer "I'm committed but I hold back" (or any
   sincere covenant-sounding choice) → Enter.
2. MUST land on MILK. Journey ≠ DISCIPLE_GROWING. Zero churchofjesuschrist.org
   links anywhere. First dialogue question = "Where does that faith live right
   now?" (no church named).
3. In chat, type "I'm LDS, I want to go deeper" → member track unlocks (Law 3).
4. In chat, express "God sounds good" + "does God still speak?" → gate opens
   mid-conversation; a direct question about the app's beliefs gets the honest
   restored answer (never a dodge).
