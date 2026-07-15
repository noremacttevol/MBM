# ⛔ FACTORY IS BLOCKED ON TWO HUMAN STEPS (as of 2026-07-15, Machine B / ElliLovett)

No machine can build a single video until BOTH of these are done, because every
video now shows Jesus's face locked to a master reference that does not exist yet,
and every still is generated in Flow which is not logged in.

## 1. Log Flow into Google (unblocks ALL image generation)
The Playwright driver profile `~/.mbm-flow-profile` had to be created fresh on this
machine. A Chrome window was opened via `python media-production/flow_driver.py open`.
**A human must log into Cameron's Google (Ultra) account in that window once.** Then:
```
python media-production/flow_driver.py check    # must print logged_in=True project=saved
```
(If the window was closed, just run `open` again and log in.)

## 2. Pick the Jesus master face (unblocks the v3 redo + every Jesus still)
`JESUS-MASTER-REF/` is empty — no master face has ever been chosen. The 3 candidate
portrait prompts are staged in `JESUS-MASTER-REF/candidates/CANDIDATE-PROMPTS.md`.
Once step 1 is done, generate them at $0:
```
python media-production/gen_candidates.py
```
Push, then Cameron picks 1, 2 or 3. Move the winner to `JESUS-MASTER-REF/jesus-face.jpeg`,
delete the losers, push. NOW the v3 redo and all new Jesus builds can run.

## What this session (ElliLovett) already did — no need to redo
- Installed playwright + Pillow; verified Chrome, ffmpeg, edge-tts all present.
- Created `JESUS-MASTER-REF/candidates/` + the 3 candidate prompts (JESUS LOCK v3,
  painted style block byte-identical).
- Wrote `gen_candidates.py` (one command generates all 3 post-login).
- Did NOT claim any numbered row (blocked before any build could start).

## Identity note for Cameron
This machine's hostname is `ElliLovett`, which MACHINE-IDENTITY.md still lists as
"extra worker," while the operator is running it as **Machine B** (rows 51–100).
Please reconcile MACHINE-IDENTITY.md so the two schemes agree.
