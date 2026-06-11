# SIM-REPORT — engine simulation, 108 persona-trials (2026-06-11)

## What was tested
The prototype's actual engine (`mbm-data.js` — the same module the app runs):
routing, milk gate, member rules, framework discernment, two-witnesses belief
rule, and the targeted question engine. 12 archetypes × all 9 entry stories =
108 trials; each trial = onboarding tap → faith-background page → 10 targeted
dialogue answers → 2 chat utterances harvested, with every law checked after
every mutation.

Archetypes: hostile atheist, curious skeptic (ready arc), grieving secular,
loyal Calvinist ("Tam"), awakening Calvinist, warm Baptist (ready arc),
drifted Catholic, hurt-by-church, active LDS member, one-tap-member regression,
new-age spiritual (ready arc), lonely young seeker.

## Results
- **Law violations: 0 / 108 trials.** No MAINTENANCE without explicit member
  self-ID, no RESTORATION without the gate, no gate without both signals, no
  framework persona credited with god-good without their own rejection, no
  repeated questions, no question-pool exhaustion within 10 steps.
- **Routing accuracy: 11 of 12 archetypes perfect on first run.** Hostile
  atheist & grieving folks stay in gentle milk (CURIOUS); ready arcs reach
  OPEN_TO_RESTORATION; the LDS member reaches DISCIPLE_GROWING only via own
  words; the one-tap regression stays CURIOUS.

## Finding #1 (fixed): the breakthrough sentence was being silenced
`calvinist_awakening` scored 0/9. At the exact moment of breakthrough, people
say both things in one breath — *"a god who does that is not good. God is good
though — the real one."* The whole-message negation guard saw "not good" and
discarded the affirmation, so the person this app most exists to reach never
opened the gate. **Fix:** per-sentence harvesting (the rejection can never
silence the affirmation). Re-run: 9/9, with loyal-Tam still correctly closed.
Ported to PORT-BACK §3 (harvest function).

## What this simulation CANNOT test (needs the owner's machine)
The conversational voice — tone, over-reach at the close, premature disclosure
in free prose, handoff timing. That is `ministry-sim`'s job with a live model:
run MINISTRY-FUNNEL-SPEC.md (F1–F5 + vetoes) over the 102 personas, seed-locked,
plus an adversarial second agent. The engine underneath is now verified ground.

## Addendum — atheist sub-archetypes (72 trials, 2026-06-11)

8 kinds of atheist × 9 stories = 72 trials. **0 violations, 9/9 correct per type.**
- Debater / scientist materialist → BRIDGE (evidence), gate closed, asked
  god_you_reject + picture-of-God probes. Met at the head, never pitched.
- Apatheist → MILK (story only), invitation: read Mark 1.
- Angry ex-believer → faith_history_named asked by Q5; invitation:
  small_forgive; "I don't believe in a god who tortures" harvested as
  rejects_harsh_god (progress toward the true God, not away).
- Moral objector → his conscience ("everyone deserves a chance") treated as
  the seed; gate correctly closed.
- Grieving atheist → presence questions + forgiveness exercise. WATCH ITEM:
  his "empty air" answer routed him to BRIDGE; conversational sims should
  check whether comfort ought to outrank evidence for the grieving.
- Atheist-with-experience & curious deconvert → legitimately opened the gate
  through own words across many steps; invitation: ask_direct (Moroni-shaped).

## Addendum 2 — tradition sweep (90 trials, 2026-06-11)

10 traditions × 9 stories. 0 law violations. Measures per tradition (track /
journey / gate / invitation) and ground-truth correctness:

| Tradition | Result | How the app serves them |
|---|---|---|
| Southern Baptist (devout, canon-closed) | 9/9 after FIX #2 | MILK that honors their faith; gate closed; journey BELIEVES_GOD_GOOD |
| Southern Baptist (seeking) | 9/9 | Gate opens via their own "why would God stop speaking?"; ask_direct invitation |
| Pentecostal (devout) | 9/9 | Gate lawfully OPEN — they genuinely affirm both signals. VOICE WATCH: ministering "restored" framing to someone who already believes God speaks needs conversational care |
| Catholic (devout) | 9/9 | MILK, gate closed, BELIEVES_GOD_GOOD honored |
| Catholic (cultural/drifted) | 9/9 | MILK + faith_history_named asked by Q5; notice_alive invitation |
| Non-denom seeker ("something is missing") | 9/9 | Gate opens through their reach; ask_direct |
| Muslim | 9/9 | MILK, gate closed. CONTENT WATCH: milk library is Bible/Jesus-framed; fine for Jesus-honoring Muslims, but content fit deserves review |
| Jewish secular | 9/9 | MILK, CURIOUS, presence-first |
| Buddhist-leaning | 9/9 after FIX #3 | CURIOUS until a personal good God is affirmed in their own words |
| LDS inactive | 9/9 | Member track via own words; small_forgive invitation (the ward wound) |

**FIX #2 (engine):** "I DON'T think God still speaks" was heard as openness —
per-sentence + negation guard on the open_to_restoration harvest; added the
positive "why would God stop?" pattern.
**FIX #3 (engine):** `nontheistic_framework` signal — warm spirituality toward
a non-personal God no longer counts toward believing in a good personal God
until they affirm one explicitly.

**Improvement queue (in priority order):**
1. Port FIX #2/#3 + two-witnesses + framework rules to mobile/src (PORT-BACK §1b–1d, §3).
2. Conversational sims (owner's machine): Pentecostal "already speaks" framing;
   grief comfort-vs-evidence ordering; Muslim/Buddhist content fit.
3. Consider tradition-specific milk variants (e.g., common-ground content for
   Muslims) — owner call, Phase 2.

## Standing protocol
Re-run this engine sim (script preserved in chat history; results in
`sim-results.json`) after ANY change to signals, questions, or routing.
Add a new archetype for every real person the app fails — Tam is archetype #4
forever.
