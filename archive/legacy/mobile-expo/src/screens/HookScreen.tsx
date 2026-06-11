import React, { useEffect, useRef } from 'react';
import {
  View,
  Text,
  Animated,
  TouchableOpacity,
  StyleSheet,
  Dimensions,
} from 'react-native';
import { NativeStackScreenProps } from '@react-navigation/native-stack';
import { LinearGradient } from 'expo-linear-gradient';
import { StatusBar } from 'expo-status-bar';
import { RootStackParamList } from '../navigation/AppNavigator';
import { colors, spacing } from '../theme';

type Props = NativeStackScreenProps<RootStackParamList, 'Hook'>;

const { width } = Dimensions.get('window');

export default function HookScreen({ navigation }: Props) {
  // ── Animation refs ────────────────────────────────────────────────────────
  const stoneTranslateX = useRef(new Animated.Value(0)).current;
  const stoneRotate     = useRef(new Animated.Value(0)).current;
  const stoneOpacity    = useRef(new Animated.Value(1)).current;
  const glowOpacity     = useRef(new Animated.Value(0)).current;
  const glowScale       = useRef(new Animated.Value(0.3)).current;
  const textOpacity     = useRef(new Animated.Value(0)).current;
  const subOpacity      = useRef(new Animated.Value(0)).current;
  const btnOpacity      = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    // 1. Brief pause so the user sees the stone
    // 2. Stone rolls away to the right
    // 3. Glow expands from behind the tomb opening
    // 4. Text and button fade in

    const sequence = Animated.sequence([
      Animated.delay(800),

      // Stone rolls away
      Animated.parallel([
        Animated.timing(stoneTranslateX, {
          toValue:         width * 0.7,
          duration:        900,
          useNativeDriver: true,
        }),
        Animated.timing(stoneRotate, {
          toValue:         1,       // mapped to 60deg in interpolate below
          duration:        900,
          useNativeDriver: true,
        }),
        Animated.timing(stoneOpacity, {
          toValue:         0,
          duration:        700,
          delay:           200,
          useNativeDriver: true,
        }),
      ]),

      // Glow expands
      Animated.parallel([
        Animated.timing(glowOpacity, {
          toValue:         1,
          duration:        700,
          useNativeDriver: true,
        }),
        Animated.spring(glowScale, {
          toValue:         1,
          friction:        5,
          tension:         40,
          useNativeDriver: true,
        }),
      ]),

      // Text fades in
      Animated.timing(textOpacity, {
        toValue:         1,
        duration:        600,
        useNativeDriver: true,
      }),

      Animated.delay(300),

      Animated.timing(subOpacity, {
        toValue:         1,
        duration:        700,
        useNativeDriver: true,
      }),

      Animated.delay(400),

      Animated.timing(btnOpacity, {
        toValue:         1,
        duration:        600,
        useNativeDriver: true,
      }),
    ]);

    sequence.start();
  }, []);

  const stoneRotateDeg = stoneRotate.interpolate({
    inputRange:  [0, 1],
    outputRange: ['0deg', '60deg'],
  });

  return (
    <View style={styles.container}>
      <StatusBar style="light" />

      {/* ── Tomb + glow ──────────────────────────────────────────────────── */}
      <View style={styles.tombContainer}>
        {/* Glow behind the opening */}
        <Animated.View
          style={[
            styles.glowWrapper,
            { opacity: glowOpacity, transform: [{ scale: glowScale }] },
          ]}
        >
          <LinearGradient
            colors={['rgba(255,235,160,0.55)', 'rgba(255,220,120,0.18)', 'transparent']}
            style={styles.glowGradient}
          />
        </Animated.View>

        {/* Tomb arch (opening) */}
        <View style={styles.tombArch} />

        {/* Rolling stone */}
        <Animated.View
          style={[
            styles.stone,
            {
              opacity:   stoneOpacity,
              transform: [
                { translateX: stoneTranslateX },
                { rotate:     stoneRotateDeg  },
              ],
            },
          ]}
        />
      </View>

      {/* ── He Is Risen ──────────────────────────────────────────────────── */}
      <Animated.Text style={[styles.risenText, { opacity: textOpacity }]}>
        He Is Risen.
      </Animated.Text>

      <Animated.Text style={[styles.subText, { opacity: subOpacity }]}>
        Every moment of pure peace you have ever felt has a source.
      </Animated.Text>

      {/* ── CTA ──────────────────────────────────────────────────────────── */}
      <Animated.View style={{ opacity: btnOpacity }}>
        <TouchableOpacity
          style={styles.btn}
          activeOpacity={0.75}
          onPress={() => navigation.navigate('Onboard')}
        >
          <Text style={styles.btnText}>I want to understand that →</Text>
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

  // Tomb
  tombContainer: {
    width:          110,
    height:         110,
    alignItems:     'center',
    justifyContent: 'flex-end',
    marginBottom:   spacing.xl,
    position:       'relative',
  },
  tombArch: {
    width:           66,
    height:          84,
    backgroundColor: '#1a1a22',
    borderRadius:    33,
    borderTopLeftRadius:  33,
    borderTopRightRadius: 33,
    borderBottomLeftRadius: 4,
    borderBottomRightRadius: 4,
  },
  stone: {
    position:        'absolute',
    bottom:          0,
    width:           60,
    height:          76,
    backgroundColor: '#3a3830',
    borderRadius:    30,
    borderTopLeftRadius:  30,
    borderTopRightRadius: 30,
  },
  glowWrapper: {
    position:        'absolute',
    top:             -10,
    left:            -20,
    width:           110,
    height:          110,
    alignItems:      'center',
    justifyContent:  'center',
  },
  glowGradient: {
    width:           110,
    height:          110,
    borderRadius:    55,
  },

  // Text
  risenText: {
    fontSize:        32,
    fontFamily:      'Georgia',
    color:           colors.goldLight,
    letterSpacing:   2,
    textAlign:       'center',
    marginBottom:    spacing.md,
  },
  subText: {
    fontSize:        15,
    fontFamily:      'Georgia',
    color:           colors.textMuted,
    textAlign:       'center',
    lineHeight:      24,
    maxWidth:        280,
    marginBottom:    spacing.xxl,
  },

  // Button
  btn: {
    borderWidth:   1,
    borderColor:   colors.borderDim,
    paddingVertical:   12,
    paddingHorizontal: 28,
    borderRadius:  4,
  },
  btnText: {
    color:       colors.gold,
    fontSize:    15,
    fontFamily:  'Georgia',
    letterSpacing: 0.5,
  },
});
