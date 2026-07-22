---
description: Safely sync this machine to origin/main (rebase over the divergence) and push
allowed-tools: Bash(git status:*), Bash(git fetch:*), Bash(git pull:*), Bash(git rebase:*), Bash(git push:*), Bash(git stash:*), Bash(git log:*), Bash(git rev-list:*)
---

Sync this machine's commits to `origin/main`, following the multi-machine safety rules.
All four machines push to `main` constantly, so origin is usually hard-diverged and a
plain push will be rejected. Do this carefully:

1. Run `git status -s` and `git rev-list --left-right --count origin/main...HEAD` after a
   `git fetch` to see the divergence (left = commits on origin I lack, right = my unpushed).
2. If I have uncommitted SOURCE changes, note them — do NOT blindly autostash, because a
   concurrent session may be editing this shared tree and an autostash can sweep up THEIR
   files (this has caused conflicts on `docs/index.html` / `site/review.html`). If the tree
   is dirty with another session's work, tell Cameron and stop rather than risk it.
3. `git pull --rebase origin main`. If it hangs on the large media history for more than
   ~30s, or hits conflicts you can't cleanly resolve, STOP and report — the commits are
   durable locally and can sync from an idle machine. Never force-push.
4. On a clean rebase, `git push origin main` and confirm it succeeded.
5. Report the final state: what pushed, or exactly why it's blocked.

Never run `git push --force`, `git reset --hard`, or drop another session's stash.
