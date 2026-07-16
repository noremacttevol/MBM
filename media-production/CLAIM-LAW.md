# CLAIM LAW — no two machines ever build the same row (2026-07-16, Hermes)

> Written after two machines both painted row 73 (build-73-nazareth-synagogue AND
> build-73-this-day-fulfilled) — duplicate stills, wasted Flow credits. This law
> closes that hole. EVERY brain/painter/all-in-one machine obeys it before touching
> any row. The check is on the ROW NUMBER (the build-NN prefix), never the folder name.

## THE TWO RULES

### 1. DEDUP ON THE NUMBER, NOT THE NAME
Before you take row NN, run this check first:
  git pull --rebase
  Does ANY folder matching `media-production/build-NN-*` already exist? (match the
  number after "build-", ignore everything after the next dash)
  Is row NN marked CLAIMED or Built (✅) in QUEUE.md?
If EITHER is true → that row is taken. SKIP IT. Take the next open number.
A folder named build-73-anything means 73 is DONE or IN PROGRESS. Do not make a
second build-73-* under a different name. There is ONE folder per row, ever.

### 2. CLAIM BEFORE YOU PAINT (write it down FIRST, then work)
The instant you decide to take row NN — BEFORE generating narration, prompts, or a
single still — record the claim and PUSH it, so every other machine sees it:
  a) Create the folder media-production/build-NN-short-name/
  b) Create an empty marker file inside it: CLAIMED-by-<machine>-<date>
     (e.g. CLAIMED-by-W1-2026-07-16)
  c) git add that folder, commit "claim: build-NN by <machine>", git pull --rebase,
     git push  — IMMEDIATELY, before any Flow work.
Only after the claim is pushed do you build the sheet / paint the stills.
If your `git push` of the claim fails because someone else already pushed a
build-NN-* folder → they beat you to it. Delete your local folder, take the next
open number.

## WHY THIS ORDER MATTERS
Painting first and claiming later is what caused the row-73 duplicate: two machines
both saw 73 "free," both painted it, both pushed different folder names. Pushing the
CLAIM first makes the race impossible — whoever pushes the claim first owns the row;
the loser's push is rejected on pull and they move on. The repo is the memory; the
claim must be IN the repo before the work starts, not after.

## SCOPE DISCIPLINE (the other half of the row-73 mistake)
build-73-nazareth-synagogue also PAINTED PAST its draft — it added the cliff/mob
"thrust him out" rejection scene the draft deliberately left out. Paint the DRAFT's
storyboard beats, not your own extension of the story. If a draft stops at a verse,
stop there. The draft's scope is law; do not add scenes it omitted.
