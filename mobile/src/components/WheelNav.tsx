/**
 * WheelNav — the bottom navigation chrome for Feed 2.0 (FEED-2.0-SPEC §5).
 *
 * One dot per page created (including ignored pages and honored-history buckets),
 * accumulating left→right. The HOME icon is the current prescribed page and always
 * sits at the right end. Tapping any dot jumps to that page; every previous page
 * is re-viewable at any time. The home dot returns to today's page fast.
 */

import React from 'react';
import { View, Text, TouchableOpacity, ScrollView, StyleSheet } from 'react-native';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing } from '../theme';

export default function WheelNav() {
  const pages            = useAppStore(s => s.pages);
  const currentPageIndex = useAppStore(s => s.currentPageIndex);
  const goToPage         = useAppStore(s => s.goToPage);

  if (pages.length <= 1) return null; // no history yet — nothing to navigate

  const homeIdx = pages.length - 1;

  return (
    <View style={styles.bar}>
      <ScrollView
        horizontal
        showsHorizontalScrollIndicator={false}
        contentContainerStyle={styles.row}
      >
        {pages.map((p, i) => {
          const active = i === currentPageIndex;
          const isHome = i === homeIdx;
          return (
            <TouchableOpacity
              key={p.id}
              onPress={() => goToPage(i)}
              activeOpacity={0.7}
              style={styles.hit}
              accessibilityLabel={isHome ? "Today's page" : `Page ${i + 1}`}
            >
              {isHome ? (
                <Text style={[styles.home, active && styles.homeActive]}>⌂</Text>
              ) : (
                <View style={[
                  styles.dot,
                  p.honorArchive && styles.dotArchive,
                  active && styles.dotActive,
                ]} />
              )}
            </TouchableOpacity>
          );
        })}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  bar: {
    borderTopWidth: 1,
    borderTopColor: colors.border,
    backgroundColor: colors.bg,
    paddingVertical: spacing.sm,
  },
  row: {
    alignItems:     'center',
    justifyContent: 'center',
    paddingHorizontal: spacing.md,
    gap:            14,
    minWidth:       '100%',
  },
  hit: {
    padding: 6,
    alignItems: 'center',
    justifyContent: 'center',
  },
  dot: {
    width: 7,
    height: 7,
    borderRadius: 4,
    backgroundColor: colors.textMuted,
  },
  dotArchive: {
    backgroundColor: 'transparent',
    borderWidth: 1,
    borderColor: colors.textMuted,
  },
  dotActive: {
    backgroundColor: colors.gold,
    borderColor: colors.gold,
    width: 9,
    height: 9,
    borderRadius: 5,
  },
  home: {
    fontSize: 18,
    color: colors.textMuted,
    fontFamily: 'Jost_400Regular',
  },
  homeActive: {
    color: colors.gold,
  },
});
