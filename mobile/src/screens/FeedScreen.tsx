import React, { useCallback, useRef } from 'react';
import {
  View,
  Text,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  NativeSyntheticEvent,
  NativeScrollEvent,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useNavigation, useFocusEffect } from '@react-navigation/native';
import { useAppStore, isMemberSignal } from '../store/useAppStore';
import { QUESTION_BANK } from '../data/questionBank';
import { EXERCISES } from '../engine/exercises';
import { Page, PageItem } from '../engine/pageEngine';
import VideoCard from '../components/VideoCard';
import VerseBlock from '../components/VerseBlock';
import DialogueCard from '../components/DialogueCard';
import InvitationCard from '../components/InvitationCard';
import FollowUpCard from '../components/FollowUpCard';
import WheelNav from '../components/WheelNav';
import NextPageButton from '../components/NextPageButton';
import BlessingToast from '../components/BlessingToast';
import { pickExercise } from '../engine/exercises';
import { colors, spacing, radius } from '../theme';

// The content level is an INTERNAL routing signal — never shown to the user.
// A visible tier label ("The Restoration") would tell a person they've been
// categorized, which is exactly the pharisaical gate the app must never create.

export default function FeedScreen() {
  const navigation      = useNavigation<any>();

  // Feed 2.0 page engine
  const pages            = useAppStore(s => s.pages);
  const currentPageIndex = useAppStore(s => s.currentPageIndex);
  const ensureHomePage   = useAppStore(s => s.ensureHomePage);
  const honorPageItem    = useAppStore(s => s.honorPageItem);
  const leaveHomePage    = useAppStore(s => s.leaveHomePage);
  const refreshHomeIfUntouched = useAppStore(s => s.refreshHomeIfUntouched);
  const goToPage         = useAppStore(s => s.goToPage);

  // Spiritual exercise state — invite → try → report → learn.
  const activeExercise  = useAppStore(s => s.activeExercise);
  const acceptedSession = useAppStore(s => s.acceptedSession);
  const sessionCount    = useAppStore(s => s.sessionCount);
  const dialogueSignals = useAppStore(s => s.dialogueSignals);
  const doneExerciseIds = useAppStore(s => s.doneExerciseIds);

  const scrolledDown = useRef(false);

  // Make sure a home page exists whenever the feed comes into focus; on return,
  // apply the tab-away refresh rule (honored nothing, left → fresh page).
  useFocusEffect(
    useCallback(() => {
      ensureHomePage();
      refreshHomeIfUntouched();
      // Leaving the feed archives any honored items and refills their slots.
      return () => { leaveHomePage(); };
    }, [ensureHomePage, refreshHomeIfUntouched, leaveHomePage]),
  );

  const isMember = isMemberSignal(dialogueSignals);

  const homeIdx  = pages.length - 1;
  const onHome   = currentPageIndex === homeIdx;
  const page: Page | undefined = pages[currentPageIndex];

  // A follow-up is due once a NEW session began after the invitation was accepted.
  const followUpDue = !!(activeExercise && acceptedSession !== null && acceptedSession < sessionCount);

  // Scroll-away replacement (SPEC §2): once the user has scrolled down into the
  // page and comes back to the top, honored items have been swapped for fresh
  // content. Un-honored items never move, so the view isn't yanked out from under.
  function handleScroll(e: NativeSyntheticEvent<NativeScrollEvent>) {
    const y = e.nativeEvent.contentOffset.y;
    if (y > 240) scrolledDown.current = true;
    else if (scrolledDown.current && y < 40 && onHome) {
      scrolledDown.current = false;
      leaveHomePage();
    }
  }

  function renderItem(item: PageItem) {
    switch (item.kind) {
      case 'videoPair':
        return <VideoCard key={item.slotId} item={item} pageIndex={page!.index} />;

      case 'verse': {
        return (
          <View key={item.slotId} style={styles.verseCard}>
            <Text style={styles.verseLabel}>A VERSE</Text>
            <VerseBlock
              scriptureRef={item.scriptureRef}
              contentId={item.contentId}
              honored={item.honored}
              onRead={() => honorPageItem(item.slotId)}
              pageRef={{ pageIndex: page!.index, slotId: item.slotId }}
              reminderTitle={item.recycledFromTitle}
            />
          </View>
        );
      }

      case 'question': {
        const q = QUESTION_BANK.find(x => x.id === item.questionId);
        if (!q) return null;
        if (item.honored) {
          return (
            <View key={item.slotId} style={styles.answeredChip}>
              <Text style={styles.answeredText}>Thank you for sharing that.</Text>
            </View>
          );
        }
        return (
          <DialogueCard
            key={item.slotId}
            question={q}
            onAnswered={() => honorPageItem(item.slotId)}
          />
        );
      }

      case 'invitation': {
        const ex = EXERCISES.find(x => x.id === item.exerciseId)
          ?? pickExercise(dialogueSignals, doneExerciseIds);
        if (!ex) return null;
        if (item.honored) return null; // acted on — it slides into history on scroll-away
        return (
          <InvitationCard
            key={item.slotId}
            exercise={ex}
            onResolved={() => honorPageItem(item.slotId)}
          />
        );
      }
    }
  }

  return (
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />

      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      >
        <ScrollView
          style={styles.scroll}
          contentContainerStyle={styles.container}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
          onScroll={handleScroll}
          scrollEventThrottle={64}
        >
          {/* No tier label is ever shown — routing is invisible by law. */}

          {/* ── Member ("meat") track: a quiet doorway into deeper discipleship ── */}
          {isMember && onHome && (
            <TouchableOpacity
              style={styles.memberBanner}
              activeOpacity={0.85}
              onPress={() => navigation.navigate('Discipleship')}
            >
              <Text style={styles.memberBannerTitle}>Walk with Christ</Text>
              <Text style={styles.memberBannerSub}>
                Your private discipleship companion — examen, your walk so far, and personal rhythms. Tap to open →
              </Text>
            </TouchableOpacity>
          )}

          {/* ── Following a previous page? A quiet marker it's re-viewable history ── */}
          {!onHome && (
            <TouchableOpacity
              style={styles.historyBanner}
              activeOpacity={0.8}
              onPress={() => goToPage(homeIdx)}
            >
              <Text style={styles.historyText}>
                A page you've seen before — everything you honored is kept here. Tap for today's page ⌂
              </Text>
            </TouchableOpacity>
          )}

          {/* ── Follow-up on a tried exercise — the most personal thing, first ── */}
          {followUpDue && onHome && activeExercise && (
            <FollowUpCard followUpText={activeExercise.followUp} />
          )}

          {/* ── The prescribed page ─────────────────────────────────────────── */}
          {page ? page.items.map(renderItem) : (
            <Text style={styles.loading}>Preparing your page…</Text>
          )}

          {/* ── Next page (home only) — honest wait ladder ──────────────────── */}
          {onHome && page && <NextPageButton />}

          <View style={{ height: spacing.xl }} />
        </ScrollView>

        {/* ── Wheel navigation along the bottom ─────────────────────────────── */}
        <WheelNav />
      </KeyboardAvoidingView>

      <BlessingToast />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe:   { flex: 1, backgroundColor: colors.bg },
  scroll: { flex: 1 },
  container: {
    paddingHorizontal: spacing.md,
    paddingTop:        spacing.md,
    paddingBottom:     spacing.xxl,
  },

  memberBanner: {
    width:             '100%',
    borderWidth:       1,
    borderColor:       colors.gold,
    borderRadius:      8,
    backgroundColor:   (colors.gold ?? '#caa75a') + '14',
    paddingVertical:   14,
    paddingHorizontal: spacing.md,
    marginBottom:      spacing.md,
  },
  memberBannerTitle: {
    color:      colors.gold,
    fontSize:   16,
    fontFamily: 'Jost_400Regular',
    marginBottom: 4,
  },
  memberBannerSub: {
    color:      colors.textDim,
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    lineHeight: 19,
  },

  historyBanner: {
    width:             '100%',
    borderWidth:       1,
    borderColor:       colors.borderDim,
    borderRadius:      8,
    paddingVertical:   12,
    paddingHorizontal: spacing.md,
    marginBottom:      spacing.md,
  },
  historyText: {
    color:      colors.textMuted,
    fontSize:   12,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    lineHeight: 18,
  },

  verseCard: {
    backgroundColor: colors.bgCard,
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.sm + 4,
  },
  verseLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
    marginBottom:  spacing.xs,
  },

  answeredChip: {
    borderWidth:   1,
    borderColor:   '#2a2820',
    backgroundColor: '#0d0c0a',
    borderRadius:  radius.md,
    padding:       spacing.md,
    marginBottom:  spacing.md,
    alignItems:    'center',
  },
  answeredText: {
    fontSize:   13,
    fontStyle:  'italic',
    color:      colors.textMuted,
    fontFamily: 'Jost_400Regular',
  },

  loading: {
    color:      colors.textMuted,
    fontSize:   13,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    textAlign:  'center',
    marginTop:  spacing.xl,
  },
});
