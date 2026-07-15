# ⛔ THE WHOLE FACTORY IS BLOCKED ON HUMAN STEPS (2026-07-15)

No machine can build a video yet. Every video now shows Jesus's face locked to a
master reference that does not exist, and every still is generated in Flow, which is
not logged in on any machine (the Playwright profile is per-machine, so each box
needs its own one-time Google login).

## Blocker 1 — Flow login (per machine, unblocks all image generation)
On THIS machine (`ElliLovett`) the driver profile `~/.mbm-flow-profile` was created
fresh and a Chrome window was opened with `python media-production/flow_driver.py open`.
**A human must log into Cameron's Google (Ultra) account in that window once**, then:
```
python media-production/flow_driver.py check    # must print logged_in=True project=saved
```

## Blocker 2 — the Jesus master face (one-time, whole-factory)
`JESUS-MASTER-REF/` has no face yet. **Machine A has claimed the candidate bootstrap**
(see `JESUS-MASTER-REF/candidates/CLAIM.md`) and will push 3 candidate portraits once
its Flow is logged in. Cameron then picks 1, 2 or 3; the winner becomes
`JESUS-MASTER-REF/jesus-face.jpeg`. Only then can the v3 redo and any new Jesus build run.
(Machines B and C should NOT also generate candidates — defer to A to avoid duplicates.)

## State of this machine (Machine B, rows 51–100) — ready to run the instant Flow is up
- playwright + Pillow installed; Chrome, ffmpeg, edge-tts all verified present.
- No numbered row claimed (every build is blocked upstream on the two gates above).
- Next Machine-B new build when unblocked = row 51 (The first catch of fish, Luke 5).

## Identity note for Cameron
Hostname `ElliLovett` is still listed as "extra worker" in MACHINE-IDENTITY.md, but is
being operated as **Machine B**. Please reconcile that table so the schemes agree.
