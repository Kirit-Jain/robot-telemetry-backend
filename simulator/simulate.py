import requests
import time
import random
from faker import Faker

fake = Faker()

API_URL = "http://localhost:8000/telemetry"

ROBOTS = ["R2-D2", "C-3PO", "BB-8", "T-800"]

print("--- Robot Telemetry Simulator Started ---")
print(f"Sending data to {API_URL}")

while True:
    try:
        robot_id = random.choice(ROBOTS)

        location_data = {
            "latitude": float(fake.latitude()),
            "longitude": float(fake.longitude())
        }
        battery = round(random.uniform(5.0, 100.0), 2)

        payload = {
            "robot_id": robot_id,
            "location": location_data,
            "battery_level": battery
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            print(f"Successfully sent data for {robot_id}: Bat={battery}%, Loc=({location_data['latitude']}, {location_data['longitude']})")
        else:
            print(f"Error sending data: {response.status_code} - {response.text}")
        
        time.sleep(random.randint(3, 10))
    
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Is the backend running?")
        time.sleep(10)
    except KeyboardInterrupt:
        print("\n--- Simulator Stopped ---")
        break