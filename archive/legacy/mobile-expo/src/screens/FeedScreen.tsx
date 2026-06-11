import React from 'react';
import {
  View,
  Text,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
  SafeAreaView,
  Linking,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { useAppStore, isRestorationReady } from '../store/useAppStore';
import ContentCard from '../components/ContentCard';
import DialogueCard from '../components/DialogueCard';
import { colors, spacing, radius } from '../theme';

// Phase 1: connection requests go directly to Cameron for review
const CONNECT_EMAIL =
  'mailto:noremacttevol@gmail.com' +
  '?subject=MBM%20Connect%20Request' +
  '&body=Hi%2C%20I%20was%20using%20the%20Milk%20Before%20Meat%20app%20and%20would%20love%20to%20talk%20to%20a%20real%20person.';

const TAG_LABEL: Record<string, string> = {
  MILK:        'Foundation',
  BRIDGE:      'Evidence',
  RESTORATION: 'The Restoration',
  MAINTENANCE: 'Discipleship',
};

export default function FeedScreen() {
  const feed              = useAppStore(s => s.feed);
  const feedTag           = useAppStore(s => s.feedTag);
  const showTalkToSomeone = useAppStore(s => s.showTalkToSomeone);
  const dialogueSignals   = useAppStore(s => s.dialogueSignals);
  const currentQuestion   = useAppStore(s => s.currentQuestion);

  const restorationReady = isRestorationReady(dialogueSignals);
  const thumbsUp          = useAppStore(s => s.thumbsUp);
  const bookmark          = useAppStore(s => s.bookmark);
  const keepSimple        = useAppStore(s => s.keepSimple);
  const goDeeper          = useAppStore(s => s.goDeeper);

  function handleTalkToSomeone() {
    Linking.openURL(CONNECT_EMAIL).catch(() => {});
  }

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
        {/* ── Tag pill ──────────────────────────────────────────────────────── */}
        <View style={styles.tagRow}>
          <View style={styles.tagPill}>
            <Text style={styles.tagText}>{TAG_LABEL[feedTag] ?? feedTag}</Text>
          </View>
        </View>

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

        {/* ── Talk to Someone — engagement threshold + restoration-ready gate */}
        {showTalkToSomeone && restorationReady && (
          <View style={styles.talkCard}>
            <Text style={styles.talkTitle}>Talk to someone real.</Text>
            <Text style={styles.talkBody}>
              A member of the Church of Jesus Christ of Latter-day Saints would be glad
              to sit with your questions. No agenda. No pressure.
            </Text>
            <TouchableOpacity style={styles.talkBtn} activeOpacity={0.75} onPress={handleTalkToSomeone}>
              <Text style={styles.talkBtnText}>Request a visit from missionaries →</Text>
            </TouchableOpacity>
            <Text style={styles.talkSub}>
              Or just keep reading — there's no rush.
            </Text>
          </View>
        )}

        {/* ── Feed controls ─────────────────────────────────────────────────── */}
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

  tagRow: {
    alignItems:   'flex-start',
    marginBottom: spacing.md,
  },
  tagPill: {
    borderWidth:       1,
    borderColor:       colors.borderDim,
    borderRadius:      20,
    paddingVertical:   4,
    paddingHorizontal: 12,
  },
  tagText: {
    fontSize:      11,
    color:         colors.textMuted,
    letterSpacing: 1.0,
    textTransform: 'uppercase',
    fontFamily:    'Georgia',
  },

  talkCard: {
    borderWidth:     1,
    borderColor:     '#2a3a28',
    backgroundColor: '#0a0f0a',
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.md,
  },
  talkTitle: {
    fontSize:     16,
    fontFamily:   'Georgia',
    color:        colors.textMid,
    marginBottom: spacing.sm,
  },
  talkBody: {
    fontSize:     13,
    fontFamily:   'Georgia',
    color:        colors.textDim,
    lineHeight:   20,
    marginBottom: spacing.md,
  },
  talkBtn: {
    borderWidth:       1,
    borderColor:       colors.green,
    borderRadius:      4,
    paddingVertical:   10,
    paddingHorizontal: 14,
    marginBottom:      spacing.sm,
  },
  talkBtnText: {
    color:      colors.green,
    fontSize:   13,
    fontFamily: 'Georgia',
  },
  talkSub: {
    fontSize:   11,
    color:      colors.textMuted,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
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
    paddingVertical:   10,
    alignItems:        'center',
  },
  controlBtnText: {
    color:      colors.textMuted,
    fontSize:   12,
    fontFamily: 'Georgia',
  },
});
