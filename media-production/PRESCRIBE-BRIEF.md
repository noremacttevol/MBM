# PRESCRIBER BRIEF — write PRESCRIPTION.md for assigned builds

Repo root: `/home/noremacttevol/Desktop/MBM`. Work in `media-production/`.

## Read first, fully, in this order (they define the exact format + rules)
1. `STORY-BLUEPRINT-SYSTEM.md` — the charter. Especially Part 2 (impact read),
   Part 3 (beats + the **NO-CLOCK rule**), Part 4 (speakers/narrator), Part 5 (the
   PRESCRIPTION.md template).
2. `SPEAKER-LAW.md` — who speaks decides voice AND caption colour.
3. Two worked examples — copy their structure and depth EXACTLY:
   - `build-57-jairus-daughter/PRESCRIPTION.md`
   - `build-63-man-born-blind/PRESCRIPTION.md`
4. `STORY-BLUEPRINT-TABLE.md` — the tier + range for each row number.
5. `THE-200.md` — one-line impact + (for Member rows 151–200) the Gospel Library
   handoff page.

## Per build in your assigned range
- **Find the folder:** glob `build-<n>-*` and `build-0<n>-*` (zero-pad 1–9). Ignore
  anything under `archive/`. For **#89** use `build-89-the-last-supper`. For dupes
  (**44** = pentecost+two-debtors, **86** = the-wise-men+wise-men) pick the folder
  matching the table row; note which you chose.
- **If `PRESCRIPTION.md` already exists, SKIP it** — do not overwrite.
- **Read that build's `make_narration.py`** and extract the `SEGMENTS` list — each
  entry is `(id, SPEAKER, text)`. **This is the ONLY source of story content.**
- **ANTI-FABRICATION (hard repo rule):** every beat must come from something the
  actual narration text SAYS. Do NOT invent scenes, actions, or details not in the
  SEGMENTS text. If the words don't paint it, it is not a beat.
- **Impact read (Part 2):** the one thing (the point, not the plot); the turn/hinge;
  the character shown OR wound answered OR doctrine + GL page; whose face carries it
  (almost never Jesus's face in an emotional beat — the witness's face; Jesus face
  only via master ref, over-the-shoulder); what the card question falls out of.
- **Beat list = every DISTINCT visual moment the words paint,** in order, one per
  line, each tagged with the segment id(s) and the exact narration phrase it must
  agree with. **THE PICTURE COUNT IS THE BEAT COUNT — no clock, no seconds-per-still,
  no formula, no target.** A frame may hold long if the words stay on that moment;
  the only miss is when the words move to a new thing and the picture would stay
  behind. Split moments a lazy cut collapses (an action + its reaction = two beats).
- **Speaker map:** list segment ids grouped by SPEAKER exactly as tagged (NARRATOR
  white, JESUS red, GOD green, SCRIPTURE light-blue, WOMEN pink, per SPEAKER-LAW).
  For Member rows add the GL handoff line.
- **Header:** note the tier from the table. Do NOT treat the range as a target —
  write what the beats gave you; if outside the range, one line saying why.
- **Write** `build-NN-name/PRESCRIPTION.md` using the EXACT section structure of the
  two examples: header block · `## The impact read` · `## Beat list (= the picture
  plan)` · `## Speaker map` · `## The fix` (only if the current cut is starved) ·
  `## Story-change note` (only if proposing one — with the "Jesus would approve
  because ___" line) · `## Self-check before the board`.

You prescribe pictures/coverage/voices only — never rewrite the narration or audio.

## When done
Reply with a plain list: each build number → `written` / `skipped(existing)` /
`problem: <reason>`. Nothing else.
