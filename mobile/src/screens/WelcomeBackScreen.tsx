/**
 * WelcomeBackScreen — the person is known. No cold restarts (Law 5).
 *
 * Shown on launch when there is persisted main-state: their name (if given), a
 * gentle recall of the last thing they wrote or were in the middle of, and one
 * quiet button back into the app — picking up exactly where they left off.
 */

import React, { useEffect, useRef } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Animated } from 'react-native';
import { NativeStackScreenProps } from '@react-navigation/native-stack';
import { StatusBar } from 'expo-status-bar';
import { RootStackParamList } from '../navigation/AppNavigator';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing } from '../theme';

type Props = NativeStackScreenProps<RootStackParamList, 'WelcomeBack'>;

export default function WelcomeBackScreen({ navigation }: Props) {
  const name           = useAppStore(s => s.name);
  const journalEntries = useAppStore(s => s.journalEntries);
  const chatMessages   = useAppStore(s => s.chatMessages);

  const fade = useRef(new Animated.Value(0)).current;
  useEffect(() => {
    Animated.timing(fade, { toValue: 1, duration: 800, useNativeDriver: true }).start();
  }, []);

  const welcomeName = name ? `, ${name}` : '';

  const lastJournal = journalEntries[0]?.text ?? '';
  const recall = lastJournal
    ? `Last time you wrote: "${lastJournal.slice(0, 90)}${lastJournal.length > 90 ? '…' : ''}"`
    : chatMessages.length > 0
      ? 'You were in the middle of a conversation. It’s still here, just as you left it.'
      : 'Your place here is just as you left it. No rush.';

  return (
    <View style={styles.container}>
      <StatusBar style="light" />
      <Animated.View style={[styles.inner, { opacity: fade }]}>
        <View style={styles.hairline} />
        <Text style={styles.title}>Welcome back{welcomeName}.</Text>
        <Text style={styles.recall}>{recall}</Text>
        <TouchableOpacity
          style={styles.btn}
          activeOpacity={0.85}
          onPress={() => navigation.replace('Main')}
        >
          <Text style={styles.btnText}>Pick up where you left off →</Text>
        </TouchableOpacity>
      </Animated.View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex:            1,
    backgroundColor: colors.bg,
    alignItems:      'center',
    justifyContent:  'center',
    paddingHorizontal: spacing.xl,
  },
  inner: { alignItems: 'center' },
  hairline: {
    width:           60,
    height:          1,
    backgroundColor: colors.borderDim,
    marginBottom:    spacing.xl,
  },
  title: {
    fontSize:     26,
    fontFamily:   'Georgia',
    color:        colors.goldLight,
    textAlign:    'center',
    lineHeight:   36,
    marginBottom: spacing.md,
  },
  recall: {
    fontSize:     14,
    fontFamily:   'Georgia',
    color:        colors.textDim,
    textAlign:    'center',
    lineHeight:   24,
    maxWidth:     280,
    marginBottom: spacing.xxl,
    fontStyle:    'italic',
  },
  btn: {
    backgroundColor:   colors.gold,
    borderRadius:      26,
    paddingVertical:   13,
    paddingHorizontal: 36,
  },
  btnText: {
    fontSize:      15,
    fontFamily:    'Georgia',
    color:         colors.onAccent,
    letterSpacing: 0.5,
    fontWeight:    '600',
  },
});
