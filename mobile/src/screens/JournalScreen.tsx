import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  Animated,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useAppStore, generateBlessing, NoteSource } from '../store/useAppStore';
import { getCurrentPrompt } from '../data/journalPrompts';
import { colors, spacing, radius } from '../theme';

// How many kept notes to show before the "Show all" link appears.
const RECENT_NOTES = 5;

// A short, human label for where a note came from — shown above each note.
const NOTE_SOURCE_LABEL: Record<NoteSource, string> = {
  feed:     'From a reading',
  chat:     'From a conversation',
  blessing: 'A word you kept',
  story:    'From a story',
  dialogue: 'From a question',
};

export default function JournalScreen() {
  const feedTag          = useAppStore(s => s.feedTag);
  const dialogueSignals  = useAppStore(s => s.dialogueSignals);
  const journalEntries   = useAppStore(s => s.journalEntries);
  const answeredPromptIds = useAppStore(s => s.answeredPromptIds);
  const addJournalEntry  = useAppStore(s => s.addJournalEntry);

  const learnedNotes     = useAppStore(s => s.learnedNotes);
  const pendingNoteId    = useAppStore(s => s.pendingNoteId);
  const clearPendingNote = useAppStore(s => s.clearPendingNote);

  const prompt = getCurrentPrompt(feedTag, dialogueSignals, answeredPromptIds);

  const [text,      setText]      = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [blessLine, setBlessLine] = useState('');
  const fadeAnim  = useRef(new Animated.Value(1)).current;
  const thankAnim = useRef(new Animated.Value(0)).current;

  // Kept-notes view state: which note is expanded, and whether to show them all.
  const [expandedNoteId, setExpandedNoteId] = useState<string | null>(null);
  const [showAllNotes,   setShowAllNotes]   = useState(false);

  // The scroll position of the notes section, so arriving from a "Save" can
  // bring the person straight to the note they just kept.
  const scrollRef  = useRef<ScrollView>(null);
  const notesYRef  = useRef(0);

  // When the person saved a note elsewhere and was carried here, open to it:
  // expand it, scroll to the notes section, then clear the one-time target.
  useEffect(() => {
    if (!pendingNoteId) return;
    setExpandedNoteId(pendingNoteId);
    setShowAllNotes(false);
    const id = setTimeout(() => {
      scrollRef.current?.scrollTo({ y: Math.max(notesYRef.current - 12, 0), animated: true });
    }, 250);
    clearPendingNote();
    return () => clearTimeout(id);
  }, [pendingNoteId]);

  const visibleNotes = showAllNotes ? learnedNotes : learnedNotes.slice(0, RECENT_NOTES);

  function toggleNote(id: string) {
    setExpandedNoteId(cur => (cur === id ? null : id));
  }

  function handleSubmit() {
    if (!text.trim()) return;
    const written = text.trim();
    addJournalEntry(prompt.id, prompt.text, written);
    // A blessing in words after the truest thing is said — never numbers, and
    // never a canned line. The disciple reads what they actually wrote and either
    // speaks one personal blessing or stays silent. It is handed every line it has
    // said before, so it never repeats itself; a spoken line is remembered too.
    setBlessLine('');
    generateBlessing('journal', written, useAppStore.getState().blessingHistory).then(line => {
      if (line) {
        setBlessLine(line);
        useAppStore.getState().recordBlessing(line);
      }
    });

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
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />

      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      >
        <ScrollView
          ref={scrollRef}
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

          {/* ── Notes you kept ──────────────────────────────────────────── */}
          <View onLayout={e => { notesYRef.current = e.nativeEvent.layout.y; }}>
            <View style={styles.sectionDivider} />
            <Text style={styles.sectionLabel}>NOTES YOU KEPT</Text>

            {learnedNotes.length === 0 ? (
              <Text style={styles.notesEmpty}>
                When something is worth remembering — a reading, a line from a
                conversation, a story — tap “Save to my notes” and it will be kept
                for you right here.
              </Text>
            ) : (
              <>
                {visibleNotes.map(note => {
                  const open = expandedNoteId === note.id;
                  return (
                    <TouchableOpacity
                      key={note.id}
                      activeOpacity={0.8}
                      onPress={() => toggleNote(note.id)}
                      style={[styles.noteCard, open && styles.noteCardOpen]}
                    >
                      <View style={styles.noteMeta}>
                        <Text style={styles.noteSource}>{NOTE_SOURCE_LABEL[note.source]}</Text>
                        <Text style={styles.noteDate}>{formatDate(note.timestamp)}</Text>
                      </View>

                      <Text style={styles.noteTitle} numberOfLines={open ? undefined : 2}>
                        {note.title}
                      </Text>

                      <Text style={styles.noteSummary}>
                        {note.summary}
                        {note.pending ? '  ·  summarizing…' : ''}
                      </Text>

                      {open && note.body && note.body !== note.summary && (
                        <View style={styles.noteBodyBox}>
                          <Text style={styles.noteBodyLabel}>WHAT YOU KEPT</Text>
                          <Text style={styles.noteBody}>{note.body}</Text>
                        </View>
                      )}

                      <Text style={styles.noteToggle}>
                        {open ? 'Show less' : 'Read what you kept →'}
                      </Text>
                    </TouchableOpacity>
                  );
                })}

                {learnedNotes.length > RECENT_NOTES && (
                  <TouchableOpacity
                    activeOpacity={0.7}
                    onPress={() => setShowAllNotes(v => !v)}
                    style={styles.allNotesBtn}
                  >
                    <Text style={styles.allNotesText}>
                      {showAllNotes
                        ? 'Show fewer notes'
                        : `Show all ${learnedNotes.length} notes →`}
                    </Text>
                  </TouchableOpacity>
                )}
              </>
            )}
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

  // ── Kept notes ─────────────────────────────────────────────────────────
  notesEmpty: {
    fontSize:   13,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.textMuted,
    lineHeight: 21,
    marginBottom: spacing.md,
  },
  noteCard: {
    backgroundColor: colors.bgCard,
    borderWidth:     1,
    borderColor:     colors.border,
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.sm,
  },
  noteCardOpen: {
    borderColor: colors.gold,
  },
  noteMeta: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    alignItems:     'center',
    marginBottom:   6,
  },
  noteSource: {
    fontSize:      10,
    letterSpacing: 1.2,
    textTransform: 'uppercase',
    color:         colors.textMuted,
    fontFamily:    'Georgia',
  },
  noteDate: {
    fontSize:   10,
    color:      colors.textMuted,
    fontFamily: 'Georgia',
    letterSpacing: 0.8,
  },
  noteTitle: {
    fontSize:     15,
    fontFamily:   'Georgia',
    color:        '#e8e0c8',
    lineHeight:   22,
    marginBottom: 6,
  },
  noteSummary: {
    fontSize:   13,
    fontFamily: 'Georgia',
    color:      colors.textDim,
    lineHeight: 21,
  },
  noteBodyBox: {
    marginTop:       spacing.sm,
    paddingTop:      spacing.sm,
    borderTopWidth:  1,
    borderTopColor:  colors.borderDim,
  },
  noteBodyLabel: {
    fontSize:      9,
    letterSpacing: 1.2,
    color:         colors.textMuted,
    fontFamily:    'Georgia',
    marginBottom:  4,
  },
  noteBody: {
    fontSize:   13,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.textMid,
    lineHeight: 21,
  },
  noteToggle: {
    fontSize:   11,
    fontFamily: 'Georgia',
    fontStyle:  'italic',
    color:      colors.blue,
    marginTop:  spacing.sm,
  },
  allNotesBtn: {
    alignSelf:         'center',
    paddingVertical:   8,
    paddingHorizontal: 12,
    marginTop:         spacing.xs,
    marginBottom:      spacing.md,
  },
  allNotesText: {
    fontSize:   12,
    fontFamily: 'Georgia',
    color:      colors.gold,
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
