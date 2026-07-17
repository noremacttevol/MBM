# Feed Home Page — Rules & Flow (LAW, approved by Cameron 2026-07-17)

> This is the authoritative spec for how the Feed tab's home page and page flow
> behave. Any model building MBM reads this before touching the feed. It overrides
> older feed notes where they conflict. Implemented in `mobile/src/store/useAppStore.ts`
> (page engine), `mobile/src/screens/FeedScreen.tsx`, `mobile/src/components/WheelNav.tsx`.

## The one-paragraph plan (Cameron's words, approved)

The home page is the fresh stuff we prescribe — videos, verses, questions, invitations.
A person can sit on it forever. If they ignore it all and swipe right, they get a new
page that works exactly the same, and home stays home — they're just venturing into new
prescribed pages, and we quietly note what they skipped. But the moment they interact
with something — watch a video to 90%, tap Read on a verse, check "this helped me," save
it, chat about it, or answer a question — it counts. Then when they try to scroll past
that item, we hold them for a beat, drop a fresh new thing into its place, and file the
finished one into their history on the left. They never get pulled off home; home just
keeps refreshing as they engage. Left of home = everything they've interacted with, to
revisit anytime. It's listening first, then prescribing more of Jesus based on what they
respond to — milk now, deeper later. (This mirrors how Jesus taught: listen, ask, then
give more as the person is ready.)

## The wheel (page markers)

- **HOME is a fixed anchor**, marked with the ⌂ home icon. It never moves.
- **Right of ⌂ = new pages** the person swiped to for more content (ignored/unreviewed).
  Each is a plain dot. The more they ignore, the more dots pile to the right.
- **Left of ⌂ = history**: pages holding what they've interacted with. Plain dots too.
- The dot you're currently on is highlighted ("you're here"). Tap ⌂ to jump home anytime.
- Ignored right-pages are ephemeral: they **recycle (clear) when the app is closed**.
  Home and the left history persist.

## What "interacted / seen" means (the standard)

Any ONE of these counts as interacting with an item:
- Watched the video to **90%**.
- Tapped **Read** on a verse (whether it opens inline in-app or links out — either way
  the Read tap is the interaction; an in-app verse never needs to leave the app).
- Checked **"this helped me"** (the takeaway checkbox).
- **Saved** it to the journal.
- **Chatted** about it ("Talk about it").
- **Answered** a question or acted on an invitation.

## Flow rules

1. **Ignoring is free.** Scroll past anything you didn't interact with — it stays put,
   home stays home. Swipe right for a whole new page that behaves identically. We record
   what was skipped, but nothing is forced.
2. **Interacting earns a swap.** Once an item is interacted with, the next time the person
   scrolls it (mostly) out of view, we HOLD the scroll for ~2 seconds, visibly drop fresh
   content into that exact slot, and file the finished item into the history on the left.
3. **Never get pulled off the page.** Interacting and swapping keeps the person exactly
   where they are. Filing to history happens on the left WITHOUT scrolling them there.
4. **Swaps happen on home AND on the new right pages** — anywhere the person can interact.
   History pages (left) are frozen and never swap.
5. **The "you've walked through this" banner appears ONLY on history pages** (left of home)
   — never on home, never on the new right pages.
6. **A completed page renews.** As every slot on a page gets interacted with and swapped,
   the page keeps refreshing with new prescribed content — the person can stay on home
   forever and always have something new.

## Why (the mission)

The whole feed prescribes the good news of Jesus Christ the way the Church of Jesus Christ
of Latter-day Saints understands it — but in **milk** form: we never name the doctrine to a
new seeker. We listen (what they interact with, ignore, save, ask), and prescribe more of
what lands. As signals show they're ready (bridging), we show deeper content chosen for
them. The home page is the conversation; interaction is how they talk back; history is the
record of that conversation, which they own and can revisit.
