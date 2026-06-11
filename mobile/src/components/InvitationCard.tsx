/**
 * InvitationCard — "AN INVITATION".
 *
 * Something to DO, the way Jesus gave people things to do. A spiritual exercise
 * matched to the person's signals. "I'll try it" accepts it (a follow-up will be
 * waiting next time); "Not this time" sets it aside, no guilt. Jesus let the rich
 * young ruler walk away.
 */

import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { SpiritualExercise } from '../engine/exercises';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing } from '../theme';

interface Props {
  exercise: SpiritualExercise;
}

export default function InvitationCard({ exercise }: Props) {
  const acceptExercise = useAppStore(s => s.acceptExercise);
  const passExercise   = useAppStore(s => s.passExercise);

  return (
    <View style={styles.card}>
      <Text style={styles.label}>AN INVITATION</Text>
      <Text style={styles.body}>{exercise.text}</Text>
      <Text style={styles.ref}>{exercise.ref}</Text>
      <View style={styles.actions}>
        <TouchableOpacity style={styles.acceptBtn} activeOpacity={0.85} onPress={() => acceptExercise(exercise)}>
          <Text style={styles.acceptText}>I'll try it</Text>
        </TouchableOpacity>
        <TouchableOpacity activeOpacity={0.7} onPress={() => passExercise(exercise)}>
          <Text style={styles.passText}>Not this time</Text>
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
    fontFamily: 'Georgia', marginBottom: spacing.sm,
  },
  body: {
    fontSize: 15, fontFamily: 'Georgia', color: '#d0c8b0',
    lineHeight: 24, marginBottom: spacing.sm,
  },
  ref: {
    fontSize: 11, fontFamily: 'Georgia', fontStyle: 'italic',
    color: colors.textMuted, lineHeight: 17, marginBottom: spacing.md,
  },
  actions: { flexDirection: 'row', alignItems: 'center', gap: 12 },
  acceptBtn: {
    backgroundColor: colors.gold, borderRadius: 20,
    paddingVertical: 10, paddingHorizontal: 24,
  },
  acceptText: { color: colors.onAccent, fontSize: 13, fontFamily: 'Georgia', fontWeight: '600' },
  passText: { color: colors.textMuted, fontSize: 12, fontFamily: 'Georgia', fontStyle: 'italic', paddingVertical: 10, paddingHorizontal: 4 },
});
