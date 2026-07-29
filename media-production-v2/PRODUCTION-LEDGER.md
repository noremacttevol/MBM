# V2 PRODUCTION LEDGER

State of record for the V2 picture rebuild. **The repo is the memory; this file is
the state.** A fresh session reads `V2-KICKOFF.md` top to bottom, then this ledger,
then continues at the first row that is not DONE (finishing any IN-PROGRESS row from
its last completed step A–I).

Status values: `DONE` / `IN-PROGRESS (last step X)` / `BLOCKED(reason)`.

---

## Session 1 — 2026-07-28

- **Model:** Opus 5 (Claude Code)
- **Machine:** Machine A — hostname `Dev`
- **Start:** 2026-07-28 22:01:09 EDT

### Bootstrap

| step | result |
|---|---|
| flow_driver check | `logged_in=True project=saved` |
| media-production-v2 skeleton | created (`.gitignore` blocks jpeg/jpg/png/mp4/mp3/wav/m4a/mov) |
| flow_driver `--model` | ADDED — the driver had no model selector; it used whatever the project remembered and only verified the chip said "Nano Banana". V2 needs Nano Banana Pro per shot, so `gen --model "Nano Banana Pro"` now selects it on the chip and ABORTS rather than spending on a lesser model (override: `--model-best-effort`). |
| Jesus V2 face | see below |

#### Jesus V2 face candidates

Three front bust portraits, **identity sentence byte-identical across all three** —
only light and background varied, so the comparison was "which render of the same
described man is best", not "which of three men". Prompts: `candidate-prompts.md`.

| candidate | light / background | outcome |
|---|---|---|
| **candidate-1** | soft even daylight, plain deep earth-brown background | **WINNER → `jesus-v2-face.jpeg`** |
| candidate-2 | warm low late-afternoon sun, limestone wall behind | kept for Cameron |
| candidate-3 | open shade, olive grove behind | kept for Cameron |

**Why candidate-1 won:** a face-lock reference wants neutral even light, a neutral
background and a straight-on symmetric view, so the model copies the FACE and not a
scene. Candidate-2 is the most beautiful of the three but bakes a warm backlight into
the hair edge — with a rim-light law on the books, that is the wrong thing to
propagate into 200 videos. Candidate-3 has the best fabric and the fullest beard and
is the runner-up. **All three are the same man**, so Cameron can swap the pick later
without re-locking anything.

Angle refs generated with the winner attached as `--ref`:
`jesus-v2-three-quarter.jpeg`, `jesus-v2-profile.jpeg`, `jesus-v2-full-body.jpeg`.
The three-quarter came back as a seated street scene rather than the plain-background
ref that was asked for — accepted as supporting reference (the face matches and the
FACE ref is the operative lock); not re-rolled, since rerolling a support asset buys
nothing. Useful signal: **ref-echo did not occur** — the model composed new scenes
rather than copying the portrait.

**JESUS V2 FACE = CANDIDATE, locked for this run, pending Cameron's approval of video #1.**

#### Measured facts (record these — the plan rested on estimates)

| fact | measured value |
|---|---|
| Flow image model | chip reads **🍌 Nano Banana Pro**; the driver had NO model selector before today and was riding whatever the project remembered |
| Flow output resolution | **768×1376** for 9:16 — same as V1's painted refs. Flow's image size, not a model limit; build.py supersamples to 4320×7680 and lands at 1080×1920 |
| credit figure printed by the driver | `0 credits` on every generation this session (recorded verbatim, not interpreted) |
| generation wall-time | ~2–3.5 min per still including download |

### Videos

| row | slug | start | end | mins | beats | gens | accepted | rerolls | credits-noted | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| _pending_ | | | | | | | | | | | |
