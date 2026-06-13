/**
 * Firebase client — the thin, free cloud channel that carries a person's words
 * to a real human and brings the reply back INTO the app.
 *
 * The whole app stays local-first. This is the ONE place that reaches the cloud,
 * and only for the "talk to a real person" inbox — exactly the delivery channel
 * the on-device ConnectRequest queue was always designed to grow into.
 *
 * No login, ever: every install signs in ANONYMOUSLY, so the device gets a real
 * hidden identity (auth uid) without the person creating an account or giving an
 * email. Firestore security rules on the server scope every read/write to that
 * identity — a person can only ever see their own thread.
 *
 * Key safety (Cameron's standing rule):
 *   - The EXPO_PUBLIC_FIREBASE_* values are the Firebase "web config." They are
 *     DESIGNED to be public and ship in the app; the security rules are what
 *     protect the data. These are the only Firebase values the app ever holds.
 *   - The ADMIN service account (which bypasses the rules) NEVER goes in the app
 *     or in git. It lives only in the local admin page.
 *
 * If the config env vars are not set, this module no-ops gracefully: messaging is
 * simply "not configured yet," and the app falls back to the on-device queue.
 */

import { Platform } from 'react-native';
import { initializeApp, getApps, getApp, FirebaseApp } from 'firebase/app';
import {
  getAuth,
  initializeAuth,
  // @ts-ignore — getReactNativePersistence is exported by firebase/auth at runtime
  // but is missing from some versions' type defs.
  getReactNativePersistence,
  signInAnonymously,
  Auth,
} from 'firebase/auth';
import { getFirestore, Firestore } from 'firebase/firestore';
import AsyncStorage from '@react-native-async-storage/async-storage';

const firebaseConfig = {
  apiKey:            (process.env.EXPO_PUBLIC_FIREBASE_API_KEY ?? '').trim(),
  authDomain:        (process.env.EXPO_PUBLIC_FIREBASE_AUTH_DOMAIN ?? '').trim(),
  projectId:         (process.env.EXPO_PUBLIC_FIREBASE_PROJECT_ID ?? '').trim(),
  storageBucket:     (process.env.EXPO_PUBLIC_FIREBASE_STORAGE_BUCKET ?? '').trim(),
  messagingSenderId: (process.env.EXPO_PUBLIC_FIREBASE_MESSAGING_SENDER_ID ?? '').trim(),
  appId:             (process.env.EXPO_PUBLIC_FIREBASE_APP_ID ?? '').trim(),
};

// We need, at minimum, the project to talk to and the key to talk with.
export const isMessagingConfigured = !!(
  firebaseConfig.apiKey && firebaseConfig.projectId && firebaseConfig.appId
);

let app: FirebaseApp | null = null;
let authInstance: Auth | null = null;
let dbInstance: Firestore | null = null;

if (isMessagingConfigured) {
  app = getApps().length ? getApp() : initializeApp(firebaseConfig);

  // On a phone, Auth must persist its session in AsyncStorage so the device keeps
  // the SAME hidden identity across app restarts. On web, the browser's built-in
  // persistence is used. initializeAuth throws if it was already set up (e.g. a
  // hot reload), so fall back to getAuth in that case.
  try {
    authInstance =
      Platform.OS === 'web'
        ? getAuth(app)
        : initializeAuth(app, {
            persistence: getReactNativePersistence(AsyncStorage),
          });
  } catch {
    authInstance = getAuth(app);
  }

  dbInstance = getFirestore(app);
}

export const auth = authInstance;
export const db = dbInstance;

// Make sure the device has an anonymous session, creating one the first time.
// Returns the person's stable hidden id (auth uid), or null if unconfigured /
// offline. The id is the conversation key — it never changes for this install.
let ensuring: Promise<string | null> | null = null;
export function ensureAnonSession(): Promise<string | null> {
  if (!auth) return Promise.resolve(null);
  if (ensuring) return ensuring;
  ensuring = (async () => {
    try {
      if (auth!.currentUser?.uid) return auth!.currentUser.uid;
      const cred = await signInAnonymously(auth!);
      return cred.user?.uid ?? null;
    } catch {
      return null;
    } finally {
      ensuring = null;
    }
  })();
  return ensuring;
}
