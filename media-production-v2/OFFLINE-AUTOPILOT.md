# MBM offline production operator

The unattended reasoning worker runs on Machine A through Codex OSS mode and
Ollama. Its default model is `qwen3.5:27b`, selected on this exact RTX 3090
after it passed both repository tool-use and rendered-frame caption tests.
`gpt-oss:20b` is installed but failed the production tool-use gate here, so it
is not the default.

"Offline" applies to the reasoning model. Picture generation (Gemini), voice
generation (ElevenLabs), source coordination (GitHub), Reviewer data and
publishing (Firebase) still use their existing online services.

## What the loop guarantees

- One GPU worker at a time.
- The launcher claims the selected row on both coordination boards and pushes
  that claim before the model may inspect, generate or edit production work.
  A rejected claim push stops the tick.
- Current Reviewer complaints before new production.
- Lowest numbered actionable complaint first.
- Current-cut hash matching, so a complaint against an older replaced cut is
  not rebuilt again.
- Complaint classification before spending: caption-only fixes reuse every
  picture and preserve audio; audio-only fixes generate no pictures; visual
  complaints get new pictures only after the current rendered frame proves
  they are necessary.
- The same claim-by-push, Jesus/cast locks, face gate, full-cut visual QC,
  narration QC, audio-lock, assembly, deploy and live-verification rules used
  by the former Claude worker.
- Existing unrelated tracked changes and untracked production files are
  preserved.
- Every extracted complaint frame and full-cut QC sheet is sent to the local
  vision model through `offline_vision.py`; its literal result is recorded in
  the row QC. A text-only worker is forbidden to claim that it viewed pixels.
- Reviewer candidates stay Reviewer-only. The worker may update only the
  row's existing `site/review.html` card and must never copy an unapproved cut
  into `site/story-videos/` or the app/gallery.
- Context-bounded retrieval keeps append-only historical boards from crowding
  the actual row out of a local model's working memory. The worker reads the
  master rules, the current status header, the full rebuild rubric, the exact
  row outline and targeted shared lessons; it never dumps whole board-history
  rows into its context.

## Commands

Preview the next selected job without changing anything:

```bash
media-production-v2/offline-autopilot.sh --dry-run
```

Run one foreground job:

```bash
media-production-v2/offline-autopilot.sh
```

Watch the dispatcher and worker logs:

```bash
tail -f media-production-v2/autopilot-logs/autopilot.log
```

```bash
tail -f media-production-v2/autopilot-logs/offline-cron.log
```

Start the persistent five-minute loop:

```bash
( crontab -l 2>/dev/null | grep -v 'autopilot.sh'; echo '*/5 * * * * /home/noremacttevol/Desktop/MBM/media-production-v2/offline-autopilot.sh >> /home/noremacttevol/Desktop/MBM/media-production-v2/autopilot-logs/offline-cron.log 2>&1' ) | crontab -
```

Pause future jobs (a foreground job already running is allowed to finish):

```bash
crontab -l | grep -v 'autopilot.sh' | crontab -
```

For an interactive local Codex session in this repository, use the installed
profile:

```bash
codex --profile mbm-offline --oss
```
