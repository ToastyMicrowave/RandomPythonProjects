# Running the ISS notifier 24/7

This guide runs the notifier as a **systemd service** on an always-on Linux box
(Raspberry Pi, or a cheap/free cloud VM such as Oracle Cloud Free Tier, AWS Lightsail,
a DigitalOcean droplet, etc.). systemd starts it on boot and restarts it if it crashes.

## 1. Get the code onto the host

On the Raspberry Pi / VM:

```bash
sudo apt update && sudo apt install -y python3-venv git   # Debian/Ubuntu/Raspberry Pi OS
mkdir -p ~/iss-notifier && cd ~/iss-notifier
# copy main.py and requirements.txt here (scp, git clone, or paste)
```

To copy just this folder from your Mac:

```bash
scp -r "ISS overhead notifier/"* pi@<host-ip>:~/iss-notifier/
```

## 2. Create the virtualenv and install deps

```bash
cd ~/iss-notifier
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## 3. Add your credentials

```bash
cp .env.example .env
nano .env        # set EMAIL and PASSWORD (Gmail App Password)
```

Set your location at the top of `main.py` (`MY_LAT` / `MY_LONG`) if it isn't already.

## 4. Test it runs

```bash
.venv/bin/python main.py
```

You should see a log line like `ISS notifier started for lat=... lon=...`.
Press `Ctrl+C` to stop, then set it up as a service.

## 5. Install the systemd service

Edit `iss-notifier.service` and fix the three paths/user if you didn't use
`pi` + `~/iss-notifier` (e.g. on a cloud VM the user is often `ubuntu`):

- `User=` your login name
- `WorkingDirectory=` the folder you put the code in
- `ExecStart=` the venv python + the path to `main.py`

Then:

```bash
sudo cp iss-notifier.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now iss-notifier     # start now + on every boot
```

## 6. Check on it

```bash
systemctl status iss-notifier      # is it running?
journalctl -u iss-notifier -f      # live logs
```

To update the code later: replace `main.py`, then `sudo systemctl restart iss-notifier`.

---

### Notes
- Gmail needs an **App Password** (not your normal password): https://myaccount.google.com/apppasswords
- The service emails at most **once every 6 hours** (`ALERT_COOLDOWN` in `main.py`) so a long ISS pass doesn't spam you.
- Some cloud providers block outbound SMTP on port 25; this script uses port **587**, which is normally allowed. If port 587 is also blocked, switch to a transactional email API (SendGrid, Mailgun) instead of Gmail SMTP.
- `PROXIMITY_DEG = 5` means "within 5° of your lat/long" (~550 km). Lower it for a tighter definition of "overhead".
