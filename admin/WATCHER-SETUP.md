# Turn on professional alerts — branded email from your own MBM domain

This makes you (and later your helpers) get an email the second someone asks to
talk to a real person. The email arrives as **MBM <notify@yourdomain>** — not from
any personal account. You set this up once.

There's no Gmail and no app password. You need two things: a **domain** for MBM,
and a free **Resend** account that sends the email for you.

---

## Step 1 — Domain ✅ DONE

The MBM domain is **milkb4meat.org**. It's your app's web address, your admin
console link, and your branded email, all looking like one real product. The
planned layout:

- `milkb4meat.org` — public landing page + `/privacy` + `/support`
- `admin.milkb4meat.org` — the hosted reply desk (Step B)
- `notify@milkb4meat.org` — the address alert emails are sent from (this step)

Keep your registrar login handy for Step 2 (you'll add a few DNS records there).

---

## Step 2 — Make a free Resend account and connect your domain

Resend is the service that actually sends the alert emails, professionally.

1. Go to **https://resend.com** and sign up (free tier is plenty — thousands of
   emails/month).
2. In Resend: **Domains → Add Domain** → type your domain from Step 1.
3. Resend shows you a few **DNS records** to add. You add these where you bought
   the domain (the registrar's DNS settings).
   - **Send me the records and I'll tell you exactly what to paste where** — this
     is the one slightly technical bit and I'll walk you through it line by line.
4. Wait a few minutes, then click **Verify** in Resend. Green check = done.
5. **API Keys → Create API Key** → copy the key (starts with `re_`).

---

## Step 3 — Put the key + your address in the settings file

In the `admin` folder:

1. Make your settings file from the template (one time):
   ```
   cp .env.example .env
   ```
2. Open `.env` and fill in:
   ```
   RESEND_API_KEY=re_thekeyyoucopied
   ALERT_FROM=MBM <notify@yourdomain>
   OWNER_EMAIL=where_you_want_alerts_to_land@example.com
   ```
   (`notify@yourdomain` can be anything on your domain — it doesn't need to be a
   real mailbox; Resend just sends *as* it. `OWNER_EMAIL` is where the alert
   actually lands — your normal inbox is fine here.)

`.env` stays on your machine and is gitignored — never committed or shared.

---

## Step 4 — Start it

In the `admin` folder:
```
npm install      # only the first time
npm run start:watch
```

You'll see `Email sending: ON (from MBM <notify@yourdomain>)`. Leave it running
and it watches for you.

**Test it:** open the app, tap "talk to a real person," send a note. Within a few
seconds a branded email should land in your inbox with the message and a desk link.

---

## Good to know

- **Before this is set up**, the watcher still runs — it just prints alerts to the
  screen and says email is off, so nothing is ever lost.
- **Want to test before your domain is ready?** Resend gives every account a ready
  address `onboarding@resend.dev`. Put `ALERT_FROM=MBM <onboarding@resend.dev>` and
  it'll send to your own email immediately, then swap in your domain later. (This
  is just the default in `.env.example`.)
- **When you add helpers**, new conversations get emailed to whichever approved
  helper is least busy instead of always you — no change needed here.
- **When your desk goes on the web** (Step B), change `ADMIN_DESK_URL` so the email
  link opens it on your phone.
