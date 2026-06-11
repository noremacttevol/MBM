import React from 'react';
import {
  View,
  Text,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
  SafeAreaView,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { useAppStore } from '../store/useAppStore';
import ContentCard from '../components/ContentCard';
import DialogueCard from '../components/DialogueCard';
import ConnectCard from '../components/ConnectCard';
import { colors, spacing } from '../theme';

// The content level is an INTERNAL routing signal — never shown to the user.
// A visible tier label ("The Restoration") would tell a person they've been
// categorized, which is exactly the pharisaical gate the app must never create.

export default function FeedScreen() {
  const feed            = useAppStore(s => s.feed);
  const currentQuestion = useAppStore(s => s.currentQuestion);

  const thumbsUp        = useAppStore(s => s.thumbsUp);
  const bookmark        = useAppStore(s => s.bookmark);
  const keepSimple      = useAppStore(s => s.keepSimple);
  const goDeeper        = useAppStore(s => s.goDeeper);

  // Split feed into two halves so the dialogue card lands between item 2 and item 3
  const topItems    = feed.slice(0, 2);
  const bottomItems = feed.slice(2);

  return (
    <SafeAreaView style={styles.safe}>
      <StatusBar style="light" />

      <ScrollView
        style={styles.scroll}
        contentContainerStyle={styles.container}
        showsVerticalScrollIndicator={false}
        keyboardShouldPersistTaps="handled"
      >
        {/* No tier label is ever shown — routing is invisible by law. */}

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

        {/* ── A real person is ALWAYS one tap away — never gated (CLAUDE.md law) */}
        <ConnectCard />

        {/* ── Feed controls — ungated user preferences, never gates ─────────── */}
        <View style={styles.controls}>
          <TouchableOpacity
            style={styles.controlBtn}
            activeOpacity={0.7}
            onPress={keepSimple}
          >
            <Text style={styles.controlBtnText}>← Keep it simple</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.controlBtn}
            activeOpacity={0.7}
            onPress={goDeeper}
          >
            <Text style={styles.controlBtnText}>Take me deeper →</Text>
          </TouchableOpacity>
        </View>

        <View style={{ height: spacing.xl }} />
      </ScrollView>
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

  controls: {
    flexDirection: 'row',
    gap:           spacing.sm,
    marginTop:     spacing.sm,
  },
  controlBtn: {
    flex:              1,
    borderWidth:       1,
    borderColor:       colors.borderDim,
    borderRadius:      4,
    paddingVertical:   12,
    alignItems:        'center',
    minHeight:         48,
    justifyContent:    'center',
  },
  controlBtnText: {
    color:      colors.textMuted,
    fontSize:   12,
    fontFamily: 'Georgia',
  },
});
