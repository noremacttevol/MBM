import React from 'react';
import { registerRootComponent } from 'expo';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import AppNavigator from './src/navigation/AppNavigator';

function App() {
  // SafeAreaProvider supplies the real device insets (status bar at the top,
  // the gesture/button nav bar at the bottom) so nothing the app draws hides
  // behind the system UI. Phones without an on-screen nav bar simply report a
  // zero bottom inset, so the same code uses the full screen there.
  return (
    <SafeAreaProvider>
      <AppNavigator />
    </SafeAreaProvider>
  );
}

registerRootComponent(App);

export default App;
