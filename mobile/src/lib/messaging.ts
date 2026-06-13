/**
 * messaging.ts — the small, honest API the app uses for the human inbox.
 *
 * Everything here is scoped on the server (Firestore security rules) to the
 * device's own anonymous identity, so a person can only ever read or write their
 * own thread. All calls fail soft: if messaging is not configured or the network
 * is down, they return empty / false and the UI shows the on-device fallback
 * instead of breaking.
 *
 * The shape below stays snake_case on purpose — it is the contract the store was
 * built against, so the rest of the app does not change when the backend does.
 * Firestore stores camelCase fields; we translate at the boundary.
 */

import {
  collection,
  query,
  where,
  orderBy,
  getDocs,
  addDoc,
  updateDoc,
  doc,
  onSnapshot,
  serverTimestamp,
  Timestamp,
  DocumentData,
  QueryDocumentSnapshot,
} from 'firebase/firestore';
import { db, ensureAnonSession, isMessagingConfigured } from './firebase';

export interface InboxMessage {
  id:            string;
  user_id:       string;
  sender:        'user' | 'admin';
  body:          string;
  excerpt:       string | null;
  journey_stage: string | null;
  created_at:    string;
  read_by_admin: boolean;
  read_by_user:  boolean;
}

export { isMessagingConfigured };

const MESSAGES = 'messages';

// Turn a Firestore document into the snake_case shape the app expects. A freshly
// written row may not have its serverTimestamp yet — fall back to "now" so the
// UI can still sort and show it.
function toInboxMessage(
  snap: QueryDocumentSnapshot<DocumentData> | { id: string; data: () => DocumentData },
): InboxMessage {
  const d = snap.data();
  const created =
    d.createdAt instanceof Timestamp
      ? d.createdAt.toDate().toISOString()
      : new Date().toISOString();
  return {
    id:            snap.id,
    user_id:       d.userId ?? '',
    sender:        d.sender === 'admin' ? 'admin' : 'user',
    body:          d.body ?? '',
    excerpt:       d.excerpt ?? null,
    journey_stage: d.journeyStage ?? null,
    created_at:    created,
    read_by_admin: !!d.readByAdmin,
    read_by_user:  !!d.readByUser,
  };
}

// Send the person's note to a real human. `excerpt` optionally carries the piece
// of chat they wanted to talk about. Returns the saved row, or null on failure.
export async function sendMessage(
  body: string,
  excerpt?: string,
  journeyStage?: string,
): Promise<InboxMessage | null> {
  if (!db) return null;
  const uid = await ensureAnonSession();
  if (!uid) return null;
  try {
    const ref = await addDoc(collection(db, MESSAGES), {
      userId:       uid,
      sender:       'user',
      body:         (body ?? '').trim(),
      excerpt:      excerpt?.trim() || null,
      journeyStage: journeyStage ?? null,
      createdAt:    serverTimestamp(),
      readByAdmin:  false,
      readByUser:   true, // the person has, by definition, seen their own note
    });
    return {
      id:            ref.id,
      user_id:       uid,
      sender:        'user',
      body:          (body ?? '').trim(),
      excerpt:       excerpt?.trim() || null,
      journey_stage: journeyStage ?? null,
      created_at:    new Date().toISOString(),
      read_by_admin: false,
      read_by_user:  true,
    };
  } catch {
    return null;
  }
}

// Load the whole thread for this device, oldest first.
export async function fetchThread(): Promise<InboxMessage[]> {
  if (!db) return [];
  const uid = await ensureAnonSession();
  if (!uid) return [];
  try {
    const q = query(
      collection(db, MESSAGES),
      where('userId', '==', uid),
      orderBy('createdAt', 'asc'),
    );
    const snap = await getDocs(q);
    return snap.docs.map(toInboxMessage);
  } catch {
    return [];
  }
}

// Mark every admin reply in this thread as seen, so the unread dot can clear.
export async function markRepliesRead(): Promise<void> {
  if (!db) return;
  const uid = await ensureAnonSession();
  if (!uid) return;
  try {
    const q = query(
      collection(db, MESSAGES),
      where('userId', '==', uid),
      where('sender', '==', 'admin'),
      where('readByUser', '==', false),
    );
    const snap = await getDocs(q);
    await Promise.all(
      snap.docs.map(d => updateDoc(doc(db!, MESSAGES, d.id), { readByUser: true })),
    );
  } catch {
    /* fail soft */
  }
}

// Subscribe to new rows in this device's thread (the admin's replies arrive live).
// Returns an unsubscribe function. No-ops to a noop unsub if unconfigured.
export function subscribeToThread(
  onMessage: (msg: InboxMessage) => void,
): () => void {
  if (!db) return () => {};
  let unsub: (() => void) | null = null;
  let cancelled = false;

  ensureAnonSession().then(uid => {
    if (!uid || !db || cancelled) return;
    const q = query(
      collection(db, MESSAGES),
      where('userId', '==', uid),
      orderBy('createdAt', 'asc'),
    );
    // onSnapshot replays the existing thread as "added" on first fire; the store
    // de-dupes by id, so that is harmless. After that, only the admin's new
    // replies (and the person's own sends) arrive as fresh "added" changes.
    unsub = onSnapshot(
      q,
      snap => {
        snap.docChanges().forEach(change => {
          if (change.type === 'added') onMessage(toInboxMessage(change.doc));
        });
      },
      () => {/* fail soft on permission / network errors */},
    );
  });

  return () => {
    cancelled = true;
    if (unsub) unsub();
  };
}
