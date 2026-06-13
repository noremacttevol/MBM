/**
 * messaging.ts — the small, honest API the app uses for the human inbox.
 *
 * Everything here is RLS-scoped on the server to the device's own anonymous
 * identity, so a person can only ever read or write their own thread. All calls
 * fail soft: if messaging is not configured or the network is down, they return
 * empty / false and the UI shows the on-device fallback instead of breaking.
 */

import { supabase, ensureAnonSession, isMessagingConfigured } from './supabase';

export interface InboxMessage {
  id:           string;
  user_id:      string;
  sender:       'user' | 'admin';
  body:         string;
  excerpt:      string | null;
  journey_stage: string | null;
  created_at:   string;
  read_by_admin: boolean;
  read_by_user:  boolean;
}

export { isMessagingConfigured };

// Send the person's note to a real human. `excerpt` optionally carries the piece
// of chat they wanted to talk about. Returns the saved row, or null on failure.
export async function sendMessage(
  body: string,
  excerpt?: string,
  journeyStage?: string,
): Promise<InboxMessage | null> {
  if (!supabase) return null;
  const uid = await ensureAnonSession();
  if (!uid) return null;
  try {
    const { data, error } = await supabase
      .from('messages')
      .insert({
        user_id:       uid,
        sender:        'user',
        body:          (body ?? '').trim(),
        excerpt:       excerpt?.trim() || null,
        journey_stage: journeyStage ?? null,
      })
      .select()
      .single();
    if (error) return null;
    return data as InboxMessage;
  } catch {
    return null;
  }
}

// Load the whole thread for this device, oldest first.
export async function fetchThread(): Promise<InboxMessage[]> {
  if (!supabase) return [];
  const uid = await ensureAnonSession();
  if (!uid) return [];
  try {
    const { data, error } = await supabase
      .from('messages')
      .select('*')
      .order('created_at', { ascending: true });
    if (error || !data) return [];
    return data as InboxMessage[];
  } catch {
    return [];
  }
}

// Mark every admin reply in this thread as seen, so the unread dot can clear.
export async function markRepliesRead(): Promise<void> {
  if (!supabase) return;
  const uid = await ensureAnonSession();
  if (!uid) return;
  try {
    await supabase
      .from('messages')
      .update({ read_by_user: true })
      .eq('sender', 'admin')
      .eq('read_by_user', false);
  } catch {
    /* fail soft */
  }
}

// Subscribe to new rows in this device's thread (the admin's replies arrive live).
// Returns an unsubscribe function. No-ops to a noop unsub if unconfigured.
export function subscribeToThread(
  onMessage: (msg: InboxMessage) => void,
): () => void {
  if (!supabase) return () => {};
  let channel: ReturnType<NonNullable<typeof supabase>['channel']> | null = null;
  ensureAnonSession().then(uid => {
    if (!uid || !supabase) return;
    channel = supabase
      .channel('inbox-' + uid)
      .on(
        'postgres_changes',
        { event: 'INSERT', schema: 'public', table: 'messages', filter: `user_id=eq.${uid}` },
        payload => onMessage(payload.new as InboxMessage),
      )
      .subscribe();
  });
  return () => {
    if (channel && supabase) supabase.removeChannel(channel);
  };
}
