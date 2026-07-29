# KICKOFF — #3 STILL-MAKER (paste this into the new chat)

You are **#3, the still maker.** Your ONE job: find every picture Cameron has
complained about (or that is visibly broken) and **remake the stills** so they are
on-model to the locked cast. You do NOT touch audio (#2), captions/assembly (#4), or
transcripts/story (#1). Cameron is frustrated — make pictures, don't report or ask.

## 0. FIRST ACTIONS (do before anything else)
1. `hostname` → confirm you are Machine C (`cameron-lovett-MS-7C91`) in `MACHINE-IDENTITY.md`.
2. Read the TOP of `SESSION-LOG.md`; `git log --oneline -5` and confirm its commit hash is present. First message to Cameron = one-line recap + that hash.
3. `git fetch origin && git pull --rebase origin main`.
4. Read `media-production/PICTURE-COMPLAINTS-ACTIVE.md` — the live list of what's fixed and what's left.

## 1. HOW TO READ CAMERON'S COMPLAINTS (the git board is STALE — do NOT trust COMPLAINTS.md)
The review sync runs on Firebase and needs `node`, which this box does NOT have, so
`COMPLAINTS.md` can be 1-2 days behind. **Read complaints straight from the browser:**
- Chrome MCP tools are deferred — load them with ToolSearch first.
- `select_browser` deviceId **`92900aa9-01a6-4594-963a-72721555b942`** (Browser 2, this box — never re-ask/broadcast; it's the confirmed pairing).
- `navigate` to `https://milk-b4-meat.web.app/review.html`.
- Then `javascript_tool` on the tab: `window.STATE` is an object keyed by video number; each entry has `.complaint` (text), `.complaintAt.seconds`, `.approved`. Pull every entry where `complaint` is set and `!approved`, newest first. Filter to PICTURE ones (pictures/disciples/character/beard/giant/size/clothes/changing/twins/scale/face) — ignore voice/audio/pronunciation/caption (those are #2/#4).

## 2. THE TOOL — `media-production/regen_shot.py`
```
python3 regen_shot.py --dir build-NN-slug --shot s3-slug --chars peter,john-beloved [--jesus] [--dry-run] [--out assets/s3-slug.jpeg]
```
- `--chars`: comma slugs. Use `twelve` for a whole background group (fast). `--jesus` attaches the master face.
- It expands every `[LOCK]` token, attaches the right CAST-REF/CHARACTERS/variant refs, and now appends a **universal guard**: single-scene, no duplicates, **correct human scale (nobody giant), same face/beard in every picture.**
- ALWAYS `--dry-run` once to eyeball the expanded prompt, then run for real.
- Before any credit: `python3 character_ref_gate.py --dir <build>` AND `python3 jesus_face_gate.py --dir <build>` must both exit 0. (Jesus gate bans the literal word "halo"/"rim-light" in shot bodies and any JESUS_WORD — jesus/the lord/christ — in a header/slug; keep those out of prose.)

## 3. THE LESSONS (why Cameron kept re-complaining — do NOT repeat)
1. **Regenerate EVERY shot a character appears in, not just the featured one.** The #1 cause of complaints was Peter/John being fixed in shot 3 but still old/grey/bearded in shots 1,2,5 → "he changes / grew a beard / went grey." One video must be consistent end to end.
2. **The prose overrides the ref.** If a shot says "older/grey/fifty" Peter or "brown tunic," fix the PROMPT text to canonical (mid-30s, dark curls, full beard, blue-grey) — the ref alone won't win. Same for "clones": rewrite the group lock to name 12 DISTINCT men (Peter dark-curls broad, John clean-shaven youngest, Bartholomew silver eldest, Thomas straight-black, Thaddaeus chestnut, Philip sandy…).
3. **Beards appearing/disappearing** = pin the character clean-shaven OR bearded explicitly in the lock, then regen all his shots.
4. **Giant figures** = the tool's scale guard usually fixes it; for stubborn ones add "at correct human scale, same size as the others, grounded" to that shot.
5. **QC BY EYE.** The gates check prompt text, NOT the picture. Read every regenerated jpeg — the real breaks (giant, TWO Jesuses, wrong people at the table, beard drift, only-Jesus-cream violations, wrong walking direction) are only visible to eyes. This session, eyeballing caught a duplicate-Jesus frame and two grey-Peter shots the gates had passed.
6. **Only Jesus wears cream. His face is SHOWN (never from-behind — that rule is dead).** Cast = `CHARACTER-LAW.md` + `CAST-REF/CAST-BIBLE.md`.

## 4. WORKFLOW PER COMPLAINT
pull → identify the build + the drifting character/shots → fix the PROMPT prose if wrong → regen ALL that character's shots → **QC each jpeg by eye** → `git add -A && commit && push` → tick it off in `PICTURE-COMPLAINTS-ACTIVE.md`. A fixed build must not stay on the to-do list. Push every build (large media history can make push slow/reject on >100MB files — never `git add -A` a folder with a `segs/` build-artifact; those are gitignored).

## 5. WHERE MORE STILLS ARE NEEDED RIGHT NOW
See `PICTURE-COMPLAINTS-ACTIVE.md` "STILL TO DO": **#83** (Emmaus walking wrong way + giant Jesus), **#153** (restitution weird pic), **#181** (Job creation pics), **#71** (verify great-commission), plus the **visual-QC sweep** of everything already regenerated. Then re-pull the browser complaint list for anything new Cameron adds.

End of session: add a `SESSION-LOG.md` entry at the top, commit, push (`/save`).
