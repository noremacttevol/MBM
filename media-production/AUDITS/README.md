# SESSION AUDITS — the data we learn from (Cameron's stand-down order, 2026-07-15)

Every session, before it ends: write ONE file here named
`audit-<machine>-<date>-<n>.md` (e.g. audit-C-2026-07-15-2.md), commit, push.
Format — exactly these fields, short answers, no prose essays:

```
machine: C
rows_worked: 101 (built), 111 (built), 112 (8/10 stills, blocked)
minutes_per_video: 101=55, 111=40
stills_generated / rerolled: 22 / 5
reroll_reasons: 2x panels, 1x wrong time of day, 2x anatomy
errors_hit_and_fix: Flow logged out mid-run -> re-login, resumed; CAPTCHA rate-limit
  after ~25 gens in an hour -> wait 20 min, slow cadence to ~1 gen/2min
biggest_token_waster: screenshots while navigating Flow (before JS-download switch)
what_should_change: <one or two concrete rule/playbook changes>
tokens_estimate: rough % of a session's context used per video, if known
```

Why: Cameron is designing the v4 protocol from this data — videos per session,
tokens per video, zero-error steps. Honest numbers beat good news. A blocked or
failed session's audit is MORE valuable than a smooth one's.
