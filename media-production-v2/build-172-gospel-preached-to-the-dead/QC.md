# QC / RUNNER HANDOFF — build-172-gospel-preached-to-the-dead

Row 172 · 1 Peter 4:6 + 1 Peter 3:18-19 ("he went and preached unto the spirits
in prison"). RESTORATION shelf. Authored fresh 2026-08-07 (Machine A `Dev`,
Fable-5 author lane, $0).

## COMPLAINT LEDGER
- **No open Cameron complaint.** `v2_outline.py 172` shows none. This is a
  first-time V2 picture map on the already-authored SPEAKER-LAW narration
  (audio column OK).

## What this row is
Peter's two verses set side by side: the gospel was preached even to the dead,
and Christ himself, quickened by the Spirit, went and preached to the spirits in
prison. MILK: the narration quotes the two verses and stops — it never says the
words "spirit world," never explains who is saved, never argues. The pictures
hold the same restraint.

## SPEAKER LAW (verified)
Peter's epistle — **NO red-letter, NO God-voice.** s1 and s19 are the SCRIPTURE
voice → LIGHT-BLUE captions. Jesus is *embodied* on b06-b09 (the risen, quickened
Lord who "went and preached"), but the caption stays scripture-blue, never red.
`jesus=True` + `ref=True` on b06-b09 only; the shared JESUS lock + JESUS-MASTER-REF
inject automatically (confirmed in ASSEMBLED-PROMPTS.txt). Only Jesus wears cream.

## CONTENT-CARE — the subject is the DEAD (gates before any credit)
- The departed are shown with DIGNITY and HOPE. **NO corpse, body, bones, gore or
  open bier** anywhere; the grave (b01/b04/b10) is plain and closed, the tomb at
  b10 is quiet and empty.
- The "spirits in prison" (SPIRIT-PRISON place) are **REAL, SOLID, FULLY-CLOTHED
  people** on real ground — **NEVER ghosts, mist, translucent, floating or faded.**
- "Prison" is a place of **WAITING, not a dungeon**: NO bars/cell/chain/shackle/
  iron/prisoner-in-irons, NO fire/flame/torment/torture/chasm/gulf/devil/monster —
  and equally NO painted-heaven kitsch (cloud floor, pearly gate, golden street,
  throne, harp, wings). Deliberately NOT the Luke-16 `SPIRIT-WORLD` lock (two
  regions + gulf + torment) and NOT the earthly `ANCIENT-PRISON` lock (a real jail
  with timber bars + irons); neither fits 1 Peter or Cameron's church's teaching.
- The light is **real directional daylight from an opening** — NEVER a halo, glow
  or rim-light on anyone, least of all Jesus.

## The human spine (keep it consistent)
One believing man dies → his **widow** (MOURNER) mourns at the grave → that same
**departed man** (DEPARTED-MAN) waits in the spirit place, is reached by the
gospel, is brought to God by Christ. Hold DEPARTED-MAN identical across b03/b05/
b07/b11 and MOURNER identical across b01/b04.

## 🅿️ RUNNER — build steps (paid image lane)
Two NEW places; promote each from its first good frame BEFORE generating the rest
that share it (lesson 11):

1. **Generate b01 first.** QC it (graveside, widow, closed tomb, realistic, no
   lettering). Then promote it as the GRAVESIDE-MORNING plate:
   `python3 media-production-v2/v2_stash.py --promote build-172-gospel-preached-to-the-dead GRAVESIDE-MORNING build-172-gospel-preached-to-the-dead/assets/s01-a-believer-had-died.jpeg`
2. **Generate b02 next.** QC it (the waiting place: real solid clothed people, dim
   expanse, warm light breaking in low, NO ghosts/bars/fire/gulf/heaven-kitsch).
   Then promote it as the SPIRIT-PRISON plate:
   `python3 media-production-v2/v2_stash.py --promote build-172-gospel-preached-to-the-dead SPIRIT-PRISON build-172-gospel-preached-to-the-dead/assets/s02-preached-to-the-dead.jpeg`
   Promote b02 (a NON-Jesus frame) for the place — **not** b06-b09 (Jesus frames).
3. Re-run `v2_stash.py --wire build-172-gospel-preached-to-the-dead` so both
   plates wire into PLACE_REFS, then `v2_prompt.py … --check` (must PASS) and
   `--dump`.
4. Generate the remaining 9 beats (b03-b11) against the plated places.
5. **Gates:** `jesus_face_gate.py --dir build-172-gospel-preached-to-the-dead`
   must exit 0 (b06-b09). Face/identity board: DEPARTED-MAN identical b03/b05/b07/
   b11, MOURNER identical b01/b04. Content-care sweep every frame for the bans
   above. Scale gate: everyone ordinary-sized (no giant Christ).
6. Assemble (AUDIO LOCK — narration is authored + OK, byte-identical; do NOT
   re-voice). Re-audit, then ship with a review card. There is no open complaint
   to answer, so the card just presents the finished cut.

## Coverage / windows (authored, verified)
11 beats, windows contiguous 0.400 → 49.641 (= card_start), monotonic, each
segment's speech onset inside its window. ~4.5 s/picture. `--check` v4 PASS.
