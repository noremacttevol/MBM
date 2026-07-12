/**
 * TakeawayCheck — Rev 2.2 (Cameron, 2026-07-12).
 *
 * The one-line, checkbox-confirmable INTENTION of a scripture or story — what
 * the God-inspired word is for in a life: "[ ] This helped me see how God loves
 * all of us." Tapping it records a traceable confirmation (kept on the record,
 * showable later), counts as interacting with the item (earns the Get-new /
 * scroll-past replacement), and quietly makes the discipling intention of every
 * piece of content plain. Disagreement is welcome — the Reply row sits right
 * below for saying it differently.
 */

import React from 'react';
import { Text, TouchableOpacity, StyleSheet } from 'react-native';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing } from '../theme';

interface Props {
  /** Stable key for the record — e.g. "video-8" or "verse-42". */
  takeawayKey: string;
  text:        string;
  /** The feed slot this confirms — marks it interacted. */
  slotId?:     string;
}

export default function TakeawayCheck({ takeawayKey, text, slotId }: Props) {
  const confirmTakeaway    = useAppStore(s => s.confirmTakeaway);
  const confirmed          = useAppStore(s =>
    s.confirmedTakeaways.some(t => t.key === takeawayKey));

  return (
    <TouchableOpacity
      style={[styles.row, confirmed && styles.rowConfirmed]}
      activeOpacity={0.7}
      onPress={() => confirmTakeaway(takeawayKey, text, slotId)}
      disabled={confirmed}
      accessibilityRole="checkbox"
      accessibilityState={{ checked: confirmed }}
    >
      <Text style={[styles.box, confirmed && styles.boxConfirmed]}>
        {confirmed ? '☑' : '☐'}
      </Text>
      <Text style={[styles.text, confirmed && styles.textConfirmed]}>{text}</Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  row: {
    flexDirection: 'row',
    alignItems:    'flex-start',
    gap:           8,
    marginTop:     spacing.sm + 2,
    paddingVertical:   6,
    paddingHorizontal: 8,
    borderWidth:   1,
    borderColor:   colors.borderDim,
    borderRadius:  4,
  },
  rowConfirmed: {
    borderColor: colors.green + '66',
    backgroundColor: colors.green + '0d',
  },
  box: {
    fontSize:   15,
    lineHeight: 20,
    color:      colors.textMuted,
  },
  boxConfirmed: { color: colors.green },
  text: {
    flex:       1,
    fontSize:   13,
    color:      colors.textDim,
    fontFamily: 'Jost_400Regular',
    lineHeight: 20,
  },
  textConfirmed: { color: colors.textMid },
});
