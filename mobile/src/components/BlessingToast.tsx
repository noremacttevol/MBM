/**
 * BlessingToast — a moment of blessing, in WORDS only (never numbers).
 *
 * The store sets `blessing` to a BlessingCard after a meaningful act (a dialogue
 * answer, a heart, an accepted invitation, a journal reflection). Unlike the old
 * toast, it does NOT clear itself. It STAYS until the person swipes it — so they
 * can read it slowly, sit with it, and feel its absence when it goes:
 *   • swipe LEFT  → dismiss it.
 *   • swipe RIGHT → carry the question, their answer, AND this word into Chat,
 *                   so a quiet moment can become a real conversation.
 */

import React, { useEffect, useRef } from 'react';
import { Animated, PanResponder, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { useAppStore } from '../store/useAppStore';

const SWIPE_THRESHOLD = 90;   // how far is a deliberate swipe, not a stray touch

export default function BlessingToast() {
  const blessing          = useAppStore(s => s.blessing);
  const clearBlessing     = useAppStore(s => s.clearBlessing);
  const openBlessingInChat = useAppStore(s => s.openBlessingInChat);
  const navigation        = useNavigation<any>();

  const opacity = useRef(new Animated.Value(0)).current;
  const pan     = useRef(new Animated.ValueXY()).current;

  // Keep the latest handlers/values reachable from the gesture closure (which is
  // built once) without rebuilding the PanResponder on every render.
  const blessingRef = useRef(blessing);
  blessingRef.current = blessing;

  useEffect(() => {
    if (blessing) {
      pan.setValue({ x: 0, y: 0 });
      opacity.setValue(0);
      Animated.timing(opacity, { toValue: 1, duration: 280, useNativeDriver: true }).start();
    } else {
      Animated.timing(opacity, { toValue: 0, duration: 320, useNativeDriver: true }).start();
    }
  }, [blessing]);

  const finishLeft = () => {
    // Slide off to the left, then dismiss.
    Animated.timing(pan, {
      toValue: { x: -500, y: 0 },
      duration: 220,
      useNativeDriver: true,
    }).start(() => clearBlessing());
  };

  const finishRight = () => {
    // Slide off to the right, carry it into Chat, then switch to the Chat tab.
    Animated.timing(pan, {
      toValue: { x: 500, y: 0 },
      duration: 220,
      useNativeDriver: true,
    }).start(() => {
      openBlessingInChat();
      navigation.navigate('Chat');
    });
  };

  const responder = useRef(
    PanResponder.create({
      onMoveShouldSetPanResponder: (_e, g) =>
        Math.abs(g.dx) > 8 && Math.abs(g.dx) > Math.abs(g.dy),
      onPanResponderMove: (_e, g) => {
        pan.setValue({ x: g.dx, y: 0 });
      },
      onPanResponderRelease: (_e, g) => {
        if (g.dx <= -SWIPE_THRESHOLD) {
          finishLeft();
        } else if (g.dx >= SWIPE_THRESHOLD) {
          finishRight();
        } else {
          // Not far enough — settle back into place.
          Animated.spring(pan, {
            toValue: { x: 0, y: 0 },
            useNativeDriver: true,
            friction: 7,
          }).start();
        }
      },
    }),
  ).current;

  if (!blessing) return null;

  return (
    <View style={styles.wrap} pointerEvents="box-none">
      <Animated.View
        {...responder.panHandlers}
        style={[
          styles.toast,
          { opacity, transform: [{ translateX: pan.x }] },
        ]}
      >
        <Text style={styles.text}>{blessing.line}</Text>
        {/* Tappable too, so it works on web where there is no swipe. */}
        <View style={styles.hintRow}>
          <TouchableOpacity onPress={finishLeft} hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}>
            <Text style={styles.hint}>swipe or tap to close</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={finishRight} hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}>
            <Text style={styles.hint}>talk about it →</Text>
          </TouchableOpacity>
        </View>
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
    backgroundColor: 'rgba(22,20,14,0.96)',
    borderWidth: 1,
    borderColor: '#3a3526',
    borderRadius: 20,
    paddingVertical: 16,
    paddingHorizontal: 22,
    maxWidth: 340,
    shadowColor: '#000',
    shadowOpacity: 0.5,
    shadowRadius: 16,
    shadowOffset: { width: 0, height: 4 },
    elevation: 6,
  },
  text: {
    fontSize: 15,
    fontFamily: 'MBMCross',
    fontStyle: 'italic',
    color: '#e8dfc0',
    lineHeight: 23,
    textAlign: 'center',
  },
  hintRow: {
    marginTop: 12,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  hint: {
    fontSize: 11,
    letterSpacing: 0.3,
    color: '#8c7a5f',
  },
});
