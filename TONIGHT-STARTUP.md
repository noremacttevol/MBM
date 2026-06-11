# Tonight Startup Guide

Use this file every time we come back to work on MBM.

## Fast start
From the repo root:

```bash
cd /home/noremacttevol/Desktop/Brain/MBM
npm run mobile:web
```

This is the stable path we verified.

## If the port is already in use
Expo will ask to use the next port. Say yes.

## If the app does not start
1. Check that you are in the repo root.
2. Run `npm run mobile:web` again.
3. If Metro still fails, stop the old Expo process and rerun the same command.

## If you want the normal Expo path
```bash
cd /home/noremacttevol/Desktop/Brain/MBM
npm run mobile:dev
```

## If you want to try the tunnel again later
```bash
cd /home/noremacttevol/Desktop/Brain/MBM
npm run mobile:tunnel
```

## What success looks like
- The terminal says `Starting project at /home/noremacttevol/Desktop/Brain/MBM/mobile`
- Metro starts and the app bundles without crashing
- The web preview loads in the browser

## What not to do tonight
- Do not run `npx expo start` from the repo root by itself.
- Do not spend the first hour on tunnel/auth issues.
- Do not create or switch to duplicate app folders.
