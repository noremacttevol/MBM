# social/ — MBM Social Media Distribution

> **What this folder is.** Everything needed to put the approved scripture videos in
> front of people on YouTube Shorts, Instagram Reels, TikTok, and Facebook Reels.
> Built 2026-08-06. This folder SUPERSEDES the older `Marketing-Launch-Kit/social-pages/`
> and `FACEBOOK-LAUNCH-KIT.md` for anything about posting videos — those were written
> in July against V1 cuts that have since been redone. Their voice guardrails were
> good and are carried forward here.

## The one rule that can never be broken

**Only videos Cameron has APPROVED — at the exact approved cut — ever get posted.**

A row is postable only when ALL of these are true:
1. `approved: true` in the admin approvals (`cd admin && node dump-approvals.mjs`),
2. its `approvedHash` matches the `data-hash` currently served on `site/review.html`,
3. the actual file bytes are verified against that hash.

**Never post from `media-production-v2/` working-tree files.** The production
autopilot rewrites those mp4s mid-rebuild — on 2026-08-06, 22 of 41 approved rows
had a working-tree file that was NEWER than the approved cut. The approved bytes
live in git history, so `refresh-postable.py` extracts every approved cut
byte-exact from git objects into `exports/` and verifies the hash. Post ONLY from
`exports/`.

## Files here

| File | What it is |
|---|---|
| `refresh-postable.py` | Run `python3 social/refresh-postable.py` from the repo root. Re-pulls approvals, re-verifies every row, re-exports approved cuts to `exports/`, re-extracts covers. Run it whenever Cameron approves more videos. |
| `postable.json` | The machine-readable verified list: row, title, scripture, duration, hash, export path, cover path, plus the excluded rows and why. |
| `POST-QUEUE.md` | The human posting queue — one entry per approved video: title, caption, hashtags, cover, scripture reference, per-platform checkboxes. **This is the working file; tick boxes as you post.** |
| `CHANNEL-PLAN.md` | Account names, handles, bios, and 5-minute setup instructions for each platform. |
| `SCHEDULE.md` | Posting cadence, the 41-day launch order, and the weekly batching rhythm. |
| `GROWTH-PLAYBOOK.md` | Everything else recommended to spread the app: comment handling, member-sharer moves, what to measure, what never to do. |
| `covers/row-NNN.jpg` | Cover frame per video, pulled from the approved cut with ffmpeg (1080×1920). |
| `exports/` | The byte-verified approved cuts (gitignored — regenerate anytime with the refresh script). |

## Tone laws (bind every caption, comment, and reply)

From the Gospel principles in CLAUDE.md / AGENT-RULES.md:
- **Reverent and honest. No clickbait that cheapens the stories.** The story does the work.
- **Never pressure, shame, or manipulate.** No "share this or else," no guilt, no fear.
- **Ask, don't tell.** End with an honest open question, the way the app does.
- **The app is never hidden about what it is.** Captions say plainly the video is from
  the Milk Before Meat app.
- **These pages are MILK.** No Church, no doctrine, no Book of Mormon in posts or
  comments. If someone directly asks who makes this, answer honestly and plainly —
  never hide, never push. Depth belongs in private conversation when someone seeks it.
- **Never argue doctrine in comments.** Respond with kindness or with the words of
  Jesus, or take it to DM. A real person (Cameron) is always one message away.

## Workflow for any future session

1. `python3 social/refresh-postable.py` — refresh the verified list.
2. Open `POST-QUEUE.md` — new approved rows get appended with caption + cover
   (follow the entry format; keep the voice).
3. Never edit `media-production-v2/`, the boards, QUEUE.md, or autopilot files from
   a social session. This folder and SESSION-LOG are the only workspace.
