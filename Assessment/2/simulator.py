# simulator.py
import time
import random
import paho.mqtt.client as mqtt

# === HiveMQ Public Broker ===
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_PRESSURE = "sensors/pressure"
TOPIC_TEMPERATURE = "sensors/temperature"

# === MQTT Callbacks ===
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Connected to {BROKER}:{PORT}")
    else:
        print(f"Connection failed, code: {rc}")

def on_publish(client, userdata, mid):
    pass  # Optional: remove if you don't want per-message log

# === Setup Client ===
client = mqtt.Client(client_id="iot-simulator-lenovo")  # Unique ID
client.on_connect = on_connect
client.on_publish = on_publish

# Start background network loop
client.loop_start()

# === Connect to HiveMQ ===
try:
    client.connect(BROKER, PORT, keepalive=60)
    time.sleep(2)  # Wait for connection
except Exception as e:
    print(f"Failed to connect: {e}")
    exit(1)

print("Simulator started – publishing every 5 seconds\n")

# === Main Loop ===
while True:
    pressure = round(random.uniform(50, 95), 2)     # High pressure
    temperature = round(random.uniform(-10, 50), 2)

    client.publish(TOPIC_PRESSURE, str(pressure))
    client.publish(TOPIC_TEMPERATURE, str(temperature))

    print(f"Published → Pressure: {pressure:5.2f} psi | Temp: {temperature:5.2f} °C")
    time.sleep(5)