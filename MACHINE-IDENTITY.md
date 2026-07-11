# WHICH COMPUTER AM I? — the machine name-tag list

**Problem this solves:** all of Cameron's computers run Claude Code on the SAME
GitHub repo, so they all read the same files. A note inside a shared file that
says "I am the linux desktop" is read by EVERY computer — so they can't tell
each other apart, and they claim the wrong videos and write the wrong session
logs. (This bit us on 2026-07-11: a session on Machine C called itself Machine A.)

**The fix:** every computer has its own unique built-in name (its "hostname")
that the others do NOT share. This file maps each hostname to the machine it is.
Because the lookup key (hostname) is different on every computer, there is no
more mix-up.

---

## FIRST ACTION FOR EVERY CLAUDE ON EVERY COMPUTER (do this before touching the video board)

1. Run `hostname` in the terminal.
2. Find that exact hostname in the table below → that tells you which machine you are.
3. If your hostname is NOT in the table yet, STOP and ask Cameron which machine
   this is, then add the row and commit it. Never guess, and never trust a
   "this machine = ..." sentence written in any other file — only this table.

---

## The list (hostname → machine)

| Computer's built-in name (`hostname`) | Which machine it is | Confirmed |
|---|---|---|
| `cameron-lovett-MS-7C91` | **Machine C — "Linux desktop number two"** | Cameron, 2026-07-11 |
| _(unknown — fill in when that computer runs)_ | Machine A — "linux desktop" | — |
| _(unknown — fill in when that computer runs)_ | Machine B — "HP laptop" | — |
| _(unknown — fill in when that computer runs)_ | Elli's Windows laptop (extra worker) | — |

> To add your computer: run `hostname`, put the result in a new/blank row next to
> the machine Cameron says it is, and commit + push. Each computer only ever
> writes its OWN row.

## What this changes

- The machine ranked lists in `media-production/VIDEO-ASSIGNMENTS.md` are still
  MACHINE A / B / C. Use THIS file to learn which of those you are, then claim
  only from your own list.
- Ignore any older "this machine = linux desktop" style notes in the session log
  or elsewhere — they were written before this file existed and may be wrong.
  This table is the only source of truth for machine identity.
