/**
 * FeedScreen — the prescribed feed, Rev 2 (Cameron, 2026-07-12).
 *
 * Horizontally SWIPED pages — no next button, ever. Left of home is the
 * re-viewable history; right of home is the gated next page (Cameron's
 * invitation + escalating wait only when the page was ignored).
 *
 * Rev 2 replacement law: honored content STAYS PUT — the person gets all the
 * time they want to watch, then read, then reply. Only when they scroll fully
 * past an item that earned it (watched 90% / read / interacted at all) does the
 * screen stop, glide back to the slot, visibly pull a fresh piece in, and
 * release. Questions chain the same way; answered items keep their Reply row.
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
import { CONTENT } from '../data/content';
import { videoById } from '../data/videos';
import { QUESTION_BANK } from '../data/questionBank';
import { EXERCISES } from '../engine/exercises';
import { Page, PageItem, isReplaceEligible } from '../engine/pageEngine';
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

// ── One page of the feed (own component so it can hold scroll state) ─────────
function FeedPage({ page, isHome, width }: { page: Page; isHome: boolean; width: number }) {
  const navigation = useNavigation<any>();
  const preparingSlots     = useAppStore(s => s.preparingSlots);
  const honorPageItem      = useAppStore(s => s.honorPageItem);
  const notifyScrolledPast = useAppStore(s => s.notifyScrolledPast);
  const answeredQuestions  = useAppStore(s => s.answeredQuestions);
  const activeExercise  = useAppStore(s => s.activeExercise);
  const acceptedSession = useAppStore(s => s.acceptedSession);
  const sessionCount    = useAppStore(s => s.sessionCount);
  const dialogueSignals = useAppStore(s => s.dialogueSignals);

  const isMember    = isMemberSignal(dialogueSignals);
  const followUpDue = !!(activeExercise && acceptedSession !== null && acceptedSession < sessionCount);

  const scrollRef = useRef<ScrollView>(null);
  const layouts   = useRef<Record<string, { y: number; h: number }>>({});
  const swapping  = useRef(false);
  const [locked, setLocked] = useState(false);

  // Rev 2.1 (Cameron): an earned item 75% scrolled off the top counts as
  // "scrolled past" — the next scroll is ignored (screen locks ~2.4s) while the
  // slot visibly pulls a fresh piece in, then releases. The old 100%-off rule
  // could never fire for items near the bottom of the page.
  function handleScroll(e: NativeSyntheticEvent<NativeScrollEvent>) {
    // Runs on the home page AND the new (ignored) pages to its right — anywhere a
    // person can interact. History pages (honorArchive) are frozen and never swap.
    if (page.honorArchive || swapping.current) return;
    const offsetY = e.nativeEvent.contentOffset.y;
    for (const it of page.items) {
      const box = layouts.current[it.slotId];
      if (!box) continue;
      // Fire once the item's top has scrolled a bit above the viewport. Capped so a
      // long expanded verse (taller than the screen) can still cross the line and
      // earn its swap-to-history instead of being un-passable.
      const mostlyPast = offsetY > box.y + Math.min(box.h * 0.6, 240);
      if (mostlyPast && isReplaceEligible(it) && !preparingSlots.includes(it.slotId)) {
        swapping.current = true;
        notifyScrolledPast(it.slotId);   // store starts the 2.2s swap
        setLocked(true);                 // the next scroll is ignored while it lands
        setTimeout(() => { setLocked(false); swapping.current = false; }, 2400);
        break; // one visible swap at a time
      }
    }
  }

  function renderItem(item: PageItem) {
    const preparing = preparingSlots.includes(item.slotId);
    const inner = renderItemInner(item);
    if (!inner) return null;
    return (
      <View
        key={item.slotId}
        onLayout={e => {
          layouts.current[item.slotId] = {
            y: e.nativeEvent.layout.y,
            h: e.nativeEvent.layout.height,
          };
        }}
      >
        {inner}
        {preparing && (
          <View style={styles.preparingOverlay}>
            <ActivityIndicator color={colors.gold} size="small" />
            <Text style={styles.preparingText}>
              {item.kind === 'question' ? 'Thank you for sharing — another question is coming…'
                : item.kind === 'videoPair' ? 'Bringing you a new story…'
                : 'Bringing you something new…'}
            </Text>
          </View>
        )}
      </View>
    );
  }

  function renderItemInner(item: PageItem) {
    switch (item.kind) {
      case 'videoPair':
        return <VideoCard item={item} pageIndex={page.index} />;

      case 'verse': {
        // Rev 2: every standalone verse carries its personally-made question —
        // how Jesus is found to be a good God in this scripture. Reply answers it.
        // A RECYCLED verse (its video was watched, it was skipped) falls back to
        // its source video's question and takeaway, so the reminder still asks.
        const content = item.contentId != null ? CONTENT.find(c => c.id === item.contentId) : undefined;
        const srcVideo = item.recycledFromVideoId != null ? videoById(item.recycledFromVideoId) : undefined;
        const question = content?.seedQuestion ?? srcVideo?.seedQuestion;
        const takeaway = content?.takeaway ?? srcVideo?.takeaway;
        const takeawayKey = content ? `verse-${content.id}`
          : srcVideo ? `video-${srcVideo.id}` : undefined;
        return (
          <View style={styles.verseCard}>
            <VerseBlock
              scriptureRef={item.scriptureRef}
              contentId={item.contentId}
              honored={item.honored}
              onRead={() => honorPageItem(item.slotId)}
              pageRef={{ pageIndex: page.index, slotId: item.slotId }}
              reminderTitle={item.recycledFromTitle}
              question={question}
              takeaway={takeaway}
              takeawayKey={takeawayKey}
              onGetNew={isReplaceEligible(item) ? () => notifyScrolledPast(item.slotId) : undefined}
            />
          </View>
        );
      }

      case 'question': {
        const q = QUESTION_BANK.find(x => x.id === item.questionId);
        if (!q) return null;
        if (item.honored) {
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
                reflectPlaceholder='e.g. “Saying it out loud made me realize I believe more than I thought.”'
                onGetNew={() => notifyScrolledPast(item.slotId)}
                getNewLabel="Get a new question →"
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
                reflectPlaceholder='e.g. “I tried it last night. It was quieter than I expected.”'
                onGetNew={() => notifyScrolledPast(item.slotId)}
                getNewLabel="Get a new one →"
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

  return (
    <ScrollView
      ref={scrollRef}
      style={{ width }}
      contentContainerStyle={styles.pageContainer}
      showsVerticalScrollIndicator={false}
      keyboardShouldPersistTaps="handled"
      automaticallyAdjustKeyboardInsets
      scrollEnabled={!locked}
      onScroll={handleScroll}
      scrollEventThrottle={96}
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

      {page.honorArchive && (
        <Text style={styles.historyNote}>
          A page you've walked through — everything here is kept for you.
        </Text>
      )}

      {isHome && followUpDue && activeExercise && (
        <FollowUpCard followUpText={activeExercise.followUp} />
      )}

      {page.items.map(renderItem)}
      <View style={{ height: spacing.xl }} />
    </ScrollView>
  );
}

// ── The screen: horizontal pager + gate + wheel ───────────────────────────────
export default function FeedScreen() {
  const { width } = useWindowDimensions();

  const pages            = useAppStore(s => s.pages);
  const currentPageIndex = useAppStore(s => s.currentPageIndex);
  const homeIndex        = useAppStore(s => s.homeIndex);
  const ensureHomePage   = useAppStore(s => s.ensureHomePage);
  const refreshHomeIfUntouched = useAppStore(s => s.refreshHomeIfUntouched);
  const requestNextPage  = useAppStore(s => s.requestNextPage);
  const commitNextPage   = useAppStore(s => s.commitNextPage);
  const goToPage         = useAppStore(s => s.goToPage);

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

  const homeIdx = Math.min(homeIndex, pages.length - 1);

  // When an interaction files something into history, a page is prepended to the
  // LEFT and homeIndex grows. The person must NOT be slid over to that history page
  // — they stay put on the page they were on. Detect that prepend and re-pin their
  // view instantly (no animation), so interacting never takes them anywhere.
  const prevHome = useRef(homeIndex);
  useEffect(() => {
    if (pages.length === 0) return;
    const prependedHistory = homeIndex > prevHome.current;
    prevHome.current = homeIndex;
    pagerRef.current?.scrollToIndex({
      index: Math.min(currentPageIndex, pages.length),
      animated: !prependedHistory,
    });
  }, [currentPageIndex, pages.length, homeIndex]);

  function armGate() {
    if (gateArmed.current) return;
    gateArmed.current = true;
    const { wait, invited } = requestNextPage();
    setGateInvited(invited);
    setGateWait(wait);
    // Free choice (Cameron 2026-07-17): wait 0 → make the next page immediately.
    if (wait <= 0) {
      commitNextPage();
      gateArmed.current = false;
      return;
    }
    gateTimer.current = setInterval(() => {
      setGateWait(prev => {
        if (prev <= 1) {
          if (gateTimer.current) clearInterval(gateTimer.current);
          commitNextPage();
          gateArmed.current = false;
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
  }

  function handlePageSettled(e: NativeSyntheticEvent<NativeScrollEvent>) {
    const idx = Math.round(e.nativeEvent.contentOffset.x / width);
    if (idx >= pages.length) {
      armGate();
    } else {
      goToPage(idx);
    }
  }

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
    return (
      <FeedPage
        page={pageOrGate}
        isHome={pages[homeIdx]?.id === pageOrGate.id}
        width={width}
      />
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
