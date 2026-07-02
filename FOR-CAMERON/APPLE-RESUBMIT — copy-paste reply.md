# ✅ NO LONGER NEEDED — the resubmission was completed via the API on 2026-07-02.
# Build 8 is WAITING_FOR_REVIEW. Nothing for you to do. Kept only for reference
# in case Apple writes back with questions.

# Apple resubmission — your copy-paste reply

## Where to paste it
1. Sign in at https://appstoreconnect.apple.com (your Apple Developer account).
2. Click **Apps → Milk Before Meat**.
3. On the left, under the 1.0 version, you'll see the rejection — open
   **App Review** (or the banner that says "View messages" / "Resolution Center").
4. Paste the reply below into the message box and send it.
5. On the version page, under **Build**, remove build 6 if it's still attached and
   select the NEW build (**build 8** — it appears after Apple finishes processing,
   usually 10–30 minutes after upload).
6. Press **Add for Review** / **Resubmit for Review** (blue button, top right).

That's it. Steps 1–6 are the only human parts; everything else is already done.

## The reply (copy everything between the lines)

---

Hello, and thank you for the review.

We have resolved the issue in build 8 (version 1.0). The concern was that user
text was sent to a third-party AI service (Anthropic's Claude, which powers the
app's conversational voice) without disclosure or consent. In build 8:

1. Before anything a user writes can be sent to the AI service, the app now
   shows a plain-language consent screen as the final step of onboarding. It
   names Anthropic, states exactly what is transmitted (the user's messages,
   and, if shared, their first name and self-described faith background) and
   why (solely to generate the response shown in the app).

2. Consent is opt-in. If the user declines, no user content ever leaves the
   device: every AI call site in the app is hard-blocked, and the app continues
   to work fully in its offline mode. The chat screen shows the same consent
   choice in place of the message composer for users who have not decided.

3. The choice can be reversed at any time via a clearly labeled control on the
   user's Profile screen.

4. Our privacy policy (https://milk-b4-meat.web.app/privacy.html), linked in
   the app and on the App Store listing, has been updated to name Anthropic and
   list exactly what is transmitted and for what purpose. No data is sold, used
   for advertising, or used for tracking, consistent with our published App
   Privacy label.

Thank you for your time, and please let us know if anything further is needed.

---
