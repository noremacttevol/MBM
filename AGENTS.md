# MBM — Agent Entry Point (Codex, Claude, any AI worker)

**Read [`AGENT-RULES.md`](./AGENT-RULES.md) first. It is the single master manual for
this project — the vision, the laws, the architecture, and how Cameron wants to work.**

Then read [`STATUS.md`](./STATUS.md) for the current build state, then read the code
before changing it.

If anything in any other file conflicts with `AGENT-RULES.md`, that file wins.

---

## VIDEO WORK — THE NON-NEGOTIABLES (distilled; Cameron rejected finished videos over each)

Multiple AI tools and multiple computers work this repo at once. Git is the only
coordination channel. These rules keep workers from colliding and keep videos in spec.

### Coordination — do these or another worker WILL duplicate/destroy your work
1. **Start every session:** `git pull --rebase origin main`.
2. **Claim before building.** Open `media-production/QUEUE.md`, take the lowest open row
   in your range (Built ⬜, Claim empty), write your machine name + date in the Claim
   column, **commit and push the claim BEFORE generating anything.** If the push is
   rejected, someone else took it — pull and take the next row. Never touch a row
   claimed by another worker.
3. **Commit and push as you go.** Work that only exists on one machine's disk does not
   exist. Tick `Prep`/`Built` in QUEUE.md as you go and push each change.
4. **End of session:** add an entry at the TOP of `SESSION-LOG.md` (what was done, the
   commit hash), commit, push. The next session on any tool verifies this chain.

### Content laws — a video violating any of these is NOT done, no matter how it looks
5. **One locked Jesus face.** Every shot with Jesus attaches the master reference image
   as a `REF:` line plus the byte-identical JESUS LOCK paragraph. Middle Eastern Jewish
   man (~33), warm tan/olive skin, shoulder-length dark wavy hair, full dark beard, ONE
   plain cream/off-white wool robe (only Jesus wears cream). NO halo, glow, or rim-light.
   V2 rebuilds use `media-production-v2/JESUS-V2-REF/`. Recurring cast (the Twelve etc.)
   are locked the same way via the CAST-REF bibles.
6. **Run the gate before spending any generation credit:**
   `python3 media-production/jesus_face_gate.py --dir <build-folder>` must exit 0.
7. **Stills only (Phase 1).** Narrated painted stills + slow Ken Burns, serif captions,
   KJV verse card, closing question card. NO AI motion clips. A delivery containing an
   AI-animated clip is out of spec.
8. **Two-Voice law.** Narrator speaks modern English; Jesus speaks ONLY exact KJV words.
   American-accent Jesus voice, never a "Multilingual" model.
9. **REDO-ALL law.** Every video gets redone with the new voice AND re-approved. Prior
   approvals are void. Nothing sits in the reviewer marked done unless it carries the
   new voices.
10. **No music, no tone bed — narration + intentional silence only.** Ear-check every
    narration (`qc_narration.py`) before assembly.
11. **Captions live only in the bottom band**, split long lines in sync with narration,
    never covering the art.
12. **Scene logic QC:** lighting matches the scripture's stated time of day; every
    figure's action must read correctly at a glance; figures stay visibly inside boats.
13. **Story law:** ONE EVENT = ONE VIDEO; blend gospel accounts into one telling. Read
    `media-production/STORY-LEDGER.md` before any story work.

### Working with Cameron
- He watches the FINISHED video once and says yes/no. Never show partial work, never ask
  him to test or debug, never ask permission he already gave. Verify everything yourself
  (gate, QC scripts, watch the output) before presenting.
- If he corrects something, write the correction into `PRODUCTION-BIBLE.md` §1 and
  `CLAUDE.md` in the same session.
