# Put the reply desk online (so it's not localhost)

This hosts your Ministry console at a real web address with a login, so you and
approved helpers can answer people from any phone or browser. Same Railway you
used for the proxy.

---

## 1. Get your key as one line of text
Your desk needs its Firebase key, but a host can't use the file — so we turn it
into one line. In a terminal:
```
cd ~/Desktop/Brain/MBM/admin
base64 -w0 serviceAccount.json
```
It prints a long line. **Copy the whole thing** (you'll paste it in step 3).

## 2. Deploy the desk
```
cd ~/Desktop/Brain/MBM/admin
railway init        # name it: mbm-desk
railway up
```

## 3. Add the settings (Railway dashboard → mbm-desk → Variables)
Add these three:

- **FIREBASE_SERVICE_ACCOUNT** = the long line you copied in step 1
- **ADMIN_PASSWORD** = a password you choose for your team (share it only with
  helpers you approve)
- **SESSION_SECRET** = any long random string. Make one with:
  ```
  openssl rand -hex 32
  ```

Save — Railway redeploys automatically.

## 4. Get the web address
Railway → mbm-desk → **Settings → Networking → Generate Domain**.
(If the page shows a 502, set the domain's **target port** the same way you did
for the proxy.) You'll get a link like `https://mbm-desk-production.up.railway.app`.

## 5. Use it
Open that link on any device → sign in with **your name + the team password**.
Your name is what your replies get signed with. To add a helper, just give them
the link and the password — they sign in with their own name.

---

### Notes
- Nothing personal is exposed: the powerful key lives only in Railway's settings,
  never in the app or in git.
- The local desk still works exactly as before (`npm start`) with no password —
  the login only turns on once `ADMIN_PASSWORD` is set (which it is, on the host).
- Later we can point `admin.milkb4meat.org` at this, but the Railway link works
  now.
