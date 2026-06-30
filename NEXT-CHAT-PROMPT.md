# Prompt to paste into the next MBM chat

Copy everything inside the line below into a brand-new chat in the MBM project.

---

You are my Principal Systems Architect and advisor on MBM (Milk Before Meat). Before anything
else, follow the session-chain protocol in CLAUDE.md: read the top entry of SESSION-LOG.md,
confirm its commit hash is in `git log`, then read START-HERE.md and AGENT-RULES.md so you know
the true current state. Give me a one-line recap of the last session and its commit hash, then
begin.

**This chat has one big job: organize my MBM folder and get all my materials release-ready. I am
not a developer — when I open my MBM folder it's cluttered and I can't tell what's mine to read
vs. what's just code you work with. Take full initiative; don't hand me homework or make me decide
technical things. Build it, then tell me plainly what you did.**

Here's what I need, in order:

1. **Sort everything into a clear, human-friendly arrangement.** Reorganize the folder (or add a
   clear labeling/index layer over it) so it's obvious at a glance what each thing is. I want three
   clear buckets:
   - **"For me" / what Cameron should read or look at** — documents, plans, brochures, the roadmap,
     things I open when I need to do my side of the work.
   - **"To print"** — the exact things I should print off to have ready when I review MBM with
     people and start spreading it (a real print kit).
   - **"Computer only"** — the code, the website files, internal/agent stuff I don't need to see.
     Tuck it away or clearly mark it so it's not the first thing I trip over.

2. **Make me a simple table of contents / index** at the top level — a single file that says, in
   plain language, "here's everything, here's where it lives, here's what it's for, click here for
   X." If a folder named something like `FOR-CAMERON/` and `TO-PRINT/` makes it easier, do that.

3. **Build the print kit.** Put in one place (and tell me) everything I should physically print to
   have ready: the roadmap PDF, the brochures, the members-only outreach brochure, any outlines, and
   the website sign-up instructions. As my advisor, decide what's actually worth printing and say so.
   Keep printable versions light on ink, like the roadmap PDF we made.

4. **Go back through ALL of it and make it consistent and correct for the release phase.** This is
   the polish pass. Check every brochure, outline, the roadmap, and the website against each other:
   - Make sure the website address (milkb4meat.org) is shown correctly everywhere — on the
     brochures, the overall look, the members-only outreach brochure, sign-up instructions.
   - Make sure the website itself is correct and that it links to the public PDFs/documents people
     should be able to find (for example, the roadmap PDF — confirm there's a clear link to it, and
     add links to any brochures/outlines that should be downloadable).
   - Fix anything stale, mismatched, or out of date so a stranger could pick up any single piece and
     it would line up with everything else.

5. **Tell me what, if anything, still needs me.** Only flag the things that genuinely require me
   (passwords, an auth screen, a physical print run, a phone call). Everything else, just do.

When you've reorganized, screenshot/verify the website still works, and present me the new index
file plus the print kit so I can see it. Then update SESSION-LOG.md and ask me before pushing
anything live or committing.

---

(Background context the new chat will already have from the project: the React Native + Expo app is
built and in an invite-only testing phase — Android closed internal test, iPhone on TestFlight,
awaiting public App Store approval. The promotional website is live-ready at milkb4meat.org with a
new Roadmap tab and printable roadmap PDF. The accounts all exist and are paid. The real near-term
work is organization, brochures, and getting the print/outreach materials consistent for the
release push.)
