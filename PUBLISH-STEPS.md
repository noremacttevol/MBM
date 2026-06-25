# Publish MBM — simple steps

Do these in order. After each one, tell me and I'll handle my part and check it.

---

## 1. Fix the AI key
- Go to Railway → **mbm-proxy** → **Variables**
- Set **ANTHROPIC_API_KEY** to your real key → Save
- Tell me "done" — I'll confirm the AI works.

## 2. Connect Expo
In Terminal, paste:
```
cd ~/Desktop/Brain/MBM/mobile
npx eas-cli login
npx eas-cli init
```
- Sign in as **admin@milkb4meat.org**
- If it asks to create a project, say **yes**
- Paste me what it shows.

## 3. Put your privacy page online
- I give you 2 commands here. You run them. Done.

## 4. Build the app
In Terminal, paste:
```
npx eas-cli build -p android --profile production
```
- Wait ~15 minutes
- Download the file it gives you (ends in **.aab**)

## 5. Put it on Google Play
- Go to **play.google.com/console** → create app **"Milk Before Meat"**
- **Internal testing** → upload your **.aab** file
- Paste the listing text + privacy link (I give you these)
- Add your friends' emails → **Roll out** → copy the install link and share it

---

That's the whole list. You're on **Step 1**.
