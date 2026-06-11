# MBM — Handoff Brief for the Next Agent

You are taking over work on **MBM (Milk Before Meat)**, Cameron's gospel-outreach app.
You have filesystem access and a working `ANTHROPIC_API_KEY`. Read this whole file first,
then read `CLAUDE.md` and `.claudecode.md` in this same folder. Those two files are the law.
Do not violate them.

Project root: `/home/noremacttevol/Desktop/Brain/MBM/`

---

## THE PLAN / DIVISION OF LABOR (Cameron's current strategy — read this first)

- **Hermes (you, if you are the tester): GENERATE DATA.** Run the simulation many, many
  times across all personas to pile up trials. Each run appends to a durable, append-only
  dataset that survives sessions and credit limits. Do NOT overthink it — just run lots of
  trials. Commands are in section 4.
- **The building agent: LEARN AND REFINE.** Reads the accumulated trials, finds where the
  minister fails, fixes the app (`knowing_engine.py` and `ministry-sim/minister.py`), and
  re-runs. Over time the app gets measurably better at meeting each person like Jesus did.
- Why this works even when credits run out: all data lives in files
  (`ministry-sim/outputs/trials.jsonl` and `evidence.json`), not in any agent's memory. The
  pile keeps growing; refinement can happen anytime against it.

---

## 1. What MBM is (in one breath)

A mobile-first (React Native + Expo) app that ministers the way Jesus did: it meets each
person exactly where they are, learns who they are, and guides them gently from foundational
truth ("milk") toward the restored gospel of The Church of Jesus Christ of Latter-day Saints
("meat") — without ever pressuring, shaming, sorting, or gating them.

## 2. The non-negotiables (these override any instinct to "optimize")

- **No visible gates, tiers, or progress bars.** Routing is invisible and emergent from what
  the person says. They never feel they "haven't qualified" for the next step.
- **Story first, always.** A person's first experience is a story they see themselves in, then
  ONE open question, then the app reflects their words back so they feel seen — before any content.
- **Milk before meat is a hard law.** Nothing LDS-specific — Joseph Smith, the Book of Mormon,
  the Restoration, missionaries — is mentioned until the person has shown BOTH: (1) they believe
  God is fundamentally good, and (2) openness to God still speaking today. The code enforces this.
- **Never argue doctrine.** When someone holds a harsh view of God, do not debate. Set the Jesus
  they already accept beside that harsh inherited God and ask one honest question. Let Jesus correct
  error in his own voice.
- **Faithfulness is the only success metric. NEVER conversion.** A person who is met honestly,
  unpressured, and walks away freely is a SUCCESS. The system must never be tuned toward conversion
  rate — that is how it would become manipulative. Conversion is fruit, never the target. The
  evidence store literally refuses to record a "converted" outcome on purpose. Keep it that way.
- **A real human is always one tap away** (Phase 1 = Cameron himself; do not label that human "LDS"
  — don't lead with it, never deny it when asked).
- **Let people walk away.** Jesus let the rich young ruler go. So does this app.

## 3. What is already built and working (verified)

All in the project root unless noted.

- **`knowing_engine.py`** — THE APP'S BRAIN. This ships. It reads each person's messages for
  signals (grief, anger, analytical/debate, "God-is-not-good" wound, two readiness signals,
  warmth, curiosity, disengage), grows a per-person `Profile`, and recommends the next faithful
  move (PRESENCE, COMPARISON, HONEST_EVIDENCE, GENTLE_QUESTION, GENTLE_EXPLORE, HONOR_AND_RELEASE).
  `may_reference_lds()` returns True ONLY when both readiness signals are confident. An
  `EvidenceStore` learns across people which move ministered faithfully — and refuses "converted".
  Run `python3 knowing_engine.py` to see its self-test pass.
- **`ministry-sim/`** — THE TESTER (separate from the app). Role-plays people so Cameron doesn't
  have to be the lone bug reporter. `personas.py` (10 personas), `minister.py` (the app's real
  ministering voice + system prompt), `judge.py` (grades FAITHFULNESS, not conversion), and
  `run_sim.py` (the runner — already wired so `knowing_engine` steers the minister every turn and
  prints `brain> approach=...` live).
- Design docs: `KNOWING-ENGINE.md`, `APP-FLOW-SPEC.md`, `LEARNING-ENGINE.md`. Read them.
- `router.py` and the old `SPEC.md` journey describe a RETIRED gate-ladder system. Do not build on
  them. They are reference for porting logic only.

Verified working from a sandbox (with scripted inputs, no API key): the brain self-test passes,
and the four-person end-to-end pipeline routes a Calvinist to HONEST_EVIDENCE→COMPARISON, a
grieving widow to PRESENCE, an opening seeker's LDS gate flips only after both readiness signals,
and someone leaving gets HONOR_AND_RELEASE.

## 4. The ONLY thing currently blocking progress

The full live simulation needs a valid `ANTHROPIC_API_KEY`. The last attempt returned a
**401 invalid x-api-key** — that is purely a bad/empty key in the shell, not a code bug. You have a
working key, so this stops being a problem for you.

The key is also stored in `mobile/.env`, `server/.env`, and `backend/server/.env` as
`ANTHROPIC_API_KEY=...`. Export it from there if your shell doesn't already have it.

**Confirm the key, then run trials:**

```bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim
export ANTHROPIC_API_KEY=$(grep ANTHROPIC_API_KEY ../mobile/.env | head -1 | cut -d= -f2- | tr -d '"'"'"' \r')
python3 -c "import anthropic; print(anthropic.Anthropic().messages.create(model='claude-haiku-4-5-20251001', max_tokens=5, messages=[{'role':'user','content':'hi'}]).content[0].text)"
# if that prints text, the key works.
```

**HERMES — generate as much data as possible (this is the job):**

```bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim
# run all personas, many turns; repeat this line as many times as you can afford.
python3 run_sim.py --personas all --turns 6 --out ./outputs
```

Every run APPENDS full trials to `outputs/trials.jsonl` (never overwrites) and updates
`outputs/evidence.json`. Run it in a loop if you want — e.g. `for i in $(seq 1 20); do
python3 run_sim.py --personas all --turns 6 --out ./outputs; done`. More runs = better data.

**BUILDER — learn from the pile (spends no credits):**

```bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim
python3 learn.py --dir ./outputs
```

This reads ALL accumulated trials and writes `outputs/LEARNINGS.md`: the minister's weakest
dimensions, concrete failures flagged (manipulation, dishonesty, premature LDS, missing
human), how it does per kind of person, which faithful move fits which situation, and a
ranked backlog of fixes the judge asked for. Act on that backlog, then have Hermes run more.

### Data files (the project's durable memory)
- `ministry-sim/outputs/trials.jsonl` — append-only, one full trial per line. The source of truth.
- `ministry-sim/outputs/evidence.json` — the across-people brain, rebuilt from all trials by learn.py.
- `ministry-sim/outputs/LEARNINGS.md` — the human-readable refinement report.
- `ministry-sim/outputs/transcript_<persona>.md` / `REPORT.md` — latest-run snapshots.

## 5. What to build next, in order

1. **Run the live sim** (above) and fix any place the minister violates section 2. The minister's
   voice lives in `ministry-sim/minister.py` (`MINISTER_SYSTEM_PROMPT`). Tune that prompt, re-run.
2. **Make the tested voice the shipped voice.** Port the validated `MINISTER_SYSTEM_PROMPT` and the
   `knowing_engine` guidance into the real app's response path (`ai_guide.py` is the current
   reference RAG pipeline; the app uses `claude-haiku-4-5-20251001`). The voice that passed the sim
   must be the exact voice that talks to real people.
3. **Build the onboarding heart as real Expo screens:** Sanctuary (one image + one true statement,
   no branding) → one Story told in 3–5 sentences → one open mirror question → reflect their words
   back → feed silently initialized from `knowing_engine`'s read. No labels ever shown to the user.
4. **Local-first storage:** persist `Profile` and `EvidenceStore` to on-device SQLite via
   `expo-sqlite`. Graceful offline fallback when there's no network for the API.
5. **Screenshot and verify all UI yourself** (Playwright or device preview) before telling Cameron
   anything is done. Never ask Cameron to be the bug reporter.

## 6. How to treat Cameron

He sets the vision; you are the Principal Systems Architect responsible for building it right.
Take initiative. Don't push decisions back on him. Don't make him paste error logs or test your
work. His examples are illustrations, not hard rules — when in doubt, don't ask "does this match
Cameron's example?" Ask "is this what Jesus would do with the person in front of him?" Deliver
working code first, then a brief plain-language explanation. No jargon.
