# Running the ISS notifier on GitHub Actions

The notifier runs as a scheduled GitHub Actions workflow — no server to babysit.
Each run does one check (is it night here? is the ISS overhead?) and emails me if so.
The workflow lives at [`.github/workflows/iss-notifier.yml`](../.github/workflows/iss-notifier.yml).

## Setup

1. **Add the email credentials as repo secrets** (Settings → Secrets and variables →
   Actions → *Secrets*):
   - `EMAIL` — the Gmail address that sends (and receives) the alert.
   - `PASSWORD` — a Gmail [App Password](https://myaccount.google.com/apppasswords),
     **not** your normal account password.

2. **Set your location** (optional). It defaults to the values in `main.py`. To override
   without touching code, add repo *Variables* (same settings page → *Variables*):
   - `MY_LAT`, `MY_LONG` — your latitude / longitude.
   - `PROXIMITY_DEG` — how close (in degrees) counts as "overhead" (default `5`, ≈550 km).

3. **That's it.** The workflow runs every 5 minutes on a cron schedule. To test it
   immediately, open the **Actions** tab → *ISS overhead notifier* → **Run workflow**.

## How it behaves

- **Schedule:** `*/5 * * * *`. GitHub's minimum interval is 5 minutes, and scheduled
  runs can be delayed when the platform is busy — fine for this.
- **No duplicate spam:** the last-sent timestamp is cached between runs
  (`.iss_state.json` via `actions/cache`), and `ALERT_COOLDOWN` in `main.py` (6 h) stops a
  single pass from emailing on every tick.
- **Cost:** free on a public repo. On a private repo this would eat Actions minutes fast
  (~288 runs/day), so raise the cron interval if you make the repo private.

## Running it locally

```bash
cd "ISS overhead notifier"
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # fill in EMAIL + PASSWORD
python main.py              # one check, then exits
```

To send a test email regardless of where the ISS is:

```bash
python -c "import main; main.send_email(); print('sent')"
```

## Notes

- Gmail needs an **App Password**: https://myaccount.google.com/apppasswords
- The notifier only makes outbound HTTPS/SMTP calls — no inbound ports, nothing to expose.
</content>
