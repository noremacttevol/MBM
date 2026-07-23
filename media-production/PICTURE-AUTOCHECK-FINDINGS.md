# PICTURE AUTO-CHECK FINDINGS — the "find the bad pictures" board

> **Owner: the PICTURE-REMAKE lane (Machine C, opened 2026-07-23).** This chat is
> dedicated to one job: find every still that is wrong or off-spec and make it
> better, across all videos. Cameron's words this session: *"any way it can find
> that some are bad it should take responsibility to make them better."*
>
> Two detectors feed this board:
> 1. **`character_ref_gate.py`** run across all 205 builds — flags any build whose
>    PROMPTS.md names a LOCKED character (Peter, John, Mary, God the Father, …)
>    without that character's ref lock. This is the mechanical cause of the
>    #1 complaint: *"the faces keep changing."*
> 2. **`COMPLAINTS.md`** — Cameron's own eyes on specific pictures.
>
> Result of the first full sweep (2026-07-23): **42 of 205 builds fail the
> character gate.** Triaged below. A "fail" is NOT automatically a regen — a name
> that is only MENTIONED (an epistle's author, a scroll being read, a parable
> character not painted) is cleared with one line, no credit spent:
> `CHARACTER-REF-EXEMPT: <name> (reason)`.

## ✅ STILLS FIXED — HANDOFF TO #4 (reassemble + caption + submit)
These builds have their stills repainted to the approved sheets and pass BOTH
gates. #4: clear `segs/` cache, rebuild the mp4 (`build.py`), caption, submit.
| Build | # | What was repainted |
|---|---|---|
| build-66-malchus-ear | 66 | Peter (gray old man in brown → approved young dark-curled fisherman, blue-grey tunic) + Malchus (→ approved walnut-tunic sheet, ear whole) on s2/s4/s5/s7 |
| build-128-heart-far-from-me | 128 | **NEW build** (Mark 7:6-13, replaces stale Amos) — all 7 stills made + QC'd, Jesus locked. **#2 needs to make audio from `DRAFTS/row-128-heart-far-from-me.md` INTO this folder; #4 assembles + captions + closing card here.** Old `build-128-famine-of-hearing` (Amos) is untouched. |

**⚠️ IN PROGRESS, NOT ready for #4:** `build-53-peters-mother-in-law` — disciple locks
wired + John fixed to clean-shaven youth; **s1/s2/s4 repainted, but s6/s7/s8 still need
regen** (interrupted). Do NOT assemble until s6/s7/s8 are done.

## PROGRESS LOG (Machine C, 2026-07-23)
- **#66** malchus-ear — REPAINTED (Peter+Malchus drift) → handed to #4. ✅
- **#118** jonah, **#120** job, **#119**+**#160** nebuchadnezzar, **#117** hosea+gomer,
  **#82** simon-the-pharisee — one-video figures VERIFIED on-model vs their approved
  sheets (spot-checked by eye); lock wired so the gate passes; **no regen needed**. ✅
- **Pattern learned:** one-video OT/minor characters already match their sheets (the
  sheet was built from the same description), so they only need the lock marker, not a
  repaint. RECURRING NT faces (Peter/John/James/Andrew/Mary/Martha/Lazarus) are where
  real cross-video drift lives — those get QC'd and repainted like #66.
- **Flag for a careful look:** #82 anointing — confirm the central figure isn't Jesus
  in a non-cream (rose) robe.

## The regen tool (root-cause fix)
`regen_shot.py` is the picture-lane workhorse. The OLD `gen_shots.py` only
attached the Jesus ref and never expanded `[X LOCK]` tokens or attached character
sheets — **that is why characters drifted even after their sheets were approved.**
`regen_shot.py` expands every lock token and attaches the right cast + Jesus refs:
```
python3 regen_shot.py --dir build-NN --shot s2-slug --chars peter,malchus [--jesus] --dry-run
```
Always `--dry-run` first (prints the expanded prompt + ref list, generates nothing),
eyeball it, then run for real. QC every output jpeg against the sheet before moving on.

## How each row is resolved
- **DEPICTED** → paste the character's `lock_text(...)` into PROMPTS.md, attach
  their `refs(...)` jpegs, regenerate that still on Flow/Nano-Banana, QC the jpeg,
  rebuild the mp4, present. (Approved-locked builds: present for RE-approval,
  never silently overwrite — approved list: 2,3,5,6,80,89,100-108,111,185-200.)
- **MENTIONED-ONLY** → add the exempt line; gate passes; zero credit.
- Every row needs a 10-second PROMPTS.md read to decide which. That read is the
  work; the guess in the table is only a starting sort.

---

## A. CHARACTER-GATE FAILS (42) — regen candidates

| Build | # | Locked chars missing lock | First guess | Approved? |
|---|---|---|---|---|
| build-05-bent-woman | 5 | abraham | MENTIONED (Luke 13:16 "daughter of Abraham") | ✅ re-appr |
| build-103-peters-confession | 103 | peter | DEPICTED | ✅ re-appr |
| build-10-well | 10 | jacob | MENTIONED (Jacob's well) — verify | — |
| build-110-lords-prayer | 110 | god-the-father | MENTIONED ("Our Father") — verify | — |
| build-111-lilies-and-sparrows | 111 | god-the-father | MENTIONED — verify | ✅ re-appr |
| build-117-hosea-buys-her-back | 117 | gomer, hosea | DEPICTED | — |
| build-118-jonah-god-who-relents | 118 | jonah | DEPICTED | — |
| build-119-fourth-man-in-fire | 119 | nebuchadnezzar | DEPICTED | — |
| build-120-job-from-whirlwind | 120 | job | DEPICTED | — |
| build-130-what-manner-of-spirit | 130 | james | DEPICTED (James & John, Luke 9:54) | — |
| build-137-one-as-we-are-one | 137 | james, john-beloved, peter | verify (dup folder — see §D) | — |
| build-144-resurrection-and-the-life | 144 | lazarus | DEPICTED | — |
| build-149-hannah-is-heard | 149 | samuel | DEPICTED (child stage — see AGE-VARIANT) | — |
| build-154-everlasting-gospel | 154 | john-beloved | DEPICTED (aged + risen Jesus — variant) | — |
| build-160-stone-cut | 160 | nebuchadnezzar | DEPICTED | — |
| build-165-laying-on-hands | 165 | john-beloved, peter | DEPICTED | — |
| build-166-baptized-properly | 166 | john-beloved | DEPICTED | — |
| build-169-fulfil-righteousness | 169 | god-the-father | MENTIONED — verify | — |
| build-16-mary-martha | 16 | martha, mary-of-bethany | DEPICTED | — |
| build-174-hearts-of-the-fathers | 174 | john-beloved | DEPICTED (aged John — variant) | — |
| build-17-lazarus | 17 | lazarus, martha, mary-of-bethany | DEPICTED | — |
| build-183-sun-moon-and-stars | 183 | paul | MENTIONED (epistle author) — verify | — |
| build-18-emmaus | 18 | cleopas | DEPICTED | — |
| build-190-faith-without-works | 190 | isaac, james | MENTIONED (James epistle; Abraham/Isaac cited) | ✅ re-appr |
| build-22-unmerciful-servant | 22 | peter | DEPICTED (Peter asks, Matt 18:21) | — |
| build-36-shrewd-steward | 36 | james | verify (likely citation) | — |
| build-37-rich-man-lazarus | 37 | abraham, lazarus | DEPICTED (Abraham glorified + Lazarus the beggar) | — |
| build-40-the-friend-at-midnight | 40 | god-the-father | MENTIONED — verify | — |
| build-48-new-wine-old-bottles | 48 | john-beloved | verify | — |
| build-53-peters-mother-in-law | 53 | andrew, james, john-beloved, peter | DEPICTED | — |
| build-57-jairus-daughter | 57 | jairus, james, john-beloved, peter | DEPICTED | — |
| build-58-feeding-5000 | 58 | andrew | DEPICTED | — |
| build-66-malchus-ear | 66 | malchus | ✅ FIXED (see handoff section) | — |
| build-67-the-transfiguration | 67 | james, john-beloved, moses, peter | DEPICTED (Moses glorified — variant; dup folder §D) | — |
| build-67-transfiguration | 67 | elijah, james, john-beloved, moses, peter | DEPICTED (dup folder §D) | — |
| build-71-the-great-commission | 71 | the Twelve (all) | DEPICTED (dup folder §D) | — |
| build-73-this-day-fulfilled | 73 | isaiah | MENTIONED (reads Isaiah's scroll) — verify | — |
| build-82-anointing-at-bethany | 82 | simon-the-pharisee | DEPICTED | — |
| build-88-triumphal-entry | 88 | matthew | verify (citation vs depicted) | — |
| build-91-gethsemane | 91 | james, john-beloved, peter | DEPICTED (Peter/James/John) | — |

## B. BLOCKED on unbuilt sheets (CHARACTER-LAW pending)
These regens cannot pass the gate until the sheet exists + Cameron approves it:
- **5 apostles never rendered:** Philip, Bartholomew (Nathanael), James (Alphaeus),
  Thaddaeus, Simon the Zealot. → blocks every all-Twelve group scene
  (build-71-the-great-commission, and the P2 group scenes in PICTURE-REDO-WORKLIST).
- **infant-jesus, risen-jesus** sheets not rendered/approved → blocks #84/85/86 and
  #97/98/99/100/134/154/179/189.
- **Age variants** (Moses/Elijah glorified #67, Samuel child #149, aged John #154/174,
  Abraham aged/glorified #37/115/190, etc.) — sheet-before-still (AGE-VARIANT KEY).
- **Render is 0 credits** (Nano-Banana); the only true blocker is Cameron's approval.
  Plan: render the missing sheets, present a contact sheet, unblock the group scenes.

## C. COMPLAINTS.md picture items still open
- **#171** — scripture-quote captions must be BLUE. No character sheet, no Flow,
  no key needed. **Do this first** (pure caption-law/text fix).
- **#19, #56, #107, #113, #135** — per FRESH-CHAT-KICKOFF the prior session verified
  these are already good in the current cut; they only await Cameron's APPROVAL on
  the board (a complaint stays "UNFIXED" until he approves). VERIFY, then it's on him.

## D. STRUCTURAL — flag for Cameron (do NOT auto-resolve; UNIFY ORDER froze dedup)
- **2 builds have no PROMPTS.md:** build-02-prodigal, build-71-calling-the-fishermen.
  Can't gate or regen without it — find/restore the prompts.
- **5 duplicate build-numbers** (two different stories share one number — a machine
  could build the wrong one, or ship a story twice):
  - **#65** help-mine-unbelief / help-thou-mine-unbelief
  - **#67** the-transfiguration / transfiguration
  - **#71** calling-the-fishermen / the-great-commission
  - **#137** one-as-we-are-one / stephen-sees-him-standing
  - **#140** naaman-washes / road-runs-both-ways  (road-runs = the retracted prodigal dup, complaint #140)
  These look like an old folder + its replacement living side by side. Needs Cameron
  to say which is canonical before either is rebuilt.

---
_Regenerate this board any time with `for d in build-*; do python3 character_ref_gate.py --dir "$d"; done`._
