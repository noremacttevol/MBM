import React from 'react';
import { View, Text, Pressable, StyleSheet } from 'react-native';
import { colors, spacing, radius, typography } from '../theme';

type Props = {
  children: React.ReactNode;
  // Shown in place of the crashed subtree.
  label?: string;
};

type State = {
  hasError: boolean;
};

// Catches render/runtime errors in any child screen so a single crash shows a
// calm fallback instead of blanking the whole app. Tapping "Try again" remounts
// the subtree, which recovers from transient errors.
export default class ErrorBoundary extends React.Component<Props, State> {
  state: State = { hasError: false };

  static getDerivedStateFromError(): State {
    return { hasError: true };
  }

  componentDidCatch(error: Error) {
    console.error('[ErrorBoundary]', this.props.label ?? '', error);
  }

  reset = () => {
    this.setState({ hasError: false });
  };

  render() {
    if (!this.state.hasError) {
      return this.props.children;
    }

    return (
      <View style={styles.container}>
        <Text style={styles.title}>Something needs a moment</Text>
        <Text style={styles.body}>
          This part of the app ran into a problem. Nothing you wrote is lost — the
          rest of the app is still here.
        </Text>
        <Pressable style={styles.button} onPress={this.reset}>
          <Text style={styles.buttonText}>Try again</Text>
        </Pressable>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.bg,
    alignItems: 'center',
    justifyContent: 'center',
    padding: spacing.xl,
  },
  title: {
    fontFamily: typography.serif,
    fontSize: 22,
    color: colors.goldLight,
    marginBottom: spacing.md,
    textAlign: 'center',
  },
  body: {
    fontFamily: typography.sansSerif,
    fontSize: 15,
    lineHeight: 22,
    color: colors.textDim,
    textAlign: 'center',
    marginBottom: spacing.xl,
  },
  button: {
    backgroundColor: colors.bgCard,
    borderColor: colors.borderDim,
    borderWidth: 1,
    borderRadius: radius.lg,
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.xl,
  },
  buttonText: {
    fontFamily: typography.sansSerif,
    fontSize: 15,
    color: colors.gold,
  },
});
