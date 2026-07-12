/**
 * NextPageButton — advancing to the next prescribed page (FEED-2.0-SPEC §4).
 *
 * The wait is presented HONESTLY as the page being prepared — never an error,
 * never a spinner that looks broken. Tapping asks the store for the wait (a
 * ladder that grows the more you skip, and shrinks by the time you've already
 * spent on the current page). While it counts down we show "Preparing your next
 * page…"; when it reaches zero the next page is built and shown.
 */

import React, { useEffect, useRef, useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing } from '../theme';

export default function NextPageButton() {
  const requestNextPage = useAppStore(s => s.requestNextPage);
  const commitNextPage  = useAppStore(s => s.commitNextPage);

  const [remaining, setRemaining] = useState(0); // seconds left while preparing
  const [preparing, setPreparing] = useState(false);
  const timer = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => () => { if (timer.current) clearInterval(timer.current); }, []);

  function start() {
    if (preparing) return;
    const wait = requestNextPage();
    if (wait <= 0) { commitNextPage(); return; }
    setPreparing(true);
    setRemaining(wait);
    timer.current = setInterval(() => {
      setRemaining(prev => {
        if (prev <= 1) {
          if (timer.current) clearInterval(timer.current);
          setPreparing(false);
          commitNextPage();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
  }

  return (
    <View style={styles.wrap}>
      <TouchableOpacity
        style={[styles.btn, preparing && styles.btnPreparing]}
        activeOpacity={0.8}
        onPress={start}
        disabled={preparing}
      >
        <Text style={styles.btnText}>
          {preparing
            ? `Preparing your next page… ${remaining}s`
            : 'Next page →'}
        </Text>
      </TouchableOpacity>
      {preparing && (
        <Text style={styles.hint}>
          Time spent with what's here brings the next page sooner.
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: { marginTop: spacing.md, alignItems: 'center' },
  btn: {
    width:           '100%',
    borderWidth:     1,
    borderColor:     colors.gold,
    borderRadius:    24,
    paddingVertical: 13,
    minHeight:       48,
    alignItems:      'center',
    justifyContent:  'center',
  },
  btnPreparing: { borderColor: colors.borderDim },
  btnText: {
    color:      colors.gold,
    fontSize:   14,
    fontFamily: 'Jost_400Regular',
  },
  hint: {
    marginTop:  spacing.sm,
    color:      colors.textMuted,
    fontSize:   11,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    textAlign:  'center',
  },
});
