/**
 * ConnectCard — the human-relationship rung, rendered as a living conversation.
 *
 * THE LAW (CLAUDE.md): a real human is ALWAYS one tap away. Never buried, never
 * gated, always there. So the "talk to a real person" rung is ALWAYS shown.
 *
 * The ladder, top to bottom:
 *   1. Talk to a real person (Cameron in Phase 1) — ALWAYS available.
 *   2. Recommend missionaries + the contact form — ONLY when the person has passed
 *      the milk gate AND is reaching toward the church on their own. Offered gently,
 *      never pushed. Jesus let the rich young ruler walk away; so do we.
 *
 * TWO-WAY THREAD:
 *   When the cloud inbox is configured, this card becomes the real conversation.
 *   The person's notes and the real person's replies appear here as a quiet thread,
 *   it updates live the moment a reply is sent, and they can write back. We are
 *   honest about it: a person reads every word, and a reply can take time — this is
 *   never dressed up as an instant bot.
 *
 *   When the cloud inbox is NOT configured (or offline), nothing breaks: the note is
 *   captured ON-DEVICE (the durable fallback) and the card honestly confirms a real
 *   person will reach out. No fake two-way, no dead-end mailto.
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Linking,
  ActivityIndicator,
  Alert,
} from 'react-native';
import { useAppStore, isMissionaryReady, selectRealThreads } from '../store/useAppStore';
import { isMessagingConfigured, InboxMessage } from '../lib/messaging';
import { MISSIONARY_CONTACT_URL } from '../engine/connect';
import { colors, spacing, radius } from '../theme';

interface Props {
  /** Optional softer framing when shown inside the time-cap or chat surfaces. */
  compact?: boolean;
}

function shortTime(ts: string): string {
  const d = new Date(ts);
  if (isNaN(d.getTime())) return '';
  return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
}

// A small, reusable "ask the missionaries" block — shown gently only once a
// person has passed the milk gate and is reaching toward the church on their own.
function MissionaryBlock() {
  return (
    <View style={styles.missionaryBlock}>
      <Text style={styles.missionaryBody}>
        If you'd like, you can also ask for a visit from people who would be glad
        to walk this road with you in person. Only if and when you want to.
      </Text>
      <TouchableOpacity
        style={styles.missionaryBtn}
        activeOpacity={0.85}
        onPress={() => Linking.openURL(MISSIONARY_CONTACT_URL).catch(() => {})}
      >
        <Text style={styles.missionaryBtnText}>Request a visit →</Text>
      </TouchableOpacity>
    </View>
  );
}

export default function ConnectCard({ compact = false }: Props) {
  const dialogueSignals       = useAppStore(s => s.dialogueSignals);
  const sendConnectMessage    = useAppStore(s => s.sendConnectMessage);
  const submitConnectRequest  = useAppStore(s => s.submitConnectRequest);
  const markInboxRead         = useAppStore(s => s.markInboxRead);
  const inboxMessages         = useAppStore(s => s.inboxMessages);
  const inboxLoading          = useAppStore(s => s.inboxLoading);
  const activeRealThreadId    = useAppStore(s => s.activeRealThreadId);
  const openRealPersonThread  = useAppStore(s => s.openRealPersonThread);
  const newRealPersonThread   = useAppStore(s => s.newRealPersonThread);
  const closeRealPersonThread = useAppStore(s => s.closeRealPersonThread);
  const cancelledThreadIds    = useAppStore(s => s.cancelledThreadIds);
  const cancelRealThread      = useAppStore(s => s.cancelRealThread);
  const missionaryReady       = isMissionaryReady(dialogueSignals);

  // Every real-person message, grouped into separate titled conversations —
  // minus any the person has cancelled (hidden from their own list).
  const threads      = selectRealThreads(inboxMessages).filter(t => !cancelledThreadIds.includes(t.id));

  // Confirm, then withdraw a conversation: tells the admin team to disregard it
  // and removes it from the person's list.
  function confirmCancel(threadId: string, title: string) {
    Alert.alert(
      'Cancel this request?',
      `“${title || 'This conversation'}” will be withdrawn — the admin team will be told to disregard it, and it will be removed from your list.`,
      [
        { text: 'Keep it', style: 'cancel' },
        { text: 'Cancel request', style: 'destructive', onPress: () => { cancelRealThread(threadId); } },
      ],
    );
  }
  const activeThread = threads.find(t => t.id === activeRealThreadId) || null;
  // A conversation the person just started, with nothing sent into it yet.
  const inNewEmpty   = !!activeRealThreadId && !activeThread;
  const showConversation = !!activeThread || inNewEmpty;

  const [draft, setDraft]       = useState('');
  const [sending, setSending]   = useState(false);
  // The first-ever reach-out keeps the gentle two-step invitation; once the cloud
  // can't carry it, this shows the honest "a real person will reach out" note.
  const [writingFirst, setWritingFirst] = useState(false);
  const [sentOffline, setSentOffline]   = useState(false);

  // Send the draft into whatever conversation is open (or a new one). Always keeps
  // an on-device copy; reaches the real person when the cloud inbox is configured.
  async function send(text: string, isFirst = false) {
    const clean = text.trim();
    setSending(true);
    if (!clean) {
      submitConnectRequest('');             // a blank reach-out still registers interest
      setSending(false);
      setDraft('');
      if (isFirst) setSentOffline(true);
      return;
    }
    await sendConnectMessage(clean);
    setSending(false);
    setDraft('');
    setWritingFirst(false);
    // Cloud carried it → the thread view takes over automatically. Offline → give
    // the honest confirmation instead of a fake two-way bubble.
    if (isFirst && !isMessagingConfigured) setSentOffline(true);
  }

  function ackThread() {
    if (activeThread && activeThread.unread > 0) markInboxRead();
  }

  // ── One open conversation — the live two-way thread ─────────────────────────
  if (showConversation) {
    const msgs    = activeThread?.messages ?? [];
    const unread  = activeThread?.unread ?? 0;
    const title   = activeThread?.title ?? 'New conversation';
    // You can ALWAYS get back to your list of conversations whenever at least one
    // saved conversation exists — so you're never stuck inside a single thread with
    // no way to start another (Cameron's bug).
    const canGoBack = threads.length >= 1;

    return (
      <View style={[styles.card, compact && styles.cardCompact]}>
        <View style={styles.headerRow}>
          {canGoBack && (
            <TouchableOpacity activeOpacity={0.7} onPress={closeRealPersonThread}>
              <Text style={styles.backLink}>‹ All conversations</Text>
            </TouchableOpacity>
          )}
          <Text style={[styles.title, { flex: 1 }]} numberOfLines={1}>{title}</Text>
          {/* Withdraw this request — only meaningful once it's a real, sent thread. */}
          {activeThread && (
            <TouchableOpacity activeOpacity={0.7} onPress={() => confirmCancel(activeThread.id, activeThread.title)}>
              <Text style={styles.cancelInline}>Cancel</Text>
            </TouchableOpacity>
          )}
          {/* Start another conversation right from inside one — no dead ends. */}
          <TouchableOpacity activeOpacity={0.7} onPress={() => newRealPersonThread()}>
            <Text style={styles.newInline}>+ New</Text>
          </TouchableOpacity>
        </View>

        {unread > 0 && (
          <TouchableOpacity style={styles.unreadBanner} activeOpacity={0.7} onPress={ackThread}>
            <Text style={styles.unreadText}>Our admin team replied. Tap to mark as read.</Text>
          </TouchableOpacity>
        )}

        {msgs.length > 0 ? (
          <View style={styles.thread}>
            {msgs.map((m: InboxMessage) => {
              const mine = m.sender === 'user';
              return (
                <View key={m.id} style={[styles.row, mine ? styles.rowMine : styles.rowTheirs]}>
                  {!mine && <Text style={styles.fromLabel}>Our admin team</Text>}
                  <View style={[styles.bubble, mine ? styles.bubbleMine : styles.bubbleTheirs]}>
                    {!!m.excerpt && <Text style={styles.excerpt}>“{m.excerpt}”</Text>}
                    <Text style={styles.bubbleText} selectable>{m.body}</Text>
                  </View>
                  {!!m.created_at && <Text style={styles.time}>{shortTime(m.created_at)}</Text>}
                </View>
              );
            })}
          </View>
        ) : (
          <Text style={styles.body}>
            Start a new conversation with our admin team. Write whatever you'd like to
            ask or talk through — there's no rush, and no pressure.
          </Text>
        )}

        <Text style={styles.honest}>
          A real person on our admin team reads every word. A reply can take a day or two — this is a
          person, not a bot.
        </Text>

        <View style={styles.composer}>
          <TextInput
            style={styles.composerInput}
            placeholder={msgs.length ? 'Write back…' : 'Write your message…'}
            placeholderTextColor={colors.textMuted}
            multiline
            maxLength={1000}
            value={draft}
            onChangeText={setDraft}
            onFocus={ackThread}
            textAlignVertical="top"
          />
          <TouchableOpacity
            style={[styles.sendBtn, (!draft.trim() || sending) && styles.sendBtnDim]}
            activeOpacity={0.85}
            disabled={!draft.trim() || sending}
            onPress={() => send(draft)}
          >
            {sending
              ? <ActivityIndicator size="small" color={colors.onAccent} />
              : <Text style={styles.sendBtnText}>Send →</Text>}
          </TouchableOpacity>
        </View>

        {missionaryReady && <MissionaryBlock />}
      </View>
    );
  }

  // ── The conversation list — many separate real-person threads ───────────────
  // This IS the real-person history, with the "New" button right beside it, kept
  // entirely separate from the AI "Talk About It" history.
  if (threads.length > 0) {
    return (
      <View style={[styles.card, compact && styles.cardCompact]}>
        <View style={styles.listHeader}>
          <Text style={[styles.title, { marginBottom: 0, flex: 1 }]}>Your messages with the admin team</Text>
          <TouchableOpacity activeOpacity={0.85} onPress={() => newRealPersonThread()}>
            <Text style={styles.newInline}>+ New</Text>
          </TouchableOpacity>
        </View>

        {threads.map(t => (
          <TouchableOpacity
            key={t.id}
            style={styles.listRow}
            activeOpacity={0.7}
            onPress={() => openRealPersonThread(t.id)}
          >
            <View style={styles.listRowMain}>
              <Text style={styles.rowTitle} numberOfLines={1}>{t.title}</Text>
              <Text style={styles.rowSnippet} numberOfLines={1}>
                {t.lastSender === 'admin' ? 'Reply: ' : 'You: '}{t.lastBody}
              </Text>
            </View>
            <View style={styles.listRowSide}>
              {t.unread > 0 && <View style={styles.unreadDot} />}
              <Text style={styles.rowTime}>{shortTime(t.lastAt)}</Text>
              <TouchableOpacity
                activeOpacity={0.7}
                hitSlop={{ top: 8, bottom: 8, left: 8, right: 8 }}
                onPress={() => confirmCancel(t.id, t.title)}
              >
                <Text style={styles.rowCancel}>Cancel</Text>
              </TouchableOpacity>
            </View>
          </TouchableOpacity>
        ))}

        <TouchableOpacity
          style={styles.newBtn}
          activeOpacity={0.85}
          onPress={() => newRealPersonThread()}
        >
          <Text style={styles.newBtnText}>+ Start a new conversation</Text>
        </TouchableOpacity>

        {missionaryReady && <MissionaryBlock />}
      </View>
    );
  }

  // ── No conversations yet — the first, gentle invitation ─────────────────────
  return (
    <View style={[styles.card, compact && styles.cardCompact]}>
      <Text style={styles.title}>A real person from our admin team is always here.</Text>

      {sentOffline ? (
        <Text style={styles.confirm}>
          Thank you for reaching out. Our admin team will read this and get back to
          you. You don't have to do anything else — there's no rush, and no pressure.
        </Text>
      ) : (
        <>
          <Text style={styles.body}>
            Anything you want to ask, or just talk through — a real person on our admin
            team reads these. No agenda. No pressure. Whenever you're ready.
          </Text>

          {!writingFirst ? (
            <TouchableOpacity
              style={styles.humanBtn}
              activeOpacity={0.8}
              onPress={() => setWritingFirst(true)}
            >
              <Text style={styles.humanBtnText}>Talk to a real person</Text>
            </TouchableOpacity>
          ) : (
            <View style={styles.writeBox}>
              <TextInput
                style={styles.input}
                placeholder="Write whatever you'd like to say, or leave it blank — either way, someone will reach out."
                placeholderTextColor={colors.textMuted}
                multiline
                numberOfLines={4}
                maxLength={1000}
                value={draft}
                onChangeText={setDraft}
                autoFocus
                textAlignVertical="top"
              />
              <View style={styles.writeActions}>
                <TouchableOpacity
                  activeOpacity={0.7}
                  onPress={() => { setWritingFirst(false); setDraft(''); }}
                >
                  <Text style={styles.cancelText}>Cancel</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={[styles.sendBtn, sending && styles.sendBtnDim]}
                  activeOpacity={0.85}
                  disabled={sending}
                  onPress={() => send(draft, true)}
                >
                  {sending
                    ? <ActivityIndicator size="small" color={colors.onAccent} />
                    : <Text style={styles.sendBtnText}>Send to a real person</Text>}
                </TouchableOpacity>
              </View>
            </View>
          )}
        </>
      )}

      {missionaryReady && !writingFirst && <MissionaryBlock />}

      {!sentOffline && (
        <Text style={styles.sub}>
          {inboxLoading ? 'Reaching the thread…' : 'Or just keep going — there’s no rush.'}
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    borderWidth:     1,
    borderColor:     '#2a3a28',
    backgroundColor: '#0a0f0a',
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.md,
  },
  cardCompact: { marginBottom: spacing.sm },
  title: {
    fontSize: 16, fontFamily: 'Jost_400Regular', color: colors.textMid, marginBottom: spacing.sm,
    flexShrink: 1,
  },

  // ── Conversation header (back ‹ All + title) ────────────────────────────────
  headerRow: {
    flexDirection: 'row', alignItems: 'center', gap: spacing.sm, marginBottom: spacing.xs,
  },
  backLink: {
    fontSize: 13, fontFamily: 'Jost_400Regular', color: colors.blue, paddingVertical: 2, paddingRight: 4,
  },
  newInline: {
    fontSize: 13, fontFamily: 'Jost_400Regular', color: colors.green, paddingVertical: 2, paddingLeft: 4,
  },
  cancelInline: {
    fontSize: 13, fontFamily: 'Jost_400Regular', color: colors.textMuted, paddingVertical: 2, paddingHorizontal: 4,
  },
  listHeader: {
    flexDirection: 'row', alignItems: 'center', gap: spacing.sm, marginBottom: spacing.sm,
  },
  rowCancel: {
    fontSize: 11, fontFamily: 'Jost_400Regular', color: colors.textMuted, fontStyle: 'italic',
  },

  // ── Conversation list (multiple real-person threads) ────────────────────────
  listRow: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between',
    borderWidth: 1, borderColor: '#2a3a28', backgroundColor: '#0c120c',
    borderRadius: radius.md, paddingVertical: 10, paddingHorizontal: 12,
    marginBottom: spacing.sm, gap: spacing.sm,
  },
  listRowMain: { flex: 1 },
  rowTitle: {
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textMid, marginBottom: 2,
  },
  rowSnippet: {
    fontSize: 12, fontFamily: 'Jost_400Regular', color: colors.textDim,
  },
  listRowSide: { alignItems: 'flex-end', gap: 4 },
  rowTime: {
    fontSize: 10, fontFamily: 'Jost_400Regular', color: colors.textMuted,
  },
  unreadDot: {
    width: 9, height: 9, borderRadius: 5, backgroundColor: colors.green,
  },
  newBtn: {
    borderWidth: 1, borderColor: colors.green, borderRadius: radius.sm,
    paddingVertical: 10, paddingHorizontal: 14, alignItems: 'center', marginTop: 2,
  },
  newBtnText: {
    color: colors.green, fontSize: 13, fontFamily: 'Jost_400Regular', fontWeight: '600',
  },
  body: {
    fontSize: 13, fontFamily: 'Jost_400Regular', color: colors.textDim,
    lineHeight: 20, marginBottom: spacing.md,
  },
  confirm: {
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.green,
    lineHeight: 22, marginBottom: spacing.sm, fontStyle: 'italic',
  },

  // ── Unread reply banner ─────────────────────────────────────────────────────
  unreadBanner: {
    backgroundColor: '#13201a',
    borderWidth: 1, borderColor: colors.green, borderRadius: radius.sm,
    paddingVertical: 8, paddingHorizontal: 12, marginBottom: spacing.sm,
  },
  unreadText: {
    color: colors.green, fontSize: 12, fontFamily: 'Jost_400Regular',
  },

  // ── Thread ──────────────────────────────────────────────────────────────────
  thread: { marginBottom: spacing.sm },
  row: { marginBottom: spacing.sm, maxWidth: '88%' },
  rowMine:   { alignSelf: 'flex-end',   alignItems: 'flex-end' },
  rowTheirs: { alignSelf: 'flex-start', alignItems: 'flex-start' },
  fromLabel: {
    fontSize: 10, fontFamily: 'Jost_400Regular', color: colors.green,
    letterSpacing: 0.5, marginBottom: 3, marginLeft: 4,
  },
  bubble: {
    borderRadius: radius.lg, paddingVertical: spacing.sm + 2, paddingHorizontal: spacing.sm + 4,
    borderWidth: 1,
  },
  bubbleMine: {
    backgroundColor: '#1a1a12', borderColor: colors.border,
  },
  // A real person's reply is BLUE, so it's unmistakable from the AI (Cameron's
  // ask): a real human is talking now, not the app.
  bubbleTheirs: {
    backgroundColor: '#0d1b2e', borderColor: colors.blue,
  },
  bubbleText: {
    fontSize: 14, fontFamily: 'Jost_400Regular', color: colors.textMid, lineHeight: 21,
  },
  excerpt: {
    fontSize: 12, fontFamily: 'Jost_400Regular', color: colors.textDim,
    fontStyle: 'italic', lineHeight: 18, marginBottom: 6,
    borderLeftWidth: 2, borderLeftColor: colors.borderDim, paddingLeft: 8,
  },
  time: {
    fontSize: 10, fontFamily: 'Jost_400Regular', color: colors.textMuted, marginTop: 3, marginHorizontal: 4,
  },

  honest: {
    fontSize: 11, fontFamily: 'Jost_400Regular', color: colors.textMuted,
    fontStyle: 'italic', lineHeight: 16, marginBottom: spacing.sm,
  },

  // ── Composer ────────────────────────────────────────────────────────────────
  composer: { flexDirection: 'row', alignItems: 'flex-end', gap: spacing.sm },
  composerInput: {
    flex: 1, backgroundColor: colors.bgInput, borderWidth: 1, borderColor: '#2a3a28',
    borderRadius: radius.md, color: colors.textMid, fontSize: 14, fontFamily: 'Jost_400Regular',
    paddingHorizontal: 12, paddingVertical: 10, minHeight: 44, maxHeight: 120, lineHeight: 20,
  },

  // Rung 1 button — filled so it reads as the real, inviting action.
  humanBtn: {
    backgroundColor: colors.green,
    borderRadius: radius.sm,
    paddingVertical: 12, paddingHorizontal: 16,
    marginBottom: spacing.sm, alignItems: 'center',
  },
  humanBtnText: {
    color: '#0a0f0a', fontSize: 14, fontFamily: 'Jost_400Regular', fontWeight: '600',
  },

  // Writing mode
  writeBox: { marginBottom: spacing.sm },
  input: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: '#2a3a28',
    borderRadius: radius.md, color: colors.textMid, fontSize: 14,
    fontFamily: 'Jost_400Regular', padding: 12, minHeight: 96, lineHeight: 22,
    marginBottom: spacing.sm,
  },
  writeActions: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between',
  },
  cancelText: {
    color: colors.textMuted, fontSize: 13, fontFamily: 'Jost_400Regular', paddingVertical: 8,
  },
  sendBtn: {
    backgroundColor: colors.green, borderRadius: radius.sm,
    paddingVertical: 10, paddingHorizontal: 16, alignItems: 'center', justifyContent: 'center',
    minHeight: 40,
  },
  sendBtnDim: { opacity: 0.5 },
  sendBtnText: {
    color: '#0a0f0a', fontSize: 13, fontFamily: 'Jost_400Regular', fontWeight: '600',
  },

  missionaryBlock: {
    borderTopWidth: 1, borderTopColor: colors.borderDim,
    paddingTop: spacing.sm, marginTop: spacing.sm, marginBottom: spacing.sm,
  },
  missionaryBody: {
    fontSize: 12, fontFamily: 'Jost_400Regular', color: colors.textDim,
    lineHeight: 18, marginBottom: spacing.sm, fontStyle: 'italic',
  },
  missionaryBtn: {
    borderWidth: 1, borderColor: colors.gold, borderRadius: 4,
    paddingVertical: 8, paddingHorizontal: 12, alignSelf: 'flex-start',
  },
  missionaryBtnText: { color: colors.gold, fontSize: 12, fontFamily: 'Jost_400Regular' },
  sub: {
    fontSize: 11, color: colors.textMuted, fontFamily: 'Jost_400Regular', fontStyle: 'italic',
  },
});
