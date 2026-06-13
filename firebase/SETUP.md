# Firebase setup — the "talk to a real person" inbox

This is the one cloud piece in the whole app. It carries a person's note to you and
brings your reply back into their app, live. Everything else stays on the phone.

You only do this once. Until it's filled in, the app quietly uses the on-device
queue instead — nothing breaks.

---

## 1. Make the project (free)

1. Go to https://console.firebase.google.com and click **Add project**.
2. Name it `mbm` (or anything). Turn Google Analytics **off** — you don't need it.
3. When it's ready, click the **web** icon `</>` to add a web app. Name it `mbm`.
   Firebase shows you a `firebaseConfig` block with six values. Keep that tab open.

## 2. Turn on Anonymous sign-in

This is what gives each phone a hidden identity with no login screen.

1. Left menu → **Build → Authentication → Get started**.
2. **Sign-in method** tab → **Anonymous** → toggle **Enable** → **Save**.

## 3. Make the database

1. Left menu → **Build → Firestore Database → Create database**.
2. Pick **Production mode** (the rules below lock it down). Choose any location.

## 4. Paste the security rules

1. In Firestore, open the **Rules** tab.
2. Replace everything with the contents of `firestore.rules` (in this folder).
3. Click **Publish**.

These rules mean: each phone can only ever read and write its own messages. No
phone can read anyone else's thread.

## 5. Put the six values in the app

Open `mobile/.env` and fill in the six `EXPO_PUBLIC_FIREBASE_*` lines from the
config block in step 1:

| Firebase config field | `.env` line                                |
|-----------------------|--------------------------------------------|
| `apiKey`              | `EXPO_PUBLIC_FIREBASE_API_KEY`             |
| `authDomain`          | `EXPO_PUBLIC_FIREBASE_AUTH_DOMAIN`         |
| `projectId`           | `EXPO_PUBLIC_FIREBASE_PROJECT_ID`          |
| `storageBucket`       | `EXPO_PUBLIC_FIREBASE_STORAGE_BUCKET`      |
| `messagingSenderId`   | `EXPO_PUBLIC_FIREBASE_MESSAGING_SENDER_ID` |
| `appId`               | `EXPO_PUBLIC_FIREBASE_APP_ID`              |

Then restart the app with a clean cache: `npx expo start --clear`.

These six are **public-safe** — they're meant to ship inside the app, and the
rules are what actually protect the data. `.env` is gitignored, so they don't get
committed regardless.

## 6. What you (the admin) use

You reply to people from a small local admin page (built separately). That page
uses a **service account key** that bypasses the rules so you can see every
thread. That key is the one secret that must **never** go in the app or in git —
it lives only on your machine. (Firebase console → Project settings → Service
accounts → Generate new private key, when the admin page is ready.)
