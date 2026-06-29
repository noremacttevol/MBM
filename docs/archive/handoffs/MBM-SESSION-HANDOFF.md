# MBM — Session Handoff (Design-tab conversation, 2026-06-13)

> Reconstructed from the full design-tab transcript
> (`work-logs/anthropic design work 6-13.txt`) so Claude Code can pick up cold
> without re-litigating anything. This is the decision record of a long
> conversation between Cameron and a design-tab agent about the scoring /
> profile system. Where the conversation reached a settled answer, it is marked
> **DECIDED**. Where Cameron stated his own position firmly, it is recorded as
> **CAMERON'S CALL** — his app, his theology, his decision.

---

## 1. The core design: two tracks that never bleed into each other

The profile is built from **two separate tracks**. The whole point of the
design is that belief lives in the belief column and character lives in the
character column — they are measured and shown separately, and one never
silently becomes the other.

### Track 1 — Faith background (what the person believes)
A descriptive, transparent ladder that names everyone respectfully and counts
no one out:

`atheist → agnostic → other faith (Hindu, Muslim, etc.) → Jesus-believer
(churched or not) → investigator (friend of the restored gospel) → member →
meat (deeper discipleship)`

- This is the **only** place where "agrees with / progresses in the restored
  gospel" belongs, because here it is an honest *description of belief*, not a
  verdict on a person's worth.
- It is shown and explained to the user. Status climbs on **real, self-reported
  steps** (e.g. "I talked to the missionaries," "I was baptized"). The app keeps
  in touch with someone before it ever calls them a faithful member.

### Track 2 — Christlike character / celestial striving (how the person engages)
The seven character virtues already defined in `minister.ts`:
**honesty, humility, courage, compassion, hunger, openness, sincerity.**

- Read from how the person actually engages — sit-with-the-grieving, forgive a
  debt, ask honest questions, change their mind.
- For **members**, this becomes the "celestial 10/10" discipleship tool: it
  questions a member and reflects how close their actual thinking is to a
  Christlike, celestial ideal they can strive to perfect. This is a real,
  motivating discipleship feature and is to be built well.

---

## 2. The agreement / alignment meter — the heart of the long argument

Cameron wants a meter that measures **agreement with God as the restored gospel
describes Him** — "a Perfectly Loving and Just God: a Being of absolute truth
and boundless mercy, who possesses total power and complete knowledge of all
things, and whose ultimate purpose is the eternal happiness and salvation of His
children."

Two ways the meter could work were named explicitly:

- **(A)** Raise the score for agreement with that *description of God* — a devout
  Muslim or Catholic who wholeheartedly agrees would score high.
- **(B)** Raise the score for agreement with the **restored gospel
  specifically** — Book of Mormon, living prophets, becoming like God. The same
  person scores lower, because this is the part distinctive to the faith.

**DECIDED: (B).** Cameron chose B deliberately. His reasoning: creation *ex
nihilo* (out of nothing) makes God ultimately responsible for the conditions
that send people to hell, which is not good; only the restored gospel allows for
a truly good God (see `CREATION-DILEMMA.md`). So on this scale, a person who does
not hold that view does not score at the top — and because the meter is
**honestly labeled as agreement with the restored gospel's God**, a non-believer
scoring low is simply *true*, not an insult.

---

## 3. The one settled boundary on labeling (the rename that turns "no" into "yes")

The entire argument in the transcript came down to **one** thing: a number must
not assert something false about a real person under a bare, universal word.

- The design agent's refusal was narrow and specific: it would not wire a
  per-person number, shown to that person, that caps the **plain words**
  "honesty / compassion / courage" by whether they accept the theology — because
  to a reader, the bare word "compassion: 4" reads as "this app thinks I'm not
  very compassionate," which may be false about who they actually are. This app
  is built for the lonely and the grieving, and that is where false-feeling
  verdicts do harm.
- The resolution both sides converged on: **name the capped dimensions for what
  they actually measure.** Not "Compassion" but **"Christlike compassion as the
  restored gospel measures it"** (or Cameron's own words). Then the label and the
  number agree, a non-believer scoring low is honestly true, and no one is told a
  bare English word names a deficiency in them. With that naming, the full scale
  — caps and all — is buildable.

**DECIDED design principle:** every capped dimension is labeled as a *Christlike
/ restored-gospel* measure, so the label always matches what the meter rewards.

**CAMERON'S CALL (record faithfully):** on this app, a person who is not saved
and believing in the restored gospel does not score above **7/10** on the proof
dimensions; someone unwilling to even examine the restored gospel tops out around
**5/10** (he reads that as a lack of courage). Members who showcase their faith
against what a truly good God (as the restored gospel defines Him) would approve
can be rewarded fully. This is his theology and his decision; the honest-labeling
principle above is the agreed way to express it so the numbers never lie.

---

## 4. The invitation flow (open, named, explained)

- The app may openly affirm some openness ("maybe God still speaks through
  prophets," "maybe we're meant to become like Him") and then extend a clear,
  **named** invitation to read the Book of Mormon.
- **Accepting the invitation advances the person's Track-1 faith-background
  status** (→ investigator / friend of the restored gospel), and the change is
  **explained to them in the reply**. This is where accepting the invitation
  honestly "counts."
- Accepting/declining the Book of Mormon does **not** move the seven character
  virtues — that was the line. (Cameron's own framing is recorded above; the
  honest-labeling rule is how both intents are satisfied at once.)
- The milk-before-meat law still governs *timing*: no LDS reference / BoM /
  missionary link until the two readiness signals are present (believes God is
  fundamentally good; open to God still speaking / continuing revelation). See
  `CLAUDE.md` / `AGENT-RULES.md`.
- Instructions / how the scoring works are revealable on request.

---

## 5. Build queue (what to actually do, with the files to touch)

1. **Pull the owner-view panel** out of the user-facing profile.
2. **Build the Track-1 faith-background ladder** (atheist → … → investigator →
   member → meat) as an honest, shown, explained status. Touches the Zustand
   store `mobile/src/store/useAppStore.ts` (status field + transitions) and
   `mobile/src/screens/ProfileScreen.tsx`.
3. **Build the Track-2 Christlike-virtues scale** beside it — the seven virtues
   from `mobile/src/engine/minister.ts`, each dimension **named as a Christlike /
   restored-gospel measure** per §3, with caps per Cameron's call. Keep the
   read-of-character logic and labels honest to what they measure.
4. **Agreement / alignment meter (Track B)** — labeled "alignment with the
   restored gospel's God" (or Cameron's words), capped by theology, sitting
   beside the ladder.
5. **Member discipleship "celestial 10/10" tool** — questions a member and
   reflects how Christlike their thinking is against the celestial ideal.
6. **Wire the Creation-Dilemma reasoning** into the minister so it can make its
   own case well (see `CREATION-DILEMMA.md`). Keep `minister.py` and
   `minister.ts` byte-in-sync per existing project discipline.
7. Keep `connect.ts` / `connect.py` (journey + human ladder) and the
   invisible-routing rules intact; the human is never gated.

---

## 6. The one line not to cross

Never show a belief-capped number under a **bare universal virtue word**
("Compassion: 4") as the app's honest read of a person. Always name the capped
dimension for what it measures ("Christlike compassion as the restored gospel
measures it"), so the number never asserts something false about a vulnerable
person to their face. This is the single resolution that lets the entire scale —
caps included — be built honestly. It protects the lonely and grieving people the
app exists for, and it gives Cameron exactly the reward structure he asked for.

---

## 7. Status of the build

Nothing from this conversation was coded — the design tab could not write files.
This document plus `CREATION-DILEMMA.md` are the spec. The next agent (Claude
Code) should build items 1–7 above, verify with the existing harness
(`ministry-sim/`) and `tsc`, and keep `minister.py`/`minister.ts` in sync.
