# PROTOCOL v4 — two Linux machines, minimum tokens, zero-error target (2026-07-15)

Supersedes the v3 machine table. Windows machines are RETIRED from building
(audio/font defects); they may only write DRAFTS or AUDITS, never assemble.

## Machines
| Machine | Rows |
|---|---|
| **L1** (Linux #1) | 1–100 (redo triage first, then new builds) |
| **L2** (Linux #2) | 101–200 (same order) |
Claim rules, triage buckets, laws: unchanged — FACTORY-ORDERS.md still governs.

## The v4 session shape — a video in ~10 model turns
1. ONE compound command: pull → claim row → push.
2. If media-production/DRAFTS/row-NNN.md exists (outside-agent draft): VALIDATE it
   against the laws (KJV exact, Translation Law, homograph list, care flags,
   number-stress) and adapt into make_narration.py + PROMPTS.md. If no draft:
   write them from the templates. Never compose from scratch what a draft supplies.
3. Face gate → generate stills via the playbook JS method ONLY (JS submit, JS
   download). ZERO screenshots for navigation. Batch: submit next prompt while the
   previous image renders. After ~20 generations in an hour, slow to 1 per 2 min
   (CAPTCHA ceiling, measured).
4. QC stills with Read on the saved jpegs, 3–4 per turn, against the QC list.
5. build.py (silence map, size cap, loudness are in-script — trust the script).
6. ONE compound command: queue tick → TITLES → gen_site_index.py → add/commit/pull
   --rebase/push.
7. Max 4 videos, then audit (AUDITS/README.md format) + "SESSION DONE".

## Outside-agent lane (Hermes or any helper AI) — the DRAFTS spec
Helpers do the token-heavy WRITING; Claude sessions validate and build.
A draft is one file: media-production/DRAFTS/row-NNN.md containing:
  1) NARRATION: numbered segments exactly like a make_narration.py SEGMENTS list —
     narrator lines in plain modern English (never quoting KJV), Jesus lines EXACT
     KJV only, a closing-card line that is an invitation (never fear).
  2) STORYBOARD: 8–16 beats, one line each — what the still shows, time of day,
     who is in frame. Note the two sacred-silence beats.
  3) Must state the row number, story, scripture reference.
Helpers NEVER touch git, QUEUE.md, or generate images. Cameron (or any Claude
session) drops the file into DRAFTS/ and the building machine takes it from there.
Claude validates EVERYTHING — a draft is raw material, not law.

## Standing token rules (from today's trials)
- Screenshots for navigation = the single biggest waster. Banned.
- Browser: 2 attempts then fall back (extension → driver → browserless work).
- The repo is the memory. Never re-read what the playbook summarizes.
- Narration/QC text stays terse; no progress narration between steps.

## STILLS-RUNNER role (Windows W1) — pictures only, added 2026-07-15

Windows is retired from ASSEMBLY (audio/font defects) but is safe for IMAGE
generation. W1 runs a dedicated stills-only session so the Linux/Fable sessions
never wait on Flow's render clock.

The relay, via a marker file:
1. A prep machine (L1/L2) that has written a gate-passing PROMPTS.md but not yet
   generated art creates an empty file `STILLS-WANTED` in that build folder,
   commits, pushes, and moves on to its next row's prep or assembly.
2. W1 loops: `git pull --rebase` → find `media-production/build-*/STILLS-WANTED` →
   for each: re-run jesus_face_gate.py (must exit 0), generate every still per the
   playbook (JS submit + JS download, master-ref attached on every Jesus shot,
   CAPTCHA cadence: after ~20 generations slow to 1 per 2 min), save to that
   folder's assets/, delete the STILLS-WANTED marker, commit, push. Repeat.
3. L1/L2 loop the other side: any build folder with full assets/ and no marker is
   ready — QC the stills, build, publish.
W1 does ONLY this. No narration, no build.py, no ffmpeg, no queue ticks beyond a
note in the Claim column ("stills by W1 <date>"). Same session hygiene: audit +
fresh chat every ~4 folders. If Flow logs out or CAPTCHAs, say ONE line and wait.
