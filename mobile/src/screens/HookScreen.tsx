import React, { useEffect, useRef, useState } from 'react';
import {
  View,
  Text,
  Animated,
  Easing,
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
import { useAppStore } from '../store/useAppStore';
import { STORY_IDS } from './OnboardScreen';

type Props = NativeStackScreenProps<RootStackParamList, 'Hook'>;

const { width, height } = Dimensions.get('window');

// Short / oddly-proportioned phones (many budget Androids) don't have room for
// the full-size layout — everything scales down a notch so the invitation and
// the honest-word footer NEVER fight for the same pixels.
const COMPACT = height < 700;

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

  // The fade-in text/buttons/disclaimer are NOT rendered on the very first frame.
  // A native-driven opacity-0 element can paint at full opacity for one frame
  // before the native driver syncs, which made the bottom disclaimer flash on,
  // disappear, then fade in ~2.5s later. Mounting them one frame later (after the
  // first paint) removes that flash so the cold-open is smooth.
  const [showContent, setShowContent] = useState(false);

  useEffect(() => {
    // A calm, smooth open: the stone rolls away, light rises from the tomb, then
    // the words and invitation settle in. Eased timing throughout (no springy
    // bounce) and tightened delays so it feels gentle, not laggy or glitchy.
    const ease    = Easing.out(Easing.cubic);
    const easeIn  = Easing.in(Easing.cubic);

    const sequence = Animated.sequence([
      Animated.delay(350),

      // Stone rolls away to the right and fades.
      Animated.parallel([
        Animated.timing(stoneTranslateX, {
          toValue: width * 0.7, duration: 750, easing: easeIn, useNativeDriver: true,
        }),
        Animated.timing(stoneRotate, {
          toValue: 1, duration: 750, easing: easeIn, useNativeDriver: true,
        }),
        Animated.timing(stoneOpacity, {
          toValue: 0, duration: 600, delay: 200, easing: ease, useNativeDriver: true,
        }),
      ]),

      // Light rises from the opening — smooth grow, no spring overshoot.
      Animated.parallel([
        Animated.timing(glowOpacity, {
          toValue: 1, duration: 650, easing: ease, useNativeDriver: true,
        }),
        Animated.timing(glowScale, {
          toValue: 1, duration: 700, easing: ease, useNativeDriver: true,
        }),
      ]),

      // Words and invitation settle in together, gently staggered.
      Animated.stagger(180, [
        Animated.timing(textOpacity, { toValue: 1, duration: 550, easing: ease, useNativeDriver: true }),
        Animated.timing(subOpacity,  { toValue: 1, duration: 550, easing: ease, useNativeDriver: true }),
        Animated.timing(btnOpacity,  { toValue: 1, duration: 550, easing: ease, useNativeDriver: true }),
      ]),

      // The honest word, last and quiet — never the headline, but never hidden.
      // JS driver ON PURPOSE (the one exception): with the native driver, the
      // footer's opacity-0 must be handed off to the native side after mount,
      // and on iOS that handoff can paint ONE full-opacity frame first — the
      // exact "disclaimer flashes before the animation" bug (seen live in
      // build 8). JS-driven opacity is a plain prop from the first frame:
      // starts at 0, stays 0, fades in only when this step runs. One small
      // Text fading at the end of the sequence costs nothing on the JS thread.
      Animated.timing(footerOpacity, {
        toValue: 1, duration: 700, easing: ease, useNativeDriver: false,
      }),
    ]);

    // Reveal the fade-in elements on the next frame, after the first paint.
    const raf = requestAnimationFrame(() => setShowContent(true));
    sequence.start();
    return () => { cancelAnimationFrame(raf); sequence.stop(); };
  }, []);

  const stoneRotateDeg = stoneRotate.interpolate({
    inputRange:  [0, 1],
    outputRange: ['0deg', '60deg'],
  });

  return (
    <View style={styles.container}>
      <StatusBar style="light" />

      {/* Everything above the footer lives in its own centered zone. The footer
          sits BELOW it in normal layout flow (never absolutely positioned), so
          on short or oddly-shaped screens the button and the disclaimer can
          never overlap — the center zone simply centers in whatever space is
          left above the footer. */}
      <View style={styles.centerZone}>

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
      {showContent && (
      <Animated.Text style={[styles.risenText, { opacity: textOpacity }]}>
        Come to me, all who are weary.
      </Animated.Text>
      )}

      {showContent && (
      <Animated.Text style={[styles.subText, { opacity: subOpacity }]}>
        However you arrived — hopeful, guarded, or unsure why you opened this —
        nothing is asked of you here. Every bit of real peace you have ever felt
        has a source.
      </Animated.Text>
      )}

      {/* ── CTA ──────────────────────────────────────────────────────────── */}
      {showContent && (
      <Animated.View style={{ opacity: btnOpacity }}>
        <TouchableOpacity
          style={styles.btn}
          activeOpacity={0.85}
          onPress={() => {
            // The sanctuary opening plays on EVERY cold open, but where it leads
            // depends on the person (CLAUDE.md locked direction):
            //   • First launch, or unseen stories remain → Onboard (story → question)
            //   • All stories seen and answered          → straight into the app
            const s = useAppStore.getState();
            const seen = s.seenStoryIds ?? [];
            const hasUnseenStory = STORY_IDS.some(id => !seen.includes(id));
            if (!s.onboardingComplete || hasUnseenStory) {
              navigation.navigate('Onboard');
            } else {
              navigation.replace('Main');
            }
          }}
        >
          <Text style={styles.btnText}>Come and see</Text>
        </TouchableOpacity>
      </Animated.View>
      )}

      </View>

      {/* ── The honest word (Elder Gong, on AI) ───────────────────────────────
          Subtle, never the headline — but said plainly at the threshold so no one
          ever mistakes the app for the Lord, and so no one mistakes it for an
          official Church product. The non-affiliation line is required honesty:
          this is an independent app made by members, not owned, endorsed, or
          sponsored by any church. Anchored in Elder Gerrit W. Gong's counsel:
          "Artificial intelligence can answer questions, but it cannot answer
          prayers... it is not God and cannot be God." What stirs here is a
          spiritual exercise to take to God and to people who love you — and to let
          the Spirit, not an app, confirm as true. */}
      {/* Opacity binds to the JS-driven footerOpacity from the FIRST frame — no
          static-0 → animated-0 handoff, so the one-frame flash cannot happen.
          The text stays mounted the whole time, so layout never jumps. */}
      <Animated.Text
        style={[
          styles.footerText,
          { opacity: footerOpacity, marginBottom: insets.bottom + (COMPACT ? 12 : 24) },
        ]}
      >
        This app is not officially affiliated with any Church. It is not God either —
        it cannot answer a prayer or know you the way Jesus does, only point you
        toward Him. Take what you feel here to God and to people who love you, and
        let the Spirit, not an app, tell you what is true.
      </Animated.Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex:            1,
    backgroundColor: colors.bg,
    paddingHorizontal: spacing.xl,
  },

  // The invitation centers itself in whatever space remains ABOVE the footer,
  // so the two can never collide on any screen shape.
  centerZone: {
    flex:           1,
    alignItems:     'center',
    justifyContent: 'center',
  },

  // Tomb
  tombContainer: {
    width:          110,
    height:         110,
    alignItems:     'center',
    justifyContent: 'flex-end',
    marginBottom:   COMPACT ? spacing.md : spacing.xl,
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
    fontSize:        COMPACT ? 27 : 32,
    fontFamily:      'Jost_400Regular',
    color:           colors.goldLight,
    letterSpacing:   2,
    textAlign:       'center',
    marginBottom:    spacing.md,
  },
  subText: {
    fontSize:        COMPACT ? 14 : 15,
    fontFamily:      'Jost_400Regular',
    color:           colors.textMuted,
    textAlign:       'center',
    lineHeight:      COMPACT ? 21 : 24,
    maxWidth:        280,
    marginBottom:    COMPACT ? spacing.xl : spacing.xxl,
  },

  // The honest word — small, dim, low. Present without competing with the
  // invitation. In normal layout flow (NOT absolute) so it always keeps its own
  // space below the button, on every screen size and shape.
  footerText: {
    alignSelf:       'center',
    fontSize:        COMPACT ? 10 : 11,
    fontFamily:      'Jost_400Regular',
    fontStyle:       'italic',
    color:           '#6f6a5c',
    textAlign:       'center',
    lineHeight:      COMPACT ? 15 : 17,
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
