/**
 * FeedScreen — the prescribed feed, Rev 1 (Cameron, 2026-07-12).
 *
 * Horizontally SWIPED pages — there is no next button, ever (§2). Left of home
 * is everything seen and interacted with (the re-viewable history); right of
 * home is the gate to a new page (§4): interacted pages earn it after a short
 * honest "preparing" moment, ignored pages get Cameron's gentle invitation plus
 * the escalating wait. Interacted items are replaced IN PLACE by the store's
 * engine (§3) — a brief "preparing a new story…" state where they stood, then
 * fresh content, reel-style. Questions chain; answered ones keep their
 * interaction row in history (§5) instead of dead-ending.
 */

import React, { useCallback, useEffect, useRef, useState } from 'react';
import {
  View,
  Text,
  ScrollView,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  useWindowDimensions,
  ActivityIndicator,
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
import InteractionRow from '../components/InteractionRow';
import DialogueCard from '../components/DialogueCard';
import InvitationCard from '../components/InvitationCard';
import FollowUpCard from '../components/FollowUpCard';
import WheelNav from '../components/WheelNav';
import BlessingToast from '../components/BlessingToast';
import { colors, spacing, radius } from '../theme';

// Cameron's approved right-swipe invitation (Rev 1 §4, his exact words).
const GATE_INVITATION =
  'There might be more here for you — wait a second with this page. The next one is being prepared.';

// The content level is an INTERNAL routing signal — never shown to the user.

export default function FeedScreen() {
  const { width } = useWindowDimensions();
  const navigation = useNavigation<any>();

  const pages            = useAppStore(s => s.pages);
  const currentPageIndex = useAppStore(s => s.currentPageIndex);
  const preparingSlots   = useAppStore(s => s.preparingSlots);
  const ensureHomePage   = useAppStore(s => s.ensureHomePage);
  const honorPageItem    = useAppStore(s => s.honorPageItem);
  const refreshHomeIfUntouched = useAppStore(s => s.refreshHomeIfUntouched);
  const requestNextPage  = useAppStore(s => s.requestNextPage);
  const commitNextPage   = useAppStore(s => s.commitNextPage);
  const goToPage         = useAppStore(s => s.goToPage);

  const answeredQuestions = useAppStore(s => s.answeredQuestions);
  const activeExercise  = useAppStore(s => s.activeExercise);
  const acceptedSession = useAppStore(s => s.acceptedSession);
  const sessionCount    = useAppStore(s => s.sessionCount);
  const dialogueSignals = useAppStore(s => s.dialogueSignals);

  // Gate state — the pseudo-page to the right of home.
  const [gateWait, setGateWait]       = useState(0);
  const [gateInvited, setGateInvited] = useState(false);
  const gateTimer = useRef<ReturnType<typeof setInterval> | null>(null);
  const gateArmed = useRef(false);

  const pagerRef = useRef<FlatList<Page | 'gate'>>(null);

  useFocusEffect(
    useCallback(() => {
      ensureHomePage();
      refreshHomeIfUntouched();
    }, [ensureHomePage, refreshHomeIfUntouched]),
  );

  useEffect(() => () => { if (gateTimer.current) clearInterval(gateTimer.current); }, []);

  const homeIdx  = pages.length - 1;
  const isMember = isMemberSignal(dialogueSignals);
  const followUpDue = !!(activeExercise && acceptedSession !== null && acceptedSession < sessionCount);

  // Keep the pager in step with the store (deep links from the Journal, dot taps).
  useEffect(() => {
    if (pages.length === 0) return;
    pagerRef.current?.scrollToIndex({ index: Math.min(currentPageIndex, pages.length), animated: true });
  }, [currentPageIndex, pages.length]);

  // ── The right-swipe gate (Rev 1 §4) ─────────────────────────────────────────
  function armGate() {
    if (gateArmed.current) return;
    gateArmed.current = true;
    const { wait, invited } = requestNextPage();
    setGateInvited(invited);
    setGateWait(wait);
    gateTimer.current = setInterval(() => {
      setGateWait(prev => {
        if (prev <= 1) {
          if (gateTimer.current) clearInterval(gateTimer.current);
          commitNextPage();          // the new page becomes home…
          gateArmed.current = false; // …and the gate re-arms for the next one
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
  }

  function handlePageSettled(e: NativeSyntheticEvent<NativeScrollEvent>) {
    const idx = Math.round(e.nativeEvent.contentOffset.x / width);
    if (idx >= pages.length) {
      armGate();       // swiped right of home — the gate surface
    } else {
      goToPage(idx);
    }
  }

  // ── One item on a page ───────────────────────────────────────────────────────
  function renderItem(page: Page, item: PageItem) {
    const preparing = preparingSlots.includes(item.slotId);
    const inner = renderItemInner(page, item);
    if (!inner) return null;
    return (
      <View key={item.slotId}>
        {inner}
        {preparing && (
          <View style={styles.preparingOverlay}>
            <ActivityIndicator color={colors.gold} size="small" />
            <Text style={styles.preparingText}>
              {item.kind === 'question' ? 'Thank you for sharing — another question is coming…'
                : item.kind === 'videoPair' ? 'Preparing a new story…'
                : 'Preparing something new…'}
            </Text>
          </View>
        )}
      </View>
    );
  }

  function renderItemInner(page: Page, item: PageItem) {
    switch (item.kind) {
      case 'videoPair':
        return <VideoCard item={item} pageIndex={page.index} />;

      case 'verse':
        return (
          <View style={styles.verseCard}>
            <VerseBlock
              scriptureRef={item.scriptureRef}
              contentId={item.contentId}
              honored={item.honored}
              onRead={() => honorPageItem(item.slotId)}
              pageRef={{ pageIndex: page.index, slotId: item.slotId }}
              reminderTitle={item.recycledFromTitle}
            />
          </View>
        );

      case 'question': {
        const q = QUESTION_BANK.find(x => x.id === item.questionId);
        if (!q) return null;
        if (item.honored) {
          // Answered — in history it keeps its full interaction row (Rev 1),
          // shown with what they said, never a dead "thank you" end.
          const answered = answeredQuestions.find(a => a.prompt === q.questionText);
          return (
            <View style={styles.answeredCard}>
              <Text style={styles.answeredLabel}>A QUESTION YOU ANSWERED</Text>
              <Text style={styles.answeredQuestion}>{q.questionText}</Text>
              {answered?.answer ? <Text style={styles.answeredAnswer}>{answered.answer}</Text> : null}
              <InteractionRow
                kind="question"
                title={q.questionText}
                pageRef={{ pageIndex: page.index, slotId: item.slotId }}
                talkPrefill={`I was asked: “${q.questionText}” — can we talk about it?`}
                reflectPlaceholder="What did answering stir? A line is plenty."
              />
            </View>
          );
        }
        return (
          <DialogueCard question={q} onAnswered={() => honorPageItem(item.slotId)} />
        );
      }

      case 'invitation': {
        const ex = EXERCISES.find(x => x.id === item.exerciseId);
        if (!ex) return null;
        if (item.honored) {
          return (
            <View style={styles.answeredCard}>
              <Text style={styles.answeredLabel}>AN INVITATION YOU TOOK UP</Text>
              <Text style={styles.answeredQuestion}>{ex.text}</Text>
              <InteractionRow
                kind="invitation"
                title={ex.text.length > 60 ? ex.text.slice(0, 57) + '…' : ex.text}
                pageRef={{ pageIndex: page.index, slotId: item.slotId }}
                talkPrefill={`I was invited to try something: “${ex.text}” — can we talk about it?`}
              />
            </View>
          );
        }
        return (
          <InvitationCard exercise={ex} onResolved={() => honorPageItem(item.slotId)} />
        );
      }
    }
  }

  // ── One full page of the pager ───────────────────────────────────────────────
  function renderPage({ item: pageOrGate }: { item: Page | 'gate' }) {
    if (pageOrGate === 'gate') {
      return (
        <View style={[styles.gatePage, { width }]}>
          <ActivityIndicator color={colors.gold} />
          <Text style={styles.gateTitle}>
            {gateInvited ? GATE_INVITATION : 'Preparing your next page…'}
          </Text>
          {gateWait > 0 && <Text style={styles.gateCount}>{gateWait}</Text>}
        </View>
      );
    }
    const page = pageOrGate;
    const isHome = pages[homeIdx]?.id === page.id;
    return (
      <ScrollView
        style={{ width }}
        contentContainerStyle={styles.pageContainer}
        showsVerticalScrollIndicator={false}
        keyboardShouldPersistTaps="handled"
      >
        {isHome && isMember && (
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

        {!isHome && (
          <Text style={styles.historyNote}>
            A page you've walked through — everything here is kept for you.
          </Text>
        )}

        {isHome && followUpDue && activeExercise && (
          <FollowUpCard followUpText={activeExercise.followUp} />
        )}

        {page.items.map(it => renderItem(page, it))}
        <View style={{ height: spacing.xl }} />
      </ScrollView>
    );
  }

  const data: (Page | 'gate')[] = [...pages, 'gate'];

  return (
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />

      {pages.length === 0 ? (
        <View style={styles.loadingWrap}>
          <ActivityIndicator color={colors.gold} />
        </View>
      ) : (
        <FlatList
          ref={pagerRef}
          data={data}
          keyExtractor={p => (p === 'gate' ? 'gate' : p.id)}
          renderItem={renderPage}
          horizontal
          pagingEnabled
          showsHorizontalScrollIndicator={false}
          onMomentumScrollEnd={handlePageSettled}
          getItemLayout={(_, i) => ({ length: width, offset: width * i, index: i })}
          initialScrollIndex={Math.min(currentPageIndex, data.length - 1)}
          windowSize={3}
        />
      )}

      {/* ── The wheel: history dots · home · the ghost of the next page ─────── */}
      <WheelNav />

      <BlessingToast />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe:        { flex: 1, backgroundColor: colors.bg },
  loadingWrap: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  pageContainer: {
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

  historyNote: {
    color:      colors.textMuted,
    fontSize:   12,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    textAlign:  'center',
    marginBottom: spacing.md,
  },

  verseCard: {
    backgroundColor: colors.bgCard,
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.sm + 4,
  },

  answeredCard: {
    borderWidth:     1,
    borderColor:     '#2a2820',
    backgroundColor: '#0d0c0a',
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.md,
  },
  answeredLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
    marginBottom:  spacing.sm,
  },
  answeredQuestion: {
    fontSize:   14,
    color:      '#d0c8b0',
    fontFamily: 'Jost_400Regular',
    lineHeight: 21,
  },
  answeredAnswer: {
    fontSize:   13,
    color:      colors.textDim,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    lineHeight: 19,
    marginTop:  6,
  },

  preparingOverlay: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: 'rgba(10,10,15,0.88)',
    borderRadius:    radius.md,
    alignItems:      'center',
    justifyContent:  'center',
    gap:             10,
    paddingHorizontal: spacing.lg,
  },
  preparingText: {
    color:      colors.textDim,
    fontSize:   13,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    textAlign:  'center',
    lineHeight: 19,
  },

  gatePage: {
    alignItems:        'center',
    justifyContent:    'center',
    paddingHorizontal: spacing.xl,
    gap:               spacing.md,
  },
  gateTitle: {
    color:      colors.textMid,
    fontSize:   15,
    fontStyle:  'italic',
    fontFamily: 'Jost_400Regular',
    textAlign:  'center',
    lineHeight: 24,
  },
  gateCount: {
    color:      colors.gold,
    fontSize:   22,
    fontFamily: 'Jost_400Regular',
  },
});
