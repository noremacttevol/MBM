/**
 * MilkBeforeMeatNote — the quiet, honest warning shown every time the app opens.
 *
 * It sits low and small, never as a popup or a tappable lure. Above the note is
 * the label "Milk Before Meat" so that, over opens, the label itself comes to
 * carry the meaning: MILK = what this app gives (teaching, practice, a finger
 * pointing toward the good); MEAT = worshipping the living God Himself, which
 * only ever happens with Him and with real people. Once a returning person
 * recognizes the label, they know the point and don't need to read the body.
 *
 * A different variant shows each open (pickMilkNote), so the same truth lands
 * through a different door until the label alone says it all.
 */

import React, { useRef } from 'react';
import { View, Text, StyleSheet, Animated } from 'react-native';
import { MILK_BEFORE_MEAT_LABEL, pickMilkNote } from '../data/milkBeforeMeat';
import { colors } from '../theme';

interface Props {
  // Optional pre-picked note, so a parent can keep the same one stable across a
  // re-render. Defaults to a fresh random variant for this open.
  note?: string;
}

export default function MilkBeforeMeatNote({ note }: Props) {
  // Pick once for the life of this mount so the text doesn't flicker between
  // variants on re-render.
  const line = useRef(note ?? pickMilkNote()).current;

  const fade = useRef(new Animated.Value(0)).current;
  React.useEffect(() => {
    Animated.timing(fade, {
      toValue:         1,
      duration:        1100,
      delay:           400,
      useNativeDriver: true,
    }).start();
  }, []);

  return (
    <Animated.View style={[styles.wrap, { opacity: fade }]} pointerEvents="none">
      <Text style={styles.label}>{MILK_BEFORE_MEAT_LABEL}</Text>
      <View style={styles.rule} />
      <Text style={styles.note}>{line}</Text>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  wrap: {
    alignItems:        'center',
    paddingHorizontal: 28,
    maxWidth:          360,
    alignSelf:         'center',
  },
  label: {
    fontSize:      11,
    fontFamily:    'MBMCross',
    color:         colors.textMuted,
    letterSpacing: 1.5,
    textTransform: 'uppercase',
    marginBottom:  8,
  },
  rule: {
    width:           28,
    height:          1,
    backgroundColor: colors.borderDim,
    marginBottom:    10,
  },
  note: {
    fontSize:   11,
    fontFamily: 'MBMCross',
    fontStyle:  'italic',
    color:      colors.textMuted,
    textAlign:  'center',
    lineHeight: 18,
  },
});
