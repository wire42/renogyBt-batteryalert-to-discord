# Renogy Solar Battery Monitor with Discord Alerts
by Patrick Elliott


This Python script connects to your Renogy solar charge controller or battery via Bluetooth and monitors real-time battery voltage and percentage. It sends alert notifications to a Discord channel when battery levels fall below critical thresholds (50%, 40%, and 35%).

---

## Features

- Connects to Renogy devices using Bluetooth (BT-1 or BT-2 modules).
- Displays battery voltage and battery percentage in real time.
- Sends Discord alerts when battery percentage drops below:
  - 50% (warning)
  - 40% (urgent warning)
  - 35% (critical alert with shutdown recommendation)
- Logs all data and errors to a log file and console.
- Handles errors gracefully and reconnects as needed.
- Prevents duplicate alerts for the same battery level.

---

## Requirements

- Python 3.7+
- Bluetooth adapter on your computer
- Renogy device with BT-1 or BT-2 Bluetooth module
- Discord webhook URL for sending alerts

---

## Installation

1. Clone the repository or download the script files.

2. Install dependencies using pip:

pip install renogybt requests

text

Or, if you cloned the [renogy-bt](https://github.com/wingchen/renogy-bt) repo, install its requirements:

pip install -r requirements.txt

text

3. Make sure your Bluetooth is enabled and your Renogy device is powered on and within range.

---

## Setup

1. **Find your Renogy device's Bluetooth MAC address:**

- Use a Bluetooth scanner app on your phone, or
- Run the `example.py` script from the `renogy-bt` library to scan for devices.

2. **Create a Discord webhook:**

- Go to your Discord server.
- Open the channel where you want alerts.
- Go to Channel Settings > Integrations > Webhooks > New Webhook.
- Copy the webhook URL.

3. **Edit the script:**

Open the Python script and update the following:

DEVICE_CONFIG = {
"address": "AA:BB:CC:DD:EE:FF", # Replace with your device's MAC address
"alias": "MyRenogy",
"type": "controller" # or "battery"
}

DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL" # Replace with your webhook URL

text

---

## Usage

Run the script:

python renogy_monitor.py

text

The script will:

- Connect to your Renogy device.
- Print battery voltage and percentage to the console.
- Send alerts to Discord when battery levels cross thresholds.
- Log events and errors to `renogy_monitor.log`.

To stop the script, press `Ctrl+C`.

---

## Troubleshooting

- **Bluetooth connection issues:**
  - Ensure your Bluetooth adapter is working and enabled.
  - Make sure the Renogy device is powered on and within range.
  - Verify the MAC address is correct.

- **Discord alerts not sending:**
  - Confirm the webhook URL is correct.
  - Check your internet connection.
  - Look for errors in the console or `renogy_monitor.log`.

- **Python errors:**
  - Ensure all dependencies are installed.
  - Use Python 3.7 or higher.

---

## Customization

- Modify alert thresholds or messages in the script.
- Extend the script to save data to CSV or database.
- Integrate with other notification services (email, SMS, etc.).
- Build a web dashboard for real-time monitoring.

---

## License

This project is open source and free to use.

---

## Acknowledgments

- [renogy-bt](https://github.com/wingchen/renogy-bt) library for Renogy Bluetooth communication.
- Discord for webhook integration.

---
