/**
 * FollowUpCard — "YOU TRIED SOMETHING".
 *
 * Renders at the TOP of the feed when a previously accepted spiritual exercise's
 * follow-up is due (the person went away and came back). This is the most
 * personal thing on the screen, so it comes first. Invite → try → report → learn:
 * what comes back is where the engine learns the most.
 */

import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing } from '../theme';

interface Props {
  followUpText: string;
}

export default function FollowUpCard({ followUpText }: Props) {
  const answerFollowUp = useAppStore(s => s.answerFollowUp);
  const [note, setNote] = useState('');

  return (
    <View style={styles.card}>
      <Text style={styles.label}>YOU TRIED SOMETHING</Text>
      <Text style={styles.body}>{followUpText}</Text>

      <TextInput
        style={styles.input}
        value={note}
        onChangeText={setNote}
        placeholder="If you want, say what you noticed — a line is plenty. (optional)"
        placeholderTextColor={colors.textMuted}
        multiline
        textAlignVertical="top"
      />

      <View style={styles.options}>
        <TouchableOpacity style={styles.optBtn} activeOpacity={0.7} onPress={() => answerFollowUp('something', note)}>
          <Text style={styles.optText}>Something happened that I don't know what to call.</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.optBtn} activeOpacity={0.7} onPress={() => answerFollowUp('good', note)}>
          <Text style={styles.optText}>It was quieter than I expected — but good.</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.optBtn} activeOpacity={0.7} onPress={() => answerFollowUp('nothing', note)}>
          <Text style={styles.optText}>Honestly? Nothing came back.</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.optBtn, styles.optBtnDashed]} activeOpacity={0.7} onPress={() => answerFollowUp('not_yet', note)}>
          <Text style={styles.optTextMuted}>I didn't get to it yet.</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    borderWidth: 1,
    borderColor: '#3a3526',
    backgroundColor: '#12100b',
    borderRadius: 6,
    padding: spacing.md,
    marginBottom: spacing.md,
  },
  label: {
    fontSize: 10, letterSpacing: 1.5, color: '#8a7d50',
    fontFamily: 'MBMCross', marginBottom: spacing.sm,
  },
  body: {
    fontSize: 15, fontFamily: 'MBMCross', color: '#d0c8b0',
    lineHeight: 23, marginBottom: 12,
  },
  input: {
    width: '100%', borderWidth: 1, borderColor: '#1e1c18', borderRadius: 4,
    backgroundColor: colors.bgInput, color: '#d0c8b0', fontSize: 13,
    fontFamily: 'MBMCross', padding: spacing.sm, minHeight: 56,
    marginBottom: 12, lineHeight: 19,
  },
  options: { gap: spacing.xs },
  optBtn: {
    borderWidth: 1, borderColor: '#1e1c18', borderRadius: 4,
    paddingVertical: 10, paddingHorizontal: 12,
  },
  optBtnDashed: { borderStyle: 'dashed' },
  optText: { fontSize: 13, fontFamily: 'MBMCross', color: colors.textDim, lineHeight: 19 },
  optTextMuted: { fontSize: 13, fontFamily: 'MBMCross', color: colors.textMuted, fontStyle: 'italic' },
});
