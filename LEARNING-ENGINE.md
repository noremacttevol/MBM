# The Learning Engine — the app's brain (and how it differs from the tester)

Plain-language design note. Reads on top of `KNOWING-ENGINE.md` and `APP-FLOW-SPEC.md`.

---

## Two machines, kept separate

There are two different systems in this project. They are easy to confuse because both
involve AI and conversation, but they do opposite jobs and must never be merged.

**1. The tester — `ministry-sim/`.** A practice room. It invents people of every common
background, has them answer the app's questions the way real people of that kind would, and
grades how the app ministered. It never ships to anyone. Its only job is to throw realistic
data at the app's brain so the brain gets sharp and trustworthy before a single real person
opens the app.

**2. The app's brain — `knowing_engine.py`.** The thing that actually goes out to real people.
This is the part that *learns each person*. It builds a living picture of the individual from
what they say, decides how to meet them next, and keeps that picture growing across the whole
conversation. The old `router.py` did not do this — it sorted people up a fixed ladder. The
learning engine replaces that with genuine attention to the unique person.

The relationship in one line: **the tester generates the data; the app's brain learns from it.**

---

## What the app's brain learns

Two layers of learning, both pointed at the same target.

### Layer 1 — learning the one person in front of it (the important one)
No two people answer the same question the same way, so the engine never assumes. With every
message it reads signals and updates a profile of *this* person:

- their emotional state right now (grief, anger, curiosity, warmth, indifference);
- the picture of God they inherited — and whether it's the real obstacle (a God who damns,
  pre-rejects, or is cruel);
- what they're actually reaching for under what they said;
- which door fits them: presence, a gentle question, honest evidence, open exploration;
- the two readiness signals — do they believe God is good, and are they open to God still
  speaking — which together (and only together) unlock anything LDS-specific;
- their own language and frame, so the app speaks in their words, not its own.

From that profile it recommends the next move: what to do, what *not* to do, and whether
milk-before-meat allows any restored-gospel reference yet. This is the knowing engine made
literal — the app meeting each person as the specific person they are.

### Layer 2 — learning across many people (accumulated pastoral wisdom)
As real (and simulated) conversations finish, the engine records what *kind* of move helped a
*kind* of situation, and what lost people. Over time it builds evidence: "people arriving in
fresh grief open up when met with presence and shut down when handed doctrine." Future
recommendations lean on that evidence. With little data it leans on the rules above; as data
grows, the evidence sharpens the choices. This is the "learns from data" part — honest and
transparent, so you can always see *why* it chose a move, and ready to grow into real
statistical learning once enough real conversations exist.

---

## The target it optimizes — this is everything

A learning machine becomes whatever you point it at. If the reward were "conversions," it
would discover pressure and manipulation, because those move that number in the short run.
That would build the opposite of Jesus.

So the target is **faithful ministry**, defined exactly as the simulator's judge defines it:
did it meet the person where they were, stay honest, ask more than it told, use the comparison
method instead of arguing, apply zero pressure, withhold LDS content until both readiness
signals were truly present, and leave the person free? A person freely coming toward truth is
the *fruit* of faithful ministry — never the number we optimize. A person who is met well and
chooses to walk away is not a failure the engine tries to eliminate; it is the rich young ruler,
and we honor it.

Concretely, the "good outcome" the across-people layer rewards is **faithful + the person
freely more open**, never raw conversion. Pressure and dishonesty are hard constraints the
learning can never trade away for a better number.

---

## How the two connect (the loop that makes it better)

1. The tester runs the app's brain against all the personas.
2. The judge grades faithfulness and reports what worked and what lost people.
3. Those results feed the across-people evidence layer and show you where the brain's reading
   or moves are wrong.
4. You (and I) adjust the engine, re-run, and watch the grade climb.
5. Only a brain that ministers faithfully across the whole range of people goes out to real
   ones — where you, in Phase 1, stay in the loop on every human handoff.

The tester earns the trust. The brain does the ministry. Real people meet a brain that has
already learned to love many kinds of them well — and a real human is always one tap away.
