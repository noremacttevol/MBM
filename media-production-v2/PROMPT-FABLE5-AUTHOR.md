# FABLE 5 AUTHOR SESSION — write the prompt packages for every remaining video

> **To start a session, paste exactly this into a new Fable 5 chat on a machine
> that holds the stash (Machine A `Dev` today):**
> `Read media-production-v2/PROMPT-FABLE5-AUTHOR.md and do the next rows.`

## Why this split exists (Cameron, 2026-08-05)

To keep Cameron's Claude limits low: the expensive model (Fable 5) does ALL the
judgment ONCE — beat maps, coverage, locks, plate wiring — and commits it. A
cheaper Opus runner in a separate chat (PROMPT-OPUS-RUNNER.md) then spends the
Gemini money mechanically. **ONE MACHINE (Cameron, 2026-08-05): both sessions
run on Machine A `Dev` — never tell Cameron to start another computer.** **This session spends $0 on generation. Nothing you
run may cost API credits — no v2_gen_api, no v2_story_cast without --dry-run.**

## First actions, every session (no exceptions)

1. `hostname` → look up in MACHINE-IDENTITY.md. Session-chain check per CLAUDE.md
   (top of SESSION-LOG.md, verify its commit is in `git log`).
2. Read AGENT-RULES.md "THE STANDING ORDER", V2-REBUILD-RUBRIC.md — the TWO
   META-LAWS at the top plus **ALL numbered lessons, to the very end of the list;
   the list grows and this file will not tell you where it ends** — and this
   file. `git pull --rebase origin main`.
3. Open `media-production-v2/AUTHOR-BOARD.md`. Your row is the LOWEST row whose
   State is NEEDS-BEATS or AUTHORED and whose Claim and Ready are empty.
   **Claim-by-push before any work**: write `AUTHOR <machine> <date>` in Claim,
   commit, push. Push rejected = someone beat you; pull and take the next.

## The job, per row

**NEEDS-BEATS rows:** author `beats_v2.py` from scratch.
**AUTHORED rows:** they may predate the newest lessons — upgrade them: re-cover
the story to the movie-coverage law, wire plates, gate any lesson added since
they were written, and fix anything the checklist flags.
Do not casually rewrite scene text that already satisfies the laws.

Per row, in order:

1. **Study first.** `python3 media-production-v2/v2_outline.py <row>` (prior
   complaints shown on top — an open one MUST be addressed by your beat map).
   Read the full KJV passage in context. Get the segment truth with
   `extract_beats` from the V1 build (v2_prep_row.py has already copied audio +
   scripts for most rows; run `python3 media-production-v2/v2_prep_row.py <row>`
   if the build folder is missing).
2. **Coverage plan (lesson 12).** Every spoken segment gets its own picture(s),
   ~3.5–5.5 s each. Every physical VERB in the narration gets a frame; an action
   sequence gets a frame per action so it reads as motion (the John 21 standard:
   "It is the Lord" on the sayer → Peter binding his coat and going over the
   gunwale → Peter swimming for shore — three frames, never one). Ask of every
   frame: which single moment is this, and whose moment is it?
3. **Movie framing (lesson 12).** Only the people the moment is about are in
   frame — singles, over-shoulder two-shots, inserts of hands/objects. Establish
   a location wide AT MOST once; everything else is coverage. Every wide beat
   states camera position and where each visible gaze/travel exits the frame
   (row-14 law — the checklist warns on this).
4. **Copy the good pictures (lesson 11 — Cameron's core order).** Before writing
   ANY setting description: `python3 media-production-v2/v2_stash.py --wire
   <build>` (run `--scan` first if the index is stale). Resolve every SUGGESTED
   token with `--take`; for NEW places, note in QC.md which beat's first good
   frame the runner must `--promote` before generating the rest of that place.
   A plated place needs NO prose architecture — scene text describes ACTION and
   LIGHT only. Then `git add -f <build>/PLACE-REF/*.jpeg` — plates are small by
   design and MUST be committed so the runner's machine has them.
5. **Locks.** Persons: build-local LOCKS with byte-identical descriptions; the
   global cast auto-attaches by token (PETER, JOHN…, and the women MARTHA,
   MARY-BETHANY, MARY-MOTHER, MARY-MAGDALENE). **The three Marys:** never lock a
   bare `MARY` for the global cast — "MARY" means three different women (Mary of
   Bethany, Mary the mother, Mary Magdalene). Lock the DISAMBIGUATED token so the
   right face attaches: `MARY-BETHANY` (Lazarus' sister — sheet ready),
   `MARY-MOTHER` / `MARY-MAGDALENE` (sheets pending a v2 render — until then the
   runner prints a TEXT-ONLY warning; wire a build-local `REFS` for that woman).
   Settings: name the shared tokens (TEMPLE-COURT, NIGHT-LAMPLIGHT,
   BACKGROUND-CAST, PERIOD families…).
   Jesus: `jesus: True` + `ref: True` on every beat he appears in; only he wears
   cream; red-letter segments sit on whoever actually speaks (the row-39 lesson:
   a quoted prayer belongs on the man praying, not on Jesus's face).
6. **Gates, then hand off.** `python3 media-production-v2/v2_prompt.py <build>
   --check` must PASS (fix every FAIL; take every WARN seriously) and `--dump`.
   Windows: contiguous, zero gaps, every speech onset inside its own window.
   Confirm the row's Audio column says OK on AUTHOR-BOARD (it is the
   audio-audit gate; if CHECK, mark the row NEEDS-AUDIO in your log and do NOT
   set Ready). Then set **Ready ✅** on AUTHOR-BOARD, clear your Claim, commit
   the whole row package (beats_v2.py, PLACE-WIRING.json, plates force-added,
   board), push.

## Session pacing and chain-out

Do rows until context runs genuinely low (typically 2–4 rows), then: SESSION-LOG
entry at the top (rows finished, decisions made, anything a next author must
know), commit, push. Never end a session with an unclaimed half-authored row —
either finish it or revert the claim.

## When your author work on a NEEDS-REBUILD row is DONE (don't strand it)

A NEEDS-REBUILD row routes ONLY to this author lane. Once you've done the author
part (scene-text/lock edits, beat removal, re-voice flag) and the ONLY thing left
is a **paid targeted re-cut** (`--only <frame>` reroll or a $0 re-assemble), you
MUST flip its board **State → BUILT** (keep the open complaint, do NOT write a
literal `C-FIX <date>` marker in the Claim). That is the state the paid **cfix**
lane picks up for exactly these targeted re-cuts. Leaving it NEEDS-REBUILD strands
it forever — every author session re-selects it, finds no author work, and moves
on, so Cameron's complaint never closes (STANDING-ORDER violation). Rows 13/15/16/
19/33/61/73 sat stranded this way until 2026-08-07. If instead only AUDIO work
remains, flip State → NEEDS-AUDIO (no `AUDIO-FIX` text in Claim) so the audio lane
takes it. (Picker fixes shipped 2026-08-07: hash regex widened to `{40,64}` for
SHA256 review cards; cfix skip-check tightened to `C-FIX \d{4}-\d\d-\d\d` so prose
mentioning "prior C-FIX" no longer hides a genuine open complaint from cfix.)

## Never

- Spend a Gemini credit, generate a portrait, or assemble a video (runner's job).
- Write a new 400-word prose lock for a place that has a plate.
- Put the whole cast in a frame because they exist in the story.
- Mark Ready on a row whose --check does not PASS or whose audio is not OK.
- End the session tooling-only or hand homework to Cameron (STANDING ORDER).
