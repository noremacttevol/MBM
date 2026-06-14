import React, { useState } from 'react';
import {
  View, Text, TouchableOpacity, Modal, StyleSheet, ScrollView, Pressable,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import ConnectCard from './ConnectCard';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing } from '../theme';

/**
 * GlobalConnect — a real person, ALWAYS one tap away, on every screen, never
 * buried (CLAUDE.md law). Mounted once over the whole tab area, it shows a single
 * floating button that opens the in-app connect panel from anywhere, and a badge
 * when a real person has replied so the person knows to come back.
 */
export default function GlobalConnect() {
  const [open, setOpen] = useState(false);
  const inboxUnread = useAppStore(s => s.inboxUnread);

  return (
    <>
      <TouchableOpacity
        style={styles.fab}
        activeOpacity={0.85}
        onPress={() => setOpen(true)}
        accessibilityRole="button"
        accessibilityLabel="Talk to a real person"
      >
        <Ionicons name="chatbubbles" size={18} color="#0a0f0a" />
        <Text style={styles.fabText}>Talk to a real person</Text>
        {inboxUnread > 0 && (
          <View style={styles.badge}>
            <Text style={styles.badgeText}>{inboxUnread}</Text>
          </View>
        )}
      </TouchableOpacity>

      <Modal
        visible={open}
        animationType="slide"
        transparent
        onRequestClose={() => setOpen(false)}
      >
        <Pressable style={styles.backdrop} onPress={() => setOpen(false)} />
        <View style={styles.sheet}>
          <View style={styles.handle} />
          <View style={styles.sheetHeader}>
            <Text style={styles.sheetTitle}>A real person is here</Text>
            <TouchableOpacity onPress={() => setOpen(false)} accessibilityLabel="Close">
              <Ionicons name="close" size={22} color={colors.textMuted} />
            </TouchableOpacity>
          </View>
          <ScrollView contentContainerStyle={{ paddingHorizontal: spacing.md, paddingBottom: spacing.lg }}>
            <ConnectCard />
          </ScrollView>
        </View>
      </Modal>
    </>
  );
}

const styles = StyleSheet.create({
  fab: {
    position: 'absolute',
    right: spacing.md,
    bottom: 84, // sits just above the tab bar
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.gold,
    paddingVertical: 10,
    paddingHorizontal: 14,
    borderRadius: 24,
    shadowColor: '#000',
    shadowOpacity: 0.3,
    shadowRadius: 6,
    shadowOffset: { width: 0, height: 2 },
    elevation: 6,
  },
  fabText: { color: '#0a0f0a', fontWeight: '700', fontSize: 13, marginLeft: 7 },
  badge: {
    position: 'absolute',
    top: -6,
    right: -6,
    backgroundColor: colors.green,
    minWidth: 18,
    height: 18,
    borderRadius: 9,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 4,
  },
  badgeText: { color: '#0a0f0a', fontSize: 11, fontWeight: '700' },
  backdrop: { flex: 1, backgroundColor: 'rgba(0,0,0,0.5)' },
  sheet: {
    position: 'absolute',
    left: 0,
    right: 0,
    bottom: 0,
    maxHeight: '85%',
    backgroundColor: colors.bgCard,
    borderTopLeftRadius: 18,
    borderTopRightRadius: 18,
    paddingBottom: spacing.lg,
    borderTopWidth: 1,
    borderTopColor: colors.borderDim,
  },
  handle: {
    alignSelf: 'center',
    width: 40,
    height: 4,
    borderRadius: 2,
    backgroundColor: colors.borderDim,
    marginTop: 8,
    marginBottom: 4,
  },
  sheetHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
  },
  sheetTitle: { color: colors.text, fontSize: 16, fontWeight: '600' },
});
