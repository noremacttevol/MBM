# MBM admin inbox

Your private desk for the "talk to a real person" threads. This runs **only on your
machine** — it never ships in the app. It reads every person's thread and lets you
reply; your reply lands in their app live.

## One-time setup

1. **Get the service-account key** (this is the admin credential that bypasses the
   security rules — it is the one secret that must never go in the app or git):
   - Firebase console → click the **gear** → **Project settings**.
   - **Service accounts** tab → **Generate new private key** → confirm.
   - A `.json` file downloads. Move it into this folder and rename it exactly:
     ```
     admin/serviceAccount.json
     ```
   - `.gitignore` already keeps it out of the repo. Never share it.

2. **Install once:**
   ```
   cd admin
   npm install
   ```

## Running it

```
cd admin
npm start
```

Then open **http://localhost:4545** in your browser.

- Left side: everyone who has written in, newest first. A green number means unread.
- Click a person to read their whole thread. Opening it marks their notes as read.
- Type in the box and **Send** — your reply appears in their app the moment you send,
  labeled simply as "a real person."

The page refreshes itself every few seconds, so new notes appear on their own.

## What stays private

- The six `EXPO_PUBLIC_FIREBASE_*` values in the app are public-safe and ship in the
  app; the rules protect the data.
- **This** key (`serviceAccount.json`) is the powerful one. It lives only here, on
  your computer. Do not commit it, email it, or paste it anywhere.
