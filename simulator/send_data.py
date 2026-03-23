"""
IoT Simulator: Mimics ESP32 gateway sending flood sensor data.
CV Link: Reflects MHEWS sensor-ingestion requirements (BNPB).
"""
import requests
import random
import time
import json

API_URL = "http://127.0.0.1:8000/api/v1/readings/"
STATION_ID = 1  # ID of your test station in Django admin

def send_reading(water_level, battery_pct):
    payload = {
        "station": STATION_ID,
        "water_level": water_level,
        "battery_pct": battery_pct
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=5)
        if response.status_code == 201:
            data = response.json()
            print(f"✓ Sent: {water_level}m → Status: {data['status']}")
            return True
        else:
            print(f"✗ Error {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        return False

def main():
    print("🌊 Flood Sensor Simulator Started (ESP32 Mimic)")
    print(f"Target: {API_URL} | Station ID: {STATION_ID}\n")
    
    while True:
        # Simulate realistic water level fluctuations
        base_level = 2.5
        fluctuation = random.uniform(-0.5, 2.5)  # Random variation
        water_level = round(base_level + fluctuation, 2)
        battery_pct = random.randint(70, 100)
        
        print(f"\n📡 Reading: {water_level}m (Battery: {battery_pct}%)")
        send_reading(water_level, battery_pct)
        
        # Wait 10 seconds between readings (simulates sensor interval)
        time.sleep(10)

if __name__ == "__main__":
    main()