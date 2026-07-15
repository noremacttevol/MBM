# MACHINE B HANDOFF — read this, then continue rows 51–100 (2026-07-15)

Written by the Machine B session that got the face-shown pipeline working end-to-end and
shipped the first three face-shown videos. A fresh low-context session can pick up here.

## ✅ SHIPPED & LIVE (on the gallery, https://noremacttevol.github.io/MBM/)
- **Row 51 — The First Catch of Fish (Luke 5)** — new build, first face-shown video.
- **Row 71 — Calling the Fishermen (Matt 4)** — v3 REDO, face shown.
- **Row 72 — Calling Matthew (Matt 9)** — v3 REDO, face shown.

## 🔧 CRITICAL FIXES ALREADY MADE & PUSHED (don't re-debug these)
1. **git could not push/fetch** on this machine → root cause was the Windows **schannel
   SSL backend negotiating HTTP/2, which corrupts git's pack transfer** (`ls-remote`
   worked, every pack op failed with `invalid index-pack output` / stalled push). **FIX
   (already set globally):** `git config --global http.version HTTP/1.1`. If a future
   machine shows the same symptom, run that one line.
2. **gen_site_index.py crashes on Windows** with `UnicodeEncodeError … '\U0001f7e1'`
   (a 🟡 emoji) while WRITING index.html, leaving it truncated/empty. **FIX: always run
   it as** `PATH="$(pwd)/bin:$PATH" PYTHONUTF8=1 python gen_site_index.py` **from
   media-production/**. (PYTHONUTF8=1 makes file writes UTF-8; PYTHONIOENCODING is not
   enough.) It now writes **docs/index.html** (GitHub Pages source = /docs; repo-root
   index.html is vestigial). After running, confirm `grep -c '<video' docs/index.html`
   is ~80, not 0.
3. **jesus_face_gate.py** was rejecting every Jesus build (its own LOCK_V3 text contains
   "never caucasian/blond", and a Windows em-dash cp1252 bug). Fixed (blanks the lock
   from the BANNED scan + reads UTF-8). Gate PASSES on face-shown builds now.
4. **flow_driver.py `gen --ref`** now (a) attaches the master face via Flow's hidden
   `input[type=file]`, and (b) **downloads the generated scene, not the uploaded ref**
   (it records the ref's gallery name and excludes it). Both fixes pushed.

## THE MASTER FACE IS LOCKED
`media-production/JESUS-MASTER-REF/jesus-face.jpeg` (Cameron picked candidate 1). Attach
it as `--ref` on EVERY shot where Jesus appears. His face must match it in every frame.

## PER-VIDEO PIPELINE (proven on rows 51/71/72)
Preflight: `python media-production/flow_driver.py check` → `logged_in=True project=saved`.
Python is `python` (not python3); playwright + Pillow + edge-tts + ffmpeg are installed.
1. `git pull --rebase` (commit any WIP first — see GIT DISCIPLINE). Pick the next job
   (see WHAT'S NEXT). Claim the row in QUEUE.md, commit, push BEFORE generating.
2. **v3 REDO of a built (face-never) row:** keep narration + all non-Jesus stills;
   rewrite ONLY the Jesus-shot prompts to face-shown + the byte-identical JESUS LOCK v3
   paragraph + a `REF: jesus-master-ref` line (copy them from build-71/72 PROMPTS.md);
   replace the old header/JESUS-LOCK block (it has banned words "halo/rim-light"); port
   caption-v2 build.py (copy build-72/build.py, change slugs/BEATS/KJV/OUT).
   **New build:** write PROMPTS.md 8–12 beats, Master Style Block byte-identical.
3. `python media-production/jesus_face_gate.py --dir <build>` → exit 0.
4. Generate: `python media-production/gen_shots.py --dir <build> --shots <slugs> --jesus <jesus-slugs>`
   (I committed gen_shots.py — it reads PROMPTS.md, prepends the style block, attaches
   --ref on the --jesus shots, 3 retries each). Non-Jesus shots omit --jesus.
5. **QC every generated jpeg** by `Read`-ing it: face matches the master; only Jesus in
   cream; single frame (NO triptych); portrait 768×1376. **A ~421KB jpeg identical to
   jesus-face.jpeg = the ref got downloaded — reroll.** Wide "four follow / a wider view"
   shots come back as TRIPTYCHS — reword to "one single tall upright vertical scene,
   no panels, no dividing lines" + pull the subject close, and reroll.
6. `python make_narration.py` (edge-tts; only if new/changed). `python build.py`
   (caption-v2 + Windows Georgia fonts + 30MB cap; DONE line prints size/duration).
7. QC 2–3 frames from the mp4 (ffmpeg -ss … -frames:v 1): KJV caption exact & cream-italic,
   face right, closing card an invitation.
8. Tick Prep+Built in QUEUE.md (for a redo, set Appr → ⬜, note "v3 REDONE <date>").
   Add title to gen_site_index.py TITLES if new; run gen_site_index with **PYTHONUTF8=1**.
9. Stage EXPLICIT files (build.py, PROMPTS.md, make_narration.py, .gitignore, assets/,
   audio/, the .mp4, QUEUE.md, gen_site_index.py, docs/index.html — NOT segs/). Commit,
   `git pull --rebase`, `git push`. That publishes it. One video per chat, then hand off.

## GIT DISCIPLINE (this bit me hard — avoid the mess)
- **Commit BEFORE `git pull --rebase`.** NEVER `--autostash` while build.py is running or
  with uncommitted locked assets — OneDrive locks the files, the reset aborts, and you
  land in detached-HEAD with work in a dangling autostash.
- **Never `rm -rf .git/rebase-merge` while a rebase is mid-way** — it aborts the rebase.
  The `error: could not remove '.git/rebase-merge'` after "Successfully rebased" is a
  harmless OneDrive artifact — ignore it, the rebase is done.
- 4+ machines push constantly → expect QUEUE.md + index.html conflicts every push.
  QUEUE: keep both sides' rows, use YOUR row's line. index.html is generated → just
  re-run gen_site_index (PYTHONUTF8=1) and `git add` it. flow_driver.py conflicts: keep
  origin's ref-ATTACH + the ref-name-exclusion download fix.

## WHAT'S NEXT for Machine B (rows 51–100), in work order
Re-derive exactly from QUEUE.md, but as of this handoff:
1. **v3 REDO row 84 — "No Room: the Manger" (Luke 2)** — built face-never; also its
   original build stopped at 11 stills (Chrome dropped before s12). Redo Jesus stills
   face-shown + finish s12 + caption-v2. (Oldest built row in range still needing redo;
   71 & 72 are done.)
2. **Fix row 91 — Gethsemane (Luke 22)** — in the Fix queue: hair grows long in s7
   (agony-drops). Regenerate s7 face-shown/hair-consistent, then redo face-shown +
   caption-v2, rebuild, tick Built.
3. **New builds, lowest number first: row 52 (The demoniac in the synagogue, Mark 1),
   then 53, 54, 55 …** through the unbuilt rows in 51–100.

## Machine identity note (still open)
This box's hostname is `ElliLovett`; MACHINE-IDENTITY.md still lists it as "extra worker"
but it's operated as **Machine B (rows 51–100)**. Worth reconciling that table.
