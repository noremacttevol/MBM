# SCHEDULER — how to make the videos build themselves

You wanted a cron that opens a fresh chat for each of the remaining ~160 jobs so
you never have to re-explain. Here it is. Two honest facts shape it:

- **A fresh chat CAN self-serve everything local** — find the next story, claim
  it, study the scripture, write the prompt sheet, pass the face gate, write the
  narration, assemble, QC. That is the bulk of the work and it needs zero talking
  from you.
- **The Flow picture burst cannot run unattended.** Only one chat can drive Chrome
  at a time, and the Jesus-face rule needs a real eyeball. So the cron does all
  the local prep and **stops** at the picture step. When you sit down, the story
  is prepped and waiting — you just do the burst and give your yes.

That's the deal: the cron removes the re-explaining and all the local grind. You
stay the eyeball on pictures and the final yes. That's what you actually want —
you said "tell me that I did that and I check it off."

---

## Run one job by hand (any time)

```bash
cd ~/Desktop/MBM/media-production
./next-job.sh
```

It pulls, claims the next open story, opens a fresh Claude chat already pointed at
it. When that video's done, run it again for the next. This alone kills the
re-explaining — you never paste a kickoff again.

---

## Turn on the cron (per computer — do this once on each of the 4)

The cron fires `next-job.sh --prep-only --spawn` on a schedule. `--prep-only`
keeps it unattended-safe (stops before Chrome). `--spawn` opens the chat in a new
terminal window so you can watch it. The lock file means it will NOT pile up — if
a job is still running on that machine, the tick does nothing.

Install it (copy-paste this whole block into that computer's terminal):

```bash
( crontab -l 2>/dev/null | grep -v 'next-job.sh';
  echo '*/30 * * * * DISPLAY=:0 /home/noremacttevol/Desktop/MBM/media-production/next-job.sh --prep-only --spawn >> /home/noremacttevol/Desktop/MBM/media-production/.cron.log 2>&1'
) | crontab -
```

That checks every 30 minutes: if the machine is idle and there's an open story,
it preps the next one. Change `*/30 * * * *` to taste:
- `*/30 * * * *` — every 30 min (default)
- `0 * * * *` — top of every hour
- `0 9,13,17,21 * * *` — four set times a day

Turn it off any time:

```bash
crontab -l | grep -v 'next-job.sh' | crontab -
```

See what it's been doing: `tail -f ~/Desktop/MBM/media-production/.cron.log`

---

## Want it fully hands-off, no window to watch?

Drop `--spawn` and it runs headless (`next-job.sh --prep-only`). The chat preps
the story, updates the queue, pushes, and exits — no window at all. You'd walk up
to a stack of prepped stories and just do picture bursts + approvals in a batch.
Headless needs your Claude login to be non-interactive on that machine; if a run
logs an auth prompt in `.cron.log`, run one `claude` by hand there once to sign in.

---

## The one thing to watch: shared Flow credits

All machines share the "MBM Story Videos" Flow project and its credits. The cron
never touches Flow (that's the `--prep-only` boundary), so the cron can't burn
credits. Credits only move when YOU do a burst. Keep doing bursts one machine at a
time and nothing collides.

---

## If two machines ever grab the same story

They can't hold it — the claim is a git push. Whoever pushes first owns it; the
other gets a rejected push, pulls, and `next-job.sh` automatically rolls to the
next open row. Worst case you lose ten seconds, never a whole build.
