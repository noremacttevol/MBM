/**
 * BlessingToast — a moment of blessing, in WORDS only (never numbers).
 *
 * The store sets `blessing` to a single warm line after a meaningful act
 * (a dialogue answer, a heart, an accepted invitation, a follow-up). It clears
 * itself after a few seconds. This renders that line as a soft, floating toast
 * near the bottom of the screen, the way the prototype does.
 */

import React, { useEffect, useRef } from 'react';
import { Animated, StyleSheet, Text, View } from 'react-native';
import { useAppStore } from '../store/useAppStore';
import { colors } from '../theme';

export default function BlessingToast() {
  const blessing = useAppStore(s => s.blessing);
  const opacity  = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    if (blessing) {
      opacity.setValue(0);
      Animated.timing(opacity, { toValue: 1, duration: 280, useNativeDriver: true }).start();
    } else {
      Animated.timing(opacity, { toValue: 0, duration: 320, useNativeDriver: true }).start();
    }
  }, [blessing]);

  if (!blessing) return null;

  return (
    <View pointerEvents="none" style={styles.wrap}>
      <Animated.View style={[styles.toast, { opacity }]}>
        <Text style={styles.text}>{blessing}</Text>
      </Animated.View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrap: {
    position: 'absolute',
    left: 24, right: 24, bottom: 96,
    alignItems: 'center',
    zIndex: 80,
  },
  toast: {
    backgroundColor: 'rgba(22,20,14,0.94)',
    borderWidth: 1,
    borderColor: '#3a3526',
    borderRadius: 20,
    paddingVertical: 10,
    paddingHorizontal: 18,
    maxWidth: 280,
    shadowColor: '#000',
    shadowOpacity: 0.5,
    shadowRadius: 16,
    shadowOffset: { width: 0, height: 4 },
    elevation: 6,
  },
  text: {
    fontSize: 13,
    fontFamily: 'Georgia',
    fontStyle: 'italic',
    color: '#e8dfc0',
    lineHeight: 19,
    textAlign: 'center',
  },
});
