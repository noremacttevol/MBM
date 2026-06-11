import React, { useEffect, useRef } from 'react';
import {
  View,
  Text,
  Animated,
  TouchableOpacity,
  StyleSheet,
  Linking,
} from 'react-native';
import { NativeStackScreenProps } from '@react-navigation/native-stack';
import { StatusBar } from 'expo-status-bar';
import { RootStackParamList } from '../navigation/AppNavigator';
import { useAppStore, isRestorationReady } from '../store/useAppStore';
import { colors, spacing } from '../theme';

type Props = NativeStackScreenProps<RootStackParamList, 'TimeCap'>;

// Phase 1: connection requests go directly to Cameron for review
const CONNECT_EMAIL =
  'mailto:noremacttevol@gmail.com' +
  '?subject=MBM%20Connect%20Request' +
  '&body=Hi%2C%20I%20was%20using%20the%20Milk%20Before%20Meat%20app%20and%20would%20love%20to%20talk%20to%20a%20real%20person.';

export default function TimeCapScreen({ navigation }: Props) {
  const resetSession    = useAppStore(s => s.resetSession);
  const dialogueSignals = useAppStore(s => s.dialogueSignals);
  const opacity         = useRef(new Animated.Value(0)).current;

  const restorationReady = isRestorationReady(dialogueSignals);

  useEffect(() => {
    Animated.timing(opacity, {
      toValue:         1,
      duration:        800,
      useNativeDriver: true,
    }).start();
  }, []);

  function handleComeBack() {
    resetSession();
    navigation.replace('Hook');
  }

  return (
    <View style={styles.container}>
      <StatusBar style="light" />

      <Animated.View style={[styles.inner, { opacity }]}>
        {/* ── Divider line ────────────────────────────────────────────── */}
        <View style={styles.divider} />

        {/* ── Cap message ─────────────────────────────────────────────── */}
        <Text style={styles.primary}>
          You have filled your cup with light for today.
        </Text>

        <Text style={styles.secondary}>
          Close this and step away from the screen.{'\n'}
          Go share that light with someone in the real world.
        </Text>

        {/* ── Scripture ───────────────────────────────────────────────── */}
        <Text style={styles.scripture}>
          "Let your light shine before others, that they may see your good deeds
          and glorify your Father in heaven."
        </Text>
        <Text style={styles.scriptureRef}>Matthew 5:16</Text>

        {/* ── Talk to someone — only when restoration-ready signals present */}
        {restorationReady && (
          <View style={styles.talkBlock}>
            <Text style={styles.talkLabel}>Not ready to leave yet?</Text>
            <TouchableOpacity
              style={styles.talkBtn}
              activeOpacity={0.75}
              onPress={() => Linking.openURL(CONNECT_EMAIL).catch(() => {})}
            >
              <Text style={styles.talkBtnText}>Talk to someone real →</Text>
            </TouchableOpacity>
          </View>
        )}

        {/* ── Come back tomorrow ──────────────────────────────────────── */}
        <TouchableOpacity
          style={styles.backBtn}
          activeOpacity={0.6}
          onPress={handleComeBack}
        >
          <Text style={styles.backBtnText}>Come back →</Text>
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
  inner: {
    alignItems: 'center',
    maxWidth:   320,
  },

  divider: {
    width:         60,
    height:        1,
    backgroundColor: colors.borderDim,
    marginBottom:  spacing.xl,
  },

  primary: {
    fontSize:     20,
    fontFamily:   'Georgia',
    color:        colors.textMid,
    textAlign:    'center',
    lineHeight:   30,
    marginBottom: spacing.lg,
  },
  secondary: {
    fontSize:     14,
    fontFamily:   'Georgia',
    color:        colors.textDim,
    textAlign:    'center',
    lineHeight:   22,
    marginBottom: spacing.xl,
  },

  scripture: {
    fontSize:     13,
    fontFamily:   'Georgia',
    color:        colors.textMuted,
    textAlign:    'center',
    lineHeight:   20,
    fontStyle:    'italic',
    marginBottom: spacing.xs,
  },
  scriptureRef: {
    fontSize:     11,
    fontFamily:   'Georgia',
    color:        colors.textMuted,
    letterSpacing: 0.8,
    marginBottom: spacing.xxl,
  },

  talkBlock: {
    alignItems:   'center',
    marginBottom: spacing.lg,
  },
  talkLabel: {
    fontSize:     12,
    color:        colors.textMuted,
    fontFamily:   'Georgia',
    marginBottom: spacing.sm,
  },
  talkBtn: {
    borderWidth:       1,
    borderColor:       colors.green,
    borderRadius:      4,
    paddingVertical:   10,
    paddingHorizontal: 20,
  },
  talkBtnText: {
    color:      colors.green,
    fontSize:   13,
    fontFamily: 'Georgia',
  },

  backBtn: {
    marginTop: spacing.md,
  },
  backBtnText: {
    color:      colors.textMuted,
    fontSize:   12,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
  },
});
