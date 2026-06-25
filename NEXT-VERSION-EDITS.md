# MBM — Edits for the Next Version

> Backlog of fixes Cameron flagged while testing the first live internal build (1.0.0, code 4, Jun 25 2026). None are blockers — the build is live and good. Address these in the next build.
>
> STATUS (Jun 25 2026): items 1–4 below are now DONE in code (mobile/src) and type-check clean. They are NOT yet on any phone — they require a new build + install. The build/install step is what was missing when these were tested on the iPhone (they had only been written here, not coded).

## UI / polish fixes

1. **Opening screen animation is glitchy.** — DONE
   - The bottom disclaimer ("not a god" / not a real church warning) flashes on screen for a split second *before* anything else, then the rest of the screen slowly animates in.
   - Fix: sequence the intro animation so the disclaimer does not flash first. It should fade in with (or after) the rest of the content, not pop in early. Remove the jump/flicker so the cold-open feels smooth.
   - Implemented: `HookScreen.tsx` now mounts the fade-in text/CTA/disclaimer one frame after first paint (`showContent` gate + `requestAnimationFrame`), eliminating the native-driver opacity-0 first-frame flash.

2. **"Talk about it" page — title/boxes smashed on small screens.** — DONE
   - The title portion with the boxes is cramped and overlapping on smaller phone screens.
   - Implemented: `ChatScreen.tsx` header reworked — square icon buttons (much narrower than text), stacked "Real/Person" label, and the title now shrinks to fit (`numberOfLines={1}` + `adjustsFontSizeToFit`), so the two button groups no longer collide on small devices.

3. **Chat buttons: replace words with small square icons.** — DONE
   - New → **+**, History → **🕐** (clock), as 30×30 square buttons. Applied to both the AI group and the Real-person group.

4. **"Real person" label should stack vertically.** — DONE
   - Now renders "Real" over "Person" (two lines, centered) to keep the right group narrow.

## Profile fix (Cameron, Jun 25 2026) — DONE
- The "WHAT THE APP HAS NOTICED" / "WHAT WE SENSE ABOUT YOU" framing read as a creeper/surveillance vibe ("ohh we noticed this about you"). The rule was only ever: list what the app keeps, plainly, with the ability to view/edit/remove — not to announce it as observation.
- Implemented in `ProfileScreen.tsx`: relabeled to "WHERE YOU ARE RIGHT NOW" and "ABOUT YOU"; neutral note ("everything the app keeps to personalize what you see … edit or remove anything anytime"); per-item "Forget" → "Remove" with neutral confirm copy. `useAppStore.ts` `humanizeSignal` fallback no longer says "We noticed:".

## Researched, not yet built
- Tiered AI models by question importance + offline-mode quality gating: see `MODEL-ROUTING-AND-OFFLINE-PLAN.md`.

## Notes
- More fixes expected once additional testers give feedback on this first version. Keep adding here.
