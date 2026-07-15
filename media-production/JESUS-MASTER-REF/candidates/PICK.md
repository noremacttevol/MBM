# 👉 CAMERON: pick the Jesus master face — 1, 2 or 3

Three candidate portraits, all obeying JESUS LOCK v3 (Middle Eastern, warm olive-brown
skin, shoulder-length dark hair, full dark beard, warm brown eyes, cream robe, no
caucasian/pale/blond). Generated in Flow (Nano Banana 2, 9:16, $0) by Machine B on
2026-07-15, using the reworked flow_driver.py.

- **candidate1.jpeg** — softer, younger (~32), gentle; slight warm backlight glow.
- **candidate2.jpeg** — leaner, stronger cheekbones, solemn; clean, no glow.
- **candidate3.jpeg** — warmer, fuller beard (~35), approachable.

## When you pick N:
The approval monitor (or any machine) runs:
```
cd media-production/JESUS-MASTER-REF
cp candidates/candidateN.jpeg jesus-face.jpeg
git rm -r candidates ; git add jesus-face.jpeg
git commit -m "Master face locked: candidate N" && git push
```
That lands `JESUS-MASTER-REF/jesus-face.jpeg` — the ref every Jesus shot attaches. The
v3 redo and all new Jesus builds unblock immediately across every machine.
