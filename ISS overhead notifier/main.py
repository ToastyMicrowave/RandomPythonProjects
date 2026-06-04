import os
import json
import time
import smtplib
import logging
from email.message import EmailMessage

import requests
import dotenv

dotenv.load_dotenv()

# ---- Config (env vars override the defaults, so you can set them in CI) ----
def _float_env(name, default):
    # An unset *or empty* env var falls back to the default. Actions passes
    # unconfigured `vars.*` as empty strings, so treat those as "not set".
    val = os.getenv(name, "").strip()
    return float(val) if val else default


MY_LAT = _float_env("MY_LAT", 52.051230)
MY_LONG = _float_env("MY_LONG", 1.144112)
PROXIMITY_DEG = _float_env("PROXIMITY_DEG", 5)         # how close (deg) the ISS must be
ALERT_COOLDOWN = 6 * 60 * 60                            # min seconds between two emails
REQUEST_TIMEOUT = 15                                    # per API/SMTP call

MY_EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASSWORD")

# Optional dedup across runs. In CI we point this at a cached file so a single
# ISS pass doesn't trigger an email on every scheduled run. Unset = no dedup.
STATE_FILE = os.getenv("STATE_FILE")

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("iss-notifier")


def is_night():
    """True if it's currently dark at our location (so the ISS would be visible)."""
    r = requests.get("https://api.sunrise-sunset.org/json",
                     params={"lat": MY_LAT, "lng": MY_LONG, "formatted": 0},
                     timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    results = r.json()["results"]
    sunrise = int(results["sunrise"].split("T")[1][:2])
    sunset = int(results["sunset"].split("T")[1][:2])
    hour = time.gmtime().tm_hour
    return hour < sunrise or hour > sunset


def iss_position():
    """Return (lat, lon) of the ISS. Tries wheretheiss.at, falls back to open-notify."""
    try:
        r = requests.get("https://api.wheretheiss.at/v1/satellites/25544",
                         timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
        d = r.json()
        return float(d["latitude"]), float(d["longitude"])
    except Exception as e:
        log.warning("wheretheiss.at failed (%s); trying open-notify", e)
        r = requests.get("http://api.open-notify.org/iss-now.json",
                         timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
        p = r.json()["iss_position"]
        return float(p["latitude"]), float(p["longitude"])


def is_overhead(lat, lon):
    return abs(lat - MY_LAT) <= PROXIMITY_DEG and abs(lon - MY_LONG) <= PROXIMITY_DEG


def send_email():
    msg = EmailMessage()
    msg["Subject"] = "Look up! The ISS is overhead!"
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL
    msg.set_content("The ISS is flying overhead right now — go outside and look up!")
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=REQUEST_TIMEOUT) as conn:
        conn.starttls()
        conn.login(MY_EMAIL, PASS)
        conn.send_message(msg)


def last_alert_time():
    """Epoch seconds of the last email we sent, or 0 if unknown."""
    if not STATE_FILE or not os.path.exists(STATE_FILE):
        return 0.0
    try:
        with open(STATE_FILE) as f:
            return float(json.load(f).get("last_alert", 0))
    except (ValueError, OSError, json.JSONDecodeError):
        return 0.0


def record_alert():
    if not STATE_FILE:
        return
    with open(STATE_FILE, "w") as f:
        json.dump({"last_alert": time.time()}, f)


def main():
    """Run a single check and exit. Cadence is driven by the caller (cron / Actions)."""
    if not MY_EMAIL or not PASS:
        raise SystemExit("EMAIL and PASSWORD must be set (env var or .env file).")

    if not is_night():
        log.info("Daytime at (%.2f, %.2f) — ISS wouldn't be visible, skipping", MY_LAT, MY_LONG)
        return

    lat, lon = iss_position()
    if not is_overhead(lat, lon):
        log.info("ISS at (%.2f, %.2f) — not overhead, nothing to do", lat, lon)
        return

    if time.time() - last_alert_time() < ALERT_COOLDOWN:
        log.info("ISS overhead at (%.2f, %.2f), but still within cooldown — not emailing", lat, lon)
        return

    send_email()
    record_alert()
    log.info("ISS overhead at (%.2f, %.2f) — email sent", lat, lon)


if __name__ == "__main__":
    main()
