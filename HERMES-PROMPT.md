# Prompt for Hermes — Generate MBM ministry test data (the loop)

**CRITICAL: This simulation IS the app's logic running headless.** Do NOT try to launch the mobile app, Expo, or any UI. Your entire job is to run `ministry-sim/run_sim.py` repeatedly to generate test data. The React Native app lives in `mobile/` — DO NOT touch anything there.

Paste everything below the line into Hermes. Your one job is to **generate data**. You
do not edit the app or the engine. You run the simulation over and over so the builder
agent can learn from the accumulated trials and refine the app. The data lives in files,
so it keeps working even after the builder runs out of credits.

---

## Who does what

- **You (Hermes): GENERATE.** Build a large, diverse persona pool, then run the ministry
  simulation many times against it. Every run appends one line per conversation to a
  durable log (`trials.jsonl`). Never delete it. Never hand-edit it. Just keep adding.
- **The builder agent: LEARN + REFINE.** It reads the whole pile of trials, finds where
  the app's minister is weakest, fixes the app/engine code, and the cycle repeats.

Do **not** modify any of these — they are the builder's job: `knowing_engine.py`,
`connect.py`, `ministry-sim/minister.py`, `ministry-sim/personas.py`,
`ministry-sim/run_sim.py`, `ministry-sim/judge.py`, `ministry-sim/learn.py`,
`ministry-sim/verify_report.py`, anything in `mobile/`. You only RUN three scripts:
`generate_personalities.py`, `run_sim.py`, and (at the end) `verify_report.py`.

## Where everything is

- Project root: `/home/noremacttevol/Desktop/Brain/MBM`
- Simulation: `/home/noremacttevol/Desktop/Brain/MBM/ministry-sim`
- The Anthropic API key already lives in the project. Load it from `mobile/.env`
  (the key is on the `ANTHROPIC_API_KEY=` / `EXPO_PUBLIC_ANTHROPIC_API_KEY=` line).
  The sandbox can reach the Anthropic API with it.
- Durable data the builder reads: `ministry-sim/outputs/trials.jsonl` (append-only) and
  `ministry-sim/outputs/evidence.json`.

## One-time setup each session

```bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim
# Export the key so the scripts can call the models:
export ANTHROPIC_API_KEY="$(grep -E 'ANTHROPIC_API_KEY' ../mobile/.env | head -1 | sed -E 's/.*=//' | tr -d '\"' )"
# Sanity check the key works (should print a short reply, not a 401):
python3 -c "import anthropic,os; print(anthropic.Anthropic().messages.create(model='claude-haiku-4-5-20251001',max_tokens=10,messages=[{'role':'user','content':'say ok'}]).content[0].text)"

# Pin the durable output dir to an ABSOLUTE path so trials always land in the
# one place the builder reads — no matter what directory you happen to be in.
export MBM_OUT="/home/noremacttevol/Desktop/Brain/MBM/ministry-sim/outputs"
mkdir -p "$MBM_OUT"
```

> IMPORTANT: `run_sim.py --out` resolves RELATIVE to your current directory. A
> previous run used `--out outputs` from the project root and the data silently
> landed in `MBM/outputs/` instead of `MBM/ministry-sim/outputs/`, so the builder
> never saw it. ALWAYS pass the absolute `$MBM_OUT` for `--out` (as below). Never
> pass a bare `outputs`.

If that prints `401` or an auth error, stop and report it — do not try to work around it.

## STOP STICKING TO 10 PERSONAS — build a big, diverse pool first

The old loop tested the same fixed ten people over and over. That is far too narrow to
trust. A real app meets the whole spectrum of humanity, and the minister must be tested
against that whole spectrum: the devout AND the hostile, the grieving AND the indifferent,
world religions AND no religion, the wounded-by-church AND the never-churched, the brilliant
skeptic AND the person who can barely name their ache.

**Step 1 — generate a BIG, diverse persona pool (once per session). Target ~1000
distinct people.** Cameron's bar for "this app is verified" is that it was tested against
roughly a thousand genuinely different personalities, not ten. This writes
`generated_personas.json` spanning nine broad categories (believers who arrive in faith,
the wounded/deconstructing, grief & crisis, secular & indifferent, sharp skeptics, world
religions, people on the margins, the full LDS arc, and cultural/global breadth):

```bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim
# 40 batches x 25 each = ~1000 personas. This takes a while and costs API — let it run.
python3 generate_personalities.py --temperature 0.95 --per-batch 25 --batches 40 \
  --out "$MBM_OUT/generated_personas.json"

# Confirm it built a real pool (target ~1000, with a healthy mix and some arrives_in_faith):
python3 -c "import json; d=json.load(open('$MBM_OUT/generated_personas.json')); ps=d['personas'] if isinstance(d,dict) else d; print('pool size:', len(ps)); print('arrives_in_faith:', sum(1 for p in ps if p.get('arrives_in_faith')))"
```

If generation is slow or partially fails, run it again with fewer `--batches` and a
different run — the script overwrites the pool file, so to ACCUMULATE toward 1000 across
several generation runs, write to numbered files (`--out "$MBM_OUT/gen_1.json"`, then
`gen_2.json`, …) and pass multiple `--persona-file` flags to `run_sim.py` if supported, or
just regenerate one large pool. A pool of several hundred is acceptable to start; keep
growing it toward a thousand. If the pool already exists and is large, you may reuse it.

## The loop — sample broadly from the big pool, aim for 100+ trials

`run_sim.py` now accepts `--persona-file` (load the generated pool) and `--sample N`
(randomly draw N personas from the combined pool of built-ins + file). **Each pass draws a
fresh random sample**, so over several passes you cover a wide, varied slice of humanity
rather than the same ten faces.

**Your goal is to cover as many DISTINCT people from the ~1000 pool as you can** — breadth
is the whole point. Aim for several hundred real trials, climbing toward one trial per
persona over time. Keep `--turns` around 4–6 so conversations are real but don't time out.
The block below runs 20 passes; each pass samples 25 fresh personas = ~500 trials, all
appended to the same durable dir. Run more passes (or raise `--sample`) to go higher:

```bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim

for pass in $(seq 1 20); do
  echo "########## PASS $pass of 20 — fresh random sample of 25 ##########"
  python3 run_sim.py \
    --persona-file "$MBM_OUT/generated_personas.json" \
    --personas all \
    --sample 25 \
    --turns 5 \
    --out "$MBM_OUT"
  echo "---- trials so far: $(wc -l < "$MBM_OUT/trials.jsonl") ----"
done

# Final count — report this exact number:
wc -l "$MBM_OUT/trials.jsonl"
```

**The judge now records two NEW things on every trial automatically — you do nothing extra,
but they are the heart of what Cameron is measuring:**
- `reach` — did this realistic person *naturally* end up wanting a real human, and was that
  reach `earned`, `premature_or_pushed`, `missed_opportunity`, or `appropriately_not_yet`.
- `handoff_action` — what the smart "Talk to a real person" button decided: `MISSIONARY_LINK`
  (they were ready), `NOTIFY_ADMIN` (alert Cameron/team to talk or verify), or `NONE`.
These flow into `trials.jsonl` on their own. Just keep the trials accumulating.

Notes:
- `--sample` draws WITHOUT replacement within a single pass, so a pass never repeats a
  person; across passes you get fresh random draws (omit `--seed` so each pass differs).
- To run one specific persona by id for a targeted check, use
  `--personas some_id --persona-file "$MBM_OUT/generated_personas.json"`.
- If a run times out, lower `--turns` to 3 and keep going. A few short trials are fine; the
  point is VOLUME across MANY DIFFERENT people. If the block dies partway, just run it
  again — it appends, so you pick up where you left off until the count clears 100.
- Want even broader coverage? Raise `--sample` toward the full pool size, or add passes.

## Report ONLY what is in the file — we check, and we know when a report is wrong

This matters. The builder does **not** trust your summary — it opens `trials.jsonl` and
reads the raw data itself: it counts the lines, reads the `flags` booleans, and opens the
actual transcripts. Last time a report claimed many runs but the file held only 3 trials
(one a `--mock` placeholder). That gap was caught immediately. Do not let it happen again.

Hard rules for your hand-off report:

- **State the real count.** Run `wc -l "$MBM_OUT/trials.jsonl"` and report that exact number.
  Do not estimate, round up, or describe runs you did not actually complete.
- **Report the persona spread.** Because you now sample a big pool, also report how many
  DISTINCT personas appeared (the self-check below prints it). Broad coverage is the goal.
- **Never claim a finding you did not pull from the file.** If you mention a failure (e.g.
  "manipulation detected on a skeptic"), it must correspond to a real line where that flag
  is actually `true`. The builder will grep for it. Invented findings waste a whole cycle.
- **Never hand-edit `trials.jsonl` or any transcript.** `run_sim.py` writes every line. If
  you touch the file by hand, the builder will see it (timestamps/structure won't match) and
  the data is poisoned.
- **Do not run `--mock`.** Mock trials are placeholder rows that look real but contain no
  ministry — they pollute the pile. Only run real trials with the live key.
- **If a run failed or timed out, say so plainly.** "I got 74 trials, the rest timed out" is
  a perfectly good, honest report. A truthful 74 beats a fictional 100 every time.

Quick self-check to paste before handing back (real vs mock, distinct personas, flag tallies):

```bash
python3 - <<'PY'
import json
from collections import Counter
rows=[json.loads(l) for l in open("/home/noremacttevol/Desktop/Brain/MBM/ministry-sim/outputs/trials.jsonl") if l.strip()]
real=[r for r in rows if "[mock]" not in str(r.get("what_to_fix","")) and "[mock]" not in str((r.get("reach") or {}).get("reach_note",""))]
print("total lines      :", len(rows))
print("real trials      :", len(real))
print("mock trials      :", len(rows)-len(real), "(should be 0)")
print("distinct personas:", len({r.get("persona_id") or r.get("persona_label") for r in real}))
fc=Counter()
for r in real:
    for k,v in (r.get("flags") or {}).items():
        if v is True: fc[k]+=1
print("flags TRUE       :", dict(fc))
print("verdicts         :", Counter(r.get("faithfulness_verdict") for r in real))
print("reach quality    :", Counter((r.get("reach") or {}).get("reach_quality") for r in real))
print("handoff action   :", Counter(r.get("handoff_action") for r in real))
PY
```

## Final step — build the verified report

When the trials are in, generate the one honest report Cameron reads. This is the whole
point of the run: it tallies faithfulness, safety, the reach, and the routing, and states
plainly whether the app is "at the bar." It only claims what the data supports — it never
claims the app "converts" anyone.

```bash
cd /home/noremacttevol/Desktop/Brain/MBM/ministry-sim
python3 verify_report.py --trials "$MBM_OUT/trials.jsonl" --out "$MBM_OUT/VERIFIED-REPORT.md"
# Then read it back so you can quote the real headline numbers in your hand-off:
cat "$MBM_OUT/VERIFIED-REPORT.md"
```

## What good looks like

- `$MBM_OUT/trials.jsonl` (i.e. `ministry-sim/outputs/trials.jsonl`) has **hundreds of real
  lines** climbing toward the ~1000-person pool, the self-check shows **0 mock trials**, and
  **hundreds of distinct personas** (not ten, not dozens).
- The self-check prints real `reach quality` and `handoff action` tallies (not all empty).
- You ran `verify_report.py` and `VERIFIED-REPORT.md` exists with real numbers.
- Confirm the count is climbing with `wc -l "$MBM_OUT/trials.jsonl"` — if it isn't, you are
  writing to the wrong directory; re-check that `--out "$MBM_OUT"` was passed.
- You generated the big pool with `generate_personalities.py` and sampled from it; you did
  not fall back to the fixed ten.
- You never edited any data file by hand; `run_sim.py` wrote every line.
- You did not touch app or engine code.

## Hand back to the builder

When the trials are in, run the self-check, build the verified report, and hand back with
the **real numbers**: "X real trials in `ministry-sim/outputs/trials.jsonl` (0 mock) across
Y distinct personas. Reach: [earned/missed/pushed counts]. Handoff: [missionary_link /
notify_admin counts]. Flags: [...]. Verified report at
`ministry-sim/outputs/VERIFIED-REPORT.md` — headline faithfulness Z/5. Run
`python3 ministry-sim/learn.py --dir ministry-sim/outputs` and refine." That's the whole loop.

## The mission (so your runs serve the real goal)

MBM ministers the way Jesus did: meet each person exactly where they are, give milk before
meat, never pressure or manipulate, and keep a real human one tap away. The simulation
grades **faithfulness to that method** — not conversions. The wider and more honest the
range of people you test against, the better the app learns to meet the real human in front
of it. Keep the conversations flowing, the personas varied, and the trials accumulating; the
builder does the rest.
