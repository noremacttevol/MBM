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
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { LinearGradient } from 'expo-linear-gradient';
import { StatusBar } from 'expo-status-bar';
import { RootStackParamList } from '../navigation/AppNavigator';
import { colors, spacing } from '../theme';

type Props = NativeStackScreenProps<RootStackParamList, 'Hook'>;

const { width } = Dimensions.get('window');

export default function HookScreen({ navigation }: Props) {
  // Real device insets — so the honest-word footer clears the Android
  // home/back gesture bar instead of overlapping it.
  const insets = useSafeAreaInsets();

  // ── Animation refs ────────────────────────────────────────────────────────
  const stoneTranslateX = useRef(new Animated.Value(0)).current;
  const stoneRotate     = useRef(new Animated.Value(0)).current;
  const stoneOpacity    = useRef(new Animated.Value(1)).current;
  const glowOpacity     = useRef(new Animated.Value(0)).current;
  const glowScale       = useRef(new Animated.Value(0.3)).current;
  const textOpacity     = useRef(new Animated.Value(0)).current;
  const subOpacity      = useRef(new Animated.Value(0)).current;
  const btnOpacity      = useRef(new Animated.Value(0)).current;
  const footerOpacity   = useRef(new Animated.Value(0)).current;

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

      Animated.delay(500),

      // The honest word, last and quiet — never the headline, but never hidden.
      Animated.timing(footerOpacity, {
        toValue:         1,
        duration:        900,
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

      {/* ── Invitation (presence before proclamation) ─────────────────────────
          The open tomb glows above as wordless hope; the words themselves lead with
          Jesus's own invitation to the weary (Matt 11:28) rather than a creed asked of
          a stranger. Trial data: the cold "He Is Risen" claim alienated grieving/secular/
          burned arrivals before any relationship existed. The resurrection greeting is
          kept for those who arrive already in faith (see build_minister_opening). */}
      <Animated.Text style={[styles.risenText, { opacity: textOpacity }]}>
        Come to me, all who are weary.
      </Animated.Text>

      <Animated.Text style={[styles.subText, { opacity: subOpacity }]}>
        However you arrived — hopeful, guarded, or unsure why you opened this —
        nothing is asked of you here. Every bit of real peace you have ever felt
        has a source.
      </Animated.Text>

      {/* ── CTA ──────────────────────────────────────────────────────────── */}
      <Animated.View style={{ opacity: btnOpacity }}>
        <TouchableOpacity
          style={styles.btn}
          activeOpacity={0.85}
          onPress={() => navigation.navigate('Onboard')}
        >
          <Text style={styles.btnText}>Come and see</Text>
        </TouchableOpacity>
      </Animated.View>

      {/* ── The honest word (Elder Gong, on AI) ───────────────────────────────
          Subtle, never the headline — but said plainly at the threshold so no one
          ever mistakes the app for the Lord. Anchored in Elder Gerrit W. Gong's
          counsel: "Artificial intelligence can answer questions, but it cannot
          answer prayers... it is not God and cannot be God." What stirs here is a
          spiritual exercise to take to God and to people who love you — and to let
          the Spirit, not an app, confirm as true. */}
      <Animated.Text style={[styles.footerText, { opacity: footerOpacity, bottom: insets.bottom + 28 }]}>
        This app is not God. It cannot answer a prayer or know you the way Jesus
        does — it can only point you toward Him. Take what you feel here to God and
        to people who love you, and let the Spirit, not an app, tell you what is true.
      </Animated.Text>
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
    fontFamily:      'Jost_400Regular',
    color:           colors.goldLight,
    letterSpacing:   2,
    textAlign:       'center',
    marginBottom:    spacing.md,
  },
  subText: {
    fontSize:        15,
    fontFamily:      'Jost_400Regular',
    color:           colors.textMuted,
    textAlign:       'center',
    lineHeight:      24,
    maxWidth:        280,
    marginBottom:    spacing.xxl,
  },

  // The honest word — small, dim, low. Present without competing with the invitation.
  footerText: {
    position:        'absolute',
    bottom:          28,
    fontSize:        11,
    fontFamily:      'Jost_400Regular',
    fontStyle:       'italic',
    color:           '#6f6a5c',
    textAlign:       'center',
    lineHeight:      17,
    maxWidth:        300,
    paddingHorizontal: spacing.lg,
  },

  // Button — a filled, inviting pill rather than a thin bare outline.
  btn: {
    backgroundColor:   colors.gold,
    paddingVertical:   14,
    paddingHorizontal: 40,
    borderRadius:      28,
    shadowColor:       colors.goldLight,
    shadowOpacity:     0.35,
    shadowRadius:      16,
    shadowOffset:      { width: 0, height: 0 },
  },
  btnText: {
    color:         '#15110a',
    fontSize:      16,
    fontFamily:    'Jost_400Regular',
    letterSpacing: 0.5,
    fontWeight:    '600',
  },
});
