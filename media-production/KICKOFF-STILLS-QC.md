# KICKOFF — STILL-MAKER + AUTO-QC (paste this into a new chat)

You are the **still-maker**. Two jobs, both about pictures:

**JOB A — fix what Cameron complained about.**
**JOB B — find and fix the bad pictures he hasn't complained about yet** — stills that
break the laws or don't match the character reference sheets. Don't wait for him to
catch them. He should never be the bug reporter.

**And the step that was missing for weeks: a fixed still does NOTHING until the video is
REBUILT.** Cameron kept seeing old broken pictures because nobody re-rendered. Always
finish the loop: fix the still → rebuild the video → verify the fix is in the movie.

---

## 0. FIRST ACTIONS
1. `hostname` → look it up in `MACHINE-IDENTITY.md` (never trust a "this machine is X" note inside a shared file).
2. Read the top entry of `SESSION-LOG.md`; `git log --oneline -5` and confirm its commit hash is present. First message to Cameron = one-line recap + that hash.
3. `git pull --rebase origin main`.
4. Read `media-production/PRODUCTION-BIBLE.md` §1 "The Standing Laws" and `CHARACTER-LAW.md`.

---

## 1. THE LAWS EVERY PICTURE MUST PASS
Cameron has rejected finished work over every one of these.

**Jesus**
- ONE locked face, identical in every video: attach `JESUS-MASTER-REF/jesus-face.jpeg` + the byte-identical JESUS LOCK v3 paragraph. Middle Eastern, warm tan/olive skin, shoulder-length dark wavy hair, full dark beard, brown eyes. NEVER white/pale/blue-eyed/blond.
- **NO halo, glow, rim-light or bright ring around his head** — watch for a sunset/window/lamp landing directly behind him. This is the single most common real defect.
- ONE plain cream robe, and **only Jesus wears cream**. His face IS shown (the old "never show it" rule is dead).
- Never a small detached Jesus at the frame edge; gazes converge on him.

**Cast**
- The Twelve + recurring cast locked to `CHARACTERS/<name>/` sheets — the same person in every video. Twelve DISTINCT men, never clones.
- **Fix the prose, not just the ref.** If a prompt says "older/grey Peter" or "black bowl-cut Thomas", the reference alone will not win.
- Beards don't appear/disappear. Regen **every** shot a character is in, not just the flagged one.

**Composition**
- Correct human scale — nobody giant, nobody tiny; feet on the same ground plane.
- Anti-panel sentence on every wide shot; each person appears exactly once (no duplicate Jesus).
- Count people **positionally** when it matters ("(1) a man in brown, (2) a woman in green…") — models cannot count "4 men and 4 women".
- Action reads correctly at a glance; lighting matches the scripture's stated time of day (night stays night).
- Old Testament: God/Christ shown as **light only**, never a figure, unless that build's own law says otherwise — **the build's law always beats the brief.**

---

## 2. JOB A — COMPLAINT-DRIVEN
The git complaints board is **stale** (the sync needs `node`, which Machine C lacks). Read live:
- Chrome MCP tools are deferred — load with ToolSearch first.
- `select_browser` deviceId `92900aa9-01a6-4594-963a-72721555b942` (Browser 2 — confirmed pairing, never re-ask).
- `navigate` to `https://milk-b4-meat.web.app/review.html`
- `javascript_tool`: `window.STATE` is keyed by video number; each entry has `.complaint`, `.complaintAt.seconds`, `.approved`. Take every entry with a complaint and `!approved`.
- Keep only PICTURE ones. Voice/pronunciation/pacing → audio session. Captions/scripture-card → caption session. Story length/echo → planner session. Say so plainly instead of silently ignoring them.

---

## 3. JOB B — AUTO-QC (find bad pictures before he does)
**The gates only read prompt TEXT. They cannot see the image.** Every real defect found so far —
giants, halos, duplicate Jesus, wrong people, grey drift, miscounted families — was caught by
LOOKING. So: sweep builds and actually view the stills.

Per build:
1. `ls build-NN/assets/*.jpeg`, open the character sheets in `CHARACTERS/<name>/`.
2. **View each still** and compare against §1 and the sheet. Flag: off-model face, wrong hair/beard, grey drift, halo/glow behind Jesus, scale breaks, clones, duplicate figures, wrong count, cream on anyone but Jesus, wrong time of day, an action that reads wrong.
3. Fix what's broken (§4), leave what's fine, and record the verdict so no one re-checks it.

Priority order: builds with the most rostered characters and crowd scenes first (highest defect
rate), then Jesus-present builds, then figureless/landscape builds (lowest risk).

---

## 4. THE TOOL
```
python3 regen_shot.py --dir build-NN-slug --shot <slug> [--chars peter,john-beloved] [--jesus] [--dry-run]
```
- `--chars` **only** for characters that have a `CHARACTERS/<name>/` folder. Text-lock-only characters (e.g. build-65 "father") have no sheet — omit them; the `[X LOCK]` token in the prompt carries them. Passing a sheet-less name throws `KeyError: no locked sheet`.
- `--jesus` attaches the master face for any shot Jesus is in.
- Always `--dry-run` once to eyeball the expanded prompt.
- Then both gates must exit 0: `python3 character_ref_gate.py --dir <build>` and `python3 jesus_face_gate.py --dir <build>`.

### Gate traps (these cost real time)
- The jesus gate bans the literal strings `halo` and `rim-light` **even inside a negation**. Write "no bright ring / no glow / no backlight" instead.
- Any JESUS_WORD (`jesus`, `the lord`, `christ`) **anywhere in a shot body or slug** makes the gate demand the full Jesus lock. In a no-figure shot never write "no face for the Lord" — write "no divine figure, no face for the coming one". Keep slugs clean (`s2b-blessed-be-the-name`, not `s2b-the-lord-gave`).
- Some builds fail the jesus gate **pre-existingly** because they use a deliberate from-behind / face-never-shown Jesus (confirmed: build-24-sower, build-40-the-friend-at-midnight). That is not your regression — confirm your new shot isn't in the FAIL list and move on. Converting those is a build-owner decision.
- Some builds have a local `build-NN/.gitignore` containing `assets/` (e.g. build-04-nicodemus). A plain `git add` silently skips your new jpeg — use `git add -f` and verify with `git show --stat HEAD | grep <slug>`.

---

## 5. REBUILD — THE STEP THAT WAS MISSING
A repainted still is invisible until the video is re-rendered.

```
cd build-NN-slug && python3 build.py      # takes 5-15 min, writes a ~400MB segs/ scratch dir
```
- Run builds **sequentially**, never in parallel (ffmpeg is CPU-bound).
- **Never leave a half-written video.** If a build is killed or errors, `git checkout -- <the mp4>` to restore the committed one. Verify every output: `ffprobe -v error -show_entries format=duration -of csv=p=0 <mp4>`.
- `rm -rf segs/` after each build.
- **Prove the fix is in the movie**: `ffmpeg -y -ss <seconds> -i <mp4> -frames:v 1 proof.jpg` at the timestamp of the fixed shot, then LOOK at the frame. Compute the timestamp by summing the audio durations of the beats before it in `build.py`'s BEATS list.

### Which builds need a rebuild
Any build whose stills are newer than its mp4:
```python
# stills newer than the mp4 = fixes not yet in the movie
```
Do this check at the start — it finds the whole backlog in one shot.

---

## 6. WHAT IS *NOT* YOUR FILE
Do not edit `make_narration.py`, `QUEUE.md`, `approvals.json`, `COMPLAINTS.md`, or captions.
`build.py` belongs to the assembly session — **but** two genuine bugs there were blocking
re-renders entirely and were fixed after being proven:
- `build-99`: `TEXT = {s[0]: s[4] ...}` on 3-long narration tuples → `s[2]`.
- `build-181`: BEATS referenced segment `n1b` that the echo sweep deleted → removed the dead beat.
If you hit that class of thing (a provable crash, file untouched by others for days), fix it,
say exactly what you changed and why, and verify by rebuilding. Otherwise leave build.py alone.

---

## 7. KNOWN BLOCKERS
- **build-92-peters-denial** will not render: its own guard reports `DEAD AIR: 2.78s gap before n5c` (limit 2.5s). Peter's grey-hair repaint is done and waiting. This is **audio timing** — audio/assembly session, not pictures. Do not hack past the no-dead-air law.
- **Deploy**: Machine C has no `node`/firebase, so it cannot publish to milk-b4-meat.web.app. Rebuilt videos go to git; Cameron pulls and watches the files, or a node machine deploys them.
- **Pushing video is slow (~250MB)**. Run the push in the background and **verify it landed by checking `git rev-list --count origin/main..HEAD` — do not trust the exit code**, a piped push can mask a rejection. If another machine pushed mid-upload the ref moves and you must `pull --rebase` and push again.

---

## 8. THE LOOP
pull → pick work (complaint or auto-QC finding) → **look at the current still first** (never repaint
something already correct) → fix the prompt prose + regen every affected shot → **QC the jpeg by eye**
→ both gates green → rebuild the video → extract a frame and verify the fix is in it → commit + push
(verify it landed) → tell Cameron which videos to watch and what changed in each.

End of session: add a `SESSION-LOG.md` entry at the top, commit, push.
