import os
import time
import smtplib
import logging
from email.message import EmailMessage

import requests
import dotenv

dotenv.load_dotenv()

# ---- Config ----
MY_LAT = 52.051230
MY_LONG = 1.144112
PROXIMITY_DEG = 5                 # how close (in degrees) the ISS must be to notify
CHECK_INTERVAL = 60              # seconds between checks
ALERT_COOLDOWN = 6 * 60 * 60      # don't send more than one email per 6 hours
REQUEST_TIMEOUT = 15              # seconds before an API/SMTP call gives up

MY_EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASSWORD")

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


def main():
    if not MY_EMAIL or not PASS:
        raise SystemExit("EMAIL and PASSWORD must be set in the .env file.")
    log.info("ISS notifier started for lat=%s lon=%s", MY_LAT, MY_LONG)
    last_alert = 0.0
    while True:
        try:
            if is_night():
                lat, lon = iss_position()
                if is_overhead(lat, lon):
                    if time.time() - last_alert >= ALERT_COOLDOWN:
                        send_email()
                        last_alert = time.time()
                        log.info("ISS overhead at (%.2f, %.2f) — email sent", lat, lon)
                    else:
                        log.info("ISS overhead, but still within cooldown — not emailing")
                else:
                    log.debug("ISS at (%.2f, %.2f) — not overhead", lat, lon)
            else:
                log.debug("Daytime here — skipping ISS check")
        except Exception as e:
            # Never let a transient network/API error kill the loop.
            log.warning("Check failed (%s) — will retry", e)
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
