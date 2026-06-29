# Tiered AI Models + Offline Mode — Plan (June 2026)

A plain-language plan for two things Cameron asked about: (1) giving harder/more
important questions a stronger AI model, and (2) whether to ship an offline mode.
Grounded in how the app actually calls the AI today.

## How the AI works right now (so we know what we're changing)

Every AI reply in the app goes through one path:

- The phone never holds the Anthropic key. It posts the conversation to a small
  proxy at `/api/chat` (`server/index.js`, and the same endpoint folded into
  `admin/inbox.mjs`). The proxy adds the secret key and forwards it to Anthropic.
- The model is hard-coded in three places to `claude-haiku-4-5-20251001`:
  `mobile/src/engine/minister.ts` (`MINISTER_MODEL`), `server/index.js`, and
  `admin/inbox.mjs`. Haiku is the small, fast, cheap model.
- `max_tokens` already varies by call type (120 / 160 / 320 / reply length), so
  the app is already used to sending different settings per situation.

The takeaway: there is ONE place that decides the model, and it is currently fixed
to the cheapest one for everybody and every question.

## Correction that changes the design: one key, many models

"Multiple API keys for different levels" is not how model choice works. A single
Anthropic API key can call ANY model — Haiku, Sonnet, or Opus — just by changing
the `model` field in the request. You do not need a second key to use a smarter
model for a hard question.

Separate keys are only worth it for one reason: **cost separation**. If you want a
hard spending cap or a clean bill for "the expensive tier" vs "the everyday tier,"
you can put each tier on its own key/billing project and watch them independently.
That is a money-tracking choice, not a technical requirement. Recommendation: start
with ONE key and tier by model; add a second key later only if you want a separate
budget you can cap.

## The tiering plan (route by how much the question needs)

Three tiers, cheapest to strongest. Exact model IDs should be confirmed against the
current list at docs.claude.com before shipping; as of now the families are
Haiku 4.5 (cheap/fast), Sonnet 4.6 (balanced), Opus 4.6 (strongest).

- **Everyday (Haiku):** greetings, reflections, short check-ins, "talk about this
  verse" — the bulk of traffic. This is what runs today. Keep it the default.
- **Medium (Sonnet):** real questions that deserve care — doubt, a hard life
  situation, a theological question that isn't a crisis.
- **Important (Opus):** the heaviest, highest-stakes moments — a sharp skeptic
  pressing a genuine contradiction, a faith crisis, a careful doctrinal question
  where a weak answer could push someone away. Rare, but worth the cost.

### How the app decides the tier

Pick ONE of these to start; they can be combined later:

1. **Signal-based (cheapest, no extra AI call):** the app already detects signals
   like `crisis`, `losing_faith`, `reformed_framework`, debater/testing language,
   and grief. Map those to a tier. Crisis or a detected sharp-debate turn -> Opus;
   doubt/hard-question signals -> Sonnet; everything else -> Haiku. This reuses
   logic that already exists and adds no latency or cost to classify.
2. **Tiny classifier turn (more accurate, small cost):** before answering, ask
   Haiku one cheap question — "how hard/important is this, 1-3?" — and route on the
   answer. Costs one small call per message; only worth it if signal-based proves
   too blunt.

Recommendation: ship **signal-based** first. It's free to run, uses what's already
there, and you can measure whether it routes the right messages up before paying
for a classifier.

### Where the change lives

Small and contained: replace the single `MINISTER_MODEL` constant with a
`pickModel(signals)` function, and let `/api/chat` accept an optional `tier` (or
`model`) field — with the **proxy enforcing an allow-list** so the phone can only
ask for one of the three approved models, never an arbitrary/expensive one. Default
stays Haiku if nothing is specified, so nothing breaks.

### Cost reality

Opus costs meaningfully more per message than Haiku, but if Opus only fires on the
rare hardest turns (a few percent of traffic), the blended cost stays low while the
moments that matter most get the best answer. The risk to avoid is Opus firing on
everyday chatter — the allow-list + conservative routing prevents that.

## Offline mode — Cameron's caution is right; here's the safe path

The concern — "how do we give offline answers without knowing they're still good?"
— is the correct instinct. A small on-device model can produce confident, wrong, or
off-voice answers, and this app's whole promise is to represent Jesus faithfully.
Shipping an unverified offline voice is a real risk to the mission, not just a bug.

Plan:

1. **Do NOT ship an offline AI voice yet.** Until quality is measured and steady,
   the honest offline behavior is: say plainly the connection is down, offer saved
   content and reflections that already live on the device, and make the "reach a
   real person" capture work offline (it already stores on-device and sends when
   back online). No fabricated AI answers offline.
2. **Measure against a steady threshold before trusting any offline answers.** You
   already have a scoring harness — `ministry-sim/minister.py` — that grades the
   minister voice. Any candidate offline model must be run through that SAME harness
   and clear an agreed bar (e.g., a minimum score, no crisis-handling failures, no
   doctrinal misses) across repeated runs before it is allowed to answer anyone.
3. **Monitor continuously, don't decide once.** Keep scoring on an interval and
   watch for drift. Only "settle on" offline once the score is high AND stable over
   time — exactly as Cameron described.

Net: tiered models is a clear, contained win to build next. Offline AI answers stay
parked behind a measured, monitored quality gate — offline *capture* and saved
content ship freely; offline *AI voice* waits until the harness says it's good and
stays good.
