import React, { useState, useRef } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  SafeAreaView,
  KeyboardAvoidingView,
  Platform,
  Animated,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { useAppStore, JOURNAL_BLESS } from '../store/useAppStore';
import { getCurrentPrompt } from '../data/journalPrompts';
import { colors, spacing, radius } from '../theme';

export default function JournalScreen() {
  const feedTag          = useAppStore(s => s.feedTag);
  const dialogueSignals  = useAppStore(s => s.dialogueSignals);
  const journalEntries   = useAppStore(s => s.journalEntries);
  const answeredPromptIds = useAppStore(s => s.answeredPromptIds);
  const addJournalEntry  = useAppStore(s => s.addJournalEntry);

  const prompt = getCurrentPrompt(feedTag, dialogueSignals, answeredPromptIds);

  const [text,      setText]      = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [blessLine, setBlessLine] = useState('');
  const fadeAnim  = useRef(new Animated.Value(1)).current;
  const thankAnim = useRef(new Animated.Value(0)).current;

  function handleSubmit() {
    if (!text.trim()) return;
    addJournalEntry(prompt.id, prompt.text, text.trim());
    // A blessing in words after the truest thing is said — never numbers.
    setBlessLine(JOURNAL_BLESS[Math.floor(Math.random() * JOURNAL_BLESS.length)] ?? '');

    Animated.sequence([
      Animated.timing(fadeAnim, { toValue: 0, duration: 300, useNativeDriver: true }),
      Animated.timing(thankAnim, { toValue: 1, duration: 400, useNativeDriver: true }),
    ]).start(() => {
      setSubmitted(true);
    });
  }

  function handleWriteMore() {
    setSubmitted(false);
    setText('');
    fadeAnim.setValue(1);
    thankAnim.setValue(0);
  }

  function formatDate(ts: number) {
    const d = new Date(ts);
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  }

  return (
    <SafeAreaView style={styles.safe}>
      <StatusBar style="light" />

      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <ScrollView
          style={styles.scroll}
          contentContainerStyle={styles.container}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          {/* ── Header ──────────────────────────────────────────────────── */}
          <Text style={styles.header}>Journal</Text>

          {/* ── Current prompt ──────────────────────────────────────────── */}
          <View style={styles.promptCard}>
            <Text style={styles.promptLabel}>TODAY'S PROMPT</Text>

            {/* Thank-you state */}
            <Animated.View
              style={[styles.thankBlock, { opacity: thankAnim }]}
              pointerEvents={submitted ? 'auto' : 'none'}
            >
              <Text style={styles.thankText}>Written.</Text>
              {blessLine ? <Text style={styles.blessLine}>{blessLine}</Text> : null}
              <TouchableOpacity onPress={handleWriteMore} activeOpacity={0.7}>
                <Text style={styles.writeMoreText}>Write again →</Text>
              </TouchableOpacity>
            </Animated.View>

            {/* Active prompt */}
            <Animated.View style={{ opacity: fadeAnim }}>
              <Text style={styles.promptText}>{prompt.text}</Text>

              <TextInput
                style={styles.input}
                value={text}
                onChangeText={setText}
                placeholder="Write what comes…"
                placeholderTextColor={colors.textMuted}
                multiline
                numberOfLines={6}
                textAlignVertical="top"
                editable={!submitted}
              />

              <TouchableOpacity
                style={[styles.submitBtn, !text.trim() && styles.submitBtnDisabled]}
                activeOpacity={0.7}
                onPress={handleSubmit}
                disabled={!text.trim() || submitted}
              >
                <Text style={styles.submitBtnText}>Save →</Text>
              </TouchableOpacity>
            </Animated.View>
          </View>

          {/* ── Past entries ────────────────────────────────────────────── */}
          {journalEntries.length > 0 && (
            <>
              <View style={styles.sectionDivider} />
              <Text style={styles.sectionLabel}>PAST ENTRIES</Text>

              {journalEntries.map(entry => (
                <View key={entry.id} style={styles.entryCard}>
                  <Text style={styles.entryDate}>{formatDate(entry.timestamp)}</Text>
                  <Text style={styles.entryPrompt}>{entry.promptText}</Text>
                  <Text style={styles.entryText}>{entry.text}</Text>
                </View>
              ))}
            </>
          )}

          {journalEntries.length === 0 && (
            <Text style={styles.emptyNote}>
              Your entries will appear here. This is only for you.
            </Text>
          )}

          <View style={{ height: spacing.xl }} />
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: {
    flex:            1,
    backgroundColor: colors.bg,
  },
  scroll: { flex: 1 },
  container: {
    paddingHorizontal: spacing.md,
    paddingTop:        spacing.lg,
    paddingBottom:     spacing.xxl,
  },

  header: {
    fontSize:     22,
    fontFamily:   'Georgia',
    color:        colors.textMid,
    marginBottom: spacing.lg,
  },

  promptCard: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    backgroundColor: colors.bgCard,
    borderRadius:    radius.lg,
    padding:         spacing.md,
    marginBottom:    spacing.lg,
    minHeight:       220,
  },
  promptLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Georgia',
    marginBottom:  spacing.sm,
  },
  promptText: {
    fontSize:     16,
    fontFamily:   'Georgia',
    color:        colors.textMid,
    lineHeight:   26,
    marginBottom: spacing.md,
  },

  thankBlock: {
    position:       'absolute',
    top:            40,
    left:           0,
    right:          0,
    alignItems:     'center',
    justifyContent: 'center',
    gap:            spacing.sm,
    paddingVertical: spacing.xl,
  },
  thankText: {
    fontSize:   18,
    fontFamily: 'Georgia',
    color:      colors.gold,
    fontStyle:  'italic',
  },
  blessLine: {
    fontSize:   13,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.textDim,
    textAlign:  'center',
    lineHeight: 20,
    paddingHorizontal: spacing.md,
  },
  writeMoreText: {
    fontSize:   13,
    fontFamily: 'Georgia',
    color:      colors.textMuted,
    fontStyle:  'italic',
  },

  input: {
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.sm,
    backgroundColor: colors.bgInput,
    color:           colors.text,
    fontFamily:      'Georgia',
    fontSize:        14,
    padding:         spacing.sm,
    minHeight:       120,
    marginBottom:    spacing.sm,
  },
  submitBtn: {
    alignSelf:         'flex-end',
    borderWidth:       1,
    borderColor:       colors.gold,
    borderRadius:      4,
    paddingVertical:   8,
    paddingHorizontal: 16,
  },
  submitBtnDisabled: {
    borderColor: colors.borderDim,
  },
  submitBtnText: {
    color:      colors.gold,
    fontFamily: 'Georgia',
    fontSize:   13,
  },

  sectionDivider: {
    height:          1,
    backgroundColor: colors.borderDim,
    marginBottom:    spacing.md,
  },
  sectionLabel: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Georgia',
    marginBottom:  spacing.md,
  },

  entryCard: {
    borderWidth:     1,
    borderColor:     colors.borderDim,
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.sm,
  },
  entryDate: {
    fontSize:      10,
    color:         colors.textMuted,
    fontFamily:    'Georgia',
    letterSpacing: 0.8,
    marginBottom:  spacing.xs,
  },
  entryPrompt: {
    fontSize:     12,
    fontFamily:   'Georgia',
    fontStyle:    'italic',
    color:        colors.textMuted,
    lineHeight:   18,
    marginBottom: spacing.xs,
  },
  entryText: {
    fontSize:   14,
    fontFamily: 'Georgia',
    color:      colors.textDim,
    lineHeight: 22,
  },

  emptyNote: {
    fontSize:   13,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.textMuted,
    textAlign:  'center',
    marginTop:  spacing.xl,
  },
});
