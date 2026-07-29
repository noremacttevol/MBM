# KICKOFF PROMPT — paste this into any new chat to start a video build

> **Simpler now:** just run `media-production/next-job.sh` — it claims the next
> open story from `QUEUE.md` and opens a fresh chat already primed on it, so you
> never paste anything. This file is the manual fallback if you want to start a
> chat by hand. `QUEUE.md` is the board; the old per-machine `VIDEO-ASSIGNMENTS.md`
> lists are retired.

Copy everything between the lines into a brand-new chat opened in the MBM project folder.

---

You are on MBM video production duty. Do these steps in order, before anything else:

1. Read CLAUDE.md and .claudecode.md at the MBM root, then media-production/PRODUCTION-BIBLE.md and media-production/CREW-GUIDE.md. Every law in those files binds this session — the Voice Law, Ear-Check Law, No-Dead-Air Law, Translation Law, Readable-Card Law, Self-Revision Law, Full-Story Law, and all of the Cameron Corrections.

2. Read the top entry of SESSION-LOG.md and verify its commit hash appears in `git log`. Your first message to me is a short recap of that entry plus the hash.

3. Find the next video in the queue: look at the highest-numbered `build-XX-*` folder in media-production/ — the next video is the production pack numbered one higher. Read that pack fully, plus its entries in THE-200.md and PAIRING-LIST.md. EXCEPTION: if my first message assigns you a specific video number (e.g. "you are on video #13"), build THAT one instead — this is how multiple chats each take a different video without colliding.

4. Study the scripture itself (KJV) for that story — the full passage in context, not just the headline moment (Full-Story Law). Understand why Jesus's goodness shows in it before you storyboard anything.

5. Build the video end to end yourself: stills, motion clips, narration, then the complete Self-Revision Law loop — ear-check every segment, silence-scan the mix, frame-strip every second and count limbs, check wardrobe and character consistency against banked references — as many passes as it takes until a full pass finds NOTHING. I see the video once, for the final yes. I never write prompts, never edit clips, never catch bugs.

6. BROWSER RULE: only ONE chat may drive Chrome/Flow at a time. Before touching the browser, ask me: "Is any other chat using Chrome right now?" If yes, do only local work (script, narration, QC, assembly of already-banked clips) and wait for my go-ahead before any browser step.

7. At the end of the session: add a new entry at the TOP of SESSION-LOG.md, commit, and push to origin/main.

---
