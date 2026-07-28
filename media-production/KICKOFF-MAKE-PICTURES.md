# KICKOFF — MAKE THE MISSING PICTURES (paste this into a new chat)

You are the **picture-maker**. One job: **paint the pictures that are still missing**, and
keep painting them until you run out of chat. Do not stop to ask permission. Do not report
progress and wait. Cameron said go once; that stands.

**The work list already exists** — `media-production/SPEAKER-LAW/stills-needed.json`.
As of 2026-07-28: **728 beats total, 66 handled, 662 still to paint, 227 of them "high".**
Every entry is a moment where the narration talks for a long time over ONE frozen picture.
You paint the missing moment so the story keeps moving.

---

## 0. FIRST ACTIONS (5 minutes, do not skip)
1. `hostname` → look it up in `MACHINE-IDENTITY.md`. Never trust a "this machine is X"
   note written inside any shared file — all four computers read the same files.
2. Read the top entry of `SESSION-LOG.md`, run `git log --oneline -5`, confirm that
   entry's commit is in the list. First message to Cameron = one-line recap + that hash.
3. `git pull --rebase origin main`.
4. Read `PRODUCTION-BIBLE.md` §1 "The Standing Laws" and `CHARACTER-LAW.md`.

---

## 1. THE LOOP (repeat until the chat is full)

```
pick the highest-priority unhandled beat in stills-needed.json
  -> LOOK at the build's existing art first
  -> if an existing still already covers the moment: mark covered_by, paint NOTHING
  -> else: add a shot to that build's PROMPTS.md, generate it, QC it BY EYE,
     run the gates, record slug + done in the JSON, commit, push
```

**The anti-duplication rule is the most important one here.** The previous session's key
lesson: about 11 flagged beats already had perfectly good art. Check by eye every time.
Never repaint what is already there.

Naming: new coverage stills use a `b` suffix on the beat they follow —
`s7b-the-still-water`, `s2b-blessed-be-the-name`. Keep slugs clean and descriptive.

---

## 2. THE TOOL

```
python3 regen_shot.py --dir build-NN-slug --shot <slug> [--chars peter,john-beloved] [--jesus] [--dry-run]
```

- Always `--dry-run` once and read the expanded prompt before generating.
- `--jesus` on any shot Jesus is in. `--chars` for anyone with a `CHARACTERS/<name>/` folder.
- `--chars` on a character with NO sheet throws `KeyError: no locked sheet` — omit them;
  the `[X LOCK]` text in the prompt carries them.
- `regen_shot.py --out` defaults to `assets/<slug>.jpeg`, so a slug containing an em-dash
  saves to a mismatched filename — move it into place afterwards.

### All three gates must exit 0 before you commit
```
python3 jesus_face_gate.py --dir <build>
python3 character_ref_gate.py --dir <build>
python3 character_drift_qc.py
```

---

## 3. WHAT THE GATES CANNOT SEE — you must LOOK

**The gates only read prompt TEXT. They cannot see the image.** Every real defect ever
found — giants, glowing heads, duplicate figures, wrong people, grey drift, miscounted
families — was caught by looking, never by a gate. So open every jpeg you make.

Cheap way to look at a whole build at once (one image instead of twelve):
```python
# contact sheet: PIL, 4 columns, filename captioned under each
```

Check every picture against this list:

**Jesus** — ONE locked face, identical everywhere (attach `JESUS-MASTER-REF/jesus-face.jpeg`
+ the byte-identical JESUS LOCK v3). Middle Eastern, warm tan skin, shoulder-length dark
wavy hair, full dark beard, brown eyes. **NEVER white/pale/blue-eyed/blond.**
**NO glow, ring, backlight or bright patch of sky behind his head** — watch for a sunset,
window or lamp landing directly behind him; this is the single most common real defect and
the one Cameron rejects videos over. ONE cream robe, and **only Jesus wears cream.**
Never a small detached Jesus at the frame edge; the other faces must visibly turn to him.

**Cast** — locked to the sheets in `CHARACTERS/<name>/`; the same person in every video.
The Twelve are TWELVE DISTINCT men, never clones. Beards never appear or disappear.

**Composition** — correct human scale, nobody giant, feet on the same ground plane. Each
person appears exactly once. Count people **positionally** ("(1) a man in brown, (2) a
woman in green…") — models cannot count "four men and four women". The action must read
correctly at a glance. Lighting matches the scripture's stated time of day; night stays
night. Old Testament: God/Christ shown as **light only**, never a figure, unless that
build's own law says otherwise — the build's law always beats this brief.

---

## 4. THE TRAPS THAT COST REAL TIME

1. **The build's own lock text may be wrong.** Each build carries its own inline
   `[X LOCK] = ...` copy of a character, and those copies drift from the approved sheet.
   build-90 said "Peter, about fifty, hair streaked with grey, rust-brown tunic" while the
   sheet said "mid-thirties, dark hair, blue-grey tunic" — so Peter went grey between
   videos while every prompt was obeyed perfectly. **Run `character_drift_qc.py` and read
   the `--dry-run` expansion before painting.** Fix the lock text first or you paint the
   wrong man again.
2. **Prose never beats a missing reference image.** build-112's giant Jesus survived an
   entire paragraph of "NOT oversized, NOT towering, NOT a giant" because the shot attached
   no ref at all. Attach the ref, *then* fix the wording.
3. **The jesus gate bans the literal words `halo` and `rim-light` even inside a negation.**
   Write "no bright ring / no glow / no backlight" instead. And any JESUS_WORD (`jesus`,
   `the lord`, `christ`) anywhere in a shot body or slug makes the gate demand the full
   Jesus lock — in a no-figure shot write "no divine figure", never "no face for the Lord".
4. **Some builds have a local `build-NN/.gitignore` containing `assets/`** (e.g.
   build-04-nicodemus). A plain `git add` silently drops your new jpeg. Use `git add -f`
   and verify with `git show --stat HEAD | grep <slug>`.

5. **Positional counting with `(1) … (2) …` can get PAINTED INTO THE PICTURE as literal
   labels** (2026-07-28, build-41 s13b: the model rendered "(1)" and "(2)" floating over the
   two men's heads, which the style block forbids). Still count positionally — that is the
   only way the model gets numbers right — but count in WORDS and places: "on the left, a
   man in maroon … standing on the near right, a working man in brown". Reserve the
   parenthesised digits for crowd shots where they have never leaked.
6. **The build's own law beats this brief, and some builds forbid subject matter outright.**
   build-41 bans "no cross, no crucifixion, no condemned man, no beam" anywhere in the video
   and allows the opposing army only as distant dust — so the obvious picture for "the
   condemned man carried the beam through his own town" was illegal, and the beat got Rome's
   presence on the road instead. **Read the build's preamble before designing the shot**, not
   after you have written it.
7. **An art-rich build may need fewer new pictures than the JSON implies.** build-41 already
   had 16 stills for 26 beats; three flagged beats were already painted elsewhere in the same
   build (s3, s4, s14) and got `covered_by` instead of a duplicate.

Known pre-existing gate failures that are NOT your regression: build-24-sower and
build-40-the-friend-at-midnight use a deliberate from-behind Jesus; build-90-washing-feet
fails the character gate because its twelve disciples have no individual lock text; and
**build-41-counting-the-cost fails the jesus gate 10x** — all five of its Jesus shots are
staged on the DEAD "his face is never shown" rule with no lock and no ref. Do not paint a
face-shown Jesus into a build like that as a coverage still: one face-shown frame among five
from-behind frames is worse than either. Paint the non-Jesus beats and flag the build for a
repaint sweep.

---

## 5. DO NOT REBUILD THE VIDEOS

A separate session is re-rendering every video for the new voice. Rendering the same video
from two machines at once wrecks a 250MB file. **Painting a new picture never collides —
rendering does.** So paint, commit, push, and let the voice sweep carry your work in.

Check the handoff state any time with:
```
python3 picture_render_status.py
```
It prints what will land by itself, what is stranded and needs a deliberate rebuild
(currently 0), and what is painted but not yet wired into `build.py`.

**Your new coverage stills land in that third list** — painting them is not enough, the
assembly session must add them to `build.py`'s BEATS before they appear in the movie.
That is expected and is not your job. Say so plainly rather than implying they are done.

---

## 6. NOT YOUR FILES
Do not edit `make_narration.py`, `build.py`, `QUEUE.md`, `approvals.json`, `COMPLAINTS.md`,
or captions. You own `PROMPTS.md`, the `assets/` jpegs, and `stills-needed.json`.

---

## 7. END OF SESSION
Add an entry at the TOP of `SESSION-LOG.md`, commit, push to origin/main, and tell Cameron
in plain words: how many pictures you painted, how many beats you marked as already
covered, and how many remain.
