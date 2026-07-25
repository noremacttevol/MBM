# KICKOFF — COVERAGE STILLS (the #3 art session's long job)

Paint the **missing-beat stills** the narration session catalogued in
`SPEAKER-LAW/stills-needed.json` (728 entries). The law is `STORY-COVERAGE-LAW.md`
+ `STILLS-NEEDED.md`: one picture per story beat; the picture must show the moment
the words are saying, at the moment they say it. This is a marathon — do it a few
builds per chat to keep context low (Cameron's one-chat-per-video law).

## STATUS (2026-07-24, Machine C) — updated live
- **31 new coverage stills painted + pushed; 12 beats marked covered_by an existing still.**
  43 of 728 resolved. ~48 "high"+wants entries remain unresolved (working worst-held first).
- `done`/`slug`/`covered_by` in `SPEAKER-LAW/stills-needed.json` is the source of truth — the
  marathon resumes from there. Painted builds so far include 120-Job, 118-Jonah, 148-Ruth,
  65, 117, 70, 05, 161, 66, 149, 164, 158, 21, 11, 150, 101, 24, 111, 40, 74, 04, 135.

## THE WORKFLOW (per entry)
1. Pick the highest `seconds_on_screen` `high`-priority entry with a `wants` brief that isn't `done`.
2. Open that build's assets and **look at the existing still for that beat BY EYE**. If the
   existing art already shows what the brief asks → mark the entry `done:true` +
   `covered_by:"<existing-slug>"` and move on. **Do NOT repaint duplicates** — this is the #1 trap
   (build-10, 118, 117, 70, 03 all had beats already covered).
3. If a genuinely-new image is needed: add a `## <slug>` shot to the build's `PROMPTS.md`
   (an ALLOWED file). Compose from `[STILL STYLE BLOCK]` + the build's `[X LOCK]` tokens +
   the `wants` brief + the verse in full context. Jesus shots need the byte-identical JESUS
   LOCK v3 paragraph + a `REF: jesus-master-ref` line (copy from an existing shot in that file).
4. Generate: `python3 regen_shot.py --dir <build> --shot <slug> [--chars a,b] [--jesus]`.
   - `--chars` ONLY for characters with a `CHARACTERS/<name>/` sheet. Text-lock-only characters
     (e.g. build-65 "father", build-70 none) have NO sheet — omit them, the `[X LOCK]` token
     carries them. Passing a sheet-less name throws `KeyError: no locked sheet`.
   - `--jesus` attaches the master face for any shot Jesus appears in.
5. **QC the jpeg by eye** against the verse and the laws (Jesus on master face, NO halo/glow
   behind his head, only Jesus in cream, scale, anti-panel, OT God = light only).
6. Gate: `character_ref_gate.py` AND `jesus_face_gate.py` must exit 0.
7. Record `slug` + `done:true` on the entry in `stills-needed.json`.
8. `git add` PROMPTS.md + the new asset(s) + the JSON; commit; pull --rebase; push. One commit per build.

## GOTCHAS
- The jesus gate bans the literal words `halo`/`rim-light` in prose AND any JESUS_WORD
  (`jesus`/`the lord`/`christ`) in a header/slug. Keep slugs clean: use `s2b-blessed-be-the-name`,
  NOT `s2b-the-lord-gave`. Say "no bright ring / glow / backlight," never "no halo."
- `regen_shot --out` defaults to `assets/<--shot value>.jpeg`. Pass a clean slug as `--shot`.
- Do NOT edit `build.py` (assembly session wires the new slug into BEATS), `make_narration.py`,
  `QUEUE.md`, `approvals.json`, or `COMPLAINTS.md`.
- **DEFER for Cameron:** theophany / Christ-figure OT builds — `build-119-fourth-man-in-fire`
  (Dan 3:25 "like the Son of God"), `build-105-face-to-face` (Ex 33). Whether to depict a
  Christ-figure there is his call, not a guess.
- Retired builds (archived): `build-44-two-debtors`, `build-128-famine-of-hearing` — skip.

## FLAG (2026-07-24): a CATEGORY of builds has PRE-EXISTING jesus-gate failures (from-behind Jesus)
Some older builds deliberately show the Lord ONLY from behind / face-never-shown (an older style,
pre-dating the face-shown v3 law), so their Jesus shots lack the byte-identical JESUS LOCK v3 +
`REF: jesus-master-ref` line BY DESIGN and `jesus_face_gate.py` exits 1 for the whole build.
Confirmed so far: **build-24-sower** (s1, s7) and **build-40-the-friend-at-midnight** (s1, s2, s12, s15);
build-24 also has the literal word "halo" in a "No halo, no glow" line (the gate bans the substring
even inside a negation).
- This is NOT caused by coverage stills — a new NON-Jesus still (hands, grain, a stone, a landscape)
  added to such a build is clean and adds none of these failures. Verify your new shot isn't in the
  FAIL list, record it, commit, and move on.
- Converting these to the face-shown v3 standard (or rewording "halo") is a BUILD-OWNER decision, not
  a coverage-pass change — forcing the "face shown" lock would contradict the intentional from-behind design.

## GOTCHA: some builds have a LOCAL `assets/` .gitignore — use `git add -f` for the new jpeg
A few builds (e.g. build-04-nicodemus) carry a `build-NN/.gitignore` containing `assets/`. The
existing stills are tracked (force-added long ago), but a NEW jpeg is silently skipped by a plain
`git add` (you'll see "paths are ignored by .gitignore"). Fix: `git add -f build-NN/assets/<slug>.jpeg`.
Always verify the asset actually committed (`git show --stat HEAD | grep <slug>`), not just the JSON/PROMPTS.
