/**
 * Supabase client — the thin, free cloud channel that carries a person's words
 * to a real human and brings the reply back INTO the app.
 *
 * The whole app stays local-first. This is the ONE place that reaches the cloud,
 * and only for the "talk to a real person" inbox — exactly the delivery channel
 * the on-device ConnectRequest queue was always designed to grow into.
 *
 * No login, ever: every install signs in ANONYMOUSLY, so the device gets a real
 * hidden identity (auth.uid()) without the person creating an account or giving
 * an email. Row-Level Security on the server scopes every read/write to that
 * identity — a person can only ever see their own thread.
 *
 * Key safety (Cameron's standing rule):
 *   - EXPO_PUBLIC_SUPABASE_ANON_KEY is DESIGNED to be public and ship in the app;
 *     RLS is what protects the data. This is the only key the app ever holds.
 *   - The SERVICE-ROLE key (which bypasses RLS) NEVER goes in the app or in git.
 *     It lives only in the local admin page.
 *
 * If the two env vars are not set, this module no-ops gracefully: messaging is
 * simply "not configured yet," and the app falls back to the on-device queue.
 */

import 'react-native-url-polyfill/auto';
import { createClient, SupabaseClient } from '@supabase/supabase-js';
import AsyncStorage from '@react-native-async-storage/async-storage';

const SUPABASE_URL      = (process.env.EXPO_PUBLIC_SUPABASE_URL ?? '').trim();
const SUPABASE_ANON_KEY = (process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY ?? '').trim();

export const isMessagingConfigured = !!(SUPABASE_URL && SUPABASE_ANON_KEY);

export const supabase: SupabaseClient | null = isMessagingConfigured
  ? createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
      auth: {
        storage:           AsyncStorage,
        autoRefreshToken:  true,
        persistSession:    true,
        detectSessionInUrl: false,   // React Native / Expo: no URL-based auth
      },
    })
  : null;

// Make sure the device has an anonymous session, creating one the first time.
// Returns the person's stable hidden id (auth.uid()), or null if unconfigured /
// offline. The id is the conversation key — it never changes for this install.
let ensuring: Promise<string | null> | null = null;
export function ensureAnonSession(): Promise<string | null> {
  if (!supabase) return Promise.resolve(null);
  if (ensuring) return ensuring;
  ensuring = (async () => {
    try {
      const { data: sessionData } = await supabase!.auth.getSession();
      if (sessionData.session?.user?.id) return sessionData.session.user.id;
      const { data, error } = await supabase!.auth.signInAnonymously();
      if (error) return null;
      return data.user?.id ?? null;
    } catch {
      return null;
    } finally {
      ensuring = null;
    }
  })();
  return ensuring;
}
