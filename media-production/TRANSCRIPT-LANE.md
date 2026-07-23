# PLANNER LANE (#1) — the narration source of truth + story oversight (LANE CLAIM)

**Claimed by Machine C (`cameron-lovett-MS-7C91`), 2026-07-23.** Cameron split the work
across FOUR sessions so they stop working over each other. This is **#1, the Video
Planner.** It does NOT make audio, stills, or captions.

## The four roles (Cameron, 2026-07-23)
- **#1 Video Planner (THIS one):** check what Jesus would want; write the transcripts and
  the plan; keep the library non-duplicated and coherent; and QC everything against what
  we actually need, cross-checking the other three. Owns `TRANSCRIPTS/` exclusively.
- **#2 Audio maker:** takes the finished transcripts, sends them to ElevenLabs, makes the
  new audio. Reads `TRANSCRIPTS/*.json` as its input; `ELEVENLABS-SETUP.md` is a handoff
  scaffold FOR #2 (not owned by #1).
- **#3 Still maker:** works `COMPLAINTS.md` + the auto-scanner, fixes bad pictures to the
  agreed rules.
- **#4 Captions + organize + submit:** builds captions, organizes the videos, submits to
  the reviewer, and keeps the review board healthy.

Each lane keeps to its own FILES (#1 → `TRANSCRIPTS/` + narration text; #2 → `audio/`;
#3 → stills/PROMPTS; #4 → captions/build+publish) — that is what stops collisions. Claim
rows in QUEUE.md before any credit-burning generation, as always.

## Source of truth
Each build's `make_narration.py` SEGMENTS IS the narration source (it's what the mp4 is
built from). `TRANSCRIPTS/` is exported FROM it — a clean, read-only handoff for #2 and a
review view for Cameron. Trims/edits are made in `make_narration.py`, then `TRANSCRIPTS/`
is re-exported. #1 edits narration text only; it never touches `audio/` or stills.

## What lives here
- `TRANSCRIPTS/<NNN>-<slug>.json` — machine-readable narration for the voice session:
  `{"row", "slug", "segments":[{"id","speaker","text"}]}`. `speaker` (narrator / jesus /
  god / scripture / woman) picks the voice AND the caption colour (SPEAKER-LAW).
- `TRANSCRIPTS/<NNN>-<slug>.txt` — the same, human-readable, for Cameron.
- `TRANSCRIPTS/INDEX.md` — all 200, segment + word counts.
- `TRANSCRIPTS/DUPLICATES.md` — rows that had more than one build folder; the canonical
  one (by QUEUE story title) was exported, the stale/archived ones were not.
- `TRANSCRIPTS/TRIM-CANDIDATES.md` — Rule-4 echoes to review and trim.

## Tools
- `export_transcripts.py` — regenerate `TRANSCRIPTS/` from each build's
  `make_narration.py` SEGMENTS. One transcript per row; canonical folder chosen by the
  QUEUE story title (so an archived old build with a leftover mp4 can't win).
- `rule4_scan.py` — rebuild `TRIM-CANDIDATES.md`.

Workflow: trim the echo in the build's `make_narration.py`, then
`python3 export_transcripts.py --rows N` to refresh the handoff.

## The Rule-4 trim (STORY-INTEGRITY-LAW Rule 4)
Drop the old habit of quoting a verse in old English and then having the narrator repeat
it in modern English. `rule4_scan.py` flags the echoes; a human trims the restatement and
KEEPS any teaching the beat adds. Leave the restatement only when the old English was
genuinely hard to follow.

## No-duplicates status
The 200 is full and clean at the STORY level (2026-07-20 audit + STORY-INTEGRITY-LAW).
This session additionally found **5 duplicate build FOLDERS** (rows 65, 67, 71, 137, 140)
— old/archived builds sitting beside the current one. The canonical build was exported;
the stale folders are listed in `DUPLICATES.md` (do not delete the audit-archived ones).
