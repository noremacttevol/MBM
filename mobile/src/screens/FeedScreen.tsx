import React from 'react';
import {
  View,
  Text,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useAppStore } from '../store/useAppStore';
import ContentCard from '../components/ContentCard';
import DialogueCard from '../components/DialogueCard';
import FollowUpCard from '../components/FollowUpCard';
import InvitationCard from '../components/InvitationCard';
import BlessingToast from '../components/BlessingToast';
import { pickExercise } from '../engine/exercises';
import { colors, spacing } from '../theme';

// The content level is an INTERNAL routing signal — never shown to the user.
// A visible tier label ("The Restoration") would tell a person they've been
// categorized, which is exactly the pharisaical gate the app must never create.

export default function FeedScreen() {
  const feed            = useAppStore(s => s.feed);
  const currentQuestion = useAppStore(s => s.currentQuestion);

  const thumbsUp        = useAppStore(s => s.thumbsUp);
  const bookmark        = useAppStore(s => s.bookmark);
  const refreshFeed     = useAppStore(s => s.refreshFeed);

  // Spiritual exercise state — invite → try → report → learn.
  const activeExercise  = useAppStore(s => s.activeExercise);
  const acceptedSession = useAppStore(s => s.acceptedSession);
  const sessionCount    = useAppStore(s => s.sessionCount);
  const dialogueSignals = useAppStore(s => s.dialogueSignals);
  const doneExerciseIds = useAppStore(s => s.doneExerciseIds);

  // A follow-up is due once a NEW session began after the invitation was accepted
  // (they went away and came back). Otherwise, offer a fresh invitation.
  const followUpDue = !!(activeExercise && acceptedSession !== null && acceptedSession < sessionCount);
  const invite = !activeExercise ? pickExercise(dialogueSignals, doneExerciseIds) : null;

  // Split feed into two halves so the dialogue card lands between item 2 and item 3
  const topItems    = feed.slice(0, 2);
  const bottomItems = feed.slice(2);

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
      >
        {/* No tier label is ever shown — routing is invisible by law. */}

        {/* ── Follow-up on a tried exercise — the most personal thing, first ── */}
        {followUpDue && activeExercise && (
          <FollowUpCard followUpText={activeExercise.followUp} />
        )}

        {/* ── First two content cards ───────────────────────────────────────── */}
        {topItems.map(item => (
          <ContentCard
            key={item.id}
            item={item}
            onThumbsUp={thumbsUp}
            onBookmark={bookmark}
          />
        ))}

        {/* ── Dialogue card — appears after 2nd content card ───────────────── */}
        {currentQuestion && (
          <DialogueCard key={currentQuestion.id} question={currentQuestion} />
        )}

        {/* ── Remaining content cards ───────────────────────────────────────── */}
        {bottomItems.map(item => (
          <ContentCard
            key={item.id}
            item={item}
            onThumbsUp={thumbsUp}
            onBookmark={bookmark}
          />
        ))}

        {/* ── An invitation — something to DO, the way Jesus gave people things to do */}
        {invite && <InvitationCard exercise={invite} />}

        {/* Talking to a real person lives on the Chat tab, never here on the Feed. */}

        {/* ── Show me more — same-track refresh, an ungated preference ──────── */}
        <TouchableOpacity
          style={styles.moreBtn}
          activeOpacity={0.7}
          onPress={refreshFeed}
        >
          <Text style={styles.moreBtnText}>Show me more →</Text>
        </TouchableOpacity>

        <View style={{ height: spacing.xl }} />
      </ScrollView>
      </KeyboardAvoidingView>

      <BlessingToast />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: {
    flex:            1,
    backgroundColor: colors.bg,
  },
  scroll: {
    flex: 1,
  },
  container: {
    paddingHorizontal: spacing.md,
    paddingTop:        spacing.md,
    paddingBottom:     spacing.xxl,
  },

  moreBtn: {
    width:          '100%',
    borderWidth:    1,
    borderColor:    colors.borderDim,
    borderRadius:   4,
    paddingVertical: 12,
    minHeight:      48,
    alignItems:     'center',
    justifyContent: 'center',
    marginTop:      spacing.sm,
  },
  moreBtnText: {
    color:      colors.textMuted,
    fontSize:   12,
    fontFamily: 'Georgia',
  },
});
