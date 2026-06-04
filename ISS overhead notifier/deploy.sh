#!/usr/bin/env bash
# Run this ON the Oracle Cloud VM, from inside the project folder:
#   cd ~/iss-notifier && bash deploy.sh
# It auto-detects your OS, user, and paths, then installs + starts the service.
set -euo pipefail

cd "$(dirname "$0")"
APP_DIR="$(pwd)"
RUN_USER="$(id -un)"
SERVICE=/etc/systemd/system/iss-notifier.service

echo "==> Project: $APP_DIR   (will run as user: $RUN_USER)"

# 1. Python venv + pip (apt for Ubuntu, dnf/yum for Oracle Linux)
echo "==> Installing python3-venv / pip ..."
if command -v apt >/dev/null 2>&1; then
    sudo apt-get update -y
    sudo apt-get install -y python3-venv python3-pip
elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y python3 python3-pip
elif command -v yum >/dev/null 2>&1; then
    sudo yum install -y python3 python3-pip
fi

# 2. virtualenv + dependencies
echo "==> Creating venv and installing requirements ..."
python3 -m venv .venv
./.venv/bin/pip install --upgrade pip >/dev/null
./.venv/bin/pip install -r requirements.txt

# 3. credentials
if [ ! -f .env ]; then
    cp .env.example .env
    echo
    echo "!! No .env found — created one from the template."
    echo "   Edit it with your Gmail + App Password, then re-run this script:"
    echo "     nano $APP_DIR/.env"
    exit 1
fi

# 4. generate the systemd unit with the REAL user/paths and install it
echo "==> Installing systemd service ..."
sudo tee "$SERVICE" >/dev/null <<UNIT
[Unit]
Description=ISS Overhead Email Notifier
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=$RUN_USER
WorkingDirectory=$APP_DIR
ExecStart=$APP_DIR/.venv/bin/python $APP_DIR/main.py
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
UNIT

sudo systemctl daemon-reload
sudo systemctl enable --now iss-notifier

echo
echo "==> Service installed and started."
sudo systemctl status iss-notifier --no-pager -l | head -n 12 || true
echo
echo "Live logs:        journalctl -u iss-notifier -f"
echo "Send a test mail: ./.venv/bin/python -c 'import main; main.send_email(); print(\"sent\")'"
