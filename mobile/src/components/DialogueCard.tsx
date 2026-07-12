import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Animated,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { DialogueQuestion } from '../data/questionBank';
import { useAppStore } from '../store/useAppStore';
import { colors, spacing, radius } from '../theme';

interface Props {
  question: DialogueQuestion;
  /** Fired after the question is answered — lets the feed honor its page slot. */
  onAnswered?: () => void;
}

export default function DialogueCard({ question, onAnswered }: Props) {
  const answerQuestion = useAppStore(s => s.answerQuestion);

  const [answered,    setAnswered]    = useState(false);
  const [freeText,    setFreeText]    = useState('');
  const [selected,    setSelected]    = useState<string | null>(null);

  const opacity   = useRef(new Animated.Value(0)).current;
  const thankOpacity = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(opacity, {
      toValue:         1,
      duration:        500,
      useNativeDriver: true,
    }).start();
  }, [question.id]);

  function submit(value: string, text?: string) {
    if (answered) return;
    setSelected(value);
    setAnswered(true);
    answerQuestion(question.id, value, text);
    onAnswered?.();

    // Fade the question out, fade the thanks in
    Animated.sequence([
      Animated.timing(opacity, {
        toValue:         0,
        duration:        300,
        delay:           600,
        useNativeDriver: true,
      }),
      Animated.timing(thankOpacity, {
        toValue:         1,
        duration:        300,
        useNativeDriver: true,
      }),
    ]).start();
  }

  function handleChoice(value: string) {
    submit(value);
  }

  function handleFreeText() {
    if (!freeText.trim()) return;
    submit(freeText.trim(), freeText.trim());
  }

  return (
    <View style={styles.wrapper}>
      {/* ── Answered thank-you state ──────────────────────────────── */}
      <Animated.View
        style={[styles.thankView, { opacity: thankOpacity }]}
        pointerEvents="none"
      >
        <Text style={styles.thankText}>Thank you for sharing that.</Text>
      </Animated.View>

      {/* ── Active question state ─────────────────────────────────── */}
      <Animated.View style={{ opacity }}>
        {/* Label */}
        <Text style={styles.label}>A QUESTION FOR YOU</Text>

        {/* Question */}
        <Text style={styles.questionText}>{question.questionText}</Text>

        {/* Answers */}
        {!answered && (
          <>
            {question.answerType === 'FREE_TEXT' && (
              <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : undefined}>
                <TextInput
                  style={styles.textInput}
                  value={freeText}
                  onChangeText={setFreeText}
                  placeholder="Type your answer…"
                  placeholderTextColor={colors.textMuted}
                  multiline
                  numberOfLines={3}
                  textAlignVertical="top"
                />
                <TouchableOpacity
                  style={[styles.submitBtn, !freeText.trim() && styles.submitBtnDisabled]}
                  onPress={handleFreeText}
                  activeOpacity={0.7}
                  disabled={!freeText.trim()}
                >
                  <Text style={styles.submitBtnText}>Share →</Text>
                </TouchableOpacity>
              </KeyboardAvoidingView>
            )}

            {(question.answerType === 'YES_NO' || question.answerType === 'CHOICE') && (
              <View style={styles.optionList}>
                {question.answerOptions.map(opt => (
                  <TouchableOpacity
                    key={opt.value}
                    style={[
                      styles.optionBtn,
                      selected === opt.value && styles.optionBtnSelected,
                    ]}
                    activeOpacity={0.7}
                    onPress={() => handleChoice(opt.value)}
                  >
                    <Text style={[
                      styles.optionText,
                      selected === opt.value && styles.optionTextSelected,
                    ]}>
                      {opt.text}
                    </Text>
                  </TouchableOpacity>
                ))}
              </View>
            )}
          </>
        )}

        {/* Jesus reference */}
        <Text style={styles.jesusRef}>{question.jesusReference}</Text>
      </Animated.View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    borderWidth:     1,
    borderColor:     '#2a2820',
    backgroundColor: '#0d0c0a',
    borderRadius:    radius.md,
    padding:         spacing.md,
    marginBottom:    spacing.md,
    minHeight:       80,
  },

  thankView: {
    position:   'absolute',
    top:        0,
    left:       0,
    right:      0,
    bottom:     0,
    alignItems: 'center',
    justifyContent: 'center',
    padding:    spacing.md,
  },
  thankText: {
    fontSize:   14,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.textMuted,
    textAlign:  'center',
  },

  label: {
    fontSize:      10,
    letterSpacing: 1.5,
    color:         colors.textMuted,
    fontFamily:    'Jost_400Regular',
    marginBottom:  spacing.sm,
  },

  questionText: {
    fontSize:     15,
    fontFamily:   'Jost_400Regular',
    color:        '#d0c8b0',
    lineHeight:   23,
    marginBottom: spacing.md,
  },

  // FREE_TEXT
  textInput: {
    borderWidth:       1,
    borderColor:       colors.border,
    borderRadius:      radius.sm,
    backgroundColor:   colors.bgInput,
    color:             '#d0c8b0',
    fontFamily:        'Jost_400Regular',
    fontSize:          13,
    padding:           spacing.sm,
    minHeight:         72,
    marginBottom:      spacing.sm,
  },
  submitBtn: {
    borderWidth:       1,
    borderColor:       colors.gold,
    borderRadius:      4,
    paddingVertical:   8,
    paddingHorizontal: 16,
    alignSelf:         'flex-end',
    marginBottom:      spacing.sm,
  },
  submitBtnDisabled: {
    borderColor: colors.border,
  },
  submitBtnText: {
    color:      colors.gold,
    fontFamily: 'Jost_400Regular',
    fontSize:   13,
  },

  // CHOICE / YES_NO
  optionList: {
    gap:          spacing.xs,
    marginBottom: spacing.sm,
  },
  optionBtn: {
    borderWidth:       1,
    borderColor:       colors.border,
    borderRadius:      4,
    paddingVertical:   10,
    paddingHorizontal: 12,
  },
  optionBtnSelected: {
    borderColor:     colors.gold,
    backgroundColor: 'rgba(212,200,154,0.07)',
  },
  optionText: {
    fontSize:   13,
    fontFamily: 'Jost_400Regular',
    color:      colors.textDim,
    lineHeight: 19,
  },
  optionTextSelected: {
    color: colors.gold,
  },

  jesusRef: {
    fontSize:   11,
    fontFamily: 'Jost_400Regular',
    fontStyle:  'italic',
    color:      colors.textMuted,
    lineHeight: 17,
    marginTop:  spacing.xs,
  },
});
