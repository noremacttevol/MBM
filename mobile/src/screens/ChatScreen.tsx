import React, { useState, useRef, useEffect } from 'react';
import {
  View, Text, TextInput, TouchableOpacity, ScrollView,
  StyleSheet, KeyboardAvoidingView, Platform,
  ActivityIndicator, Alert,
} from 'react-native';
import { SafeAreaView, useSafeAreaInsets } from 'react-native-safe-area-context';
import { StatusBar } from 'expo-status-bar';
import { useAppStore } from '../store/useAppStore';
import ConnectCard from '../components/ConnectCard';
import { colors, spacing, radius } from '../theme';

// Server URL — the same proxy the store uses for chat. Public, not a secret.
const SERVER_URL =
  (process.env.EXPO_PUBLIC_MBM_API_URL ?? process.env.EXPO_PUBLIC_SERVER_URL ?? '')
    .trim()
    .replace(/\/+$/, '');

export default function ChatScreen() {
  const chatMessages    = useAppStore(s => s.chatMessages);
  const chatLoading     = useAppStore(s => s.chatLoading);
  const sendChatMessage = useAppStore(s => s.sendChatMessage);
  const chatDraft       = useAppStore(s => s.chatDraft);
  const clearChatDraft  = useAppStore(s => s.clearChatDraft);

  const [draft,          setDraft]          = useState('');
  const [submittingFC,   setSubmittingFC]   = useState(false);
  const [showConnect,    setShowConnect]    = useState(false);
  const scrollRef = useRef<ScrollView>(null);
  const insets = useSafeAreaInsets();

  useEffect(() => {
    scrollRef.current?.scrollToEnd({ animated: true });
  }, [chatMessages, chatLoading]);

  // A "Talk about it →" / "Ask about this →" tap elsewhere fills the chat draft.
  // Pull it into the input the moment it arrives, then clear the store copy.
  useEffect(() => {
    if (chatDraft) {
      setDraft(chatDraft);
      clearChatDraft();
    }
  }, [chatDraft]);

  async function handleSend() {
    const text = draft.trim();
    if (!text || chatLoading) return;
    setDraft('');
    await sendChatMessage(text);
  }

  // Submit the last Q&A pair anonymously for Cameron to fact-check
  async function handleFactCheck() {
    const msgs = chatMessages;
    if (msgs.length < 2) return;

    // Find last user message and last assistant message
    const lastUser = [...msgs].reverse().find(m => m.role === 'user');
    const lastAI   = [...msgs].reverse().find(m => m.role === 'assistant');
    if (!lastUser || !lastAI) return;

    setSubmittingFC(true);
    try {
      await fetch(`${SERVER_URL}/api/factcheck`, {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question:  lastUser.text,
          ai_answer: lastAI.text,
        }),
      });
      Alert.alert(
        'Submitted',
        'Your question and my answer have been sent anonymously for a real person to review. Thank you for helping make this better.',
        [{ text: 'OK' }],
      );
    } catch {
      Alert.alert('Could not submit', 'Check your connection and try again.');
    } finally {
      setSubmittingFC(false);
    }
  }

  function formatTime(ts: number) {
    return new Date(ts).toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
  }

  const isEmpty = chatMessages.length === 0;
  const canFactCheck = chatMessages.length >= 2 && !submittingFC;

  return (
    <SafeAreaView style={styles.safe} edges={['top', 'left', 'right']}>
      <StatusBar style="light" />

      {/* ── Header ────────────────────────────────────────────────────────── */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Ask anything.</Text>
        {/* A real person is ALWAYS one tap away — never gated (CLAUDE.md law).
            This opens the in-app connect capture, never a dead-end mailto. */}
        <TouchableOpacity
          style={styles.missionaryBtn}
          activeOpacity={0.75}
          onPress={() => setShowConnect(v => !v)}
        >
          <Text style={styles.missionaryBtnText}>Talk to a real person →</Text>
        </TouchableOpacity>
      </View>

      {/* In-app human-connect capture — saved on-device, no mailto (Phase 1). */}
      {showConnect && (
        <View style={styles.connectPanel}>
          <ConnectCard compact />
        </View>
      )}

      {/* ── Message list ──────────────────────────────────────────────────── */}
      <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior="padding"
        keyboardVerticalOffset={insets.top + 52}
      >
        <ScrollView
          ref={scrollRef}
          style={styles.messageList}
          contentContainerStyle={styles.messageListContent}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          {isEmpty && (
            <View style={styles.emptyState}>
              <Text style={styles.emptyTitle}>What's on your mind?</Text>
              <Text style={styles.emptyBody}>
                Ask about what you've been reading, a question that won't leave you alone,
                or anything you're working through.{'\n\n'}
                There are no wrong questions here.
              </Text>
              <Text style={styles.emptySub}>
                I'll be honest when I'm not sure about something — and I can always
                submit your question anonymously to a real person who can check it.
              </Text>
            </View>
          )}

          {chatMessages.map(msg => (
            msg.kind === 'meta' ? (
              <View key={msg.id} style={styles.metaNote}>
                <Text style={styles.metaText}>{msg.text}</Text>
              </View>
            ) : (
              <View
                key={msg.id}
                style={[styles.bubble, msg.role === 'user' ? styles.bubbleUser : styles.bubbleAssistant]}
              >
                <Text style={[
                  styles.bubbleText,
                  msg.role === 'user' ? styles.bubbleTextUser : styles.bubbleTextAssistant,
                ]}>
                  {msg.text}
                </Text>
                <Text style={styles.bubbleTime}>{formatTime(msg.timestamp)}</Text>
              </View>
            )
          ))}

          {chatLoading && (
            <View style={[styles.bubble, styles.bubbleAssistant, styles.loadingBubble]}>
              <ActivityIndicator color={colors.textMuted} size="small" />
            </View>
          )}
        </ScrollView>

        {/* ── Fact-check bar — appears after first exchange ─────────────── */}
        {canFactCheck && (
          <TouchableOpacity
            style={styles.factCheckBar}
            activeOpacity={0.75}
            onPress={handleFactCheck}
          >
            <Text style={styles.factCheckText}>
              {submittingFC
                ? 'Submitting…'
                : 'Not sure about my last answer? Send it anonymously for a real person to check →'}
            </Text>
          </TouchableOpacity>
        )}

        {/* ── Input bar ─────────────────────────────────────────────────── */}
        <View style={styles.inputBar}>
          <TextInput
            style={styles.input}
            value={draft}
            onChangeText={setDraft}
            placeholder="Say something…"
            placeholderTextColor={colors.textMuted}
            multiline
            maxLength={1000}
            returnKeyType="default"
          />
          <TouchableOpacity
            style={[styles.sendBtn, (!draft.trim() || chatLoading) && styles.sendBtnDisabled]}
            activeOpacity={0.7}
            onPress={handleSend}
            disabled={!draft.trim() || chatLoading}
          >
            <Text style={styles.sendBtnText}>→</Text>
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: colors.bg },

  header: {
    paddingHorizontal: spacing.md, paddingTop: spacing.md, paddingBottom: spacing.sm,
    borderBottomWidth: 1, borderBottomColor: colors.borderDim,
    flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center',
  },
  headerTitle: { fontSize: 18, fontFamily: 'Georgia', color: colors.textMid },

  missionaryBtn: {
    borderWidth: 1, borderColor: colors.green, borderRadius: 4,
    paddingVertical: 6, paddingHorizontal: 10,
  },
  missionaryBtnText: { color: colors.green, fontSize: 11, fontFamily: 'Georgia' },

  connectPanel: {
    paddingHorizontal: spacing.md, paddingTop: spacing.sm,
  },

  messageList: { flex: 1 },
  messageListContent: {
    paddingHorizontal: spacing.md, paddingVertical: spacing.md, flexGrow: 1,
  },

  emptyState: {
    flex: 1, alignItems: 'center', justifyContent: 'center',
    paddingTop: spacing.xxl, paddingHorizontal: spacing.lg,
  },
  emptyTitle: {
    fontSize: 18, fontFamily: 'Georgia', color: colors.textMid,
    marginBottom: spacing.md, textAlign: 'center',
  },
  emptyBody: {
    fontSize: 14, fontFamily: 'Georgia', color: colors.textDim,
    lineHeight: 22, textAlign: 'center', marginBottom: spacing.lg,
  },
  emptySub: {
    fontSize: 12, fontFamily: 'Georgia', fontStyle: 'italic',
    color: colors.textMuted, textAlign: 'center',
  },

  bubble: {
    maxWidth: '80%', borderRadius: radius.lg,
    padding: spacing.sm + 4, marginBottom: spacing.sm,
  },
  bubbleUser: {
    alignSelf: 'flex-end', backgroundColor: '#1a1a12',
    borderWidth: 1, borderColor: colors.border,
  },
  bubbleAssistant: {
    alignSelf: 'flex-start', backgroundColor: colors.bgCard,
    borderWidth: 1, borderColor: colors.borderDim,
  },
  loadingBubble: { paddingVertical: spacing.md, paddingHorizontal: spacing.lg },
  bubbleText: { fontSize: 14, fontFamily: 'Georgia', lineHeight: 22 },
  bubbleTextUser: { color: colors.textMid },
  bubbleTextAssistant: { color: colors.textDim },
  bubbleTime: {
    fontSize: 10, fontFamily: 'Georgia', color: colors.textMuted,
    marginTop: 4, alignSelf: 'flex-end',
  },

  // A quiet, centered note (e.g. a spirit-level change) — not a chat bubble.
  metaNote: {
    alignSelf: 'center', maxWidth: '88%',
    paddingVertical: 4, paddingHorizontal: 8, marginVertical: 2,
  },
  metaText: {
    fontSize: 11, fontFamily: 'Georgia', fontStyle: 'italic',
    color: colors.textMuted, textAlign: 'center', lineHeight: 16,
  },

  factCheckBar: {
    marginHorizontal: spacing.md, marginBottom: spacing.xs,
    borderWidth: 1, borderColor: colors.blue, borderRadius: radius.md,
    paddingVertical: 8, paddingHorizontal: 12,
  },
  factCheckText: {
    fontSize: 11, fontFamily: 'Georgia', color: colors.blue,
    fontStyle: 'italic', lineHeight: 16,
  },

  inputBar: {
    flexDirection: 'row', alignItems: 'flex-end',
    paddingHorizontal: spacing.md, paddingVertical: spacing.sm,
    borderTopWidth: 1, borderTopColor: colors.borderDim,
    gap: spacing.sm, backgroundColor: colors.bg,
  },
  input: {
    flex: 1, backgroundColor: colors.bgInput, borderWidth: 1,
    borderColor: colors.border, borderRadius: radius.md,
    color: colors.text, fontFamily: 'Georgia', fontSize: 14,
    paddingHorizontal: spacing.sm, paddingVertical: spacing.sm, maxHeight: 100,
  },
  sendBtn: {
    backgroundColor: colors.bgCard, borderWidth: 1, borderColor: colors.gold,
    borderRadius: radius.md, width: 40, height: 40,
    alignItems: 'center', justifyContent: 'center',
  },
  sendBtnDisabled: { borderColor: colors.borderDim },
  sendBtnText: { color: colors.gold, fontSize: 18, fontFamily: 'Georgia' },
});
