import asyncio
import requests
import logging
from renogybt import RoverClient

# --- Configuration Section ---

DEVICE_CONFIG = {
    "address": "AA:BB:CC:DD:EE:FF",  # <-- Replace with your Renogy device's MAC address
    "alias": "MyRenogy",
    "type": "controller"  # or "battery" if that's your device
}

DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"  # <-- Replace with your Discord webhook URL

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("renogy_monitor.log"),
        logging.StreamHandler()
    ]
)

# Keep track of which alerts have been sent to avoid duplicates
alerted_levels = set()

def send_discord_alert(message):
    """
    Send an alert message to Discord via webhook.
    """
    data = {"content": message}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
        response.raise_for_status()
        logging.info(f"Sent Discord alert: {message}")
    except requests.RequestException as e:
        logging.error(f"Failed to send Discord alert: {e}")

def on_data_received(data):
    """
    Callback function when new data is received from the Renogy device.
    Prints battery info and sends alerts if thresholds are crossed.
    """
    voltage = data.get('battery_voltage')
    percent = data.get('battery_percentage') or data.get('battery_capacity')  # Some devices use 'battery_capacity'
    logging.info(f"Battery Voltage: {voltage} V")
    logging.info(f"Battery Level: {percent}%")

    # Print to console as well
    print(f"Battery Voltage: {voltage} V")
    print(f"Battery Level: {percent}%")

    # Define alert thresholds and messages
    thresholds = [
        (50, "⚠️ Battery below 50%!"),
        (40, "‼️ Battery below 40%!"),
        (35, "🛑 Battery below 35%! SHUT DOWN SYSTEM AND CHARGE!")
    ]
    # Check thresholds and send alerts if needed
    for level, msg in thresholds:
        if percent is not None and percent < level and level not in alerted_levels:
            send_discord_alert(f"{msg} (Current: {percent}%)")
            alerted_levels.add(level)

def on_error(error):
    """
    Callback function for errors from the Renogy client.
    Logs and prints the error.
    """
    logging.error(f"RenogyBT Error: {error}")
    print(f"Error: {error}")

async def main():
    """
    Main async function to start the Renogy Bluetooth client.
    Includes error handling for connection issues.
    """
    try:
        client = RoverClient(DEVICE_CONFIG, on_data_received, on_error)
        await client.start()
    except Exception as e:
        logging.critical(f"Critical error in main loop: {e}")
        print(f"Critical error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Script stopped by user (KeyboardInterrupt).")
        print("Script stopped by user.")
    except Exception as e:
        logging.critical(f"Unhandled exception: {e}")
        print(f"Unhandled exception: {e}")
