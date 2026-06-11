import React, { useEffect, useState } from 'react';
import { View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Ionicons } from '@expo/vector-icons';

import HookScreen        from '../screens/HookScreen';
import OnboardScreen     from '../screens/OnboardScreen';
import WelcomeBackScreen from '../screens/WelcomeBackScreen';
import FeedScreen        from '../screens/FeedScreen';
import JournalScreen     from '../screens/JournalScreen';
import ChatScreen        from '../screens/ChatScreen';
import ProfileScreen     from '../screens/ProfileScreen';
import ErrorBoundary     from '../components/ErrorBoundary';
import { useAppStore }   from '../store/useAppStore';
import { colors } from '../theme';

// Wraps a screen so a crash inside it shows a calm fallback instead of blanking
// the whole app. Each screen gets its own boundary, so one tab failing leaves
// the tab bar and other tabs usable.
function guard<P extends object>(Component: React.ComponentType<P>, label: string) {
  return function Guarded(props: P) {
    return (
      <ErrorBoundary label={label}>
        <Component {...props} />
      </ErrorBoundary>
    );
  };
}

const GuardedHook        = guard(HookScreen,        'Hook');
const GuardedOnboard     = guard(OnboardScreen,     'Onboard');
const GuardedWelcomeBack = guard(WelcomeBackScreen, 'WelcomeBack');
const GuardedFeed        = guard(FeedScreen,        'Feed');
const GuardedJournal     = guard(JournalScreen,     'Journal');
const GuardedChat        = guard(ChatScreen,        'Chat');
const GuardedProfile     = guard(ProfileScreen,     'Profile');

// ── Type maps ────────────────────────────────────────────────────────────────

export type RootStackParamList = {
  Hook:        undefined;
  Onboard:     undefined;
  WelcomeBack: undefined;
  Main:        undefined;
};

export type MainTabParamList = {
  Feed:    undefined;
  Journal: undefined;
  Chat:    undefined;
  Profile: undefined;
};

// ── Navigators ───────────────────────────────────────────────────────────────

const Stack = createNativeStackNavigator<RootStackParamList>();
const Tab   = createBottomTabNavigator<MainTabParamList>();

// The tab navigator. There is no time cap and no come-back wipe (Law 5): the app
// never locks a person out and never erases what it has learned about them.
function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }: { route: { name: string } }) => ({
        headerShown: false,
        tabBarStyle: {
          backgroundColor:  colors.bg,
          borderTopColor:   colors.borderDim,
          borderTopWidth:   1,
          height:           72,
          paddingTop:       6,
          paddingBottom:    10,
        },
        tabBarItemStyle: {
          justifyContent: 'center',
          alignItems: 'center',
          paddingVertical: 4,
        },
        tabBarActiveTintColor:   colors.gold,
        tabBarInactiveTintColor: colors.textMuted,
        tabBarShowLabel:         false,
        tabBarIcon: ({ focused, color, size }: { focused: boolean; color: string; size: number }) => {
          const icons: Record<string, { outline: string; filled: string }> = {
            Feed:    { outline: 'book-outline',        filled: 'book' },
            Journal: { outline: 'journal-outline',     filled: 'journal' },
            Chat:    { outline: 'chatbubble-outline',  filled: 'chatbubble' },
            Profile: { outline: 'person-outline',      filled: 'person' },
          };
          const iconSet = icons[route.name] ?? { outline: 'ellipse-outline', filled: 'ellipse' };
          const name    = focused ? iconSet.filled : iconSet.outline;
          return <Ionicons name={name as any} size={22} color={color} />;
        },
      })}
    >
      <Tab.Screen name="Feed"    component={GuardedFeed} />
      <Tab.Screen name="Journal" component={GuardedJournal} />
      <Tab.Screen name="Chat"    component={GuardedChat} />
      <Tab.Screen name="Profile" component={GuardedProfile} />
    </Tab.Navigator>
  );
}

export default function AppNavigator() {
  // Wait for the persisted store to rehydrate before choosing the entry screen,
  // so a returning person is met with WelcomeBack — never a cold restart (Law 5).
  const [hydrated, setHydrated] = useState(() => useAppStore.persist.hasHydrated());

  useEffect(() => {
    const unsub = useAppStore.persist.onFinishHydration(() => setHydrated(true));
    if (useAppStore.persist.hasHydrated()) setHydrated(true);
    // Never let a slow or unavailable storage layer trap the app on the blank
    // boot screen. If hydration hasn't reported in by now, proceed anyway.
    const fallback = setTimeout(() => setHydrated(true), 2000);
    return () => { unsub(); clearTimeout(fallback); };
  }, []);

  if (!hydrated) {
    return <View style={{ flex: 1, backgroundColor: colors.bg }} />;
  }

  const onboardingComplete = useAppStore.getState().onboardingComplete;
  const initialRouteName: keyof RootStackParamList = onboardingComplete ? 'WelcomeBack' : 'Hook';

  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName={initialRouteName}
        screenOptions={{
          headerShown:    false,
          animation:      'fade',
          contentStyle:   { backgroundColor: colors.bg },
          gestureEnabled: false,
        }}
      >
        <Stack.Screen name="Hook"        component={GuardedHook} />
        <Stack.Screen name="Onboard"     component={GuardedOnboard} />
        <Stack.Screen name="WelcomeBack" component={GuardedWelcomeBack} />
        <Stack.Screen name="Main"        component={MainTabs} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
