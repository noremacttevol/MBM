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
  // Which conversation this message belongs to. A device can hold MANY separate
  // real-person conversations now (Cameron's ask). Legacy rows written before
  // multi-thread have no threadId and collapse into the 'main' thread, so nothing
  // already sent is ever lost.
  thread_id:     string;
  // A short, human title for the conversation, stamped on its FIRST message so the
  // history list reads like topics, not raw text. Null on follow-up messages.
  thread_title:  string | null;
  sender:        'user' | 'admin';
  body:          string;
  excerpt:       string | null;
  journey_stage: string | null;
  // 'crisis' marks an escalation where the person showed severe distress / crisis
  // language, so the admin team can triage it first. Null/absent = normal.
  priority:      string | null;
  created_at:    string;
  read_by_admin: boolean;
  read_by_user:  boolean;
}

export { isMessagingConfigured };

const MESSAGES = 'messages';

// The bucket every pre-multi-thread message falls into, so the original single
// conversation keeps working as one titled thread.
export const LEGACY_THREAD_ID = 'main';

export interface SendOptions {
  threadId?:    string;
  threadTitle?: string;
  excerpt?:     string;
  journeyStage?: string;
  // The person's name, if they've given one — so the admin team can recognize a
  // returning person and greet them properly. Optional; null when unknown.
  userName?:    string;
  // A short, SELF-REPORTED note about their faith background / inclination (in
  // their own words) — shown beside their name in the console so a responder has
  // context. Optional; null when they haven't said anything.
  faithNote?:   string;
  // 'crisis' when the conversation showed severe distress, so admin triages first.
  priority?:    string;
}

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
    thread_id:     d.threadId ?? LEGACY_THREAD_ID,
    thread_title:  d.threadTitle ?? null,
    sender:        d.sender === 'admin' ? 'admin' : 'user',
    body:          d.body ?? '',
    excerpt:       d.excerpt ?? null,
    journey_stage: d.journeyStage ?? null,
    priority:      d.priority ?? null,
    created_at:    created,
    read_by_admin: !!d.readByAdmin,
    read_by_user:  !!d.readByUser,
  };
}

// Send the person's note to a real human, into a specific conversation thread.
// `opts.excerpt` optionally carries the piece of chat they wanted to talk about;
// `opts.threadTitle` is stamped only on the first message of a new thread. Returns
// the saved row, or null on failure.
export async function sendMessage(
  body: string,
  opts: SendOptions = {},
): Promise<InboxMessage | null> {
  if (!db) return null;
  const uid = await ensureAnonSession();
  if (!uid) return null;
  const threadId = (opts.threadId || LEGACY_THREAD_ID).trim() || LEGACY_THREAD_ID;
  const threadTitle = opts.threadTitle?.trim() || null;
  const clean = (body ?? '').trim();
  try {
    const ref = await addDoc(collection(db, MESSAGES), {
      userId:       uid,
      userName:     opts.userName?.trim() || null,
      faithNote:    opts.faithNote?.trim() || null,
      threadId,
      threadTitle,
      sender:       'user',
      body:         clean,
      excerpt:      opts.excerpt?.trim() || null,
      journeyStage: opts.journeyStage ?? null,
      priority:     opts.priority ?? null,
      createdAt:    serverTimestamp(),
      readByAdmin:  false,
      readByUser:   true, // the person has, by definition, seen their own note
    });
    return {
      id:            ref.id,
      user_id:       uid,
      thread_id:     threadId,
      thread_title:  threadTitle,
      sender:        'user',
      body:          clean,
      excerpt:       opts.excerpt?.trim() || null,
      journey_stage: opts.journeyStage ?? null,
      priority:      opts.priority ?? null,
      created_at:    new Date().toISOString(),
      read_by_admin: false,
      read_by_user:  true,
    };
  } catch {
    return null;
  }
}

// Load EVERY message for this device. We filter by userId ONLY (a single-field
// query that needs no special Firestore index) and sort by time on the device.
// Ordering server-side with `orderBy('createdAt')` here would force a composite
// index (userId + createdAt) that must be created by hand — and if it is missing
// the whole query throws and the history silently shows nothing. Sorting on the
// client avoids that entirely. The app also re-sorts when grouping into threads,
// so order is correct regardless.
export async function fetchThread(): Promise<InboxMessage[]> {
  if (!db) return [];
  const uid = await ensureAnonSession();
  if (!uid) return [];
  try {
    const q = query(
      collection(db, MESSAGES),
      where('userId', '==', uid),
    );
    const snap = await getDocs(q);
    return snap.docs
      .map(toInboxMessage)
      .sort((a, b) => +new Date(a.created_at) - +new Date(b.created_at));
  } catch {
    return [];
  }
}

// Mark admin replies as seen, so the unread dot can clear. If `threadId` is given,
// only that conversation's replies are marked (we filter on the client so no new
// composite index is required); otherwise every unseen reply is cleared.
export async function markRepliesRead(threadId?: string): Promise<void> {
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
    const target = threadId
      ? snap.docs.filter(d => (d.data().threadId ?? LEGACY_THREAD_ID) === threadId)
      : snap.docs;
    await Promise.all(
      target.map(d => updateDoc(doc(db!, MESSAGES, d.id), { readByUser: true })),
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
    // userId-only filter (no orderBy) so it needs no composite index; the store
    // sorts by time when it groups messages into threads for display.
    const q = query(
      collection(db, MESSAGES),
      where('userId', '==', uid),
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
