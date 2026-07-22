---
description: End-of-session chain — add a SESSION-LOG entry at the top, commit, and sync
allowed-tools: Bash(git status:*), Bash(git add:*), Bash(git commit:*), Bash(git log:*), Bash(git rev-list:*), Bash(git fetch:*), Bash(git pull:*), Bash(git push:*), Read, Edit
---

Close out this session per the SESSION-CHAIN PROTOCOL in CLAUDE.md:

1. Summarize what actually happened this session in a few bullets (what changed, what was
   built/fixed, any decisions Cameron made, and anything left unfinished).
2. Add a NEW entry at the TOP of `SESSION-LOG.md` with today's date, this machine's name,
   and that summary. Convert any relative dates to absolute. Keep the existing top entry
   below it (add a `---` separator).
3. If Cameron gave any NEW correction or rule this session, confirm it was written into
   `media-production/PRODUCTION-BIBLE.md` §1 AND the CLAUDE.md law list — if not, do it now.
4. `git add` the changed files and commit with a clear message (Co-Authored-By trailer).
5. Then run the same safe sync as `/sync`: rebase over origin and push if clean; if the
   rebase hangs or a concurrent session is live-editing the tree, commit locally and tell
   Cameron it needs a push from an idle machine. Never force-push.
6. Report the commit hash so the next session can verify the chain.
