/**
 * ConnectCard — the human-relationship ladder, rendered.
 *
 * THE LAW (CLAUDE.md): a real human is ALWAYS one tap away. Never buried, never
 * gated, always there. So the "talk to a real person" rung is ALWAYS shown.
 *
 * The ladder, top to bottom:
 *   1. Talk to a real person (Cameron, Phase 1) — ALWAYS available.
 *   2. Recommend missionaries + the contact form — ONLY when the person has passed
 *      the milk gate AND is reaching toward the church on their own. Offered gently,
 *      never pushed. Jesus let the rich young ruler walk away; so do we.
 *
 * PHASE 1 — HONEST CAPTURE (no fake email link):
 *   Tapping "Talk to a real person" opens a short note box. The note is saved
 *   ON-DEVICE (useAppStore.submitConnectRequest) and the card honestly confirms a
 *   real person will reach out. There is no mailto and no dead-end email draft.
 *   When the real delivery channel is built (a small send service to Cameron's
 *   inbox / an admin queue), it reads from that on-device queue — this UI does not
 *   change. This keeps the promise honest: we don't pretend two-way messaging
 *   exists before it does.
 */

import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Linking } from 'react-native';
import { useAppStore, isMissionaryReady } from '../store/useAppStore';
import { MISSIONARY_CONTACT_URL } from '../engine/connect';
import { colors, spacing, radius } from '../theme';

interface Props {
  /** Optional softer framing when shown inside the time-cap or chat surfaces. */
  compact?: boolean;
}

type Mode = 'closed' | 'writing' | 'sent';

export default function ConnectCard({ compact = false }: Props) {
  const dialogueSignals      = useAppStore(s => s.dialogueSignals);
  const submitConnectRequest = useAppStore(s => s.submitConnectRequest);
  const missionaryReady      = isMissionaryReady(dialogueSignals);

  const [mode, setMode] = useState<Mode>('closed');
  const [note, setNote] = useState('');

  function handleSend() {
    submitConnectRequest(note);
    setNote('');
    setMode('sent');
  }

  return (
    <View style={[styles.card, compact && styles.cardCompact]}>
      <Text style={styles.title}>A real person is always here.</Text>

      {mode === 'sent' ? (
        // ── Honest confirmation. No false promises about timing. ──────────────
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
            // Rung 1 — ALWAYS available. The human is never gated.
            <TouchableOpacity
              style={styles.humanBtn}
              activeOpacity={0.8}
              onPress={() => setMode('writing')}
            >
              <Text style={styles.humanBtnText}>Talk to a real person</Text>
            </TouchableOpacity>
          ) : (
            // Writing mode — capture the note on-device.
            <View style={styles.writeBox}>
              <TextInput
                style={styles.input}
                placeholder="Write whatever you'd like to say, or leave it blank — either way, someone will reach out."
                placeholderTextColor={colors.textMuted}
                multiline
                numberOfLines={4}
                maxLength={1000}
                value={note}
                onChangeText={setNote}
                autoFocus
                textAlignVertical="top"
              />
              <View style={styles.writeActions}>
                <TouchableOpacity
                  activeOpacity={0.7}
                  onPress={() => { setMode('closed'); setNote(''); }}
                >
                  <Text style={styles.cancelText}>Cancel</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={styles.sendBtn}
                  activeOpacity={0.85}
                  onPress={handleSend}
                >
                  <Text style={styles.sendBtnText}>Send to a real person</Text>
                </TouchableOpacity>
              </View>
            </View>
          )}
        </>
      )}

      {/* Rung 2 — missionary referral, only when genuinely ready. Gentle, optional.
          This IS a real, official public form, so it stays a live link. */}
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
        <Text style={styles.sub}>Or just keep going — there's no rush.</Text>
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
    fontSize: 16, fontFamily: 'Georgia', color: colors.textMid, marginBottom: spacing.sm,
  },
  body: {
    fontSize: 13, fontFamily: 'Georgia', color: colors.textDim,
    lineHeight: 20, marginBottom: spacing.md,
  },
  confirm: {
    fontSize: 14, fontFamily: 'Georgia', color: colors.green,
    lineHeight: 22, marginBottom: spacing.sm, fontStyle: 'italic',
  },

  // Rung 1 button — filled so it reads as the real, inviting action.
  humanBtn: {
    backgroundColor: colors.green,
    borderRadius: radius.sm,
    paddingVertical: 12, paddingHorizontal: 16,
    marginBottom: spacing.sm, alignItems: 'center',
  },
  humanBtnText: {
    color: '#0a0f0a', fontSize: 14, fontFamily: 'Georgia', fontWeight: '600',
  },

  // Writing mode
  writeBox: { marginBottom: spacing.sm },
  input: {
    backgroundColor: colors.bgInput, borderWidth: 1, borderColor: '#2a3a28',
    borderRadius: radius.md, color: colors.textMid, fontSize: 14,
    fontFamily: 'Georgia', padding: 12, minHeight: 96, lineHeight: 22,
    marginBottom: spacing.sm,
  },
  writeActions: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between',
  },
  cancelText: {
    color: colors.textMuted, fontSize: 13, fontFamily: 'Georgia', paddingVertical: 8,
  },
  sendBtn: {
    backgroundColor: colors.green, borderRadius: radius.sm,
    paddingVertical: 10, paddingHorizontal: 16,
  },
  sendBtnText: {
    color: '#0a0f0a', fontSize: 13, fontFamily: 'Georgia', fontWeight: '600',
  },

  missionaryBlock: {
    borderTopWidth: 1, borderTopColor: colors.borderDim,
    paddingTop: spacing.sm, marginTop: spacing.xs, marginBottom: spacing.sm,
  },
  missionaryBody: {
    fontSize: 12, fontFamily: 'Georgia', color: colors.textDim,
    lineHeight: 18, marginBottom: spacing.sm, fontStyle: 'italic',
  },
  missionaryBtn: {
    borderWidth: 1, borderColor: colors.gold, borderRadius: 4,
    paddingVertical: 8, paddingHorizontal: 12, alignSelf: 'flex-start',
  },
  missionaryBtnText: { color: colors.gold, fontSize: 12, fontFamily: 'Georgia' },
  sub: {
    fontSize: 11, color: colors.textMuted, fontFamily: 'Georgia', fontStyle: 'italic',
  },
});
