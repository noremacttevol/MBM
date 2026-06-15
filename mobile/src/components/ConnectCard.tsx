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
} from 'react-native';
import { useAppStore, isMissionaryReady } from '../store/useAppStore';
import { isMessagingConfigured, InboxMessage } from '../lib/messaging';
import { MISSIONARY_CONTACT_URL } from '../engine/connect';
import { colors, spacing, radius } from '../theme';

interface Props {
  /** Optional softer framing when shown inside the time-cap or chat surfaces. */
  compact?: boolean;
}

type Mode = 'closed' | 'writing' | 'sent';

function shortTime(ts: string): string {
  const d = new Date(ts);
  if (isNaN(d.getTime())) return '';
  return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
}

export default function ConnectCard({ compact = false }: Props) {
  const dialogueSignals      = useAppStore(s => s.dialogueSignals);
  const sendConnectMessage   = useAppStore(s => s.sendConnectMessage);
  const submitConnectRequest = useAppStore(s => s.submitConnectRequest);
  const markInboxRead        = useAppStore(s => s.markInboxRead);
  const inboxMessages        = useAppStore(s => s.inboxMessages);
  const inboxUnread          = useAppStore(s => s.inboxUnread);
  const inboxLoading         = useAppStore(s => s.inboxLoading);
  const missionaryReady      = isMissionaryReady(dialogueSignals);

  const [mode, setMode]   = useState<Mode>('closed');
  const [draft, setDraft] = useState('');
  const [sending, setSending] = useState(false);

  const hasThread = inboxMessages.length > 0;

  // Send whatever is in the draft. Always keeps an on-device copy; reaches the
  // real person when the cloud inbox is configured.
  async function send(text: string) {
    const clean = text.trim();
    setSending(true);
    if (!clean) {
      // A blank reach-out still registers interest on-device; no empty bubble.
      submitConnectRequest('');
      setSending(false);
      setDraft('');
      setMode('sent');
      return;
    }
    await sendConnectMessage(clean);
    setSending(false);
    setDraft('');
    // If the cloud carried it, the thread now shows their words — let it take over.
    // If not, give the honest "a real person will reach out" confirmation.
    setMode(isMessagingConfigured ? 'closed' : 'sent');
  }

  function acknowledgeReplies() {
    if (inboxUnread > 0) markInboxRead();
  }

  // ── Live two-way thread ─────────────────────────────────────────────────────
  if (hasThread) {
    return (
      <View style={[styles.card, compact && styles.cardCompact]}>
        <Text style={styles.title}>A real person is here.</Text>

        {inboxUnread > 0 && (
          <TouchableOpacity
            style={styles.unreadBanner}
            activeOpacity={0.7}
            onPress={acknowledgeReplies}
          >
            <Text style={styles.unreadText}>
              A real person replied. Tap to mark as read.
            </Text>
          </TouchableOpacity>
        )}

        <View style={styles.thread}>
          {inboxMessages.map((m: InboxMessage) => {
            const mine = m.sender === 'user';
            return (
              <View
                key={m.id}
                style={[styles.row, mine ? styles.rowMine : styles.rowTheirs]}
              >
                {!mine && <Text style={styles.fromLabel}>A real person</Text>}
                <View style={[styles.bubble, mine ? styles.bubbleMine : styles.bubbleTheirs]}>
                  {!!m.excerpt && (
                    <Text style={styles.excerpt}>“{m.excerpt}”</Text>
                  )}
                  <Text style={styles.bubbleText}>{m.body}</Text>
                </View>
                {!!m.created_at && <Text style={styles.time}>{shortTime(m.created_at)}</Text>}
              </View>
            );
          })}
        </View>

        <Text style={styles.honest}>
          A real person reads every word. A reply can take a day or two — this is a
          person, not a bot.
        </Text>

        <View style={styles.composer}>
          <TextInput
            style={styles.composerInput}
            placeholder="Write back…"
            placeholderTextColor={colors.textMuted}
            multiline
            maxLength={1000}
            value={draft}
            onChangeText={setDraft}
            onFocus={acknowledgeReplies}
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

        {missionaryReady && (
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
        )}
      </View>
    );
  }

  // ── No thread yet — the invitation (and on-device fallback path) ─────────────
  return (
    <View style={[styles.card, compact && styles.cardCompact]}>
      <Text style={styles.title}>A real person is always here.</Text>

      {mode === 'sent' ? (
        <Text style={styles.confirm}>
          Thank you for reaching out. A real person will read this and get back to
          you. You don't have to do anything else — there's no rush, and no pressure.
        </Text>
      ) : (
        <>
          <Text style={styles.body}>
            Anything you want to ask, or just talk through — a real person reads
            these. No agenda. No pressure. Whenever you're ready.
          </Text>

          {mode === 'closed' ? (
            <TouchableOpacity
              style={styles.humanBtn}
              activeOpacity={0.8}
              onPress={() => setMode('writing')}
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
                  onPress={() => { setMode('closed'); setDraft(''); }}
                >
                  <Text style={styles.cancelText}>Cancel</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={[styles.sendBtn, sending && styles.sendBtnDim]}
                  activeOpacity={0.85}
                  disabled={sending}
                  onPress={() => send(draft)}
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

      {missionaryReady && mode !== 'writing' && (
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
      )}

      {mode !== 'sent' && (
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
    fontSize: 16, fontFamily: 'MBMCross', color: colors.textMid, marginBottom: spacing.sm,
  },
  body: {
    fontSize: 13, fontFamily: 'MBMCross', color: colors.textDim,
    lineHeight: 20, marginBottom: spacing.md,
  },
  confirm: {
    fontSize: 14, fontFamily: 'MBMCross', color: colors.green,
    lineHeight: 22, marginBottom: spacing.sm, fontStyle: 'italic',
  },

  // ── Unread reply banner ─────────────────────────────────────────────────────
  unreadBanner: {
    backgroundColor: '#13201a',
    borderWidth: 1, borderColor: colors.green, borderRadius: radius.sm,
    paddingVertical: 8, paddingHorizontal: 12, marginBottom: spacing.sm,
  },
  unreadText: {
    color: colors.green, fontSize: 12, fontFamily: 'MBMCross',
  },

  // ── Thread ──────────────────────────────────────────────────────────────────
  thread: { marginBottom: spacing.sm },
  row: { marginBottom: spacing.sm, maxWidth: '88%' },
  rowMine:   { alignSelf: 'flex-end',   alignItems: 'flex-end' },
  rowTheirs: { alignSelf: 'flex-start', alignItems: 'flex-start' },
  fromLabel: {
    fontSize: 10, fontFamily: 'MBMCross', color: colors.green,
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
    fontSize: 14, fontFamily: 'MBMCross', color: colors.textMid, lineHeight: 21,
  },
  excerpt: {
    fontSize: 12, fontFamily: 'MBMCross', color: colors.textDim,
    fontStyle: 'italic', lineHeight: 18, marginBottom: 6,
    borderLeftWidth: 2, borderLeftColor: colors.borderDim, paddingLeft: 8,
  },
  time: {
    fontSize: 10, fontFamily: 'MBMCross', color: colors.textMuted, marginTop: 3, marginHorizontal: 4,
  },

  honest: {
    fontSize: 11, fontFamily: 'MBMCross', color: colors.textMuted,
    fontStyle: 'italic', lineHeight: 16, marginBottom: spacing.sm,
  },

  // ── Composer ────────────────────────────────────────────────────────────────
  composer: { flexDirection: 'row', alignItems: 'flex-end', gap: spacing.sm },
  composerInput: {
    flex: 1, backgroundColor: colors.bgInput, borderWidth: 1, borderColor: '#2a3a28',
    borderRadius: radius.md, color: colors.textMid, fontSize: 14, fontFamily: 'MBMCross',
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
    color: '#0a0f0a', fontSize: 14, fontFamily: 'MBMCross', fontWeight: '600',
  },

  // Writing mode
  writeBox: { marginBottom: spacing.sm },
  input: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: '#2a3a28',
    borderRadius: radius.md, color: colors.textMid, fontSize: 14,
    fontFamily: 'MBMCross', padding: 12, minHeight: 96, lineHeight: 22,
    marginBottom: spacing.sm,
  },
  writeActions: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between',
  },
  cancelText: {
    color: colors.textMuted, fontSize: 13, fontFamily: 'MBMCross', paddingVertical: 8,
  },
  sendBtn: {
    backgroundColor: colors.green, borderRadius: radius.sm,
    paddingVertical: 10, paddingHorizontal: 16, alignItems: 'center', justifyContent: 'center',
    minHeight: 40,
  },
  sendBtnDim: { opacity: 0.5 },
  sendBtnText: {
    color: '#0a0f0a', fontSize: 13, fontFamily: 'MBMCross', fontWeight: '600',
  },

  missionaryBlock: {
    borderTopWidth: 1, borderTopColor: colors.borderDim,
    paddingTop: spacing.sm, marginTop: spacing.sm, marginBottom: spacing.sm,
  },
  missionaryBody: {
    fontSize: 12, fontFamily: 'MBMCross', color: colors.textDim,
    lineHeight: 18, marginBottom: spacing.sm, fontStyle: 'italic',
  },
  missionaryBtn: {
    borderWidth: 1, borderColor: colors.gold, borderRadius: 4,
    paddingVertical: 8, paddingHorizontal: 12, alignSelf: 'flex-start',
  },
  missionaryBtnText: { color: colors.gold, fontSize: 12, fontFamily: 'MBMCross' },
  sub: {
    fontSize: 11, color: colors.textMuted, fontFamily: 'MBMCross', fontStyle: 'italic',
  },
});
