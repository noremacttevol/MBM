# Rule conflicts — these need Cameron's call

Two rules in this project can pull against each other, and where they do I have
stopped rather than silently picked a side.

## The runtime floor vs the trailing-dead-air ceiling

**The two rules**
- 63 builds enforce their own minimum runtime (`if total < 61.0: TOO SHORT`).
- The speaker-law pass caps trailing quiet: end **1.5s** after the last spoken
  word, hard ceiling **3.0s**.

Several short stories used to clear the floor by holding the closing card for
9–13 seconds — which is precisely the trailing dead air you asked me to remove.
Cutting that to 1.5s drops them under the bar.

**How the repair tries to resolve it**, in order, before giving up:
1. raise the tail toward the 3.0s ceiling
2. add the remainder to the body breaths between beats — but only while the
   worst inter-beat gap stays under the 2.5s dead-air limit the builds enforce
3. if both are exhausted, put the rest on the closing card and flag it here

### How big this actually is: 10 at risk, 8 fixed themselves

Every one of the 200 delivered videos was originally 60s or longer — measured,
not assumed. Ten of them only got there on a long closing card, and would fall
under once that became TAIL=1.5:

| Projected | Was | Actual after rebuild |
|---|---|---|
| 49.1s | 60.6s | **49.8s — still short** |
| 50.0s | 61.5s | **61.3s, but 4.96s trailing** |
| 50.0s | 61.3s | 78.6s ✓ |
| 53.5s | 61.2s | 100.2s ✓ |
| 53.5s | 61.2s | 71.1s ✓ |
| 54.0s | 61.5s | 71.5s ✓ |
| 55.6s | 63.3s | 97.1s ✓ |
| 58.3s | 61.0s | 115.0s ✓ |
| 58.8s | 61.5s | 144.8s ✓ |
| 59.7s | 62.4s | 74.8s ✓ |

**Eight of the ten fixed themselves**, because this pass ADDS content — the
lifted verses and the narrator's retelling of each. #144 went from a projected
58.8s to 144.8s. That is worth noticing on its own: the padding was replaced by
actual scripture and actual storytelling.

Only the two below genuinely conflict.

---

### build-137 — Stephen Sees Him Standing (Acts 7)

- Story runs **57.1s**. The build enforces **61.0s**.
- Body padding hit the 2.5s dead-air limit first (worst gap reached 2.77s).
- Clearing the floor therefore needs **TAIL = 5.0s**, giving **4.96s** of trailing
  quiet — over the 3.0s ceiling. My verifier rejects it, correctly.

**Your options:**

1. **Accept the longer card here.** 4.96s on a closing card the viewer is reading
   is not the same defect as a video running silent past the last word. This is
   what the build originally did (CARD_HOLD 13.0) and is the smallest change.
2. **Drop the 61s floor for this video** and ship it at ~57s.
3. **Lengthen the story** — Acts 7 has more of Stephen's witness available, and
   `build-179-stephens-witness` covers the same chapter, so there is material.
   This is the only option that fixes the cause rather than the symptom.

I'd suggest **3** if you want it right and **1** if you want it shipped today.
Tell me which and I'll apply it.

Current state: left at 61.3s with TAIL=5.0s. It has to stay there — this build
enforces its own 61s floor in code, so TAIL=1.5 makes the render fail outright.
Marked as failing verification so it does not reach the board looking clean.

---

### build-173 — The Dead Shall Hear (John 5)

- Story runs **49.8s**. Nothing in this build enforces a floor, so it renders
  happily — it is simply 11 seconds shorter than it shipped before.
- It used to reach 60.6s on a **13-second closing card**. That is the single
  worst piece of trailing dead air in the library, and removing it is exactly
  what you asked for.
- Clearing 60s again would need **TAIL = 11.4s**. That is not a fix, that is
  putting the defect back.

**Your options:**

1. **Ship it at 49.8s.** Honours the dead-air law. The video is tight and ends
   where the story ends. This is the current state.
2. **Lengthen the story.** John 5 has more — verses 21, 24 and 26-27 are all on
   the same theme and none are in the video. This is the option I'd take: the
   video is short because it is thin, not because the card was trimmed.
3. Put the 13s card back. I don't recommend it.

Current state: **option 1**, at 49.8s with a 1.5s tail. Marked needs-cameron
rather than shipped, so you decide before it counts as delivered.

---

## Why I stopped instead of choosing

Both of these are a trade between two things you asked for. The dead-air
instruction was explicit and recent; the 60-second floor is a convention every
delivered video happens to meet and 58 builds enforce in code. I can defend
either answer, which is exactly why it should be yours.
