# MBM Security Report — July 2, 2026 (plain language)

I audited the whole app for the ways someone could attack it, fixed the real problems the same day, deployed the fixes, and tested them live. Here is what was true, what I changed, and the one thing only you can do.

## What was already safe

Your Anthropic API key was never in the app, never in the code on GitHub, and never in the git history — I searched every commit. The Firebase key that IS in the app is supposed to be public (that is how Firebase works; the protection is the rules, not the key). Your Firestore rules were well built: each anonymous person can only ever read their own thread, can only write as themselves, and nobody can delete anything. The server had zero known-vulnerable packages. The signing keys and service-account files on this computer are correctly kept out of git.

## The one real hole, and what I did about it

The proxy server on Railway — the middleman that holds your Anthropic key so the app never does — would answer ANYONE on the internet, not just your app. The proxy's address ships inside every copy of the app, and anyone who dug it out could use your Anthropic key as their own free AI, at any volume, with you paying the bill. That was the attack most worth worrying about: someone quietly draining your API money.

The proxy now enforces, live as of today:

- Each internet address gets at most 10 AI requests per minute and 300 per day. Real users never notice; a thief hits a wall instantly. Tested live: the 11th rapid request is refused.
- A total ceiling of 5,000 AI requests per day across everyone — a fuse that caps the worst possible day for your wallet even if an attacker uses thousands of addresses.
- Size limits on every request, so nobody can send giant conversations that cost extra tokens.
- The model is locked server-side to Haiku — nobody can make your key run a pricier model.
- The "talk to a human" and fact-check inboxes are rate-limited and capped too, so nobody can flood you with spam or fill the server's disk.

All of this is live and none of it breaks the iOS build sitting in Apple's review queue — I verified a normal chat call still works exactly as before.

## The lock that tightens later (already in place, waiting)

Future app builds now carry a private app token that proves "this request came from the real MBM app." The server knows the token but is NOT enforcing it yet — if it did, the builds people already have (including the one Apple is reviewing) would break. Once a build carrying the token has shipped and people have updated, one Railway setting (REQUIRE_APP_TOKEN=1) shuts the door on every outside caller for good. I or any future session can flip it; it is written in the session log so it will not be forgotten.

## Firestore got tighter too

The rules now also cap how large a message document can be, so a hostile script cannot stuff huge junk into your database and run up storage costs. Published live today (I added a small script, admin/deploy-rules.mjs, so rules can be published from here without the Firebase console).

## The one thing only you can do

Set a monthly spend limit on your Anthropic account, at console.anthropic.com under Billing / Limits. Pick a number you would never miss (even $25). That is the final backstop: no matter what any attacker ever manages, your card cannot be charged past it. Five minutes, one time.

## Things I checked that need nothing

- The app's stored data lives on each person's own phone; there is no central pile of user data to breach beyond the small Firestore inbox, which the rules protect.
- The admin inbox on the proxy is protected by a token only you have.
- The 16 "vulnerabilities" npm reports in the mobile folder are all in Expo's build tools, which run on this computer, not in the app users install. Nothing to do; they clear whenever Expo is next upgraded.
- The direct-to-Anthropic code path in the app only activates if a key is deliberately placed in a local dev file; no key ships in any build (I checked the build config).
