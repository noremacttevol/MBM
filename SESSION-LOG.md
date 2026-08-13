## 2026-08-12 (cont. 91) — CAMERON'S AUTO-RELOAD RULE wired in: depleted 429 = transient, RETRY (gen backoff + live probe every tick); never "out of money", never ask him to top up — Machine A `Dev`, process-engineer session

**Commit:** this push. Cameron: "its never empty you just have to try it again it loads more cash automatically remember this."

- Probed the live API 3× (~30 s apart) at the time of his message: still `429 prepayment depleted` — reported as observation only, per the new rule.
- **v2_gen_api.py:** depleted 429 no longer `SystemExit("OUT OF MONEY")` — patient in-run retries (30/60/120/240/300 s), then a soft error saying the next tick retries; rows resume where they stopped.
- **autopilot.sh:** billing state now decided by a LIVE $0 probe each tick (3 tries, 10 s apart), never stale log-greps; a failed probe defers paid work ONE tick and re-probes — the cron loop is the retry engine and resumes the instant Google's auto-reload lands. Free (audio/author) work continues regardless. Idle message rewritten (no more top-up nagging).
- Memory: `gemini-prepay-auto-reload` (feedback). Monitor armed in-session to announce the moment the API opens.

---

