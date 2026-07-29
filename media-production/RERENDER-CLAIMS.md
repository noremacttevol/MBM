# RE-RENDER CLAIM BOARD

**Rendering is the only destructive operation in this pipeline.** Two machines running
`build.py` on the same build at the same time corrupt a ~250MB mp4. This board is the only
thing preventing that.

## The rule
1. Add your row below with the build, your machine (from `MACHINE-IDENTITY.md` — run
   `hostname`, never trust a note in a shared file), and the time.
2. **Commit and push the claim BEFORE running `build.py`.** If the push is rejected,
   another machine claimed it while you were reading — pull and take a different build.
3. Delete your row once the render is committed and pushed.
4. Before claiming, sanity-check nobody is mid-render anyway:
   `git log --oneline -5 -- <build>/*.mp4`

The REDO-ALL voice sweep also renders builds. If you see recent `REDO #NN` commits marching
through a number range, stay out of that range.

| Build | Machine | Claimed (UTC-ish local) | Status |
|---|---|---|---|
| _(none — board is open)_ | | | |
