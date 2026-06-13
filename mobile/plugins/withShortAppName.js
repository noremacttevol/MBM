// Home-screen launcher label only.
//
// The app's real name everywhere — splash, in-app, store listing — stays the
// full "Milk Before Meat" (expo.name). But the label under the icon on a phone
// home screen is narrow and truncates the full name, so there (and ONLY there)
// we show the short "Milk B4 Meat".
//
// iOS handles this with CFBundleDisplayName in app.json. Android's launcher
// label is the `app_name` string resource, which Expo otherwise fills from
// expo.name — so this plugin overrides just that one string at build time.

const { withStringsXml, AndroidConfig } = require('@expo/config-plugins');

const SHORT_NAME = 'Milk B4 Meat';

module.exports = function withShortAppName(config) {
  return withStringsXml(config, cfg => {
    cfg.modResults = AndroidConfig.Strings.setStringItem(
      [{ _: SHORT_NAME, $: { name: 'app_name', translatable: 'false' } }],
      cfg.modResults,
    );
    return cfg;
  });
};
